#!/usr/bin/env python3
"""Update hype signals from external sources and maintain signal history.

Appends today's observation to hype_signal_history (rolling window of 30).
Does NOT overwrite Claude's predicted hype/hype_justification.
"""

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
SIGNALS_PATH = Path("/tmp/inf-eco-hype-signals.json")

HISTORY_CAP = 30
SIGNAL_KEYS = ["citations", "influential_citations", "hf_upvotes", "github_stars"]


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

    signals_by_id = {s["id"]: s for s in signals_list}
    today = date.today().isoformat()

    updated_count = 0
    for paper in papers:
        signals = signals_by_id.get(paper["id"])
        if signals is None:
            continue

        new_signals = {k: signals[k] for k in SIGNAL_KEYS}

        # Migrate: seed history from existing hype_signals if no history yet
        history = paper.get("hype_signal_history", [])
        if not history and paper.get("hype_signals"):
            old = paper["hype_signals"]
            prev_date = paper.get("hype_signals_prev_date", "unknown")
            history.append({"date": prev_date, **{k: old.get(k, 0) for k in SIGNAL_KEYS}})

        # Deduplicate: update in-place if today already present
        observation = {"date": today, **new_signals}
        replaced = False
        for i, entry in enumerate(history):
            if entry["date"] == today:
                history[i] = observation
                replaced = True
                break
        if not replaced:
            history.append(observation)

        # Cap at rolling window
        if len(history) > HISTORY_CAP:
            history = history[-HISTORY_CAP:]

        paper["hype_signal_history"] = history
        paper["hype_signals"] = new_signals

        # Clean up legacy field
        paper.pop("hype_signals_prev", None)
        paper.pop("hype_signals_prev_date", None)

        updated_count += 1

    with open(PAPERS_PATH, "w") as f:
        json.dump(papers, f, indent=2)
        f.write("\n")

    print(f"Updated signals for {updated_count} papers (of {len(signals_list)} with signals).")


if __name__ == "__main__":
    main()
