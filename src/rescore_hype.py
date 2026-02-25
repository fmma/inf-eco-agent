#!/usr/bin/env python3
"""Compute observed hype scores from external signals and update data/papers.json."""

import json
import sys
from math import log2
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
SIGNALS_PATH = Path("/tmp/inf-eco-hype-signals.json")
SURGES_PATH = Path("/tmp/inf-eco-hype-surges.json")

# Minimum hype jump to count as a "surge"
SURGE_THRESHOLD = 20


def compute_hype(citations: int, influential_citations: int, hf_upvotes: int, github_stars: int) -> int:
    """Deterministic hype formula based on external signals."""
    score = (
        25 * log2(1 + citations)
        + 15 * log2(1 + influential_citations)
        + 10 * log2(1 + hf_upvotes)
        + 8 * log2(1 + github_stars / 10)
    )
    return min(100, round(score))


def format_justification(signals: dict) -> str:
    """Format a human-readable summary of the hype signals."""
    parts = []
    if signals["citations"] > 0:
        parts.append(f"{signals['citations']} citations")
    if signals["influential_citations"] > 0:
        parts.append(f"{signals['influential_citations']} influential")
    if signals["hf_upvotes"] > 0:
        parts.append(f"{signals['hf_upvotes']} HF upvotes")
    if signals["github_stars"] > 0:
        parts.append(f"{signals['github_stars']} GitHub stars")
    if not parts:
        return "No external signals yet."
    return f"Observed: {', '.join(parts)}."


def main():
    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    if not SIGNALS_PATH.exists():
        print("No signals file found. Run fetch_hype_signals.py first.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    with open(SIGNALS_PATH) as f:
        signals_list = json.load(f)

    # Build lookup: id → signals
    signals_by_id = {s["id"]: s for s in signals_list}

    updated_count = 0
    surges = []
    for paper in papers:
        signals = signals_by_id.get(paper["id"])
        if signals is None:
            continue

        observed_hype = compute_hype(
            citations=signals["citations"],
            influential_citations=signals["influential_citations"],
            hf_upvotes=signals["hf_upvotes"],
            github_stars=signals["github_stars"],
        )

        current_hype = paper.get("hype", 0)
        jump = observed_hype - current_hype

        # Only upgrade, never downgrade
        if observed_hype > current_hype:
            paper["hype"] = observed_hype
            paper["hype_justification"] = format_justification(signals)
            updated_count += 1

            # Track significant surges for news generation
            if jump >= SURGE_THRESHOLD:
                surges.append({
                    "id": paper["id"],
                    "title": paper["title"],
                    "score": paper.get("score", 0),
                    "hype_old": current_hype,
                    "hype_new": observed_hype,
                    "hype_jump": jump,
                    "hype_justification": paper["hype_justification"],
                    "signals": {
                        "citations": signals["citations"],
                        "influential_citations": signals["influential_citations"],
                        "hf_upvotes": signals["hf_upvotes"],
                        "github_stars": signals["github_stars"],
                    },
                })

        # Always store raw signals for reference
        paper["hype_signals"] = {
            "citations": signals["citations"],
            "influential_citations": signals["influential_citations"],
            "hf_upvotes": signals["hf_upvotes"],
            "github_stars": signals["github_stars"],
        }

    with open(PAPERS_PATH, "w") as f:
        json.dump(papers, f, indent=2)
        f.write("\n")

    # Write surges for news generation
    surges.sort(key=lambda s: s["hype_jump"], reverse=True)
    with open(SURGES_PATH, "w") as f:
        json.dump(surges, f, indent=2)
        f.write("\n")

    print(f"Re-scored hype for {updated_count} papers (of {len(signals_list)} with signals).")
    if surges:
        print(f"Detected {len(surges)} hype surges (jump >= {SURGE_THRESHOLD}).")


if __name__ == "__main__":
    main()
