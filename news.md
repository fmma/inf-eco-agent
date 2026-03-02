# Inference Ecosystem — Flash News
**2 March 2026**

**KEEP** scores highest this cycle: a KV-cache-centric memory system that slashes TTFT by 1.9x and overall latency by 2.68x for memory-augmented LLM serving, using static-dynamic cache partitioning and layer-balanced loading. Builds on CacheBlend (EuroSys'25). Score: 95 | Hype: 60 — [arXiv](https://arxiv.org/abs/2602.23592v1)

**LK Losses** directly optimize speculative decoding acceptance rate instead of using KL divergence as a proxy. Tested across 4 draft architectures and targets up to 685B params, gaining 8–10% in average acceptance length with zero overhead. Drop-in replacement for any speculator training loop. Score: 92 | Hype: 70 — [arXiv](https://arxiv.org/abs/2602.23881v1)

**GPU-efficient LLM adapter serving** gets a data-driven treatment: a digital twin + ML pipeline finds minimum-GPU adapter placements under throughput constraints, with <5% estimation error at 90x less cost than live benchmarking. Practical for multi-adapter deployments at scale. Score: 90 | Hype: 55 — [arXiv](https://arxiv.org/abs/2602.24044v1)

**SLA-Aware Distributed LLM Inference** brings real measurements from a 5G AI-RAN testbed. Quantized models clear sub-500ms SLAs at the RAN edge; unquantized ones stall. MIG isolation keeps baseband safe under 20 concurrent inference clients. First empirical data on where LLM inference actually fits in the device→RAN→cloud stack. Score: 88 | Hype: 60 — [arXiv](https://arxiv.org/abs/2602.23722v1)

**DiCo** tackles the parallelism gap in diffusion-based LLMs with adaptive divide-and-conquer decoding — cluster masked tokens, decode clusters in parallel, converge, then finalize. Significant speedups without quality loss. Score: 85 | Hype: 60 — [arXiv](https://arxiv.org/abs/2602.23792v1)

**No hype surges** this cycle.
