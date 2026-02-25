#!/usr/bin/env python3
"""Query Semantic Scholar and HuggingFace for external hype signals on scored papers."""

import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "data" / "papers.json"
CONFIG_PATH = ROOT / "config.json"
OUTPUT_PATH = Path("/tmp/inf-eco-hype-signals.json")

S2_BATCH_URL = "https://api.semanticscholar.org/graph/v1/paper/batch"
HF_PAPERS_URL = "https://huggingface.co/api/papers"


def extract_arxiv_id(entry_id: str) -> str:
    """Extract bare arXiv ID (with version) from full URL or ID string."""
    # "http://arxiv.org/abs/2602.20515v1" → "2602.20515v1"
    return entry_id.rsplit("/", 1)[-1]


def extract_arxiv_id_bare(entry_id: str) -> str:
    """Extract bare arXiv ID (without version) from full URL or ID string."""
    raw = extract_arxiv_id(entry_id)
    return re.sub(r"v\d+$", "", raw)


def fetch_semantic_scholar(arxiv_ids: list[str]) -> dict[str, dict]:
    """Batch-fetch citation counts from Semantic Scholar.

    Returns dict keyed by bare arXiv ID.
    """
    results = {}
    # S2 batch endpoint accepts up to 500 IDs per request
    batch_size = 500
    for i in range(0, len(arxiv_ids), batch_size):
        batch = arxiv_ids[i : i + batch_size]
        paper_ids = [f"ArXiv:{aid}" for aid in batch]
        try:
            resp = requests.post(
                S2_BATCH_URL,
                json={"ids": paper_ids},
                params={"fields": "citationCount,influentialCitationCount"},
                timeout=30,
            )
            resp.raise_for_status()
            for paper, aid in zip(resp.json(), batch):
                if paper is None:
                    continue
                results[aid] = {
                    "citations": paper.get("citationCount", 0) or 0,
                    "influential_citations": paper.get("influentialCitationCount", 0) or 0,
                }
        except requests.RequestException as e:
            print(f"Warning: Semantic Scholar batch failed: {e}", file=sys.stderr)

        # Rate-limit: be polite
        if i + batch_size < len(arxiv_ids):
            time.sleep(1)

    return results


def fetch_huggingface(arxiv_ids: list[str]) -> dict[str, dict]:
    """Fetch upvotes and GitHub stars from HuggingFace Papers API.

    Returns dict keyed by bare arXiv ID.
    """
    results = {}
    for aid in arxiv_ids:
        try:
            resp = requests.get(f"{HF_PAPERS_URL}/{aid}", timeout=10)
            if resp.status_code == 404:
                continue
            resp.raise_for_status()
            data = resp.json()
            results[aid] = {
                "hf_upvotes": data.get("upvotes", 0) or 0,
                "github_stars": data.get("githubStars", 0) or 0,
            }
        except requests.RequestException:
            continue

        # Rate-limit: be polite
        time.sleep(0.2)

    return results


def main():
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    threshold = config.get("relevance_threshold", 70)

    if not PAPERS_PATH.exists():
        print("No papers.json found.", file=sys.stderr)
        sys.exit(1)

    with open(PAPERS_PATH) as f:
        papers = json.load(f)

    # Only fetch signals for papers above the relevance threshold
    relevant = [p for p in papers if p["score"] >= threshold]
    if not relevant:
        print("No relevant papers to fetch signals for.")
        json.dump([], OUTPUT_PATH.open("w"), indent=2)
        return

    # Extract bare arXiv IDs (without version) for API lookups
    id_map = {}  # bare_id → original entry_id
    for p in relevant:
        bare = extract_arxiv_id_bare(p["id"])
        id_map[bare] = p["id"]

    bare_ids = list(id_map.keys())
    print(f"Fetching signals for {len(bare_ids)} papers...")

    # Fetch from both APIs
    s2_data = fetch_semantic_scholar(bare_ids)
    hf_data = fetch_huggingface(bare_ids)

    # Combine signals
    signals = []
    for bare_id, entry_id in id_map.items():
        s2 = s2_data.get(bare_id, {})
        hf = hf_data.get(bare_id, {})

        # Skip papers with no signals at all
        if not s2 and not hf:
            continue

        signals.append({
            "id": entry_id,
            "citations": s2.get("citations", 0),
            "influential_citations": s2.get("influential_citations", 0),
            "hf_upvotes": hf.get("hf_upvotes", 0),
            "github_stars": hf.get("github_stars", 0),
        })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(signals, f, indent=2)
        f.write("\n")

    print(f"Wrote signals for {len(signals)} papers to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
