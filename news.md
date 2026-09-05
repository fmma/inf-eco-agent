I've confirmed what's going on. Looking at `generate_news.py`: `find_top_papers` only downloads PDFs for papers scoring **≥70** on today's date (`SCORE_THRESHOLD = 70`, lines 65–73), and the prompt only gets a "Full-Text PDFs" section when `pdf_paths` is non-empty (line 124). Both of today's papers scored 10 and 8, so no PDFs were downloaded and none are listed — the "read every PDF" instruction is vacuously satisfied. There is nothing to Read, and neither paper is about LLM inference systems (one is MLLM embedding/reranking, the other CCTV violence detection). Neither can honestly be rescored to the 70 minimum.

The faithful output is a bulletin that reports this honestly rather than manufacturing relevance:

# Inference Ecosystem — Flash News
**2026-09-05 · 2 papers scanned · 0 cleared the bar**

No new papers landed on the inference-systems beat today. Both scans fall outside scope — neither touches serving, scheduling, KV-cache, quantization, batching, or any runtime concern an inference engineer would act on. No PDFs were pulled for full-text rescore (nothing crossed the relevance threshold), so these stay where the abstract scoring put them:

- [CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation](https://arxiv.org/abs/2609.04083) — Rank-KL distillation of a cross-attentive reranker's judgments into an MLLM embedding model for compositional retrieval. Solid representation-learning work (82.7% avg on COLA/SUGARCREPE++/NEGBENCH), but it's a retrieval-quality method, not systems. Score: 10 (unchanged).
- [Short-Window Sliding Learning for Real-Time Violence Detection via LLM-based Auto-Labeling](https://arxiv.org/abs/2511.10866) — 1–2s clip training with LLM auto-captioning for CCTV violence detection (95.25% on RWF-2000). The LLM is just an offline labeling tool; this is a surveillance-vision application. Score: 8 (unchanged).

Nothing to flag for inference engineers today — back tomorrow.

---

## Surge Watch

**[FreeToken](https://arxiv.org/abs/2608.16157)** is the breakout signal: HF upvotes climbed 26→107 since Aug 19, and its GitHub repo rocketed from under 100 to ~11k stars in two weeks — easily the strongest community reception in the tracker right now. Edge-native MoE serving is clearly striking a nerve.

**[DFlash](https://arxiv.org/abs/2602.06036)** keeps compounding: citations have doubled to 84 (from 42 in early July), +6 in just the last three days, with influential citations now at 30 — rare sustained academic traction for a speculative-decoding paper.

Also climbing steadily: **[DSpark](https://arxiv.org/abs/2607.05147)** (up to 48 HF upvotes and 20 citations) and **[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)** (ticking to 17 citations, 166 upvotes).
