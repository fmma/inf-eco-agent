#!/usr/bin/env python3
"""Download PDFs for top papers, invoke Claude to generate news.

PDFs give Claude full-text context for writing better summaries.
Outputs: news.md.
"""

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
PROMPT_PATH = ROOT / "news-prompt.md"
NEWS_PATH = ROOT / "news.md"
SCORES_PATH = Path("/tmp/inf-eco-scores.json")
PDF_DIR = ROOT / "data" / "pdfs"

MAX_PDF_PAPERS = 8
MAX_NEWS_PAPERS = 20
SCORE_THRESHOLD = 70


def download_pdf(url: str, dest: Path) -> bool:
    """Download a PDF, return True on success."""
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        dest.write_bytes(resp.content)
        return True
    except requests.RequestException as e:
        print(f"  Warning: PDF download failed: {e}", file=sys.stderr)
        return False


def compress_pdf(path: Path) -> None:
    """Re-encode PDF in place at /ebook quality to keep request size under the
    Anthropic API's 20 MB per-request cap. Falls back to the original on
    failure or if gs produces a larger file."""
    before = path.stat().st_size
    tmp = path.with_suffix(".pdf.gs")
    try:
        subprocess.run(
            ["gs", "-dNOPAUSE", "-dBATCH", "-dQUIET",
             "-sDEVICE=pdfwrite", "-dPDFSETTINGS=/ebook",
             f"-sOutputFile={tmp}", str(path)],
            check=True, capture_output=True, timeout=60,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"  Warning: gs compression failed ({e}); using original", file=sys.stderr)
        tmp.unlink(missing_ok=True)
        return
    after = tmp.stat().st_size
    if after < before:
        tmp.replace(path)
        print(f"    compressed {before/1e6:.1f} MB -> {after/1e6:.1f} MB")
    else:
        tmp.unlink()


def find_top_papers(papers: list[dict], today: str) -> list[dict]:
    """Find top-scoring papers from today for PDF download."""
    candidates = [
        p for p in papers
        if p["score"] >= SCORE_THRESHOLD
        and p.get("scored_date") == today
    ]
    candidates.sort(key=lambda p: p["score"], reverse=True)
    return candidates[:MAX_PDF_PAPERS]


def find_new_paper_ids() -> set[str]:
    """Get IDs of papers scored this run (from the scores temp file)."""
    if not SCORES_PATH.exists() or SCORES_PATH.stat().st_size == 0:
        return set()
    sys.path.insert(0, str(Path(__file__).parent))
    from parse_scores import parse_scores
    return {s["id"] for s in parse_scores(str(SCORES_PATH))}


def build_papers_section(papers: list[dict], new_ids: set[str]) -> str:
    """Build metadata section for top papers."""
    merged = [p for p in papers if p["id"] in new_ids]
    merged.sort(key=lambda p: (p.get("score", 0), p.get("hype", 0)), reverse=True)
    top = merged[:MAX_NEWS_PAPERS]
    return (
        f"## New Papers\n"
        f"{len(merged)} papers scanned, top {len(top)} shown below.\n"
        f"```json\n{json.dumps(top, indent=2)}\n```"
    )


def build_pdf_section(top_papers: list[dict], pdf_paths: dict[str, Path]) -> str:
    """Build a section listing PDF paths for Claude to read."""
    lines = [
        "## Full-Text PDFs",
        "Read these PDFs for deeper context when writing the news.",
        ""
    ]
    for p in top_papers:
        pdf = pdf_paths.get(p["id"])
        if pdf:
            lines.append(f"- **{p['title']}** — `{pdf}`")
    lines.append("")
    return "\n".join(lines)


def build_prompt(papers: list[dict], top_papers: list[dict],
                 pdf_paths: dict[str, Path], new_ids: set[str]) -> str:
    """Build the full prompt combining template + data sections."""
    prompt = PROMPT_PATH.read_text()
    new_count = len(new_ids)

    sections = [prompt, ""]

    sections.append(f"## Stats")
    sections.append(f"- New papers scanned: {new_count}")
    sections.append("")

    if pdf_paths:
        sections.append(build_pdf_section(top_papers, pdf_paths))

    if new_ids:
        sections.append(build_papers_section(papers, new_ids))
        sections.append("")

    return "\n".join(sections)


def main():
    today = date.today().isoformat()

    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    new_ids = find_new_paper_ids()

    if not new_ids:
        print("No new papers — nothing to generate.")
        return

    # Download PDFs for top papers (context for better news)
    top_papers = find_top_papers(papers, today)
    pdf_paths: dict[str, Path] = {}

    if top_papers:
        if PDF_DIR.exists():
            for old in PDF_DIR.glob("*.pdf"):
                old.unlink()
        PDF_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Downloading PDFs for {len(top_papers)} papers...")

        for p in top_papers:
            arxiv_id = p["id"].rsplit("/", 1)[-1]
            dest = PDF_DIR / f"{arxiv_id}.pdf"
            print(f"  [{arxiv_id}] {p['title'][:60]}...")
            if download_pdf(p["pdf_url"], dest):
                compress_pdf(dest)
                pdf_paths[p["id"]] = dest

        total = sum(p.stat().st_size for p in pdf_paths.values())
        print(f"Total PDF payload: {total/1e6:.1f} MB")

    # Build prompt and invoke Claude
    prompt = build_prompt(papers, top_papers, pdf_paths, new_ids)

    print(f"Invoking Claude ({len(pdf_paths)} PDFs referenced in prompt)...")

    result = subprocess.run(
        ["claude", "--print", "--model", "claude-opus-4-8", "--effort", "max", "--allowedTools", "Read",
         "--append-system-prompt",
         "You have the Read tool available. Use it to read PDF files when asked. "
         "Do not claim that tools are unavailable or that you cannot read PDFs."],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600,
    )

    if result.returncode != 0:
        print(f"Error: Claude returned exit code {result.returncode}", file=sys.stderr)
        if result.stderr:
            print(f"stderr: {result.stderr[:2000]}", file=sys.stderr)
        if result.stdout:
            print(f"stdout: {result.stdout[:2000]}", file=sys.stderr)
        sys.exit(1)

    news = result.stdout.strip()
    if not news:
        print("Error: Claude returned empty output", file=sys.stderr)
        if result.stderr:
            print(f"stderr: {result.stderr[:2000]}", file=sys.stderr)
        sys.exit(1)

    NEWS_PATH.write_text(news + "\n")
    print(f"Wrote {NEWS_PATH}")


if __name__ == "__main__":
    main()
