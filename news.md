# Inference Ecosystem — Flash News
**2026-07-30 · 206 new papers scanned · top 5 by rescored relevance**

### [InferScale: GPU-Native KV Injection for Personalized LLM Serving](https://arxiv.org/abs/2607.27090)
Ships as a stock vLLM KV-connector plugin — no engine fork, no fine-tuning — that precomputes each memory fact's KV once and injects it into the paged cache instead of re-prefilling retrieved context on every request. "Chunked RoPE" (store keys pre-rotation, re-rotate at inject time) makes reuse position-independent and provably exact, while Context-Window Encoding recovers the cross-fact accuracy. On LoCoMo it holds TTFT flat as retrieval grows (72–79% / 3.6–4.8× lower than Mem0 at k=50), lifts throughput 3.7–4.5× at 100 users, and scales to Qwen3-14B (5× lower TTFT). If you run a Mem0/RAG stack on vLLM, this is the most immediately deployable win in the batch. Score: 95 (was 95)

### [DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch](https://arxiv.org/abs/2607.26475)
Names a bottleneck everyone overlooks: the "KV-cache-auxiliary residency" (low-rank keys, landmarks) that sparse-KV systems like ShadowKV/SpeCache park in HBM can eat 64% of GPU memory and throttle batch size. The insight — the next step's critical KV indices are ~88% predictable from a cheap speculative token — lets it prefetch sparse KV off the critical path via a dual-token pipeline, layer-aware transfer schedule, and two-buffer ping-pong manager. Payoff: 2.62× throughput over ShadowKV with 36–62% less memory and lossless accuracy. Score: 90 (was 90)

### [Revisiting Lossy Verification in Speculative Decoding](https://arxiv.org/abs/2607.26627)
The "you've been benchmarking it wrong" paper. It shows SpecCascade and Medusa-style typical acceptance mostly inherit their gains from the truncation sampling (min-p / η) they quietly bundle in — against a distribution-matched target the quality gap widens with task difficulty (+6.67 pp on AIME) and blows up under EAGLE-3 (−8.8 pts on INCLUDE). For collaborative verification, capping draft-probability overshoot is the single knob that preserves quality. Required reading before you trust any lossy-spec-decode number; code released. Score: 87 (was 88)

### [NELSSA: A GPU–PNM Heterogeneous System for Mixed-Length LLM Serving](https://arxiv.org/abs/2607.26633)
First end-to-end serving stack on real Processing-near-Memory hardware (ARM Neoverse V2 over CXL): a hardware-derived length threshold routes short requests to GPU FlashAttention and long-context to PNM sparse attention, with a one-way background migration when a request outgrows HBM — no recompute, no swap. Up to 5.5× decode throughput and 15× lower P99 vs GPU-only on mixed Mooncake traces. A concrete signal that CXL/PNM disaggregation is maturing into a first-class decode tier, not just an offload target. Score: 86 (was 92)

### [A Photonic-CXL Memory Appliance for Scalable KV Cache Management](https://arxiv.org/abs/2607.27187)
Marvell's swing at the KV memory wall: a passive optical fiber shuffle replaces electrical CXL switches to pool 32 TB across 16 hosts at 128 GB/s/host, switch-free. The memory-tier characterization alone earns the read (host DRAM up to 100× vs recompute; SSD caps at 9.7× and can be *slower* than recomputing). Emulation shows >50% lower latency than switched CXL pools, and serving simulation keeps TTFT flat to 300 conversations (6.6× vs an eviction-bound baseline). Appliance is still emulation+sim, but the trajectory is unambiguous. Score: 84 (was 92)

---

## Surge Watch

**Unlimited OCR Works** ([2606.23050](https://arxiv.org/abs/2606.23050)) still won't quit — GitHub stars blew past **20.4k** (18.1k on Jul 24 → 20,412 on Jul 30, a +2.3k week) while HF upvotes jumped 60→72. The community pile-on is, if anything, still accelerating.

The organic riser I flagged last cycle, [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980), has cooled hard: after tripling to 125 stars by Jul 27, it's added just 4 (→129) and a single HF upvote (81→82) since. The sprint is over — call it a plateau.

New on the radar: [VLASH](https://arxiv.org/abs/2512.01031) (real-time vision-language-action inference) surfaced in tracking already carrying **10 influential citations, ~450 GitHub stars, and 27 HF upvotes** — the strongest cold-open of any on-topic paper this cycle. No timeline yet, but worth watching whether the stars keep climbing.
