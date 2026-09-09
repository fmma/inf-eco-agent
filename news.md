I've read all eight PDFs. Here's my rescored bulletin based on the full texts.

# Inference Ecosystem — Flash News
**2026-09-09 · 605 new papers scanned · top 5 by rescored relevance**

## [A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing](https://arxiv.org/abs/2608.13573)
The first publicly released year-long production serving trace — 6.12B requests, 9,174 models, 315K users from a serverless LLM platform (Chutes × Harvard MadSys). Two findings should reshape how you build routers and caches: SOTA eviction algorithms (ARC, S3FIFO, LHD) often *underperform* plain FIFO/LRU on prefix-cache workloads because reuse is strongly recency-driven (99% of repeats within 15 min), and there's a hard tension between load-balancing and prefix locality — cache-first routing recovers fleet-wide KV reuse at only 5–7% imbalance, while spreading load duplicates ~27GB KV states per long-context request. Essential empirical grounding for anyone designing serving systems right now. Score: 94 (was 95)

## [Deadline-Aware Adaptive Prefill Chunking (SLOWeave)](https://arxiv.org/abs/2609.07883)
SLOWeave picks the largest prefill chunk that still finishes before the earliest active decode's next-token deadline, via a log-time search over a monotone iteration-cost model — no per-workload tuning, no kernel changes, drops into a vLLM-style scheduler. On real A100/H100 runs it lifts goodput 39% (mixed) and 38% (long-context) at a 25ms TPOT SLO, rising to 3.3×/2.4× under a strict 10ms target. The rare scheduling paper that's both provably optimal per-iteration and immediately implementable. Score: 90 (was 92)

## [EStream: Fast, Memory-Efficient MoE Prefill via Expert Virtualization on Mobile NPUs](https://arxiv.org/abs/2609.06551)
The first system to run full-NPU MoE prefill on a commercial smartphone, solving two mismatches: a topology-invariant shared expert graph with runtime route/param binding (no CPU/GPU fallback), and expert virtualization that streams the pool through a bounded UFS→NPU arena so memory is capped by the arena, not the model. On a Snapdragon 8 Elite it delivers 2.25–27.57× prefill TTFT speedups and 6.45–12.29× less memory, scaling to Mixtral-8×7B (46.7B params) on a phone. A striking proof that on-device MoE capacity isn't bounded by resident expert memory. Score: 88 (was 90)

## [Analytical Resource Management for Fine-grained MoE Comp-Comm Overlap](https://arxiv.org/abs/2609.07536)
Tackles a subtle bottleneck in fine-grained MoE overlap: compute and communication CTAs contend for SM residency, and a fixed partition (COMET's default C=3) can't adapt to workload shape. A wave-quantized analytical model picks the comm-CTA count at launch in ~0.16µs with 3.22% regret vs oracle — no profiling, no recompilation. Dropped into COMET/FLUX on A100s it yields 2.53× geomean at the GEMM2+GatherRS operator and 1.19× on full-model prefill, beating Megatron core-TE and FastMoE at every sequence length ≥4K. Score: 87 (was 92)

## [DFlow: Verifier Information Flow in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2609.06498)
From the Miao/Cui group, DFlow plugs an "information discontinuity" in block-diffusion speculative decoding: instead of discarding verifier hidden states for the rejected suffix, it relays them to guide the next drafting round via multi-round self-conditioning — no extra target forward pass, just 1.2% overhead. On Qwen3-1.7B/4B/8B it raises acceptance length 10.4–13.4% over DFlash and lifts SGLang serving throughput across concurrency levels, while composing with Domino. A neat reminder that speculative execution produces reusable signal beyond the accepted tokens. Score: 85 (was 90)

---

## Surge Watch

Diffusion LLMs delivered this cycle's breakout: **[Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010)** rocketed from 8 → 119 HF upvotes overnight (Sep 8→9) and materialized a repo at 50 GitHub stars from nothing — by far the sharpest single-day surge on the tracker.

**[Random Attention](https://arxiv.org/abs/2609.03430)** is accelerating rather than cooling since last week: now at 170 HF upvotes (164 → 167 → 170) with GitHub stars leaping 37 → 52 in a single day (Sep 8→9) — this KV-eviction result has real staying power.

Worth a glance: **[Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737)** banked a strong debut (10 → 66 HF upvotes since Sep 3), though it's plateauing in the mid-60s now. The quant/spec-decoding names that led last week (GSQ, Verification-Aware Training) have gone flat.
