#!/usr/bin/env python3
"""Parse Claude's score output, stripping markdown fences and validating structure."""

import json
import sys


def parse_scores(path: str) -> list[dict]:
    """Read a scores JSON file, strip markdown fences, and return parsed list.

    Exits with a clear error message on failure.
    """
    try:
        raw = open(path).read()
    except FileNotFoundError:
        _die(f"Scores file not found: {path}")
    except OSError as e:
        _die(f"Cannot read scores file {path}: {e}")

    if not raw.strip():
        _die(f"Scores file is empty: {path}")

    # Strip markdown code fences if Claude wrapped the JSON output
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]  # remove opening ```json line
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0].strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        preview = raw[:300].replace("\n", "\\n")
        _die(f"Scores file is not valid JSON: {e}\nFile preview: {preview}")

    if not isinstance(data, list):
        _die(f"Expected a JSON array, got {type(data).__name__}")

    for i, entry in enumerate(data):
        if not isinstance(entry, dict) or "id" not in entry:
            _die(f"Entry {i} is missing 'id' field: {entry!r:.200}")

    return data


def _die(msg: str):
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)
