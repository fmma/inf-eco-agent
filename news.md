# Inference Ecosystem — Flash News
**2026-05-04 | 475 papers scanned**

## [SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters](https://arxiv.org/abs/2605.00528v1)

Agent workloads chain 10–100 LLM calls per task, yet today's schedulers treat each call independently — SAGA fixes this by making the entire agent workflow the schedulable unit. It introduces Agent Execution Graphs for predictive KV cache retention (within 1.31x of Bélády's offline optimal), session-affinity batching with work stealing, and Agent Fair Share scheduling with Lyapunov-drift guarantees. On a 64-GPU cluster serving SWE-bench and WebArena, SAGA cuts task completion time by 1.64x (geometric mean) over vLLM v0.15.1 with prefix caching, while hitting 99.2% SLO attainment under multi-tenant interference. This is the paper to read if you're building compound AI serving infrastructure. Score: 95 (was 95)

## [Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving](https://arxiv.org/abs/2605.00254v1)

UC Berkeley systematically challenges the assumption that expensive scale-up NVLink fabrics are necessary for MoE serving. Comparing scale-up, scale-out, 3D torus, and 3D full-mesh topologies on DeepSeek-V3 workloads across H100s, they find switchless topologies (especially 3D full-mesh) are 20.6–56.2% more cost-effective — current NVLink bandwidth is actually over-provisioned by up to 27%. A forward-looking analysis through Blackwell and Rubin generations shows the advantage persists. This directly informs billion-dollar datacenter procurement decisions. Score: 95 (was 94)

## [Eliminating Hidden Serialization in Multi-Node Megakernel Communication](https://arxiv.org/abs/2605.00686v1)

Perseus diagnoses why MoE megakernels (FlashMoE, Triton-distributed) collapse at multi-node scale: proxy-based RDMA fences serialize tile-level signaling, dropping throughput to 2% of unsignaled baselines at 96 concurrent transfers. The fix is elegant — decoupled signaling batches fences per-destination (8x fewer), and NIC-side ordering delegates the remaining fences to hardware. Result: up to 10.3x speedup on Libfabric, matching GPU-direct IBGDA performance on proxy-based IBRC. Applied to Triton-distributed's AllToAll with zero application changes, it achieves 79x speedup. Essential reading for anyone scaling MoE inference beyond a single node. Score: 94 (was 92)

## [EVICT: Adaptive Verification for MoE Speculative Decoding](https://arxiv.org/abs/2605.00342v1)

Tree-based speculative decoding hurts on MoE models because larger draft trees activate exponentially more experts, inflating verification cost. EVICT solves this by truncating draft trees to their cost-effective prefix before verification — using drafter confidence signals and offline-profiled MoE latency tables to maximize a utility ratio. Integrated with SGLang via pre-captured CUDA graphs, it achieves 1.21x average speedup over EAGLE-3 across Qwen3-30B, Qwen3-235B, and Ling-flash-2.0, while reducing active experts by 32.5%. Training-free, hyperparameter-free, and lossless. Score: 90 (was 93)

## [BWLA: Breaking the Barrier of W1AX Post-Training Quantization for LLMs](https://arxiv.org/abs/2605.00422v1)

First PTQ framework to achieve 1-bit weights with low-bit activations (W1A6) without retraining. The Orthogonal-Kronecker Transformation reshapes unimodal weights into binarization-friendly bimodal distributions via EM optimization, while simultaneously suppressing activation outliers — all through a single orthogonal rotation that preserves forward-pass equivalence. On Qwen3-32B, perplexity drops from 38 (SOTA) to 11.92 under W1A6, with 3.26x inference speedup and 80%+ memory savings. Where prior binary methods completely collapse under activation quantization, BWLA stays functional. Score: 88 (was 88)

---

## Surge Watch

Nothing noteworthy in signal trends today.
