#!/usr/bin/env python3
"""Fetch recent arXiv papers matching configured keywords and categories."""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import arxiv


def load_config():
    config_path = Path(__file__).resolve().parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)


def keyword_matches(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def fetch_papers(config: dict) -> list[dict]:
    categories = config["arxiv_categories"]
    keywords = config["keywords"]
    max_papers = config.get("max_papers", 100)

    # Build query: search across categories with keyword terms
    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
    keyword_query = " OR ".join(f'all:"{kw}"' for kw in keywords[:8])  # arXiv limits query length
    query = f"({cat_query}) AND ({keyword_query})"

    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_papers * 3,  # fetch extra, we'll filter down
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    cutoff = datetime.now(timezone.utc) - timedelta(days=3)
    papers = []

    for result in client.results(search):
        if result.published.replace(tzinfo=timezone.utc) < cutoff:
            break

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

        if len(papers) >= max_papers:
            break

    return papers


def main():
    config = load_config()
    papers = fetch_papers(config)
    json.dump(papers, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
