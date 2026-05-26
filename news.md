# Inference Ecosystem — Flash News
**2026-05-26 — 383 papers scanned, 5 selected**

### [vAttention: Verified Sparse Attention](https://arxiv.org/abs/2510.05688)
From Ion Stoica's group at Berkeley (published at ICLR 2026), vAttention is the first sparse attention mechanism with user-specified (ε, δ) approximation guarantees. It unifies top-k selection with uniform random sampling, adaptively sizing the sample per head per query via CLT-based budget computation. On RULER-HARD at 10% sparsity, it lifts HashAttention accuracy by 4.5 points on Llama-3.1-8B, and matches full-attention quality on AIME2024 at 10x sparsity with 32K-token generations on DeepSeek-R1-Distill. Near-linear wall-clock speedup demonstrated with CPU-offloaded KV caches. This sets a new bar: sparse attention you can actually trust in production.
Score: 95 (was 92)

### [Optimus: Elastic Decoding for Efficient Diffusion LLM Serving](https://arxiv.org/abs/2605.24832)
Optimus treats decoding granularity as a runtime control variable for diffusion LLM (DLLM) serving. Its chunked decoding decomposes fixed blocks into fine-grained execution units without retraining, while saturation-aware scheduling dynamically selects chunk sizes based on GPU load — riding the Pareto frontier between GPU utilization and token efficiency. On A100 with SDAR-8B, it delivers 6.1x throughput over autoregressive decoding and 4.3x over fixed-block diffusion, with 3.5x serving capacity improvement under SLO constraints. Scales to 100B parameters. If you're evaluating DLLM serving, this is the systems paper to read.
Score: 94 (was 93)

### [Prism: Spectral-Aware Block-Sparse Attention](https://arxiv.org/abs/2602.08426)
Prism identifies a clean theoretical root cause for why mean-pooling-based block importance estimation fails: under RoPE, mean pooling acts as a low-pass filter that destroys high-frequency positional signals (slash patterns) via destructive interference. The fix is elegant — split estimation into high-frequency and low-frequency branches with energy-based temperature calibration. This is purely block-level (no token-level operations), making it faster than MInference, FlexPrefill, and XAttention at every sequence length tested. Achieves 5.1x prefill speedup at 128K tokens on Llama-3.1-8B while matching full-attention quality. Training-free and works on video generation (HunyuanVideo) too.
Score: 92 (was 90)

### [Beyond the Target: From Imitation to Collaboration in Speculative Decoding](https://arxiv.org/abs/2605.24793)
CoSpec flips the speculative decoding paradigm: instead of always deferring to the target model at mismatches, an RL-trained arbitration policy decides whether the draft or target token yields better task outcomes. On LLaMA-70B/8B, it simultaneously achieves 3.96x speedup and +1.7 accuracy improvement over target-only decoding on GSM8K/HumanEval/MBPP. The 94.1% agreement with oracle branch selection and cross-domain transfer (math training generalizes to code, QA, and dialogue) make the collaboration thesis convincing. A genuinely new direction for speculative decoding.
Score: 91 (was 90)

### [IndexMem: Learned KV-Cache Eviction with Latent Memory](https://arxiv.org/abs/2605.25475)
IndexMem pairs a lightweight learnable indexer (distilled from backbone attention) with a fast-weight latent memory that compresses evicted tokens into a compact state for residual readout. On RULER-16K with Qwen3-8B at 50% eviction, it scores 80.0 vs 62.8 for SnapKV — a 17-point gap. The latent memory module is orthogonal to the eviction policy and plugs into SnapKV for consistent gains. Validated across Qwen/Mistral/Llama at compression ratios up to 90%, with only 0.52M parameters for the memory module. Accepted at ICML 2026.
Score: 88 (was 92)

---

## Surge Watch

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) (Kimi team) more than doubled its citation count in two weeks — 8 on 05-04 to 19 by 05-18, with a +6 single-batch jump on 05-18 and a fourth influential citation. Community signals (185 HF upvotes, 3,289 stars) have plateaued, but the academic pickup is accelerating — this paper is quietly becoming a standard reference for attention architecture modifications.

[KVServe](https://arxiv.org/abs/2605.13734) is the fastest-moving new entry — 0 to 11 HF upvotes and 9 GitHub stars within its first week. Service-aware KV cache compression for disaggregated LLM serving is clearly hitting a nerve with the prefill-decode split crowd.

Otherwise, a quiet cycle. Previously highlighted papers have all flatlined: [MinT](https://arxiv.org/abs/2605.13779) barely moved (216→217 HF upvotes), [FlashAttention-4](https://arxiv.org/abs/2603.05451v1) stuck at 14 citations, [DiffAdapt](https://arxiv.org/abs/2510.19669) stabilized at 10 citations, and [Prefill-as-a-Service](https://arxiv.org/abs/2604.15039v1) flat at 5 citations.
