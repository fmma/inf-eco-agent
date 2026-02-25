# Inference Ecosystem Paper Scanner

Automated agent that discovers new arXiv papers about LLM inference systems. A Python script fetches papers from arXiv, then [Claude Code](https://claude.com/claude-code) scores each paper for relevance. Results accumulate in a single living list (`papers.md`), sorted by score.

## How it works

```
fetch_papers.py (skip seen IDs) → new papers JSON → Claude scores (JSON) →
  merge_papers.py (append to data/papers.json) → render.py (write papers.md) → git commit & push
```

1. `src/fetch_papers.py` queries arXiv for recent papers, skipping papers already in `data/papers.json`
2. `scan.sh` invokes Claude Code non-interactively (`claude --print`) to score the new papers
3. Claude scores each paper 0–100 and outputs a JSON array
4. `src/merge_papers.py` merges scores with paper metadata into `data/papers.json`
5. `src/render.py` regenerates `papers.md` — the living list sorted by score
6. `scan.sh` commits and pushes

Papers accumulate across runs — no rescanning. The list grows over time.

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

To run on a schedule (e.g. daily at 8am):

```cron
0 8 * * * cd /path/to/inf-eco-agent && ./scan.sh >> /tmp/scan.log 2>&1
```

## Configuration

Edit `config.json` to change the topic, arXiv categories, keywords, relevance threshold (0–100 scale), or max papers fetched.

## Project structure

```
├── src/
│   ├── fetch_papers.py    # Fetch from arXiv, skip already-seen IDs
│   ├── merge_papers.py    # Merge Claude's scores into data/papers.json
│   └── render.py          # Generate papers.md from data/papers.json
├── data/
│   └── papers.json        # Source of truth: all scored papers
├── papers.md              # Generated output: the living list
├── scan.sh                # Orchestrates the pipeline
├── prompt.md              # Claude prompt (score only, output JSON)
├── config.json            # Topic, categories, keywords, threshold
└── requirements.txt       # Python dependencies
```
