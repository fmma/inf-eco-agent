#!/usr/bin/env python3
"""Fetch recent arXiv papers matching configured keywords and categories.

Direct HTTP calls (via curl) against the arXiv API, parsed with feedparser.
Paginates with a 5-minute sleep between pages until the published cutoff is
crossed or the page is empty. Non-2xx propagates as an exception and fails
the script — scan.sh decides how to react.
"""

import json
import logging
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode

import feedparser

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("fetch_papers")

ROOT = Path(__file__).resolve().parent.parent
ARXIV_API = "https://export.arxiv.org/api/query"
USER_AGENT = "inf-eco-agent/1.0 (mailto:frederik.meisner@gmail.com)"
PAGE_SIZE = 100
PAGE_SLEEP_SECONDS = 300
MAX_PAGES = 5


def load_config():
    with open(ROOT / "config.json") as f:
        return json.load(f)


def normalize_arxiv_id(entry_id: str) -> str:
    """Strip version suffix and URL prefix to get bare arXiv ID for comparison."""
    # e.g. "http://arxiv.org/abs/2602.20515v1" → "2602.20515"
    bare = entry_id.rsplit("/", 1)[-1]
    return re.sub(r"v\d+$", "", bare)


def load_paper_db() -> list[dict]:
    """Load all papers from data/papers.json."""
    papers_path = ROOT / "data" / "papers.json"
    if not papers_path.exists():
        return []
    with open(papers_path) as f:
        return json.load(f)


def get_cutoff(papers: list[dict], min_days: int = 3) -> datetime:
    """Compute the fetch cutoff from the most recent scored_date.

    Uses the latest scored_date in the database as the anchor, with a 1-day
    overlap buffer to catch papers published near the boundary. Falls back to
    min_days if the database is empty or has no scored_date fields.
    """
    scored_dates = [p["scored_date"] for p in papers if "scored_date" in p]
    if not scored_dates:
        days = min_days
    else:
        last_run = datetime.fromisoformat(max(scored_dates)).replace(tzinfo=timezone.utc)
        days_since = (datetime.now(timezone.utc) - last_run).days + 1  # +1 overlap buffer
        days = max(days_since, min_days)

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    log.info("Fetching papers from the last %d days (cutoff: %s)", days, cutoff.date())
    return cutoff


def keyword_matches(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def fetch_arxiv_page(query: str, start: int, max_results: int) -> feedparser.FeedParserDict:
    """Fetch one page from the arXiv API via curl and parse the Atom response.

    Uses curl(1) instead of python requests because in our testing curl
    consistently succeeded against arXiv where back-to-back python requests
    got 429s. Wire-level details (TLS/HTTP2/headers) appear to matter.
    """
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": start,
        "max_results": max_results,
    }
    url = f"{ARXIV_API}?{urlencode(params)}"
    log.info("GET %s", url)
    result = subprocess.run(
        [
            "curl",
            "--silent",
            "--show-error",
            "--max-time", "60",
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
    return feedparser.parse(body)


def get_pdf_url(entry) -> str | None:
    for link in entry.get("links", []):
        if link.get("title") == "pdf":
            return link.get("href")
    return None


def fetch_papers(config: dict) -> list[dict]:
    categories = config["arxiv_categories"]
    keywords = config["keywords"]

    # Build query: search across categories with keyword terms
    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
    keyword_query = " OR ".join(f'all:"{kw}"' for kw in keywords[:8])  # arXiv limits query length
    query = f"({cat_query}) AND ({keyword_query})"

    paper_db = load_paper_db()
    seen_ids = {normalize_arxiv_id(p["id"]) for p in paper_db}
    cutoff = get_cutoff(paper_db)

    papers = []
    cutoff_crossed = False
    for page_idx in range(MAX_PAGES):
        if page_idx > 0:
            log.info("Sleeping %d seconds before next page", PAGE_SLEEP_SECONDS)
            time.sleep(PAGE_SLEEP_SECONDS)

        start = page_idx * PAGE_SIZE
        feed = fetch_arxiv_page(query, start=start, max_results=PAGE_SIZE)
        log.info("Page %d: parsed %d entries (start=%d)", page_idx + 1, len(feed.entries), start)

        if not feed.entries:
            break

        for entry in feed.entries:
            published = datetime.fromisoformat(entry.published.replace("Z", "+00:00"))
            if published < cutoff:
                cutoff_crossed = True
                break

            if normalize_arxiv_id(entry.id) in seen_ids:
                continue

            title = entry.title
            abstract = entry.summary

            if not keyword_matches(f"{title} {abstract}", keywords):
                continue

            papers.append({
                "id": entry.id,
                "title": re.sub(r"\s+", " ", title).strip(),
                "abstract": re.sub(r"\s+", " ", abstract).strip(),
                "authors": [a.name for a in entry.authors[:10]],
                "published": published.isoformat(),
                "pdf_url": get_pdf_url(entry),
            })

        if cutoff_crossed:
            break
    else:
        log.warning("Hit MAX_PAGES=%d without crossing cutoff", MAX_PAGES)

    return papers


def main():
    config = load_config()
    papers = fetch_papers(config)
    json.dump(papers, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
