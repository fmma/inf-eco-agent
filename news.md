# Inference Ecosystem — Flash News
**2026-02-25**

## Today's Highlights

A strong batch today with **four high-relevance papers** tackling different layers of the inference stack — from KV cache management and multi-GPU SSM parallelism to edge hardware and production MoE reliability.

---

### KV Cache Cracked: 1% is All You Need

**[CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference](https://arxiv.org/abs/2602.20732)** (Score: 95)

The standout paper of the day. CHESS proposes an algorithm-system co-design for KV cache pruning that dynamically reconstructs a coherent context window per decoding step. The headline number: **4.56x throughput improvement using only 1% of the KV cache** while *surpassing* full-KV quality. The key insight is that prior pruning methods are context-agnostic — they don't consider step-wise relevance or local semantics, leading to quality degradation. CHESS fixes this with hierarchical selection at coarse granularity, eliminating expensive data movement. If these numbers hold up in production workloads, this could meaningfully change how long-context serving is deployed.

---

### FPGA Takes on Long-Context Prefill

**[FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill](https://arxiv.org/abs/2602.20515)** (Score: 94)

An FPGA accelerator specifically targeting the prefill bottleneck with dynamic sparse attention. The design is thoughtful: a fused pipeline with memory-aware execution order for sparse index generation, a dual-tier KV cache exploiting the memory hierarchy, and a hybrid MPU combining DSPs with LUT-based bit-plane decomposition. Results on Llama and Qwen (4K–128K context): **2.5x TTFT speedup and 4.5x energy efficiency** over an A5000 GPU. FPGA inference remains niche, but as long-context workloads push GPU memory and power budgets, this kind of heterogeneous approach deserves attention — especially for latency-sensitive edge deployments.

---

### ROM Meets Ternary: Edge Inference Gets Dense

**[TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence](https://arxiv.org/abs/2602.20662)** (Score: 93)

A creative hardware-quantization co-design: store ternary LLM weights as synthesized standard-cell ROM logic, achieving extreme memory density without the area overhead of zero-valued bits. A hybrid ROM-SRAM architecture preserves QLoRA tunability. The result: **3,306 tokens/sec with BitNet-2B** on a custom accelerator. The sparsity-aware ROM and workload-aware power gating are clever engineering choices. As 1-bit/ternary models gain traction (BitNet, etc.), dedicated hardware like this could define the edge inference tier.

---

### Tensor Parallelism for SSMs Finally Gets Serious

**[Scaling State-Space Models on Multiple GPUs with Tensor Parallelism](https://arxiv.org/abs/2602.21144)** (Score: 92)

SSMs (Mamba, Falcon-Mamba, Zamba) are compelling for long-context workloads, but multi-GPU inference has been an open problem — the recurrent state update couples sequence-wise computation in ways that resist naive TP partitioning. This paper presents a communication-efficient TP design that keeps recurrent updates local while introducing an SSM state cache (the SSM equivalent of KV caching) and quantized AllReduce. Results on A6000/A100 clusters: **1.6–2.1x throughput on 2 GPUs, 2.6–4.0x on 4 GPUs**, with an extra 10–18% from quantized all-reduce. As hybrid SSM-Transformer architectures proliferate, this fills a critical gap.

---

### Production MoE Fault Recovery Without Restarts

**[ReviveMoE: Fast Recovery for Hardware Failures in Large-Scale MoE LLM Inference Deployments](https://arxiv.org/abs/2602.21140)** (Score: 90)

From Huawei Cloud's production MaaS platform. When you're running MoE models across hundreds of accelerators, hardware failures are *when*, not *if*. ReviveMoE recovers without restarting the serving instance — avoiding the costly weight reload and graph recompilation that kills SLAs. Supports both collocated and disaggregated MoE/attention architectures. Not glamorous, but this is the kind of production reliability engineering that separates real inference platforms from research demos.

---

### Shared KV Cache = Shared Secrets?

**[OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Serving](https://arxiv.org/abs/2602.20595)** (Score: 75)

A security wake-up call for multi-tenant serving. OptiLeak demonstrates that shared KV caches create exploitable side-channels for prompt leakage, achieving **up to 12.48x efficiency improvement** over prior attacks via RL-based fine-tuning that targets domain-specific "hard tokens." Tested across 3B–14B parameter models on medical and financial benchmarks. If you're running vLLM or similar with shared prefix caching in multi-tenant settings, this paper argues the privacy risk is worse than previously thought. Cache isolation may need to become a first-class serving concern.

---

## Cross-Cutting Themes

- **The memory wall dominates**: Three of the top papers (CHESS, FAST-Prefill, TOM) attack inference memory bottlenecks from different angles — algorithmic pruning, FPGA hardware, and ROM density. The message is clear: memory bandwidth and capacity remain *the* constraint for inference at scale.
- **Beyond Transformers**: SSM inference scaling and ternary/1-bit model hardware are maturing, signaling the inference stack is diversifying beyond vanilla Transformer assumptions.
- **Production reality**: ReviveMoE and OptiLeak both address concerns that only matter at deployment scale — fault tolerance and security in shared infrastructure. The inference ecosystem is growing up.

---

*Notably absent this batch: nothing on speculative decoding, continuous batching improvements, or the major inference frameworks (vLLM, SGLang, TensorRT-LLM). Most remaining papers focused on training methodology, agents, or domain applications.*
