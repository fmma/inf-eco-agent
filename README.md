# Inference Ecosystem Paper Scanner

Automated agent that discovers new arXiv papers about LLM inference systems. A Python script fetches papers from arXiv, then [Claude Code](https://claude.com/claude-code) scores each paper for relevance and generates a daily markdown report.

## How it works

```
Python fetcher (arXiv API)  →  JSON  →  Claude Code scores & writes report  →  git commit & push
```

1. `src/fetch_papers.py` queries arXiv for recent papers across relevant categories, pre-filtered by keywords
2. `scan.sh` invokes Claude Code non-interactively (`claude --print`) with the fetched papers as input
3. Claude Code scores each paper 1–10 for relevance and writes a report to `reports/YYYY-MM-DD.md`
4. Papers scoring above the configured threshold (default: 7) are included in the report
5. The report is committed and pushed

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

Edit `config.json` to change the topic, arXiv categories, keywords, relevance threshold, or max papers fetched.

## Project structure

```
├── src/fetch_papers.py   # Fetches papers from arXiv, outputs JSON
├── prompt.md             # Prompt for Claude Code scoring
├── scan.sh               # Entry point script
├── config.json           # Topic, categories, keywords, threshold
├── reports/              # Generated daily reports
└── requirements.txt      # Python dependencies
```
