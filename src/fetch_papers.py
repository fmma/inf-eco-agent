#!/usr/bin/env python3
"""Fetch recent arXiv papers matching configured keywords and categories.

Harvests via arXiv's OAI-PMH endpoint (`/oai2`) instead of the relevance-
search API (`/api/query`). OAI-PMH is the interface arXiv built for bulk
metadata harvesting: documented 1-request-per-4-seconds rate limit,
date-range filtering server-side, resumption tokens for pagination.
"""

import json
import logging
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("fetch_papers")

ROOT = Path(__file__).resolve().parent.parent
OAI_ENDPOINT = "https://oaipmh.arxiv.org/oai"
USER_AGENT = "inf-eco-agent/1.0 (mailto:frederik.meisner@gmail.com)"
OAI_SLEEP_SECONDS = 4

NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "arxiv": "http://arxiv.org/OAI/arXiv/",
}


def load_config():
    with open(ROOT / "config.json") as f:
        return json.load(f)


def normalize_arxiv_id(entry_id: str) -> str:
    """Strip version suffix and URL prefix to get bare arXiv ID for comparison."""
    bare = entry_id.rsplit("/", 1)[-1]
    return re.sub(r"v\d+$", "", bare)


def load_paper_db() -> list[dict]:
    papers_path = ROOT / "data" / "papers.json"
    if not papers_path.exists():
        return []
    with open(papers_path) as f:
        return json.load(f)


def load_queued_ids() -> set[str]:
    """Return normalized arXiv IDs of papers awaiting scoring in data/queue/.

    The queue holds batches that have been fetched but not yet scored
    (daily scoring is capped to keep claude under its rate limit). Dedup
    must include the queue so re-fetching the same window does not enqueue
    the same papers again.
    """
    queue_dir = ROOT / "data" / "queue"
    if not queue_dir.exists():
        return set()
    ids: set[str] = set()
    for batch in sorted(queue_dir.glob("*.json")):
        with open(batch) as f:
            for paper in json.load(f):
                ids.add(normalize_arxiv_id(paper["id"]))
    return ids


def get_cutoff(papers: list[dict], min_days: int = 3) -> datetime:
    """Compute the fetch cutoff from the most recent scored_date."""
    scored_dates = [p["scored_date"] for p in papers if "scored_date" in p]
    if not scored_dates:
        days = min_days
    else:
        last_run = datetime.fromisoformat(max(scored_dates)).replace(tzinfo=timezone.utc)
        days_since = (datetime.now(timezone.utc) - last_run).days + 1
        days = max(days_since, min_days)

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    log.info("Fetching papers from the last %d days (cutoff: %s)", days, cutoff.date())
    return cutoff


def keyword_matches(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def oai_request(params: dict) -> ET.Element:
    """Make one OAI-PMH GET via curl and parse the XML response."""
    url = f"{OAI_ENDPOINT}?{urlencode(params)}"
    log.info("GET %s", url)
    result = subprocess.run(
        [
            "curl",
            "--silent",
            "--show-error",
            "--max-time", "120",
            "--user-agent", USER_AGENT,
            "--write-out", "%{http_code}",
            url,
        ],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"curl failed (exit {result.returncode}): {result.stderr.decode('utf-8', 'replace').strip()}"
        )
    body = result.stdout[:-3]
    status_code = int(result.stdout[-3:])
    log.info("HTTP %d (%d bytes)", status_code, len(body))
    if status_code >= 400:
        raise RuntimeError(f"arXiv returned HTTP {status_code}")
    root = ET.fromstring(body)
    error = root.find("oai:error", NS)
    if error is not None:
        raise RuntimeError(f"OAI error {error.get('code')}: {error.text}")
    return root


def parse_record(record: ET.Element, categories: set[str], keywords: list[str],
                 seen_ids: set[str], cutoff: datetime) -> dict | None:
    """Extract a paper dict from an OAI record, or None if it doesn't qualify."""
    header = record.find("oai:header", NS)
    if header is not None and header.get("status") == "deleted":
        return None

    metadata = record.find("oai:metadata", NS)
    if metadata is None:
        return None
    arxiv_meta = metadata.find("arxiv:arXiv", NS)
    if arxiv_meta is None:
        return None

    arxiv_id = (arxiv_meta.findtext("arxiv:id", default="", namespaces=NS) or "").strip()
    if not arxiv_id or normalize_arxiv_id(arxiv_id) in seen_ids:
        return None

    paper_cats = (arxiv_meta.findtext("arxiv:categories", default="", namespaces=NS) or "").split()
    if not any(c in categories for c in paper_cats):
        return None

    created = (arxiv_meta.findtext("arxiv:created", default="", namespaces=NS) or "").strip()
    if not created:
        return None
    published = datetime.fromisoformat(created).replace(tzinfo=timezone.utc)
    if published < cutoff:
        return None

    title = arxiv_meta.findtext("arxiv:title", default="", namespaces=NS) or ""
    abstract = arxiv_meta.findtext("arxiv:abstract", default="", namespaces=NS) or ""
    if not keyword_matches(f"{title} {abstract}", keywords):
        return None

    authors = []
    authors_el = arxiv_meta.find("arxiv:authors", NS)
    if authors_el is not None:
        for author in authors_el.findall("arxiv:author", NS)[:10]:
            forenames = (author.findtext("arxiv:forenames", default="", namespaces=NS) or "").strip()
            keyname = (author.findtext("arxiv:keyname", default="", namespaces=NS) or "").strip()
            name = " ".join(part for part in (forenames, keyname) if part)
            if name:
                authors.append(name)

    return {
        "id": f"http://arxiv.org/abs/{arxiv_id}",
        "title": re.sub(r"\s+", " ", title).strip(),
        "abstract": re.sub(r"\s+", " ", abstract).strip(),
        "authors": authors,
        "published": published.isoformat(),
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
    }


def fetch_papers(config: dict) -> list[dict]:
    categories = set(config["arxiv_categories"])
    keywords = config["keywords"]

    paper_db = load_paper_db()
    seen_ids = {normalize_arxiv_id(p["id"]) for p in paper_db}
    seen_ids |= load_queued_ids()
    cutoff = get_cutoff(paper_db)

    params = {
        "verb": "ListRecords",
        "set": "cs",
        "from": cutoff.strftime("%Y-%m-%d"),
        "until": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "metadataPrefix": "arXiv",
    }

    papers = []
    page = 0
    while True:
        if page > 0:
            time.sleep(OAI_SLEEP_SECONDS)

        root = oai_request(params)
        list_records = root.find("oai:ListRecords", NS)
        if list_records is None:
            log.warning("No ListRecords element in response (page %d)", page + 1)
            break

        records = list_records.findall("oai:record", NS)
        kept_before = len(papers)
        for record in records:
            paper = parse_record(record, categories, keywords, seen_ids, cutoff)
            if paper is not None:
                papers.append(paper)
        log.info("Page %d: %d records, %d matched", page + 1, len(records), len(papers) - kept_before)

        token_el = list_records.find("oai:resumptionToken", NS)
        token = (token_el.text or "").strip() if token_el is not None and token_el.text else ""
        if not token:
            break
        params = {"verb": "ListRecords", "resumptionToken": token}
        page += 1

    return papers


def main():
    config = load_config()
    papers = fetch_papers(config)
    json.dump(papers, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
