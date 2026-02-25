#!/usr/bin/env python3
"""Fetch recent arXiv papers matching configured keywords and categories."""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import arxiv

ROOT = Path(__file__).resolve().parent.parent


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
    print(f"Fetching papers from the last {days} days (cutoff: {cutoff.date()})", file=sys.stderr)
    return cutoff


def keyword_matches(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


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

    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=2000,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    papers = []

    for result in client.results(search):
        if result.published.replace(tzinfo=timezone.utc) < cutoff:
            break

        # Skip already-scored papers
        if normalize_arxiv_id(result.entry_id) in seen_ids:
            continue

        title = result.title
        abstract = result.summary

        if not keyword_matches(f"{title} {abstract}", keywords):
            continue

        papers.append({
            "id": result.entry_id,
            "title": re.sub(r"\s+", " ", title).strip(),
            "abstract": re.sub(r"\s+", " ", abstract).strip(),
            "authors": [a.name for a in result.authors[:10]],
            "published": result.published.isoformat(),
            "pdf_url": result.pdf_url,
        })

    return papers


def main():
    config = load_config()
    papers = fetch_papers(config)
    json.dump(papers, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
