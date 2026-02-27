#!/usr/bin/env python3
"""Build the news prompt by combining news-prompt.md with available data sections.

Outputs the complete prompt to stdout. Includes:
- New Papers section if /tmp/inf-eco-scores.json exists
- Hype Surges section if /tmp/inf-eco-hype-surges.json exists

At least one section must be available.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_scores import parse_scores

ROOT = Path(__file__).resolve().parent.parent
SCORES_PATH = Path("/tmp/inf-eco-scores.json")
SURGES_PATH = Path("/tmp/inf-eco-hype-surges.json")


def build_new_papers_section() -> str | None:
    """Build the New Papers section from scores + data/papers.json."""
    if not SCORES_PATH.exists() or SCORES_PATH.stat().st_size == 0:
        return None

    scores = {s["id"]: s for s in parse_scores(str(SCORES_PATH))}
    papers = {p["id"]: p for p in json.load(open(ROOT / "data" / "papers.json"))}

    merged = []
    for sid, s in scores.items():
        p = papers.get(sid, {})
        merged.append({
            **p,
            "score": s.get("score", 0),
            "justification": s.get("justification", ""),
            "hype": s.get("hype", 0),
            "hype_justification": s.get("hype_justification", ""),
        })

    return (
        "## New Papers\n"
        "```json\n"
        f"{json.dumps(merged, indent=2)}\n"
        "```"
    )


def build_surges_section() -> str | None:
    """Build the Hype Surges section from the surges temp file."""
    if not SURGES_PATH.exists() or SURGES_PATH.stat().st_size == 0:
        return None

    surges = json.load(open(SURGES_PATH))
    if not surges:
        return None

    return (
        "## Hype Surges\n"
        "These previously known papers have seen significant jumps in external signals since last check.\n"
        "```json\n"
        f"{json.dumps(surges, indent=2)}\n"
        "```"
    )


def main():
    prompt = (ROOT / "news-prompt.md").read_text()

    sections = []
    new_papers = build_new_papers_section()
    if new_papers:
        sections.append(new_papers)
    surges = build_surges_section()
    if surges:
        sections.append(surges)

    if not sections:
        print("Error: no new papers or hype surges to report on.", file=sys.stderr)
        sys.exit(1)

    print(prompt)
    print()
    for section in sections:
        print(section)
        print()

    if not surges:
        print("## Hype Surges")
        print("No hype surges detected this cycle — no previously known papers saw significant signal jumps.")
        print()


if __name__ == "__main__":
    main()
