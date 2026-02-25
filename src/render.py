#!/usr/bin/env python3
"""Render data/papers.json into papers.md — a single living list sorted by score."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
OUTPUT_PATH = ROOT / "papers.md"
CONFIG_PATH = ROOT / "config.json"


def main():
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    threshold = config.get("relevance_threshold", 70)

    if not PAPERS_PATH.exists():
        papers = []
    else:
        with open(PAPERS_PATH) as f:
            papers = json.load(f)

    # Filter and sort: score descending, hype descending, then published date descending
    relevant = [p for p in papers if p["score"] >= threshold]
    relevant.sort(key=lambda p: (p["score"], p.get("hype", 0), p["published"]), reverse=True)

    lines = []
    lines.append(f"# {config['topic']}")
    lines.append("")
    lines.append(f"Automatically discovered papers scored for relevance to: {config['description']}")
    lines.append("")
    lines.append(f"**{len(relevant)}** papers above threshold ({threshold}/100) out of **{len(papers)}** total scanned.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for p in relevant:
        arxiv_id = p["id"].rsplit("/", 1)[-1]
        authors = p["authors"]
        if len(authors) > 3:
            author_str = ", ".join(authors[:3]) + " et al."
        else:
            author_str = ", ".join(authors)

        abstract_excerpt = p["abstract"][:200]
        if len(p["abstract"]) > 200:
            abstract_excerpt += "..."

        published_date = p["published"][:10]

        hype = p.get("hype", 0)

        lines.append(f"### {p['title']}")
        lines.append(f"**Relevance: {p['score']}/100 | Hype: {hype}/100** — {p['justification']}")
        lines.append(f"*Authors: {author_str}*")
        lines.append(f"*Published: {published_date}*")
        lines.append(f"[arXiv](https://arxiv.org/abs/{arxiv_id}) | [PDF]({p['pdf_url']})")
        lines.append("")
        lines.append(f"> {abstract_excerpt}")
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(OUTPUT_PATH, "w") as f:
        f.write("\n".join(lines))

    print(f"Rendered {len(relevant)} papers to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
