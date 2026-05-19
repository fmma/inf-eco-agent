# Inference Ecosystem — Flash News
**2026-05-19 | 638 papers scanned, 5 highlighted**

### [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/abs/2605.17757)
OSCAR derives rotations from attention-aware covariance structures (query covariance Q^TQ for keys, score-weighted V^TS^TSV for values) rather than raw cache reconstruction, enabling INT2 KV quantization that actually works. Deployed end-to-end in SGLang with custom Triton decode kernels, it reduces KV memory ~8x and delivers up to 7x throughput at large batch sizes on H100. On Qwen3-32B and GLM-4.7 (358B), it matches BF16 accuracy at just 2.28 bits per element — naive Hadamard INT2 collapses to near-zero on these same models. The production-ready paged-cache integration and prefix-cache compatibility make this immediately deployable.
**Score: 96 (was 95)**

### [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://arxiv.org/abs/2605.18071)
A systems-perspective attack on KV cache offloading spanning GPU HBM, host DRAM, and SSD. Three interlocking mechanisms: attention-aware cache management with lookahead eviction and 2D layer-head window scaling, elastic SFC pipeline scheduling that overlaps selection/fetching/computation via micro-batching, and coordinated multi-tier storage with SSD-aware layouts. Achieves 1.74x throughput over ShadowKV/Quest/RetroInfer on RULER and LongBench across L20, H20, and RTX 4090 — while preserving accuracy. The cost-efficiency analysis is striking: an RTX 4090 with KVDrive outperforms an H20 baseline at 3x throughput for long-context workloads.
**Score: 95 (was 97)**

### [TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks](https://arxiv.org/abs/2605.17170)
Assigns INT2/INT4 bitwidths per-token along three axes — temporal recency, modality (text vs. image), and semantic role (instructions, reasoning, tool calls, observations) — using chat-template-only tagging with zero model inference. On Qwen3-VL-32B-Thinking running OSWorld computer-use tasks, it matches BF16 accuracy while fitting 4.5x the KV cache and delivering 1.3x end-to-end throughput. The dual-pool paged memory design with fused Triton decode kernels handling mixed INT2/INT4 on-the-fly is cleanly integrated into SGLang. Where KIVI and SGLang FP4 drop 4-5 points on BFCL Memory, TriAxialKV stays within 0.7 points of BF16.
**Score: 93 (was 95)**

### [Throughput-Optimal Scheduling Algorithms for LLM Inference and AI Agents](https://arxiv.org/abs/2504.07347)
Develops queueing-theoretic foundations proving that work-conserving schedulers (Orca, Sarathi-Serve) are throughput-optimal for LLM inference, while FasterTransformer and vanilla vLLM are provably not maximally stable. Extends to AI-agent workloads with DAG and fork-join topologies, and constructs a Rybko-Stolyar counterexample showing work-conserving policies can fail under cyclic routing. The batch-size constraint analysis reveals a surprising 2D stability region where even work-conserving algorithms can fail. This gives practitioners a rigorous design principle: work-conserving first, then optimize latency within that class.
**Score: 92 (was 95)**

### [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://arxiv.org/abs/2605.16839)
Decouples block-level KV selection from sparse-kernel execution for chunked prefill — the regime where Q << KV makes existing block-sparse kernels inefficient. Converts 2D per-head block masks into GQA-aware per-group KV block tables via Q-block union and intra-group union, then executes zero-copy through paged attention in FlashInfer. On LLaMA-3.1-8B at 128K context on H200, delivers 2.72x attention speedup and 1.96x end-to-end over dense attention while staying within 2 points of dense accuracy on RULER. The key insight: the bottleneck isn't which KV blocks to select, but how the selected blocks are executed.
**Score: 90 (was 95)**

---

## Surge Watch

Nothing noteworthy in signal trends today.
