#!/usr/bin/env python3
"""Build the hype-watch prompt from signal history.

Reads data/papers.json, picks the papers whose signals grew the most, and
outputs the complete prompt to stdout. Exits non-zero if no papers qualify.
"""

import json
import sys
from pathlib import Path

from rescore_hype import HISTORY_CAP

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
PROMPT_PATH = ROOT / "surge-prompt.md"
LAST_HYPE_PATH = ROOT / "data" / "last-hype-watch.md"

SIGNAL_KEYS = ["citations", "influential_citations", "hf_upvotes", "github_stars"]

# About 105k tokens at 1.9 chars per token. scan.sh turns the 1M context window off, so the request and the reply share 200k.
MAX_PAPERS_CHARS = 200_000


def clean_history(history: list[dict]) -> list[dict]:
    """Return the history with every signal set and failed fetches filled in.

    fetch_hype_signals.py stores 0 for a source that did not answer.
    A 0 after a positive value is such a gap, so the last value is carried forward.
    """
    cleaned = []
    last = dict.fromkeys(SIGNAL_KEYS, 0)
    for entry in history:
        last = {k: entry.get(k, 0) or last[k] for k in SIGNAL_KEYS}
        cleaned.append({"date": entry["date"], **last})
    return cleaned


def gain(history: list[dict]) -> int:
    """Total signal growth over the history. A falling signal does not cancel a rising one.

    A history shorter than the cap starts at the first observation of the paper, so it counts from zero.
    """
    first = history[0] if len(history) >= HISTORY_CAP else dict.fromkeys(SIGNAL_KEYS, 0)
    return sum(max(0, history[-1][k] - first[k]) for k in SIGNAL_KEYS)


def format_paper(paper: dict, history: list[dict]) -> str:
    """Format a single paper's signal history for the prompt."""
    lines = []
    lines.append(f"### {paper['title']}")
    lines.append(f"- **ID**: {paper['id']}")
    if paper.get("authors"):
        lines.append(f"- **Authors**: {', '.join(paper['authors'][:5])}")
    lines.append(f"- **Relevance score**: {paper.get('score', 0)}")

    lines.append("- **Signal history**:")
    runs = []
    for entry in history:
        signals = {k: entry[k] for k in SIGNAL_KEYS}
        if runs and runs[-1]["signals"] == signals:
            runs[-1]["end"] = entry["date"]
        else:
            runs.append({"start": entry["date"], "end": entry["date"], "signals": signals})
    for run in runs:
        parts = [f"{k.replace('_', ' ')}: {v}" for k, v in run["signals"].items() if v > 0]
        signal_str = ", ".join(parts) if parts else "all zero"
        span = run["start"] if run["start"] == run["end"] else f"{run['start']} to {run['end']}"
        lines.append(f"  - {span}: {signal_str}")

    return "\n".join(lines)


def select_papers(papers: list[dict], max_chars: int) -> tuple[list[str], int]:
    """Format the papers with the largest gain, as many as fit in max_chars.

    Returns the formatted papers and the number of papers that grew at all.
    """
    grew = []
    for paper in papers:
        if len(paper.get("hype_signal_history", [])) > 1:
            history = clean_history(paper["hype_signal_history"])
            if gain(history) > 0:
                grew.append((paper, history))

    def rank(item):
        history = item[1]
        return gain(history), sum(history[-1][k] for k in SIGNAL_KEYS)

    grew.sort(key=rank, reverse=True)

    blocks = []
    size = 0
    for paper, history in grew:
        block = format_paper(paper, history)
        size += len(block)
        if size > max_chars:
            break
        blocks.append(block)

    return blocks, len(grew)


def main():
    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    blocks, grew = select_papers(papers, MAX_PAPERS_CHARS)

    if not blocks:
        print("No papers with growing signals to analyze.", file=sys.stderr)
        sys.exit(1)

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

    print("## Papers with Signal History")
    print(f"The {len(blocks)} papers whose signals grew the most, of {grew} that grew, largest gain first.")
    print("Each history line is a period in which the signals did not change. A line with one date is a single observation.")
    print()
    for block in blocks:
        print(block)
        print()


if __name__ == "__main__":
    main()
