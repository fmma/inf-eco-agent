# Inference Ecosystem Paper Scanner

This repo is an automated agent that discovers new arXiv papers about LLM inference systems.

## How it works

### Pipeline (scan.sh)

1. `src/fetch_papers.py` queries arXiv for recent papers, skipping IDs already in `data/papers.json`. Lookback window is adaptive: based on last `scored_date` + 1-day overlap, minimum 3 days.
2. If new papers found: Claude Code (`claude --print`) scores each paper 0–100 for relevance **and** 0–100 for predicted hype.
3. `src/merge_papers.py` merges scores into `data/papers.json`.
4. `src/fetch_hype_signals.py` queries Semantic Scholar and HuggingFace for external signals (citations, upvotes, GitHub stars) on all relevant papers.
5. `src/rescore_hype.py` appends today's signals to `hype_signal_history` (rolling window of 30 entries). Does **not** overwrite Claude's predicted `hype`/`hype_justification`.
6. `src/build_hype_prompt.py` builds a prompt with full signal timelines for papers that have history. Claude analyzes trends and decides what's noteworthy (or outputs `NO_HYPE`).
7. If new papers: `src/generate_news.py` downloads PDFs for top papers, invokes Claude with `--allowedTools "Read"` to read them, qualitatively rescores relevance, and generates flash news.
8. Surge Watch section is always appended to `news.md` — Claude's hype analysis if noteworthy, or a "nothing to report" message.
9. `scan.sh` commits, pushes, and posts `news.md` to Discord via OpenClaw.

### Error handling

- `set -eo pipefail` catches all failures including in pipelines.
- ERR trap distinguishes no-internet (silent exit for systemd retry) from real errors (Discord notification with exit code, line number, and journalctl command).

### Scheduling

- systemd user timer (`inf-eco-scan.timer`) fires daily at 08:00 CET with `Persistent=true` (catches up after sleep/shutdown).
- One attempt per day. No automatic retries.
- Discord notifications via OpenClaw (`DISCORD_CHANNEL` env var in the service).

### Deployment

The agent runs on the remote host `foadell` at `~/inf-eco-agent`. Code is deployed via git, not rsync.

- `scan.sh` runs `git pull --rebase` at startup, so foadell always gets the latest code before each scan.
- `deploy.sh` triggers a `git pull --ff-only` on foadell for immediate deploys. It refuses to run if the local repo has uncommitted or unpushed changes.
- To deploy: commit and push changes, then run `bash deploy.sh`. Or just push and let the next scheduled scan pick it up.
- If a previous scan crashed mid-run, `git checkout -- .` at the top of `scan.sh` discards uncommitted changes. Unpushed commits (scored data) are preserved via rebase.

Avoid rsyncing files to foadell. It creates unstaged changes that break `git pull --rebase`.

### arXiv rate limits

arXiv aggressively rate-limits and bans IPs. The fetch step uses conservative settings: `page_size=200`, `delay_seconds=20`, `num_retries=1`. Do not increase retries or decrease delay. There is no application-level retry logic; if arXiv returns an error, the scan fails and retries the next day.

## Key files

- `config.json` — Topic definition, arXiv categories, keywords, scoring threshold (0–100)
- `src/fetch_papers.py` — Fetches papers from arXiv, deduplicates, adaptive lookback window
- `src/merge_papers.py` — Merges Claude's scores (relevance + hype) into the paper database
- `src/fetch_hype_signals.py` — Queries Semantic Scholar + HuggingFace for external hype signals
- `src/rescore_hype.py` — Appends today's signals to `hype_signal_history` (rolling window of 30), keeps `hype_signals` as latest snapshot
- `src/build_hype_prompt.py` — Builds prompt with signal history timelines for Claude to analyze trends
- `src/generate_news.py` — Downloads PDFs, rescores relevance via Claude (`--allowedTools "Read"`), generates flash news
- `src/parse_scores.py` — Shared helper: strips markdown fences, parses and validates score JSON
- `score-prompt.md` — The prompt used when invoking Claude Code for scoring (JSON output only)
- `news-prompt.md` — The prompt used for PDF rescore + news generation
- `surge-prompt.md` — The prompt used for "Surge Watch" — Claude analyzes signal timelines and decides what's noteworthy
- `scan.sh` — Entry point that orchestrates the full pipeline
- `data/papers.json` — Source of truth: all scored papers across runs
- `news.md` — Generated output: flash-news bulletin posted to Discord (always includes Surge Watch section)
