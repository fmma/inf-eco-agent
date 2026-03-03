#!/usr/bin/env python3
"""Build the hype-watch prompt from signal history.

Reads data/papers.json, filters to papers with signal history worth analyzing,
and outputs the complete prompt to stdout. Exits non-zero if no papers qualify.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
PROMPT_PATH = ROOT / "hype-prompt.md"
LAST_HYPE_PATH = ROOT / "data" / "last-hype-watch.md"

SIGNAL_KEYS = ["citations", "influential_citations", "hf_upvotes", "github_stars"]


def has_any_signals(history: list[dict]) -> bool:
    """Return True if any entry in the history has a non-zero signal."""
    return any(
        entry.get(k, 0) > 0
        for entry in history
        for k in SIGNAL_KEYS
    )


def format_paper(paper: dict) -> str:
    """Format a single paper's signal history for the prompt."""
    lines = []
    lines.append(f"### {paper['title']}")
    lines.append(f"- **ID**: {paper['id']}")
    if paper.get("authors"):
        lines.append(f"- **Authors**: {', '.join(paper['authors'][:5])}")
    lines.append(f"- **Relevance score**: {paper.get('score', 0)}")

    lines.append("- **Signal history**:")
    for entry in paper["hype_signal_history"]:
        parts = []
        for k in SIGNAL_KEYS:
            v = entry.get(k, 0)
            if v > 0:
                label = k.replace("_", " ")
                parts.append(f"{label}: {v}")
        signal_str = ", ".join(parts) if parts else "all zero"
        lines.append(f"  - {entry['date']}: {signal_str}")

    return "\n".join(lines)


def main():
    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    # Filter: papers with >1 history entry and any non-zero signals
    candidates = [
        p for p in papers
        if len(p.get("hype_signal_history", [])) > 1
        and has_any_signals(p["hype_signal_history"])
    ]

    if not candidates:
        print("No papers with signal history to analyze.", file=sys.stderr)
        sys.exit(1)

    # Sort by latest total signals descending
    def latest_total(p):
        last = p["hype_signal_history"][-1]
        return sum(last.get(k, 0) for k in SIGNAL_KEYS)

    candidates.sort(key=latest_total, reverse=True)

    prompt = PROMPT_PATH.read_text()

    print(prompt)
    print()

    if LAST_HYPE_PATH.exists():
        prev = LAST_HYPE_PATH.read_text().strip()
        if prev and prev != "NO_HYPE":
            print("## Previous Hype Watch Output")
            print()
            print(prev)
            print()

    print(f"## Papers with Signal History")
    print(f"{len(candidates)} papers with external signal timelines.")
    print()
    for paper in candidates:
        print(format_paper(paper))
        print()


if __name__ == "__main__":
    main()
