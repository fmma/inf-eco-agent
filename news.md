I can't access the PDFs due to sandbox restrictions on /tmp. I'll proceed with the detailed abstracts provided — they contain substantial technical detail for these papers.

# Inference Ecosystem — Flash News
**2026-04-01 | 464 papers scanned**

This was a quantization-heavy week with multiple KV cache compression papers, but the standouts are a practical KV offloading framework and a deep-dive into speculative decoding's blind spots.

### [ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference](https://arxiv.org/abs/2603.27138v1)

The key insight here is using the CPU *one layer ahead* to pre-compute sparse attention indices, so by the time the GPU needs them the results are ready — no stalling on CPU or I/O. Combined with GPU-CPU collaborative block-wise sparse attention that drastically cuts CPU workload, ScoutAttention hits 2.1x speedup over existing offloading methods while staying within 2.4% of full-precision accuracy. If you're serving long-context workloads and your KV cache is spilling to DRAM, this is the most practical offloading design we've seen.
Score: 93 (was 95)

### [TAPS: Task Aware Proposal Distributions for Speculative Sampling](https://arxiv.org/abs/2603.27027v1)

A wake-up call for anyone running speculative decoding with a generic drafter. TAPS shows draft training data *matters* — MathInstruct-trained drafters dominate on reasoning benchmarks while ShareGPT-trained ones win on MT-Bench. Naive weight averaging of specialized drafters fails, but confidence-based routing and merged-tree verification recover the gains. The practical takeaway: if you're deploying spec-dec in production with mixed workloads, train domain-specific drafters and route by confidence, not entropy. Already at 122 HF upvotes — the community noticed.
Score: 92 (was 93)

### [ITQ3_S: High-Fidelity 3-bit LLM Inference via Interleaved Ternary Quantization with Rotation-Domain Smoothing](https://arxiv.org/abs/2603.27914v2)

A mathematically rigorous 3-bit format that pre-rotates weights via Fast Walsh-Hadamard Transform before ternary quantization, spreading outlier energy uniformly. The inverse FWHT is fused directly into the CUDA MMQ kernel's shared-memory loading stage, so reconstruction error is bounded by the ternary grid alone. On RTX 5090 (Blackwell), ITQ3_S achieves FP16-competitive perplexity at 1.5x the throughput of 4-bit alternatives via DP4A and Tensor Core scheduling. Impressive engineering, though validation is currently Blackwell-only and single-author.
Score: 88 (was 95)

### [TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization](https://arxiv.org/abs/2603.27467v1)

Compresses KV cache entries by quantizing the *angle* of element pairs in Walsh-Hadamard space, where random diagonal rotation makes pairs approximately uniform on the unit circle. The per-layer early-boost mechanism independently tunes K and V codebook sizes, achieving lossless compression on 4 of 7 models and near-lossless on 6 of 7 at just 3.28–3.67 angle bits per element. Combined with 8-bit key / 4-bit log-space value norm quantization, total cost is 6.56 bits on Mistral-7B with +0.0014 perplexity degradation — no calibration data needed. The layer-group sensitivity analysis revealing K-dominated vs. V-dominated bottleneck patterns is a useful design insight.
Score: 85 (was 92)

---

## Surge Watch

[PackForcing](https://arxiv.org/abs/2603.25730v1) exploded from zero to 44 HF upvotes and 128 GitHub stars between 03-28 and 04-01. Short-video-training for long-context inference clearly struck a nerve — one of the fastest cold starts this month.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) HF upvotes broke out of their week-long plateau at 162, climbing to 170 (+8 in 4 days). GitHub stars hit 2,859 (+64). The "discovery phase is over" call may have been premature — new audiences are still finding this.

[Mamba-3](https://arxiv.org/abs/2603.15569v1) citations ticked up to 8 after the plateau at 7, confirming continued academic accumulation rather than a fade-out. Still waiting on the implementation-driven second wave.

[IndexCache](https://arxiv.org/abs/2603.12201v1) GitHub stars quietly jumped from 55 to 66 after weeks frozen in the mid-50s. HF upvotes remain flat at 52 — this looks like practitioner adoption catching up to the initial research interest.
