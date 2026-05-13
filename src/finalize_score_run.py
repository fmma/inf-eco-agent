#!/usr/bin/env python3
"""Concatenate processed queue batches and their Claude scores for merge_papers.

Reads a list of batch file paths (one per line), and for each looks up the
corresponding `/tmp/inf-eco-scores-out-<name>.json` produced by scan.sh.
Writes a combined papers JSON and a combined scores JSON ready to feed into
merge_papers.py.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_scores import parse_scores


def main():
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <batch-list> <papers-out> <scores-out>",
            file=sys.stderr,
        )
        sys.exit(1)

    list_path, papers_out, scores_out = sys.argv[1], sys.argv[2], sys.argv[3]
    batch_paths = [
        line.strip() for line in open(list_path).read().splitlines() if line.strip()
    ]

    papers: list[dict] = []
    scores: list[dict] = []
    for batch_path in batch_paths:
        with open(batch_path) as f:
            papers.extend(json.load(f))
        score_file = f"/tmp/inf-eco-scores-out-{Path(batch_path).stem}.json"
        scores.extend(parse_scores(score_file))

    with open(papers_out, "w") as f:
        json.dump(papers, f, indent=2)
    with open(scores_out, "w") as f:
        json.dump(scores, f, indent=2)
    print(
        f"Finalized {len(papers)} papers, {len(scores)} scores "
        f"from {len(batch_paths)} batch(es)"
    )


if __name__ == "__main__":
    main()
