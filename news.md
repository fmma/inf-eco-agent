# Inference Ecosystem — Flash News

**2026-04-30 | 467 papers scanned**

## [SPIN: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/abs/2604.26837v1)

Microsoft Research delivers a sparse-attention-aware serving framework built on vLLM that co-designs execution pipelines with GPU-CPU hierarchical KV storage. SPIN introduces a unified "partition" abstraction mapping different sparsity granularities (blocks, clusters, tokens) onto a shared page-based substrate, a locality-aware bucketed LRU cache manager that dynamically sizes per-request HBM budgets, and OS-style two-level metadata indexing that cuts metadata HBM consumption by 49-78x. Evaluated on Qwen3-8B/14B and Llama-3.1-70B across A100 and B200 GPUs with three integrated sparse attention algorithms (ShadowKV, RetroInfer, SeerAttention-R), SPIN delivers 1.66-5.66x higher end-to-end throughput and 7-9x lower TTFT than vLLM. This is the framework that makes sparse attention actually work at the systems level.
Score: 95 (was 95)

## [DAK: Direct-Access-Enabled GPU Memory Offloading with Optimal Efficiency for LLM Inference](https://arxiv.org/abs/2604.26074v1)

DAK repurposes NVIDIA's Tensor Memory Accelerator (TMA) — originally designed for HBM-to-SMEM transfers — to stream weights and KV caches directly from remote host memory into GPU shared memory, completely bypassing HBM staging. This is the first system to use TMA for cross-interconnect data movement. A greedy algorithm with provable optimality determines per-operation offloading ratios for compute-bound vs. memory-bound kernels, while active congestion control and TMA multicast eliminate interconnect saturation and read amplification. On GH200 (NVLink-C2C), DAK achieves up to 3x throughput over FlexGen and vLLM prefetch baselines; on RTX 6000 Blackwell (PCIe Gen5), up to 1.8x. Open-sourced and ready for integration.
Score: 94 (was 95)

## [RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts](https://arxiv.org/abs/2604.26039v1)

Every production MoE system — vLLM, SGLang, Alpha-MoE, DeepGEMM, FlashInfer — dispatches kernels from batch size alone, ignoring the expert routing distribution that changes every forward step. RaMP shows this leaves 10-70% of kernel throughput unrealized. A four-parameter wave cost model fitted from just 10-24 minutes of one-time profiling per model selects the fastest configuration from the runtime expert histogram, achieving 0.93% mean regret vs. exhaustive search across 8 MoE architectures including 3 unseen. The cost model is kernel-agnostic: applied to Alpha-MoE's own C++ kernel with zero source changes, it delivers 1.14x. Paired with a co-designed CuTe DSL kernel exposing 134-268 polymorphic configs, RaMP delivers 1.30x end-to-end in vLLM over Triton FP8, 1.41x over DeepGEMM.
Score: 93 (was 95)

## [Efficient, VRAM-Constrained xLM Inference on Clients](https://arxiv.org/abs/2604.26334v1)

From NVIDIA (accepted MLSys 2026 Industry Track), pipelined sharding is a benchmark-profile-guided CPU-GPU hybrid scheduler for client inference. It shards models at the sub-layer level and selects from three schedule plans (GPU-only, static CPU-GPU split, dynamic pipelined split) per token tier, adapting to CPU thread count, PCIe bandwidth, and VRAM budget at runtime. On a high-end desktop with Qwen3-235B (77GB on disk) at just 2GB VRAM, it achieves 7.7 TPS for 1K context — interactive speed from a 39x memory reduction. Combined with VLMOpt for Cosmos-Reason1, VRAM demand drops 10x vs. vLLM. Average TTFT improvement: 2x (up to 6.7x); TPS: 3.7x (up to 30x). This is the missing piece for running large models alongside games on consumer GPUs.
Score: 88 (was 92)

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569) is quietly building serious academic weight: 14→17 citations in the last 3 days alone (12→17 over two weeks). With only 6 HF upvotes and no GitHub repo, this is pure researcher-to-researcher traction — the SSM community is actively building on top of it.

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619) had a sudden GitHub awakening after a month of flatline: stars jumped from ~162 (where they sat for weeks) to 258 in the last 10 days. Something — likely an integration or benchmark result — sparked renewed developer interest in conditional compute at the attention layer.

Everything else is quiet. Act While Thinking's citation burst from last week has stabilized at 3. TriAttention, Attention Residuals, and the speculative decoding papers continue their expected plateau trajectories.
