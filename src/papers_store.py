"""The paper database: one JSON file per publication month in data/papers/.

A single file grows past the 100 MB that GitHub accepts per file.
"""

import json
from pathlib import Path

PAPERS_DIR = Path(__file__).resolve().parent.parent / "data" / "papers"


def load_papers() -> list[dict]:
    papers = []
    for path in sorted(PAPERS_DIR.glob("*.json")):
        with open(path) as f:
            papers.extend(json.load(f))
    return papers


def save_papers(papers: list[dict]) -> None:
    by_month: dict[str, list[dict]] = {}
    for paper in papers:
        by_month.setdefault(paper["published"][:7], []).append(paper)

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    for month, group in by_month.items():
        path = PAPERS_DIR / f"{month}.json"
        text = json.dumps(group, indent=2) + "\n"
        if not path.exists() or path.read_text() != text:
            path.write_text(text)
