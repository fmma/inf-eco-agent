I've read all eight PDFs in full. Rescoring on actual contribution: **SmartGen** and **WIDE** hold up as top-tier systems work with deployable, measured speedups; **SparseSpec-L**, **SpecPrefetch**, and **Counter-Causal Surprise** are strong training-free/practical wins. I'm dropping the two hardware-accelerator quantization papers (**GyRot ~79**, **LightRot ~77** — real but ASIC-only, not GPU-deployable) and the **MLA Functional Reconstruction** paper (~81 — honest, but it explicitly shows no end-to-end speedup and only partial acceptance recovery). Here's the bulletin:

# Inference Ecosystem — Flash News
**2026-07-31 · 287 new papers scanned · top 5 featured**

## [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/abs/2607.28150)
Attacks the "stage-transition stall" that cripples self-hosted P/D disaggregation on cheap cloud instances (10–35 Gbps), where transferring a 48K-token KV cache takes 6.5× longer than prefill itself. Three paths — profile-based proactive push of universally-important KV, parallel on-demand fetch that overlaps remote round-trips with local loading, and background speculative transfer — cut time-to-second-token up to 4.3× vs full transfer with matched accuracy, and drop into InfiniGen/HATA sparse-attention stacks unmodified. If you run disaggregated serving on rented GPUs, this is the most immediately deployable result in the batch. Score: 95 (was 95).

## [WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning](https://arxiv.org/abs/2607.28418)
The first token-level dynamic width pruning that actually ships wall-clock speedups, because it co-designs the router with the GPU kernel (mask reordering → CTA-level skip → CuTe intra-block skip) instead of dying on irregular gather-scatter. At 50% sparsity it beats dynamic-depth SkipGPT by 8.8 avg-accuracy points and hits 1.98×/4.95× kernel-level and 1.68×/1.55× end-to-end for prefill/decode under CUDA Graph. Dynamic sparsity almost always fails to translate into real acceleration — WIDE is the rare one that does, with code. Score: 91 (was 92).

## [A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding](https://arxiv.org/abs/2607.27735)
Training-free self-speculation for long context: the target model drafts against a dynamically sparsified, recallable KV cache and verifies with full attention, recycling per-head verification attention stats as a zero-extra-forward importance signal. Its efficiency analysis nails the "inversion" where longer speculation hurts once acceptance falls below draft cost, and an entropy controller adaptively picks k — reaching 2.79× over autoregressive on LongBench v2 (Llama-3.1-8B) while preserving the output distribution. Honest caveat: verification still runs non-fused dense attention, so a fused kernel leaves headroom. Score: 90 (was 93).

## [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/abs/2607.24787)
Router-preserving expert prefetching for offloaded MoE — tiny per-layer low-rank adapters predict next-layer expert priorities purely to schedule async transfers, while the frozen native router still selects executed experts, so prediction errors cost bandwidth, not accuracy. A window-aware budget caps prefetch to what the compute overlap can actually hide; on a Snapdragon 8 Elite it lifts decode throughput up to 20% under storage-constrained offloading with 6.48M params (3.1% of ProMoE). The cleanest edge-MoE serving win here, with code and weights. Score: 89 (was 90).

## [Back from the Future: Key-Value Cache Management by Counter-Causal Surprise](https://arxiv.org/abs/2607.27600)
A refreshingly simple eviction rule — a token is redundant if it's predictable from the tokens that follow it — scored by rerunning cached K/V under an upper-triangular mask, no training. It sidesteps the self-reinforcing attention bias that makes H2O/TOVA drop rarely-attended-but-critical facts (shown failing badly on LoCoMo), and a single-layer approximation cuts refresh cost 7–9× (7.9ms at 512 tokens). Competitive-to-better across MATH500, AIME, LongHealth, Qasper and LoCoMo on Qwen2.5 and Llama-3.1. Score: 88 (was 90).

---

## Surge Watch

Cleanest cold-open of the cycle: [SWE-Pruner Pro](https://arxiv.org/abs/2607.18213) (coder-LLM-guided token pruning) landed Jul 27 already holding **76 HF upvotes** — one of the strongest same-day debuts on the board — nudging to 78 by Jul 30. GitHub is lagging hard at 13 stars, so the open question is whether repo interest catches the upvote buzz or this stays a paper-only splash.

Strangest mover: [Fish Audio S2](https://arxiv.org/abs/2603.08823) snapped out of months of ~10-stars/day dormancy — GitHub stars ran **31,399 → 31,777 (Jul 29→31)**, a +378 two-day burst (HF upvotes also ticked 38→39). Almost certainly release-driven on an already-30k-star TTS repo, but the jolt is real and worth a glance.

Meanwhile last cycle's organic riser has fully stalled: [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) sits at 129 stars / 82 upvotes — no movement, confirming the plateau call.
