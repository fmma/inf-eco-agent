# Inference Ecosystem — Flash News

**2026-03-13** | 179 new papers scanned

---

[**LongFlow: Training-Free Long-Context KV Cache Compression for Reasoning Models**](https://arxiv.org/abs/2603.11504)
Fuses FlashAttention with importance estimation and token eviction in a single Triton kernel, eliminating the separate scoring pass that plagues existing KV cache compression methods. Achieves 11.8x throughput on Qwen3-1.7B at 80% compression with negligible accuracy loss, and scales to DeepSeek-R1-Distill-Llama-8B where it maintains full-score AIME accuracy under 50% compression. The kernel design (fused attention + eviction in one pass) is the real contribution; the compression policy itself is secondary.
**Rescored relevance: 94**

[**IndexCache: Cross-Layer Index Reuse for Sparse Attention Acceleration**](https://arxiv.org/abs/2603.12201)
Observes that DeepSeek-style sparse attention indexers produce nearly identical top-k selections across adjacent layers (>95% overlap), then eliminates 75% of indexer computations by reusing indices. Validated on production-scale GLM-5-744B in addition to 30B benchmarks, delivering 1.82x prefill and 1.48x decode speedup. Training-aware distillation variant recovers the small accuracy gap from greedy reuse with minimal fine-tuning cost.
**Rescored relevance: 92**

[**SFI: Training-Free Acceleration via Attention Support Stability**](https://arxiv.org/abs/2603.12038)
Exploits the observation that attention support sets are stable within sentences but shift at semantic boundaries, enabling aggressive sparse-cache fast steps between boundary-triggered full recomputations. A closed-form selector derived from reverse-KL fusion avoids any learned components. Reports 1.6x to 14.4x throughput gains across tasks with no fine-tuning, applicable to any existing checkpoint.
**Rescored relevance: 88**

[**Cornserve: Distributed Serving for Any-to-Any Multimodal Models**](https://arxiv.org/abs/2603.12118)
First system to serve generic multimodal models (text, audio, image, video in any combination) across distributed GPUs with component-level scheduling. Introduces model fission at modality boundaries and record-and-replay execution to handle dynamic computation graphs. On Qwen 2.5 Omni, delivers 3.81x throughput and 5.79x lower P99 latency versus naive pipeline parallelism; open-sourced on Kubernetes (~23K lines Python).
**Rescored relevance: 86**

[**DapQ: Position-Aware Pseudo Queries for KV Cache Compression**](https://arxiv.org/abs/2603.11564)
Demonstrates that positional information dominates query representations in importance scoring (cosine similarity 0.7238 with correct position vs. 0.3522 with correct content), then constructs position-aware pseudo queries that enable decoding-aligned eviction without access to future queries. Retains 99.5% accuracy on Needle-in-a-Haystack at a 3% KV cache budget, a notable improvement over position-agnostic baselines.
**Rescored relevance: 83**

---

**Surge Watch:** Nothing to report this cycle. No papers from the scored pool are showing notable external signal movement.

---

## Surge Watch



[FlashPrefill](https://arxiv.org/abs/2603.06199v1) GitHub stars continue climbing steadily: 3 → 12 → 16 → 21 → 27 over five days. HF upvotes plateaued at 9, but the repo traction suggests practitioners are picking it up for long-context prefilling workloads.

[Fish Audio S2](https://arxiv.org/abs/2603.08823v1) maintained its trajectory — 3 → 14 → 20 HF upvotes across three days, now with 26k GitHub stars on the parent repo. Still not core inference, but consistent community interest.

Everything else is flat. Qwen3-Coder-Next grinding at 45 HF upvotes. DualPath stuck at 43. LK Losses frozen at 18 for two weeks straight. Multi-Head Low-Rank Attention showed first signs of life (3 HF upvotes, 8 GitHub stars) but too early to call.
