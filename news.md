# Inference Ecosystem — Flash News
*2026-09-30 · 939 papers scanned · top 5 after full-text rescore*

## [SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving](https://arxiv.org/abs/2609.37626)
SPLASH reframes attention parallelism as two independent choices — where projections are sharded and who owns each request's KV — collapsing TP/CP/DP-attention plus a new layout, DOP, into 12 directed switches served by just three collectives (discard, all-gather, all-to-all). Because MLA/GQA decouples cache placement from weight sharding, most state already sits where the next layout needs it, so a live switch costs under 0.51% of the step it runs in (0.02–11.76 ms vs up to 667 ms if blocking). On B200 serving GLM-5.3, following the best layout lifts end-to-end throughput 1.3–1.73× over any fixed deployment, and DOP alone frees 12.69 GiB/GPU (27% more KV than DP-attention) — the rare paper that adds both a genuinely new layout and a near-free way to move between them. Score: 95 (was 95)

## [PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding](https://arxiv.org/abs/2609.34555)
PulseInfer nails that sparse KV offloading is really an I/O problem — recall volume is wildly dynamic and headwise selection fragments PCIe into ~8 KB transfers at 6 GB/s — and fixes it with OS-interrupt-style interruptible layer-wise scheduling (IRQ), adaptive offloading admission (IOAA), and SoloHead selection (one retrieval head picks blocks for all KV heads) fed by a gather-scatter engine. Built on SGLang, it sustains ~95% GPU utilization and improves decode throughput up to 4.7× over SGLang and 2.6× over the best offloading baseline while cutting TPOT up to 76%, across Qwen3-14B/30B-A3B and MiniMax-M2.5 (230B) on real Mooncake/ServeGen traces. SoloHead even edges out headwise selection on accuracy. Score: 95 (was 95)

## [NOSA: Native and Offloadable Sparse Attention](https://arxiv.org/abs/2510.13602)
NOSA (EMNLP'26 main) makes *trainable* sparse attention natively offloadable via a training-time locality constraint — splitting KV selection into query-aware and eviction-bounded query-agnostic parts, with a proven locality lower bound — so <25% of blocks change per step and CPU→GPU traffic stays cheap. Its NOSI system exposes communication as the true bottleneck and delivers up to 5.04×/1.92×/1.83× decode throughput over FullAttn/InfLLMv2/ShadowKV on 1–8B models, while dodging the long-generation perplexity explosion that wrecks training-free offloading like ShadowKV. Code released by THUNLP; the main caveat is efficiency is shown in NOSI, not yet inside vLLM/SGLang. Score: 94 (was 95)

## [PackServe: SLO-Aware Request Scheduling for Agentic LLM Serving at Scale](https://arxiv.org/abs/2609.33224)
PackServe is a gateway scheduler for agentic workloads that predicts TTFT/TPOT under prefill/decode interference with compact white-box models (1.9 ms/decision vs 132 ms for llm-d's XGBoost), then packs requests onto fewer instances under a recomputation budget that protects KVC reuse. On 64 H20 GPUs it burns 13–24.6% fewer GPU-hours than LMetric and llm-d+ while holding 30/50 ms TPOT SLOs — and it's already in production on 1000+ GPUs, cutting serving footprint 34.7% and lifting per-instance throughput 36.8%. Production validation at that scale is what pushes this above a typical scheduling paper. Score: 92 (was 93)

## [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains](https://arxiv.org/abs/2609.37062)
vSkipper finally converts dynamic layer skipping into real serving wins: the released FlexiDepth checkpoint skips 8/32 layers yet decodes 14.6–21% *slower* than base in a stock loop, because saved FLOPs aren't saved time. Its RUN/Project-Only cohort interface preserves continuous batching, paged KV, and captured CUDA graphs, and a roofline-based profitability switch routes only when it pays — at the load knee it cuts mean latency 36.8% (GSM8K) and 13.6% (BBH) and raises saturated throughput 11.3%/7.4% with no resolved quality loss, generalizing across two Qwen3 skippers and three GPUs. First system to realize serving gains from per-token interior skipping; gains are workload-dependent (CoQA and Qwen3-4B see little). Score: 91 (was 95)

---

## Surge Watch

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) is proving it's no launch-day spike: beyond the HF upvote climb flagged last cycle, its citations **more than tripled from 7 to 23 (09-25→09-30)** — remarkably fast academic compounding for a paper barely a week old, and the clearest sign this KV-compression report has staying power on both the community *and* citation axes.

On the systems side, [Continuum](https://arxiv.org/abs/2511.02230)'s KV-cache-TTL agent scheduling keeps quietly accruing influence — **54→63 citations (09-25→09-30)**, now 9 influential — a sustained ramp (35→63 since early August) that's outpacing most of its serving-paper cohort rather than leveling off.

Otherwise the diffusion/quant breakouts from last cycle (Flash-dLLM, HyQuant, Disaggregated Quantization) simply held their gains into 09-30 without fresh acceleration — the surge has cooled to a simmer.
