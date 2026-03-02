#!/usr/bin/env python3
"""Download PDFs for high-relevance papers, extract full text, and rescore via Claude."""

import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

import fitz  # PyMuPDF
import requests

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
CONFIG_PATH = ROOT / "config.json"
RESCORE_PROMPT_PATH = ROOT / "rescore-prompt.md"
FULLTEXT_PATH = Path("/tmp/inf-eco-fulltexts.json")

MAX_PAPERS = 8
MAX_TEXT_CHARS = 80_000
SCORE_THRESHOLD = 70


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from PDF bytes using PyMuPDF, truncated to MAX_TEXT_CHARS."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    parts = []
    total = 0
    for page in doc:
        text = page.get_text()
        if total + len(text) > MAX_TEXT_CHARS:
            parts.append(text[: MAX_TEXT_CHARS - total])
            break
        parts.append(text)
        total += len(text)
    doc.close()
    return "".join(parts)


def download_pdf(url: str) -> bytes:
    """Download a PDF from the given URL."""
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.content


def rescore_paper(paper: dict, full_text: str) -> dict | None:
    """Call Claude to rescore a single paper given its full text.

    Returns parsed JSON dict or None on failure.
    """
    prompt_template = RESCORE_PROMPT_PATH.read_text()

    prompt = (
        f"{prompt_template}\n\n"
        f"## Paper Metadata\n\n"
        f"- **ID**: {paper['id']}\n"
        f"- **Title**: {paper['title']}\n"
        f"- **Authors**: {', '.join(paper['authors'])}\n"
        f"- **Abstract**: {paper['abstract']}\n"
        f"- **Previous score**: {paper['score']}\n\n"
        f"## Full Text\n\n"
        f"```\n{full_text}\n```\n"
    )

    try:
        result = subprocess.run(
            ["claude", "--print"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(f"  Warning: Claude returned exit code {result.returncode}", file=sys.stderr)
            return None

        raw = result.stdout.strip()
        # Strip markdown fences if present
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw.rsplit("```", 1)[0].strip()

        data = json.loads(raw)
        if not isinstance(data, dict) or "score" not in data:
            print(f"  Warning: unexpected response structure", file=sys.stderr)
            return None
        return data

    except subprocess.TimeoutExpired:
        print(f"  Warning: Claude timed out", file=sys.stderr)
        return None
    except (json.JSONDecodeError, Exception) as e:
        print(f"  Warning: failed to parse Claude response: {e}", file=sys.stderr)
        return None


def main():
    today = date.today().isoformat()

    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    # Find candidates: scored today, score >= threshold, not already rescored
    candidates = [
        p for p in papers
        if p["score"] >= SCORE_THRESHOLD
        and p.get("scored_date") == today
        and not p.get("fulltext_rescored")
    ]

    if not candidates:
        print("No papers eligible for full-text rescore.")
        return

    # Take the top N by score
    candidates.sort(key=lambda p: p["score"], reverse=True)
    candidates = candidates[:MAX_PAPERS]

    print(f"Full-text rescoring {len(candidates)} papers...")

    # Build index for updating papers in-place
    paper_by_id = {p["id"]: p for p in papers}
    fulltexts = {}  # id → extracted text (saved for news generation)
    rescored = 0

    for paper in candidates:
        arxiv_id = paper["id"].rsplit("/", 1)[-1]
        print(f"  [{arxiv_id}] {paper['title'][:60]}...")

        # Download PDF
        try:
            pdf_bytes = download_pdf(paper["pdf_url"])
        except requests.RequestException as e:
            print(f"  Warning: PDF download failed: {e}", file=sys.stderr)
            continue

        # Extract text
        try:
            full_text = extract_text_from_pdf(pdf_bytes)
        except Exception as e:
            print(f"  Warning: PDF text extraction failed: {e}", file=sys.stderr)
            continue

        if not full_text.strip():
            print(f"  Warning: no text extracted from PDF", file=sys.stderr)
            continue

        fulltexts[paper["id"]] = full_text

        # Rescore via Claude
        result = rescore_paper(paper, full_text)
        if result is None:
            continue

        # Update paper in-place
        target = paper_by_id[paper["id"]]
        target["score"] = result["score"]
        target["justification"] = result.get("justification", target["justification"])
        target["hype"] = result.get("hype", target.get("hype", 0))
        target["hype_justification"] = result.get("hype_justification", target.get("hype_justification", ""))
        target["description"] = result.get("description", "")
        target["fulltext_rescored"] = True
        rescored += 1

        print(f"  Rescored: {paper['score']} → {result['score']}")

    # Write back
    with open(PAPERS_PATH, "w") as f:
        json.dump(papers, f, indent=2)
        f.write("\n")

    # Save extracted texts for downstream use (news generation)
    with open(FULLTEXT_PATH, "w") as f:
        json.dump(fulltexts, f)

    print(f"Full-text rescored {rescored}/{len(candidates)} papers.")


if __name__ == "__main__":
    main()
