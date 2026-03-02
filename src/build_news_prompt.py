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
FULLTEXT_PATH = Path("/tmp/inf-eco-fulltexts.json")

MAX_NEWS_TEXT_CHARS = 15_000


def build_new_papers_section() -> str | None:
    """Build the New Papers section from scores + data/papers.json."""
    if not SCORES_PATH.exists() or SCORES_PATH.stat().st_size == 0:
        return None

    new_ids = {s["id"] for s in parse_scores(str(SCORES_PATH))}
    papers = {p["id"]: p for p in json.load(open(ROOT / "data" / "papers.json"))}

    # Use papers.json as source of truth (has full-text rescored scores + descriptions)
    merged = [papers[sid] for sid in new_ids if sid in papers]

    return (
        "## New Papers\n"
        "```json\n"
        f"{json.dumps(merged, indent=2)}\n"
        "```"
    )


def build_fulltexts_section() -> str | None:
    """Build the Full Texts section from saved extractions."""
    if not FULLTEXT_PATH.exists() or FULLTEXT_PATH.stat().st_size == 0:
        return None

    fulltexts = json.load(open(FULLTEXT_PATH))
    if not fulltexts:
        return None

    # Include texts for the top papers (by score in papers.json), truncated for context
    papers = {p["id"]: p for p in json.load(open(ROOT / "data" / "papers.json"))}
    ranked = sorted(fulltexts.keys(), key=lambda pid: papers.get(pid, {}).get("score", 0), reverse=True)

    parts = ["## Full Paper Texts", "Use these to write more insightful summaries than the abstract alone allows.", ""]
    for pid in ranked[:5]:
        p = papers.get(pid, {})
        text = fulltexts[pid][:MAX_NEWS_TEXT_CHARS]
        parts.append(f"### {p.get('title', pid)}")
        parts.append(f"ID: {pid}")
        parts.append("```")
        parts.append(text)
        parts.append("```")
        parts.append("")

    return "\n".join(parts)


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

    fulltexts = build_fulltexts_section()
    if fulltexts:
        print(fulltexts)
        print()


if __name__ == "__main__":
    main()
