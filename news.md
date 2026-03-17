# Inference Ecosystem — Flash News
**2026-03-17** | 437 papers scanned

## [NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL](https://arxiv.org/abs/2603.13606v1)

NVIDIA ships MoE dispatch/combine primitives directly inside NCCL via the Device API, ending the fragmentation across DeepEP, pplx-kernels, and Hybrid-EP. The library offers unified `ncclEpDispatch`/`ncclEpCombine` calls with Low-Latency mode (1-128 tokens, all-to-all RDMA mesh) and High-Throughput mode (4096+ tokens, hierarchical NVLink+RDMA). On an H100 cluster, LL dispatch throughput matches or exceeds DeepEP at 2-8 nodes; end-to-end vLLM integration with Qwen3-30B-A3B trails DeepEP by 7-10% on ITL/TPOT, attributed to combine overhead the team is actively optimizing. The real value is ecosystem convergence: one API, one topology stack, one memory allocator path for all MoE communication on current and future NVIDIA platforms.
Score: 93 (was 95)

## [LMetric: Simple is Better — Multiplication May Be All You Need for LLM Request Scheduling](https://arxiv.org/abs/2603.15202v1)

Multiplying two indicators (new prefill tokens and current batch size) produces a scheduling score that jointly optimizes KV cache reuse and load balancing without any hyperparameter tuning. Built as a standalone Rust router, LMetric was evaluated on real Alibaba BAILIAN traces (ChatBot, API, Coder, Agent workloads) with Qwen2-7B and Qwen3-30B MoE on 16 H20 GPUs. It reduces mean TTFT by 92% and TPOT by 21% vs vLLM-v1, and consistently outperforms NVIDIA Dynamo, llm-d, and BAILIAN's tuned production scheduler. The paper also derives the mathematical conditions under which multiplication fails (extreme KV$ hotspots) and shows they are detectable in practice.
Score: 93 (was 92)

## [FlashHead: Efficient Drop-In Replacement for the Classification Head](https://arxiv.org/abs/2603.14591v1)

Reframes the output head as a retrieval problem: vocabulary tokens are clustered via spherical k-means into 8K balanced groups, then multiprobe retrieval scores candidate clusters in parallel at decode time. The method is training-free and hardware-friendly, reducing head parameters from 263M to 33M on Llama-3.2-1B while delivering 1.75x end-to-end speedup (INT4 GPU) and 4.85x head-only speedup. Benchmarks across Llama-3.2, Gemma-3, and Qwen-3 show negligible accuracy loss. Most impactful for small models on consumer devices where the head accounts for up to 60% of parameters, but the technique scales to 8B models as well.
Score: 92 (was 95)

## [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](https://arxiv.org/abs/2603.14224v1)

Unifies KV cache compression and sparse token retrieval into a single 1-bit sign-based vector quantization format. The compressed key representation doubles as a functional index: a LUT-GEMV kernel computes approximate attention scores directly from sign codes, selecting top-k tokens without auxiliary data structures. Custom CUDA kernels fuse dequantization with sparse FlashAttention, achieving 5x memory reduction and 2x decode throughput over full-cache FlashAttention2 on Llama3.1-8B and Qwen2.5-14B. One-pass clustering is 20x faster than k-means, and the retrieval procedure provides 4x speedup over Quest under identical sparsity budgets.
Score: 88 (was 92)

## [OmniServe: Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking](https://arxiv.org/abs/2603.12831v1)

Offloads best-effort (BE) attention computation to idle CPU cores while latency-sensitive (LS) requests keep the GPU, using asynchronous CPU-GPU streams to avoid blocking. Layer-wise batching and explicit latency modeling allow OmniServe to dynamically control how many BE requests piggyback onto each decode iteration. On a 4xA100 cluster serving Llama-2-70B, the system sustains Sarathi-Serve-level SLO attainment for LS services (within 0.6%) while boosting BE decode throughput by up to 9.85x. The approach is particularly effective under heavy LS load where baseline systems starve BE requests entirely.
Score: 88 (was 92)

---

## Surge Watch

[IndexCache](https://arxiv.org/abs/2603.12201v1) keeps accelerating: 37 → 48 HF upvotes and 12 → 35 GitHub stars in the last two days. That is faster growth than the prior 25 → 37 interval. Cross-layer index reuse for sparse attention is clearly resonating beyond the initial audience.

[LookaheadKV](https://arxiv.org/abs/2603.10899v1) emerged from zero to 6 HF upvotes and 5 GitHub stars in four days. A KV cache eviction method that peeks ahead without generation (relevance 92) getting early practitioner attention worth watching.

FlashPrefill GitHub stars quietly resumed: 28 → 33 over the last four days after the plateau flagged last time. HF upvotes remain frozen at 9. Modest developer-side interest persists even as broader community engagement has not returned.

DualPath flatlined at 43 HF upvotes for a full week. Qwen3-Coder-Next similarly stuck at 48. Both are done growing.
