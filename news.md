PDF tooling isn't available in this environment. I'll write the bulletin based on the detailed abstracts provided for all 20 papers — they contain method names, benchmarks, and concrete results.

# Inference Ecosystem — Flash News
**2026-04-08 — 526 papers scanned**

### [FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving](https://arxiv.org/abs/2604.02715)
FluxMoE rethinks MoE inference by treating expert weights as transient, streamed resources instead of persistent GPU residents. Its expert paging abstraction materializes experts on demand and evicts them immediately after use, freeing GPU memory for the KV cache that actually drives throughput. Built on vLLM, it delivers **3x throughput gains** in memory-constrained regimes without touching model fidelity. As MoE models proliferate, this is the kind of systems work that directly unblocks production serving.
Score: 94 (was 95)

### [TAPS: Task-Aware Proposal Distributions for Speculative Sampling](https://arxiv.org/abs/2603.27027)
TAPS demonstrates that *what you train your draft model on* matters as much as draft architecture for speculative decoding quality. Domain-specific HASS and EAGLE-2 drafters show clear specialization — MathInstruct drafts dominate reasoning benchmarks while ShareGPT drafts win on MT-Bench. The real gem: **confidence-based routing** across specialized drafters plus merged-tree verification yields the highest acceptance lengths overall. Already at **141 HF upvotes** — the community noticed. Practical guidance for anyone tuning spec-dec in production.
Score: 91 (was 92)

### [Fast NF4 Dequantization Kernels for Large Language Model Inference](https://arxiv.org/abs/2604.02556)
A lightweight shared-memory CUDA optimization that speeds up NF4 dequantization by **2.0–2.2x** at the kernel level and delivers up to **1.54x end-to-end improvement** on Gemma 27B, Qwen3 32B, and Llama3.3 70B. It exploits the 12–15x latency advantage of shared memory over global memory with only 64 bytes per thread block. Drop-in replacement for BitsAndBytes in the HuggingFace ecosystem — minimal engineering effort, immediate payoff on existing GPU infrastructure.
Score: 90 (was 92)

### [Attention Editing: Cross-Architecture Attention Conversion](https://arxiv.org/abs/2604.05688)
Converts already-trained LLMs to more efficient attention architectures — specifically MLA and a gated hybrid sliding-window design — via progressive distillation (layer-wise teacher-forced, then model-level). Applied to **Qwen3-8B and Qwen3-30B-A3B** with competitive quality retained. This is the post-training KV cache cost reduction approach inference teams have been waiting for: no repretraining, just swap the attention and distill. Notably trained on Ascend 910B, offering a non-NVIDIA deployment reference.
Score: 88 (was 90)

### [HybridKV: Hybrid KV Cache Compression for Multimodal LLM Inference](https://arxiv.org/abs/2604.05887)
Tackles the visual token explosion in multimodal LLMs with a three-stage hybrid compression: classify attention heads as static vs. dynamic, allocate budgets top-down, then apply text-prior pruning or chunk-wise retrieval per head type. On Qwen2.5-VL-7B across 11 benchmarks: **7.9x KV cache memory reduction** and **1.52x faster decoding** with negligible quality loss. As vision-language workloads scale, this head-aware approach is more principled than uniform token eviction.
Score: 87 (was 92)

---

## Surge Watch

[TriAttention](https://arxiv.org/abs/2604.04921v1) is this week's breakout. The trigonometric KV compression paper went from 24 to 72 HF upvotes and 9 to 194 GitHub stars in a single day — the sharpest one-day acceleration we've tracked. Relevance score of 95. Worth watching whether this sustains or was a one-day viral spike.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) crossed the 3,000-star mark (3,020 today), picking up a third citation. Growth has settled into a steady ~30 stars/day cruise — no longer explosive, but the install base keeps compounding.

Everything else is flat or showing only incremental movement. [TAPS](https://arxiv.org/abs/2603.27027v1) sits at 141 HF upvotes but has barely moved since surfacing (+7 in a week) and only 4 GitHub stars — high initial buzz, no follow-through yet.
