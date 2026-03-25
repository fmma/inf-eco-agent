I can't access the PDFs due to sandbox restrictions and missing poppler-utils. I'll write the bulletin based on the detailed abstracts provided, which contain substantial technical detail for the top papers.

# Inference Ecosystem — Flash News
**2026-03-25 — 171 papers scanned**

---

### [PCR: A Prefetch-Enhanced Cache Reuse System for Low-Latency RAG Serving](https://arxiv.org/abs/2603.23049)

RAG workloads suffer from bloated prefill times when long retrieved contexts hit the KV cache cold. PCR attacks this with three neat tricks: a prefix-tree cache with look-ahead LRU that peeks at the scheduler queue to predict hits, layer-wise pipelining of KV-cache loads across CUDA streams to hide CPU-GPU transfer, and SSD-to-DRAM prefetching for spilled caches. Result: **2.47x TTFT speedup** over existing KV-cache reuse baselines. If you're running vLLM-style serving with shared document prefixes, this is directly applicable.
**Score: 90 (was 92)**

### [Sparser, Faster, Lighter Transformer Language Models](https://arxiv.org/abs/2603.23198)

Sakana AI (Llion Jones' group) introduces a new sparse packing format and custom CUDA kernels for unstructured sparsity in LLM feedforward layers — the components that account for most parameters and FLOPs. Simple L1 regularization pushes sparsity past **99%** with negligible quality loss, and their kernels translate that into real throughput, energy, and memory gains that scale with model size. Code and kernels will be open-sourced. This could make unstructured sparsity a practical deployment axis alongside quantization.
**Score: 88 (was 88)**

### [Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference](https://arxiv.org/abs/2603.22774)

A Georgia Tech study that should be required reading for anyone provisioning inference clusters. Multi-GPU serving frequently bottlenecks not on GPUs but on CPUs — delayed kernel launches, stalled NCCL comms, and slow tokenization cause severe GPU underutilization even with CUDA Graphs enabled. Adding CPU cores (cheap relative to GPU pricing) restored responsiveness and reduced TTFT by **1.36–5.40x** across configs, preventing timeouts under moderate load. The takeaway: your CPU allocation is probably wrong.
**Score: 88 (was 88)**

### [EchoKV: Efficient KV Cache Compression via Similarity-Based Reconstruction](https://arxiv.org/abs/2603.22910)

EchoKV compresses KV caches by reconstructing evicted key-value pairs from a retained subset, exploiting inter-layer and intra-layer head similarities. Unlike irreversible low-rank projections, it allows **on-demand switching** between compressed and full-precision inference — deploy compressed when memory is tight, flip back to full precision when it's not. Training cost is ~1 A100 GPU-hour for a 7B model. Outperforms existing methods across compression ratios on LongBench and RULER while maintaining throughput for short contexts.
**Score: 82 (was 85)**

### [FAAR: Format-Aware Adaptive Rounding for NVFP4](https://arxiv.org/abs/2603.22370)

As FP4 quantization moves from spec to practice (thanks to NVIDIA's NVFP4 format), naive rounding leaves significant quality on the table because the FP4 grid is non-uniform. FAAR learns per-weight rounding decisions that respect the actual NVFP4 grid geometry, plus a 2-stage fine-tuning scheme for layer-wise alignment. On Llama3-1B, perplexity drops from 14.28 (RTN) to **12.60** — meaningful for edge deployment where every bit matters. Training overhead: just 4 GPU hours.
**Score: 75 (was 78)**

---

## Surge Watch



[Attention Residuals](https://arxiv.org/abs/2603.15031v1) continues its strong run — HF upvotes climbed to 158 and GitHub stars hit 2,673, up from 151 / 2,615 last report. Growth is decelerating but the paper has cemented itself as this month's breakout hit in the inference space.

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619v1) has essentially plateaued at 77 HF upvotes and 143 GitHub stars, up only marginally from 76 / 140. The initial wave of interest appears to have peaked.

[GradMem](https://arxiv.org/abs/2603.13875v1) also flattened out — 33 → 33 HF upvotes and 25 → 27 GitHub stars over the past week. The early burst didn't sustain into broader adoption.

[IndexCache](https://arxiv.org/abs/2603.12201v1) is the new stall story: after a promising ramp to 52 HF upvotes and 54 GitHub stars by Mar 23, signals went completely flat. A high-relevance sparse attention paper (scored 92) that the community sampled and moved on from.

Nothing else in the tracker shows meaningful momentum this cycle. Several papers from a prolific cluster (inference-fleet-sim, FleetOpt, semantic router variants) are picking up early citations from each other but no organic community traction yet.
