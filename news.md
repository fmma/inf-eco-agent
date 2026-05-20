# Inference Ecosystem — Flash News

**2026-05-20** · Scanning 334 papers

---

[C2CServe: Serverless LLM Serving on MIG-Partitioned GPUs via NVLink-C2C](https://arxiv.org/abs/2605.19481)
Turns GB200 NVLink-C2C into a serverless LLM serving platform by co-locating models on MIG partitions and fetching weights from a partner GPU over C2C on demand. The HybridGEMM kernel dynamically splits matrix ops across local HBM and remote C2C bandwidth, hiding cold-start latency. Achieves 7.1× cold-start reduction for dense models and 4.6× for MoE versus CPU offloading, with near-zero interference to co-resident workloads.
`rescored: 94`

[SuperInfer: Serving LLMs on Superchips with Inter-Chip Communication](https://arxiv.org/abs/2601.20309)
MLSys 2026 paper that builds an SLO-aware serving system for GH200 NVLink-C2C superchips. Introduces RotaSched, a rotary scheduler using a Virtual Lag Time metric to balance prefill/decode across the CPU–GPU boundary, plus DuplexKV — a full-duplex KV cache rotation engine that overlaps bidirectional C2C transfers. Improves TTFT SLO attainment by up to 74.7% over vLLM on Llama-3.1-70B. Code is open-sourced.
`rescored: 93`

[SpecSA: Bridging Speculative Decoding and Sparse Attention for Efficient LLM Inference](https://arxiv.org/abs/2605.19893)
EuroSys 2027 paper that fuses speculative decoding with Native Sparse Attention (NSA). Introduces compressed-KV-aware drafting so the draft model shares the target's sparse attention state, plus a fused verification-and-attention GPU kernel that eliminates redundant KV recomputation. On H100 with DeepSeek-R1, delivers 3.49× end-to-end throughput and 6.86× kernel-level speedup over standard sparse attention decoding.
`rescored: 93`

[KVBuffer: Efficient IO-Aware Serving for Linear Attention and Hybrid Models](https://arxiv.org/abs/2605.19049)
Tackles the hidden IO bottleneck in linear-attention models like Qwen3-Next when served naively. Proposes chunkwise decoding that batches recurrence state updates to improve arithmetic intensity, integrated into SGLang. Cuts per-token latency by 45% and supports 5× more concurrent requests under speculative decoding by trading a small chunk of extra compute for dramatically less memory traffic.
`rescored: 92`

[Graft: Hybrid Tree Construction for Lossless Speculative Decoding](https://arxiv.org/abs/2605.20104)
Combines top-k pruning with suffix-retrieval from a corpus-derived n-gram index to build richer speculation trees — training-free and lossless. The retrieval branch recovers high-probability continuations that greedy pruning misses, especially for factual and repetitive patterns. Reaches 5.41× wall-clock speedup on Qwen3-235B-A22B, improving 21.8% over EAGLE-3 with zero model modification.
`rescored: 90`

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569v1) is seeing a sharp citation surge — jumped from 21 to 33 citations between May 14–18 after weeks of plateauing around 12–17. Three influential citations now. The SSM-vs-attention debate clearly isn't settled, and researchers are building on this.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) from the Kimi Team had a similar burst: citations leapt from 13 to 19 in the same window (May 14–18), with a 4th influential citation. After stalling at 8 for most of April, renewed academic interest is clear.

[Orthrus](https://arxiv.org/abs/2605.12825) (dual-view diffusion for parallel token generation) went from 13 to 260 GitHub stars overnight between May 16–18. Explosive early traction for a brand-new paper.

[MinT](https://arxiv.org/abs/2605.13779) from Mind Lab landed with 202 HF upvotes on day one (May 16), climbing to 210 by May 18. Managed infrastructure for serving millions of LLMs clearly struck a nerve — one of the highest initial upvote counts in the tracker.

[Adaptive Block-Scaled Data Types](https://arxiv.org/abs/2603.28765v1) spent six weeks at zero signals, then suddenly materialized with 180+ GitHub stars around May 15 and 2 citations (1 influential). Likely a delayed code release triggering belated discovery.
