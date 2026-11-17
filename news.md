All eight PDFs are now read in full. Rescoring on full-text contribution, novelty, and practical impact for inference engineers: the three systems papers (Stint, CECAR, Nemotron Transcribe) hold their high scores; LoopFill eases slightly (excellent method, but niche looped-model scope); OptiDecode drops from 90 (on full read it's speculative free-space-optics hardware modeled against an ideal baseline, not deployable serving tech). The remaining three land below this top tier (MIAO 81, Text-Speeding 78, Depth-Recurrent KV Replay 73). Top 5 bulletin:

# Inference Ecosystem — Flash News

**2026-11-17** · 5 papers highlighted · New papers scanned: 244

### [Making Preemption Productive in Long-Output LLM Serving](https://arxiv.org/abs/2611.20106)
Stint rebuilds KV-cache preemption in vLLM for reasoning workloads, pairing SRJF prediction-guided victim selection (hidden-state length estimates every K=64 steps) with a contiguity-first CPU KV pool, fused bulk K/V transfer, and age-based protected recovery. On IMO-AnswerBench (median 17K output tokens) with Qwen3-32B on 8×H200 it lifts throughput +11.99% over recompute (+48.5% vs SGLang HiCache), cuts p99 TPOT by 50.69%, and eliminates the 11–14 minute request pauses baselines suffer. A production-grade fix for KV thrashing — the defining pain point of long-output serving. Score: 95 (was 95)

### [CECAR: Cache & Expert Co-Aware Routing](https://arxiv.org/abs/2611.20119)
CECAR makes on-device MoE inference practical by jointly routing on cache residency and predicted expert reuse, via an ML cache policy (FFN-Hot/Cold reuse-distance prediction) and cache-conditioned top-k pruning. It serves Qwen3-30B-A3B at 12.5 tokens/s on a consumer 16GB RTX 5070 Ti with experts streamed from SSD — 4.5× over conventional MoE and 1.8× over an all-DRAM baseline using 78.8% less memory, at a 0.5-pt mean accuracy cost. Code is released. Score: 93 (was 93)

### [High-Throughput Serving of Nemotron 3.5 Transcribe](https://arxiv.org/abs/2611.20095)
NVIDIA serves a hybrid Mamba-Transformer MoE ASR model (34B total, ~4.3B active) by choosing per-pass between megakernels and fused kernels at offline crossovers, over a Python-free C-ABI host path with MTP drafting. It peaks at 4,345× RTFx on H100 (1.39× tuned vLLM) and 6,367× on B200 (1.64×), serving 8× more concurrent requests within a 400ms p95 budget at matched WER (~1.9%). The regime-aware dispatch beats either kernel strategy alone by 9–23%. Score: 92 (was 92)

### [LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers](https://arxiv.org/abs/2611.19649)
LoopFill is a training-free speculative decoder for recurrent-depth LLMs that fuses suffix-tree drafts with the model's own shallow-loop predictions in a single draft tree, filling the pipeline bubbles that single-draft methods leave. Across seven benchmarks it averages 5.85× over greedy decoding on Ouro-2.6B and 5.13× on Huginn-3.5B — 40% and 25% beyond the strongest trained baseline (LoopAhead) — with 2.5–2.8× end-to-end throughput and zero extra training. Score: 86 (was 88)

### [Rethinking KV Caching for LLM Decode: Free-Space Optical KV Regeneration](https://arxiv.org/abs/2611.19279)
OptiDecode caches layer-input activations instead of KV (halving historical-cache traffic) and regenerates keys/values optically on free-space tiles holding resident projection weights, using activation replay, in-situ attention, and chunk pipelining to sustain the HBM fetch rate. It models 1.92–1.99× decode-attention speedup over an ideal GPU KV-read baseline across 30B–175B MHA models at 32K context. Exotic hardware, but a compelling rethink of the KV-versus-activation tradeoff. Score: 83 (was 90)

---

## Surge Watch

**Speculative decoding is this cycle's citation magnet.** [DSpark](https://arxiv.org/abs/2607.05147) doubled in a week — 42→84 citations, 19→41 influential — one of the steepest ramps on the board, while [SPEED-Bench](https://arxiv.org/abs/2604.09557) tripled (10→29 citations, 1→6 influential) and [Domino](https://arxiv.org/abs/2605.29707) jumped 31→55. The draft-and-verify layer is compounding harder than the kernels right now.

**Foundational architectures caught the same wave.** [Mamba-3](https://arxiv.org/abs/2603.15569) added 28 citations in days (105→133, 18→23 influential), and Kimi's [Attention Residuals](https://arxiv.org/abs/2603.15031) jumped 67→84 (15→24 influential) while holding ~199 HF upvotes and 3.6K stars — the SSM/attention-design layer is getting absorbed fast.

**The serving classic keeps grinding.** [Mooncake](https://arxiv.org/abs/2407.00079) pushed 298→329 citations (26→32 influential) — slow but relentless on an already heavily-cited paper, a reminder that KV-cache-centric disaggregation is still the reference point everyone builds against.
