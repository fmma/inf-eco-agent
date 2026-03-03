#!/usr/bin/env python3
"""Build the news prompt by combining news-prompt.md with new paper data.

Outputs the complete prompt to stdout. Requires /tmp/inf-eco-scores.json
with new paper scores.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_scores import parse_scores

ROOT = Path(__file__).resolve().parent.parent
SCORES_PATH = Path("/tmp/inf-eco-scores.json")
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

    # Only pass top papers to avoid blowing up the context window.
    # News only highlights top 3-5 anyway.
    merged.sort(key=lambda p: (p.get("score", 0), p.get("hype", 0)), reverse=True)
    top = merged[:20]

    return (
        "## New Papers\n"
        f"{len(merged)} papers scanned, top {len(top)} shown below.\n"
        "```json\n"
        f"{json.dumps(top, indent=2)}\n"
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


def main():
    prompt = (ROOT / "news-prompt.md").read_text()

    new_papers = build_new_papers_section()
    if not new_papers:
        print("Error: no new papers to report on.", file=sys.stderr)
        sys.exit(1)

    # Provide exact count so Claude doesn't hallucinate it
    new_count = len(parse_scores(str(SCORES_PATH))) if SCORES_PATH.exists() and SCORES_PATH.stat().st_size > 0 else 0

    print(prompt)
    print()
    print(f"## Stats")
    print(f"- New papers scanned: {new_count}")
    print()
    print(new_papers)
    print()

    fulltexts = build_fulltexts_section()
    if fulltexts:
        print(fulltexts)
        print()


if __name__ == "__main__":
    main()
