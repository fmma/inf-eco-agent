# Inference Ecosystem — Flash News
**2026-07-16 · 145 papers scanned · 5 featured**

## [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095)
Xiaomi's MiMo team documents the first production serving stack for the Hybrid SWA + MoE + multimodal combo, with a dual-pool KV cache enforcing strict O(W) SWA storage, SWA-aware prefix cache trees, and GCache — a co-located RDMA L3 cache hitting 170 GB/s single-process (350 GB/s under GDR) at zero extra storage cost. Payoffs are concrete and hard-won: 93–95% server-side cache hit rates, ~40% end-to-end gain from halving EP, 30% lower long-request TTFT P90, 2.3× MTP speedup on early decode, and 1-hour video decode cut from 156s to 23s. This is the rare end-to-end field manual for serving modern composite architectures — required reading if you run long-context MoE in production. Score: 94 (was 95)

## [NSNQuant: A Double Normalization Approach for Calibration-Free Low-Bit Vector Quantization of KV Cache](https://arxiv.org/abs/2505.18231)
NSNQuant (NeurIPS 2025) makes KV-cache vector quantization calibration-free: a Normalize–Shift–Normalize transform plus Hadamard maps tokens onto a standard normal, so one reusable codebook works across models and datasets — killing the distribution-shift fragility that sinks Coupled Quantization on OOD data. It wins at both 1-bit and 2-bit, delivers 3× throughput and 4× larger batches, and crucially *lowers* per-step decode latency (36.5ms vs 50.8ms FP16) by relieving the memory wall. Calibration-free + custom CUDA kernels + released code make this immediately deployable for decode-heavy reasoning and code workloads. Score: 89 (was 90)

## [DarwinLM: Evolutionary Structured Pruning of Large Language Models](https://arxiv.org/abs/2502.07780)
From IST-DASLab, DarwinLM (COLM 2026) does training-aware, non-uniform structured pruning via evolutionary search with lightweight fine-tuning baked into offspring selection, beating ShearedLlama while using 5× less post-training data. Structured pruning buys hardware-agnostic speedups: the 2.7B Llama-2 variant hits 1.98× throughput and 2.43× lower memory on an L40s, and it's the first non-uniform structured pruning shown to work on MoE (Qwen3-30B-A3B → 16B-A2B at ≥90% of dense accuracy). If you need a smaller, genuinely faster model on stock hardware, this is current SOTA. Score: 76 (was 70)

## [Efficient and Privacy-Aware Edge-Cloud Collaborative Inference for Large Language Models](https://arxiv.org/abs/2607.13093)
KunlunMeta splits a 7B decoder across endpoint and cloud with endpoint-authorized KV cache, a hidden-dim-split vocabulary projection, and endpoint-side speculative decoding (draft N=5). It cuts per-token latency up to 46.1% over naive split inference and downlink payload up to 67.4% via language-adaptive logit masking, while staying within ~1% of the full cloud model on MMLU/GSM8K/HumanEval. A pragmatic blueprint for latency- and privacy-sensitive on-device+cloud serving — though it's a prototype stitching known techniques together rather than one new primitive. Score: 75 (was 88)

## [Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference](https://arxiv.org/abs/2607.13205)
A sharp diagnostic: on schema-dense input (nested JSON), H2O-style attention-mass eviction retains structural noise — delimiter "sink" tokens carry ~40× the energy of answer-bearing VALUE tokens and KEY tokens are over-retained 1.8×, collapsing exact-match from 88% to 0% at a 5% budget. A retraining-free, role-conditional allocator over SnapKV closes 63–98% of the H2O gap at sub-20% budgets across four model families. The caveat: it's a masking-based study with no realized memory/latency win yet and a seed-sensitive quality claim — but the insight should change how anyone evicts cache for structured/agentic RAG. Score: 74 (was 86)

---

## Surge Watch

Long-context sparse attention is where the community's eyes are this week. [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) is the clearest breakout — GitHub stars doubled 41→83 and HF upvotes rose 55→67 in just three days (Jul 10→13), fast heat for a fresh "infinite context" paper. Riding the DeepSeek-V4 name, [FlashMemory-DeepSeek-V4](https://arxiv.org/abs/2606.09079) kept climbing to 65 HF upvotes and 88 GitHub stars, up from 58/61 in mid-June.

On the decoding side, [BlockPilot](https://arxiv.org/abs/2606.31315) landed hard: 76 HF upvotes and 60 GitHub stars almost immediately after showing up on the radar — the strongest debut in the recent diffusion speculative-decoding wave.
