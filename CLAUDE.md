# Inference Ecosystem Paper Scanner

This repo is an automated agent that discovers new arXiv papers about LLM inference systems.

## How it works

1. `src/fetch_papers.py` queries arXiv for recent papers matching configured categories and keywords
2. `scan.sh` invokes Claude Code non-interactively (`claude --print`) with the fetched papers
3. Claude Code scores each paper for relevance and writes a markdown report to `reports/`
4. The report is committed and pushed to git

## Key files

- `config.json` — Topic definition, arXiv categories, keywords, scoring threshold
- `src/fetch_papers.py` — Python script that fetches papers and outputs JSON
- `prompt.md` — The prompt used when invoking Claude Code for scoring
- `scan.sh` — Entry point script that orchestrates the pipeline
- `reports/` — Output directory for daily markdown reports

## Reports

Reports are named `reports/YYYY-MM-DD.md` and contain papers scored above the configured threshold.
`reports/README.md` is an index of all reports.
