# Inference Ecosystem — Flash News
**2026-04-20 | 431 papers scanned, 5 selected**

### [Faster LLM Inference via Sequential Monte Carlo](https://arxiv.org/abs/2604.15672v1)

SMC-SD replaces speculative decoding's token-level rejection with importance-weighted resampling over a population of draft particles, turning verification into a fixed-size vectorized operation with no rollback. On Llama 1B→70B across 4 H100s, it hits 342 tok/s — a 5.2x speedup over autoregressive and 2.36x over optimized tree-based SD in SGLang, while staying within 3% accuracy. The key insight: because LLM decoding is memory-bandwidth-bound, the extra arithmetic for scoring particles comes nearly free. Built as a fork of SGLang with PagedAttention and RadixAttention integration, plus a 72.3% KV cache reduction via prefix sharing. Code released.
Score: 95 (was 95)

### [Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU](https://arxiv.org/abs/2604.15464v1)

Google's RPA kernel fills the critical gap in TPU-native LLM serving. Built with Pallas/Mosaic, it fuses KV cache scatter/gather directly into the FlashAttention-2 compute loop, eliminating a major TensorCore bottleneck. On Llama 3 8B on TPU7x Ironwood, RPA achieves 86% memory bandwidth utilization in decode and 73% MFU in prefill. A distribution-aware compilation strategy dispatches specialized kernels for decode-only, prefill-only, and mixed workloads. Already integrated as the primary TPU backend in both vLLM and SGLang, delivering 2-5x throughput gains since February 2025.
Score: 95 (was 95)

### [The Illusion of Equivalence: Systematic FP16 Divergence in KV-Cached Autoregressive Inference](https://arxiv.org/abs/2604.15409v1)

A surprising finding: KV-cached and cache-free FP16 inference produce *different* token sequences 100% of the time — even under greedy decoding — due to FP16 non-associativity in accumulation order. Tested across LLaMA-2-7B, Mistral-7B, and Gemma-2-2B on GSM8K, the divergence is deterministic and architecturally predictable: GQA amplifies it by broadcasting rounding errors across shared query heads. FP32 eliminates it entirely (8 orders of magnitude reduction). Activation patching proves the causal variable lives in the KV cache state itself, not the residual stream. Anyone building correctness-sensitive inference pipelines with prompt caching should take note.
Score: 88 (was 88)

### [Accuracy Is Speed: Towards Long-Context-Aware Routing for Distributed LLM Serving](https://arxiv.org/abs/2604.15732v1)

Introduces Time-to-Correct-Answer (TTCA) — wall-clock time to the first *correct* response — as a routing metric for distributed serving. The insight: under long contexts, model accuracy varies unpredictably by length, language, and architecture, so incorrect responses trigger costly retries that dwarf single-shot latency differences. LAAR (Lightweight Accuracy-Aware Routing) uses logistic regression on prompt features to estimate per-model success probability, achieving up to 49% TTCA improvement over session-affinity routing. Implemented as an Envoy EPP policy for llm-d with O(|M|) overhead. A practical reframe: for long-context serving, accuracy *is* a systems metric.
Score: 82 (was 90)

### [MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs](https://arxiv.org/abs/2604.16007v1)

A memory system synthesizer for heterogeneous NPU design targeting agentic LLM workloads. MemExplorer jointly explores 3D-stacked SRAM, HBM4, LPDDR, and emerging High Bandwidth Flash across prefill/decode disaggregated architectures using multi-objective Bayesian optimization. Key finding: prefill benefits most from high-bandwidth 3D-stacked on-chip SRAM (up to 2.3x energy efficiency over baseline NPU), while decode favors larger-capacity, lower-bandwidth off-chip tiers (1.93x efficiency gain). Evaluated on Llama-3.3-70B and Qwen3-32B with real agentic traces from OSWorld and BFCL. Timely given NVIDIA's Vera Rubin heterogeneous architecture direction.
Score: 85 (was 92)

---

## Surge Watch

[TriAttention](https://arxiv.org/abs/2604.04921) continues its strong run — now at 108 HF upvotes and 607 GitHub stars after launching two weeks ago. The initial explosion (24→100 HF in 5 days) has cooled, but stars keep climbing at ~20/day. Most-engaged KV compression paper in the tracker this month.

[Nemotron 3 Super](https://arxiv.org/abs/2604.12374) (NVIDIA's hybrid Mamba-Transformer MoE) is picking up steam: 4→33 HF upvotes in 5 days since appearing Apr 15, and still accelerating. Worth watching whether this sustains as it enters agentic-reasoning benchmarks.

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619) had been completely flat at 162 GitHub stars for a week, then spiked to 193 overnight (Apr 20). Something re-surfaced it — possibly implementation activity.

[FlashAttention-4](https://arxiv.org/abs/2603.05451) is an odd case: 7 citations (1 influential) and climbing steadily in the academic graph, but just 1 HF upvote and no GitHub engagement after 6 weeks. The research community is citing it; the practitioner community hasn't touched it yet.
