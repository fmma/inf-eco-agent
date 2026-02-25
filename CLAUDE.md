# Inference Ecosystem Paper Scanner

This repo is an automated agent that discovers new arXiv papers about LLM inference systems.

## How it works

### Pipeline (scan.sh)

1. `src/fetch_papers.py` queries arXiv for recent papers, skipping IDs already in `data/papers.json`. Lookback window is adaptive: based on last `scored_date` + 1-day overlap, minimum 3 days.
2. If new papers found: Claude Code (`claude --print`) scores each paper 0–100 for relevance **and** 0–100 for predicted hype.
3. `src/merge_papers.py` merges scores into `data/papers.json`.
4. `src/fetch_hype_signals.py` queries Semantic Scholar and HuggingFace for external signals (citations, upvotes, GitHub stars) on all relevant papers.
5. `src/rescore_hype.py` computes observed hype from signals using a deterministic formula, updating `data/papers.json` (never downgrades). Surges (jump >= 20) are tracked.
6. `src/render.py` regenerates `papers.md` — the single living list sorted by score, with hype as tiebreaker.
7. If there are new papers or hype surges: `src/build_news_prompt.py` combines both into a single prompt, and Claude Code generates `news.md`.
8. `scan.sh` commits, pushes, and posts `news.md` to Discord via OpenClaw.

### Error handling

- `set -eo pipefail` catches all failures including in pipelines.
- ERR trap distinguishes no-internet (silent exit for systemd retry) from real errors (Discord notification with exit code, line number, and journalctl command).

### Scheduling

- systemd user timer (`inf-eco-scan.timer`) fires daily at 08:00 CET with `Persistent=true` (catches up after sleep/shutdown).
- systemd user service (`inf-eco-scan.service`) retries on failure every 5 min, up to 6 times per hour.
- Discord notifications via OpenClaw (`DISCORD_CHANNEL` env var in the service).

## Key files

- `config.json` — Topic definition, arXiv categories, keywords, scoring threshold (0–100)
- `src/fetch_papers.py` — Fetches papers from arXiv, deduplicates, adaptive lookback window
- `src/merge_papers.py` — Merges Claude's scores (relevance + hype) into the paper database
- `src/render.py` — Renders `papers.md` from `data/papers.json`
- `src/fetch_hype_signals.py` — Queries Semantic Scholar + HuggingFace for external hype signals
- `src/rescore_hype.py` — Computes observed hype from external signals, updates `data/papers.json`
- `src/build_news_prompt.py` — Builds combined news prompt from new papers and/or hype surges
- `src/parse_scores.py` — Shared helper: strips markdown fences, parses and validates score JSON
- `prompt.md` — The prompt used when invoking Claude Code for scoring (JSON output only)
- `news-prompt.md` — The prompt used when invoking Claude Code for news generation (markdown output)
- `scan.sh` — Entry point that orchestrates the full pipeline
- `data/papers.json` — Source of truth: all scored papers across runs
- `papers.md` — Generated output: the living paper list
- `news.md` — Generated output: flash-news bulletin posted to Discord
