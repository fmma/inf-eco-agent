# Inference Ecosystem — Flash News
**2026-07-28 · 249 papers scanned, 5 that matter**

## [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](https://arxiv.org/abs/2607.24593)
DeepSeek Sparse Attention made downstream attention cheap but left its indexer scanning the full prefix per query — up to 81% of prefill latency at 200K tokens. PIVOT amortizes one shared prefix scan across a group of nearby queries via a mean-pooled proxy, then either reuses the proxy top-k (fast) or re-scores a 2k candidate set per query (accurate); in decode it rides MTP's draft tokens for free. On DeepSeek-V3.2 and GLM-5.1 it matches dense-indexer accuracy on LongBench/RULER while cutting indexer cost up to 4× and end-to-end latency 1.6×. Training-free, drop-in, and orthogonal to existing token/head/layer-axis accelerators — the one to watch if you serve DSA models. Score: 95 (was 95)

## [LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding](https://arxiv.org/abs/2607.24555)
Attention keys are locally low-rank but globally high-rank, so LOCKS gives every KV page its own rank-8 int4 spectral summary (~10% of cache size) and selects top pages by reconstructed log-sum-exp without reading a single candidate key or value. It tracks the read-every-key oracle down to 0.5% budgets, matches FullKV at 100K+ context while attending ~2% of tokens, and halves decode latency (2.0× at 1M, 9.8× fewer bytes/step). Ships as a drop-in plugin for unmodified vLLM with full CUDA-graph decode — rare to see a shared-projection impossibility proof and retention bound behind a genuinely deployable selector. Score: 94 (was 95)

## [Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch](https://arxiv.org/abs/2607.23099)
Production serving picks fused-MoE kernels by token-count bucket alone, ignoring that per-expert routing skew shifts the optimal MMA tile shape. DA-MoE (NVIDIA/Kung) adds an "Effective Experts" metric plus Dirichlet reverse-modeling to build offline exemplar→kernel tables, then matches the live routing histogram on-GPU via conditional CUDA Graphs with zero CPU sync. On B200 HumanEval-X traces it improves geomean fused-MoE latency 1.16× on DeepSeek-V3 and 1.29× on Kimi K2 (peak 1.56×), with gains growing under skew and higher expert-parallelism. Score: 88 (was 90)

## [X-Stage: An Overlooked Pipeline Stage for Communication–Computation Overlap in DiT Inference](https://arxiv.org/abs/2607.23264)
Device-initiated remote stores don't complete at issue — X-Stage names the post-issue drain window and models it with three calibrated numbers: backpressure-free issue time, a ~717 GB/s drain rate, and ~4.25 MiB outstanding capacity. The Burst–Gap model predicts when sustained injection backpressures the Tensor Core producer, guiding two fixes: cross-wave Linear-1/Linear-2 interleaving in DeepGEMM MegaMoE (1.18× geomean, 1.62× max across 84 configs) and piggybacked FlashAttention-3/4 + Ulysses All-to-All (up to 1.43×) with no dedicated comm warp or SM. A sharp, well-instrumented lens for anyone hand-tuning fused MoE or long-context attention kernels. Score: 86 (was 85)

## [MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2607.23047)
One offline calibration, any deployment budget: MixQuant fixes the deployment-context mismatch by marginalizing each layer's distortion over random quantized upstream configs instead of FP16, then adds plan-aware AWQ/GPTQ params and a tail penalty keeping layers off the lowest bitwidths — with a cheap greedy solve that matches an ILP at deploy time. Across Llama-3.2-3B, Llama-2-7B, and Mistral-7B it beats adaptive and mixed-precision baselines by up to 8 points and drops perplexity 12.43→10.70 at the tightest budget. The wins concentrate exactly where aggressive quantization hurts most, which is where edge deployment lives. Score: 82 (was 85)

---

## Surge Watch

Nothing noteworthy in signal trends today.
