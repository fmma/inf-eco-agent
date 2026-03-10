All 8 PDFs read. Now I have the full context to rescore and write the bulletin.

**Rescored relevance (based on full papers):**
- ArcLight: 92 (up from 95 — solid but ARM-only, limited eval setup)
- SageSched: 93 (up from 92 — comprehensive system with real vLLM integration, Gittins index is clever)
- LycheeCluster: 90 (up from 88 — strong results, 3.6x speedup, outperforms Quest/ClusterKV on LongBench V2)
- DDP (Structured Pruning): 85 (same — applied to Qwen3 MoE, vLLM speedups demonstrated)
- DualSpec: 80 (down from 82 — interesting but agent-specific, not core inference)
- DyLLM: 82 (up from 80 — impressive 9.6x throughput on Dream, novel diffusion LLM focus)
- EAGLE-Pangu: 75 (down from 90 — well-engineered but Ascend-specific, modest 1.27x mean speedup)
- SERQ: 80 (down from 82 — solid W4A4 quantization but incremental over existing PTQ methods)

Top 5 selected: SageSched (93), ArcLight (92), LycheeCluster (90), DDP (85), DyLLM (82).

# Inference Ecosystem — Flash News
**2026-03-10 — 209 papers scanned**

### [SageSched: Efficient LLM Scheduling Confronting Demand Uncertainty and Hybridity](https://arxiv.org/abs/2603.07917v1)

Finally, a scheduler that treats LLM requests as what they are: jobs with unknown duration AND heterogeneous resource demands. SageSched predicts output-length *distributions* (not point estimates) using semantic-aware history retrieval, models true service cost across both compute and memory bounds, and schedules via the Gittins index — a theoretically optimal policy for unknown-duration jobs. Built on vLLM and tested on Llama-3.1-8B and Qwen3-32B with real ShareGPT/Alpaca/Write traces, it beats TRAIL by 28.7% on TTLT. The predictor runs in under 0.5ms per request with zero training overhead.
Score: 93 (was 92)

### [ArcLight: A Lightweight LLM Inference Architecture for Many-Core CPUs](https://arxiv.org/abs/2603.07770v1)

A ground-up rewrite of CPU-based LLM inference that takes the NUMA memory wall seriously. ArcLight introduces cross-NUMA tensor parallelism with per-node buffer allocation, multi-view thread groups, and asynchronous subgraph execution. Tested on a 192-core Kunpeng-920 (4 NUMA nodes) with Qwen3-4B Q4_0, it hits 46% higher decode throughput than llama.cpp. The entire engine is ~10 C++ files — deliberately minimal and hackable. Open-sourced by OpenBMB. Currently ARM-only (NEON), but the architecture is portable.
Score: 92 (was 95)

### [LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing](https://arxiv.org/abs/2603.08453v1)

Tackles the KV cache retrieval problem with a key insight: the retrieval *unit* matters as much as the retrieval *metric*. LycheeCluster segments context into variable-length semantic chunks (respecting natural boundaries), then builds a 3-tier hierarchical index (coarse units → fine clusters → chunks) with triangle-inequality pruning for O(log n) retrieval. Achieves 3.6x decode speedup at 64K context on H20 GPU vs full attention, while matching or beating Quest, ClusterKV, and ShadowKV on LongBench V2 (30.82 vs 30.02 full attention). Lazy incremental updates keep streaming overhead under 1% of decode time.
Score: 90 (was 88)

### [Deterministic Differentiable Structured Pruning for Large Language Models](https://arxiv.org/abs/2603.08065v1)

DDP replaces stochastic hard-concrete masks with deterministic ReLU gating and annealed surrogate scores for structured pruning. The mask-only optimization converges in ~20 min on 4x H20 using just 30M tokens — no weight updates needed. Applied to Qwen3-32B and Qwen3-30B-A3B (MoE), it achieves <1% accuracy loss at 20% sparsity while outperforming LoRAPrune and SlimLLM. End-to-end vLLM speedups confirmed: 1.36x on RTX 5090 at 20% sparsity, 2.20x at 50%. Practical, fast, and directly deployable.
Score: 85 (was 85)

### [DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention](https://arxiv.org/abs/2603.08026v1)

As diffusion LLMs (LLaDA, Dream) approach AR quality, their repeated full-sequence denoising remains brutally expensive. DyLLM observes that most token representations stay stable across diffusion steps — only "salient" tokens (identified by cosine similarity of attention contexts) need recomputation. It selectively recomputes FFN and attention only for salient tokens, using a dual-path approximate attention for the rest. Training-free, it achieves up to 9.6x throughput on Dream 7B while preserving baseline accuracy on GSM8K, MATH, and MBPP. This is the efficiency breakthrough diffusion LLMs needed to be practical.
Score: 82 (was 80)

---

## Surge Watch

[FlashPrefill](https://arxiv.org/abs/2603.06199v1) is picking up early community traction — HF upvotes jumped from 1 to 9 and GitHub stars from 3 to 12 in just one day since appearing. Worth watching given it was the standout paper this scan. [Qwen3-Coder-Next](https://arxiv.org/abs/2603.00729v1) continues steady accumulation at 43 HF upvotes (up from 6 a week ago), though that's modest for a major lab release. Everything else is flat or negligible.
