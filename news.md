# Inference Ecosystem — Flash News
**2026-02-25**

## Highlights

### CHESS: KV Cache Pruning That Actually Works
[CHESS](https://arxiv.org/abs/2602.20732v1) — Score: 95 | Hype: 65

The KV cache remains *the* bottleneck for long-context LLM inference, and CHESS attacks it with an algorithm-system co-design that's hard to ignore. Their context-aware hierarchical selection policy dynamically reconstructs a coherent context during decoding — using just **1% of the KV cache** while *surpassing* full-KV quality. The system-level trick: coarse-granularity selection eliminates expensive data movement, translating theoretical sparsity into real wall-clock gains of up to **4.56x throughput**. If you're running long-context workloads, this is the paper to read this week. Code available.

### FAST-Prefill: FPGAs Strike Back for Long-Context Prefill
[FAST-Prefill](https://arxiv.org/abs/2602.20515v1) — Score: 94 | Hype: 55

A bold bet on FPGA acceleration for the prefill stage — the compute-dominant phase in long-context inference. Dynamic sparse attention patterns make prefill memory-bound on GPUs, and this paper argues FPGAs are a better fit. The design features a fused pipeline with memory-aware execution, a liveness-driven dual-tier KV cache, and a hybrid MPU mixing DSPs with LUT-based bit-plane decomposition. Results on Llama and Qwen (4K–128K context): **2.5x TTFT speedup** and **4.5x energy efficiency** over an A5000 GPU. Niche but provocative — especially as long-context inference costs become untenable.

### TOM: ROM-Based Edge Inference for Ternary LLMs
[TOM](https://arxiv.org/abs/2602.20662v1) — Score: 93 | Hype: 55

An unconventional take on the memory wall: co-design ternary quantization with **read-only memory**. TOM synthesizes ternary weights as standard-cell logic in ROM, achieving extreme density while keeping QLoRA adapters in SRAM for on-device tunability. The sparsity-aware ROM eliminates area overhead from zero-valued bits, and dynamic power gating exploits ROM's logic nature. Result: **3,306 tokens/sec** with BitNet-2B on edge hardware. As ternary models like BitNet gain traction, this hardware-quantization co-design points toward a different future for edge LLM deployment.

### Tensor Parallelism for SSMs — Filling the Gap
[Scaling SSMs on Multiple GPUs](https://arxiv.org/abs/2602.21144v1) — Score: 92 | Hype: 55

Everyone's been asking how to scale Mamba/SSM inference beyond a single GPU, and this paper delivers the first serious answer. The challenge: SSM mixer blocks couple large projections with recurrent state updates whose efficiency depends on locality — you can't just naively apply Transformer TP patterns. Their solution introduces an SSM state cache (the SSM equivalent of a KV cache), partitions the mixer's packed parameter tensor to keep recurrent updates local, and adds quantized AllReduce to cut synchronization overhead. Throughput gains: **1.6–2.1x on 2 GPUs, 2.6–4.0x on 4 GPUs** for Mamba, with largest benefits at long context. Evaluated across Mamba, Falcon-Mamba, and Zamba on A6000/A100 clusters.

### ReviveMoE: No-Restart Failure Recovery for MoE Serving
[ReviveMoE](https://arxiv.org/abs/2602.21140v1) — Score: 90 | Hype: 60

From Huawei Cloud's production MaaS platform: when your MoE serving instance hits a hardware failure, reloading weights and recompiling graphs is devastating to SLAs. ReviveMoE recovers **without restarting** — supporting both collocated and disaggregated MoE/attention architectures. Built on Huawei's xDeepServe platform and XCCL communications library. The practical engineering here matters: at scale, hardware failures are *when*, not *if*, and recovery latency directly impacts revenue.

---

## Also Noteworthy

**OptiLeak** ([arxiv](https://arxiv.org/abs/2602.20595v1)) — Score: 75 | Hype: 55 — Exposes a real security vulnerability in multi-tenant LLM serving: shared KV caches enable prompt reconstruction attacks with **12.48x** efficiency improvement via RL-enhanced exploitation. If you're deploying shared KV cache optimizations (looking at you, vLLM prefix caching), the threat model just got more concrete.

**Lagom** ([arxiv](https://arxiv.org/abs/2602.20656v1)) — Score: 72 | Hype: 45 — Communication-computation overlap optimizer for distributed LLM workloads. Co-tunes communication parameters with a unified cost model, reducing optimization complexity from exponential to linear. **1.07–1.33x speedup** over NCCL across diverse parallelizations. The techniques apply to both training and inference clusters.

---

## Cross-Cutting Themes

**The memory wall is being attacked from every angle.** This batch shows three distinct strategies: algorithmic (CHESS pruning KV cache to 1%), architectural (TOM using ROM for ternary weights), and hardware (FAST-Prefill exploiting FPGA memory hierarchies). The inference community is converging on a consensus that memory bandwidth — not compute — is the binding constraint, and the solution space is broadening well beyond "just quantize harder."

**SSMs are graduating from research curiosity to systems challenge.** The tensor parallelism paper for Mamba/SSM models signals that these architectures are hitting real deployment scale. The SSM state cache concept mirrors the KV cache evolution in Transformers — expect more systems work in this space as hybrid architectures proliferate.

**Reliability joins the inference systems stack.** ReviveMoE and OptiLeak both highlight that inference at scale requires more than throughput optimization — fault tolerance and security are first-class concerns for production serving infrastructure.
