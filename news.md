# Inference Ecosystem — Flash News
September 1, 2026 · Top 5 of 433 papers scanned

## [Kascade: A Practical Sparse Attention Method for Long-Context LLM Inference](https://arxiv.org/abs/2512.16391)
Training-free sparse attention that computes exact Top-k key indices only on a few algorithmically-chosen "anchor" layers (via a dynamic-programming cross-layer-similarity objective) and reuses them across neighboring "reuse" layers, with head remapping and tile-level selection to stay GPU-friendly under GQA. Delivers up to 4.1× decode and 2.2× prefill speedup over FlashAttention-3 on H100 while matching dense accuracy on LongBench, and beats Quest/OmniKV/LessIsMore on AIME-24 by 8–10% absolute at 10% Top-k. From MSR India with TileLang kernels and code promised — the rare sparse-attention scheme actually built to deploy across models. Score: 94 (was 93)

## [Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs](https://arxiv.org/abs/2608.30310)
Fixes prefix caching for hybrid full-attention/linear-attention models: rather than storing recurrent-state checkpoints, it caches only exact FA KV plus FA output hiddens and rebuilds Gated DeltaNet states on a hit by replaying a short recent suffix — exploiting that gated recurrences attenuate distant tokens. A 5–10% replay budget retains 92.8–99.9% of full-prefill quality on LongBench/RULER and cuts TTFT 9.1–14.3× at 32K across OLMo-Hybrid-7B, Qwen3.5-4B, and Qwen3.6-27B. Unconstrained token-level prefix reuse in hybrids is a genuinely new capability as these architectures go mainstream. Score: 92 (was 93)

## [DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving](https://arxiv.org/abs/2608.30386)
Complementary attack on the same hybrid-serving problem: it reads per-head (GDN) / per-channel (KDA) "retention horizons" directly from model weights — no calibration — to pick which recurrent-state units to keep, packing survivors into a TP-balanced ragged checkpoint layout in SGLang. On Kimi-Linear it compresses KDA state checkpoints 2.63× at near-dense quality, cutting mean TTFT 42.6% and lifting input throughput 68.4% under fixed HBM, with INT8 composition reaching 8.11×. Alongside Tail-Replay, this marks recurrent-state cache management as the serving problem of the moment. Score: 92 (was 93)

## [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://arxiv.org/abs/2608.30252)
Breaks the long-context spec-decoding bind — lightweight drafts lose acceptance, strong drafts choke on full-KV access — with memory-augmented drafting (MASW): the draft keeps sink tokens, an exact local window, and periodically materialized "memory slots" from trainable mirrored KV projections, while the target verifies against its full cache (lossless). Cuts draft-side memory >70% and reaches up to 2.08× (Llama-3.1-8B) and 3.33× (70B) over autoregressive decoding at 32K prefixes, beating EAGLE-3 and full-KV SD. A clean marriage of two core techniques that keeps SD's guarantee intact. Score: 90 (was 90)

## [CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration](https://arxiv.org/abs/2608.30295)
Finds "sequentially consistent" heads — whose critical tokens, scored by coefficient-of-variation during prefill, stay fixed through decoding — and keeps only those tokens for consistent heads while preserving most KV in adaptive heads. The hybrid policy gives up to 2.72× memory reduction, 2.18× decode speedup, and 3.96× batch throughput at near-full-attention accuracy on RULER/LongBench/NIAH, and layers on top of Quest and ShadowKV. An ICML'25, plug-and-play win for long-context KV budgets. Score: 89 (was 92)

---

## Surge Watch

The upvote charts finally broke their summer silence: **[FreeToken](https://arxiv.org/abs/2608.16157)** (bandwidth-adaptive edge-MoE serving) tore from 26 → 99 HF upvotes in nine days (Aug 19→28) — easily the fastest fresh community climb this cycle, and a tell that on-device MoE is where attention is rotating.

**[DSpark](https://arxiv.org/abs/2607.05147)** is the rarer signal: it's accelerating on *both* charts at once — citations 3 → 18 (influential 1 → 6) since mid-July, HF upvotes 36 → 48 — unusual conviction for a semi-autoregressive speculative-decoding paper.

On citations alone, **[DFlash](https://arxiv.org/abs/2602.06036)** keeps compounding hard: 42 → 75 (influential 17 → 26) since early July, still the reference magnet for diffusion speculative decoding. **[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)** quietly stacks both sides — citations 2 → 12 (influential 1 → 4) plus a 150 → 164 HF tick.

Notably, last month's citation leaders — FlashAttention-4, Mamba-3, IndexCache — have all flattened (47→48, 73→74, 20 flat). Momentum has clearly rotated to the newer speculative-decoding and edge-MoE cohort.
