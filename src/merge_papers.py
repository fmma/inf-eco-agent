#!/usr/bin/env python3
"""Merge Claude's scores with fetched paper metadata into the paper database."""

import json
import sys
from datetime import date

from papers_store import load_papers, save_papers
from parse_scores import parse_scores


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <new-papers.json> <scores.json>", file=sys.stderr)
        sys.exit(1)

    new_papers_path = sys.argv[1]
    scores_path = sys.argv[2]

    with open(new_papers_path) as f:
        new_papers = json.load(f)

    scores = parse_scores(scores_path)

    # Build lookup: id → score info
    score_by_id = {s["id"]: s for s in scores}

    all_papers = load_papers()

    today = date.today().isoformat()
    existing_ids = {p["id"] for p in all_papers}

    # Merge: join new papers with their scores, skipping duplicates
    added = 0
    for paper in new_papers:
        score_info = score_by_id.get(paper["id"])
        if score_info is None:
            continue

        if paper["id"] in existing_ids:
            continue

        added += 1
        existing_ids.add(paper["id"])
        all_papers.append({
            "id": paper["id"],
            "title": paper["title"],
            "score": score_info["score"],
            "justification": score_info["justification"],
            "hype": score_info.get("hype", 0),
            "hype_justification": score_info.get("hype_justification", ""),
            "authors": paper["authors"],
            "published": paper["published"],
            "pdf_url": paper["pdf_url"],
            "abstract": paper["abstract"],
            "scored_date": today,
        })

    save_papers(all_papers)

    skipped = len(new_papers) - added
    if skipped:
        print(f"Skipped {skipped} duplicate papers.", file=sys.stderr)
    print(f"Merged {added} new papers. Total: {len(all_papers)}")


if __name__ == "__main__":
    main()
