# Inference Ecosystem — Flash News

**2026-03-03** — 100 new papers scanned · 0 hype surges

## Top Papers

**Multi-Head Low-Rank Attention (MLRA)** — score 95 · hype 82
ICLR 2026 work that cracks open DeepSeek's single-latent MLA head into multiple partitionable KV heads, making tensor-parallel decoding actually efficient: 2.8x faster than FlashMLA with no quality loss on Llama-3.1-8B.
[arXiv:2504.02835](https://arxiv.org/abs/2504.02835)

**Learning to Draft (LTD)** — score 95 · hype 82
Applies RL to jointly learn *which layers to skip* and *which smaller draft model to call* during speculative decoding — the draft policy co-adapts with the target model instead of being frozen. Up to 36.4% speedup over Eagle3 on Qwen3-32B.
[arXiv:2504.01838](https://arxiv.org/abs/2504.01838)

**TriMoE** — score 92 · hype 62
Treats MoE expert placement as a hot/warm/cold tiering problem across GPU, AMX-enabled CPU, and near-DIMM NDP accelerators. A lightweight scheduler routes experts to the right tier each step, yielding 2.1–2.8x decode speedup on DeepSeek-V2/Mixtral without extra GPUs.
[arXiv:2504.02490](https://arxiv.org/abs/2504.02490)

**KVSlimmer** — score 92 · hype 62
Uses exact Hessian-based importance scores to merge KV cache entries *asymmetrically* — keys and values get different budgets per layer. Cuts KV memory 29% and decode latency 28% on LLaMA-3-8B with negligible accuracy loss.
[arXiv:2504.02840](https://arxiv.org/abs/2504.02840)

**Quasar** — score 92 · hype 62
Quantizes the *verification* phase of speculative decoding to W8A8, not just the draft model. Custom CUDA kernels for quantized tree attention push throughput 1.28x higher while preserving lossless output quality.
[arXiv:2504.02300](https://arxiv.org/abs/2504.02300)
