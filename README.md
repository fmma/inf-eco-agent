# Inference Ecosystem Paper Scanner

Automated agent that discovers new arXiv papers about LLM inference systems. [Claude Code](https://claude.com/claude-code) scores each paper for relevance and predicted hype, external signals are tracked over time, and a flash-news bulletin is posted to Discord daily.

## How it works

```
fetch_papers.py → Claude scores → merge_papers.py → fetch_hype_signals.py →
  rescore_hype.py → generate_news.py + build_hype_prompt.py → Discord
```

1. `src/fetch_papers.py` queries arXiv for recent papers, skipping papers already scored. Lookback window adapts to time since last run (minimum 3 days).
2. Claude Code scores each paper 0–100 for relevance and 0–100 for predicted hype.
3. `src/merge_papers.py` merges scores into `data/papers.json`.
4. `src/fetch_hype_signals.py` queries Semantic Scholar + HuggingFace for citations, upvotes, and GitHub stars.
5. `src/rescore_hype.py` updates signal snapshots and detects notable activity (new traction or signal surges).
6. If notable hype activity: Claude generates a "Hype Watch" blurb from raw signal deltas.
7. If new papers: `src/generate_news.py` downloads PDFs, rescores relevance via Claude, and generates flash news.
8. `src/render.py` regenerates `papers.md` — a living list sorted by score.
9. Results are committed, pushed, and posted to Discord via [OpenClaw](https://openclaw.ai/).

## Topics covered

LLM serving, KV cache management, speculative decoding, continuous batching, PagedAttention, model quantization for inference, inference frameworks (vLLM, TensorRT-LLM, SGLang, TGI, llama.cpp), throughput/latency optimization, distributed inference, inference hardware, and I/O (memory bandwidth, NVMe, RDMA, interconnects, disk/network I/O).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Requires [Claude Code](https://claude.com/claude-code) to be installed and authenticated.

## Usage

```bash
./scan.sh
```

### Scheduled runs

A systemd user timer runs the scan daily at 08:00 with `Persistent=true` (catches up after sleep/shutdown). The service retries on failure every 5 minutes, up to 6 times. Discord notifications are sent via OpenClaw.

```bash
# Check timer status
systemctl --user status inf-eco-scan.timer

# Manual run
systemctl --user start inf-eco-scan.service

# View logs
journalctl --user -u inf-eco-scan.service -n 50
```

## Configuration

Edit `config.json` to change the topic, arXiv categories, keywords, or relevance threshold (0–100 scale).

## Project structure

```
├── src/
│   ├── fetch_papers.py        # Fetch from arXiv, adaptive lookback, dedup
│   ├── merge_papers.py        # Merge Claude's scores into data/papers.json
│   ├── fetch_hype_signals.py  # Query Semantic Scholar + HuggingFace
│   ├── rescore_hype.py        # Update signals, detect notable activity
│   ├── build_hype_prompt.py   # Build prompt for Hype Watch blurb
│   ├── generate_news.py       # PDF rescore + flash news in one Claude call
│   ├── build_news_prompt.py   # Build news prompt from new papers
│   ├── render.py              # Generate papers.md from data/papers.json
│   └── parse_scores.py        # Shared JSON parsing with error handling
├── data/
│   └── papers.json            # Source of truth: all scored papers
├── papers.md                  # Generated: the living paper list
├── news.md                    # Generated: flash-news bulletin (+ Hype Watch)
├── scan.sh                    # Orchestrates the full pipeline
├── prompt.md                  # Claude prompt for scoring (JSON output)
├── news-rescore-prompt.md     # Claude prompt for PDF rescore + news
├── news-prompt.md             # Claude prompt for news generation
├── hype-prompt.md             # Claude prompt for Hype Watch blurb
├── config.json                # Topic, categories, keywords, threshold
└── requirements.txt           # Python dependencies
```
