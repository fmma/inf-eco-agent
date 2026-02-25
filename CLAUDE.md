# Inference Ecosystem Paper Scanner

This repo is an automated agent that discovers new arXiv papers about LLM inference systems.

## How it works

### Pipeline (scan.sh)

1. `src/fetch_papers.py` queries arXiv for recent papers, skipping IDs already in `data/papers.json`
2. If new papers found: Claude Code (`claude --print`) scores each paper 0–100 for relevance **and** 0–100 for predicted hype
3. `src/merge_papers.py` merges scores (including `hype` and `hype_justification`) into `data/papers.json`
4. `src/fetch_hype_signals.py` queries Semantic Scholar and HuggingFace for external signals (citations, upvotes, GitHub stars)
5. `src/rescore_hype.py` computes observed hype from signals using a deterministic formula, updating `data/papers.json` (never downgrades)
6. `src/render.py` regenerates `papers.md` — the single living list sorted by score, with hype as tiebreaker
7. `src/build_news_prompt.py` combines new papers and/or hype surges into a single prompt
8. Claude Code generates `news.md` — an editorial covering both new papers and hype surges
9. `scan.sh` commits and pushes

## Key files

- `config.json` — Topic definition, arXiv categories, keywords, scoring threshold (0–100)
- `src/fetch_papers.py` — Fetches papers from arXiv, deduplicates against `data/papers.json`
- `src/merge_papers.py` — Merges Claude's scores (relevance + hype) into the paper database
- `src/render.py` — Renders `papers.md` from `data/papers.json`
- `src/fetch_hype_signals.py` — Queries Semantic Scholar + HuggingFace for external hype signals
- `src/rescore_hype.py` — Computes observed hype from external signals, updates `data/papers.json`
- `src/build_news_prompt.py` — Builds combined news prompt from new papers and/or hype surges
- `src/parse_scores.py` — Shared helper: strips markdown fences, parses and validates score JSON
- `prompt.md` — The prompt used when invoking Claude Code for scoring (JSON output only)
- `scan.sh` — Entry point that orchestrates the full pipeline (scan + rescore + news)
- `data/papers.json` — Source of truth: all scored papers across runs
- `news-prompt.md` — The prompt used when invoking Claude Code for news generation (markdown output)
- `papers.md` — Generated output: the living paper list
- `news.md` — Generated output: per-run editorial analysis of new papers
