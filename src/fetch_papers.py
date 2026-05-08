#!/usr/bin/env python3
"""Fetch recent arXiv papers matching configured keywords and categories.

Direct HTTP call against the arXiv API, parsed with feedparser. Bypasses
the arxiv python library so we control retry, UA, and 429 handling.
"""

import json
import logging
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode

import feedparser
import requests

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("fetch_papers")

ROOT = Path(__file__).resolve().parent.parent
ARXIV_API = "https://export.arxiv.org/api/query"
USER_AGENT = "inf-eco-agent/1.0 (mailto:frederik.meisner@gmail.com)"
TRANSIENT_STATUSES = {429, 500, 502, 503, 504}


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


def fetch_arxiv_feed(query: str, max_results: int) -> feedparser.FeedParserDict:
    """Make a single GET against the arXiv API and parse the Atom response."""
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": 0,
        "max_results": max_results,
    }
    url = f"{ARXIV_API}?{urlencode(params)}"
    log.info("GET %s", url)
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=60)
    log.info("HTTP %d (%d bytes)", resp.status_code, len(resp.content))
    resp.raise_for_status()
    return feedparser.parse(resp.content)


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

    feed = fetch_arxiv_feed(query, max_results=500)
    log.info("Parsed %d entries from feed", len(feed.entries))

    papers = []
    for entry in feed.entries:
        published = datetime.fromisoformat(entry.published.replace("Z", "+00:00"))
        if published < cutoff:
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
    return papers


def main():
    config = load_config()
    try:
        papers = fetch_papers(config)
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else None
        if status in TRANSIENT_STATUSES:
            log.warning("arXiv returned %s; emitting empty list (skip-day)", status)
            json.dump([], sys.stdout)
            sys.stdout.write("\n")
            return
        raise
    json.dump(papers, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
