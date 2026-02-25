# LLM inference systems and I/O

Automatically discovered papers scored for relevance to: Serving, optimizing, and scaling large language model inference. Includes KV cache management, speculative decoding, continuous batching, PagedAttention, model quantization for inference, inference frameworks (vLLM, TensorRT-LLM, SGLang, TGI, llama.cpp), inference throughput/latency optimization, distributed inference, inference hardware, and I/O optimization (disk I/O, network I/O, memory bandwidth, data loading, storage systems, NVMe, RDMA, interconnects) as it relates to LLM inference and serving.

**14** papers above threshold (70/100) out of **200** total scanned.

---

### CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
**Relevance: 95/100 | Hype: 65/100** — Directly about KV cache management for long-context LLM inference with algorithm-system co-design. Proposes context-aware hierarchical KV cache pruning achieving 4.56x throughput improvement using only 1% of KV cache.
*Authors: Chao Fei, Guozhong Li, Chenxi Liu et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20732v1) | [PDF](https://arxiv.org/pdf/2602.20732v1)

> Long-context LLMs demand accurate inference at low latency, yet decoding becomes primarily constrained by KV cache as context grows. Prior pruning methods are largely context-agnostic: their token sel...

---

### CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
**Relevance: 95/100 | Hype: 65/100** — Directly about KV cache management for long-context LLM inference with algorithm-system co-design. Proposes context-aware hierarchical KV cache pruning achieving 4.56x throughput improvement using only 1% of KV cache.
*Authors: Chao Fei, Guozhong Li, Chenxi Liu et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20732v1) | [PDF](https://arxiv.org/pdf/2602.20732v1)

> Long-context LLMs demand accurate inference at low latency, yet decoding becomes primarily constrained by KV cache as context grows. Prior pruning methods are largely context-agnostic: their token sel...

---

### FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill
**Relevance: 94/100 | Hype: 55/100** — FPGA accelerator for long-context LLM prefill with dynamic sparse attention. Directly addresses prefill-stage inference bottleneck with hardware-aware design: fused pipeline, dual-tier KV cache, hybrid MPU. Achieves 2.5x TTFT speedup and 4.5x energy efficiency over GPU.
*Authors: Rakshith Jayanth, Viktor Prasanna*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20515v1) | [PDF](https://arxiv.org/pdf/2602.20515v1)

> In long-context large language model (LLM) inference, the prefill stage dominates computation due to self-attention over the complete input context. Sparse attention significantly reduces self-attenti...

---

### FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill
**Relevance: 94/100 | Hype: 55/100** — FPGA accelerator for long-context LLM prefill with dynamic sparse attention. Directly addresses prefill-stage inference bottleneck with hardware-aware design: fused pipeline, dual-tier KV cache, hybrid MPU. Achieves 2.5x TTFT speedup and 4.5x energy efficiency over GPU.
*Authors: Rakshith Jayanth, Viktor Prasanna*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20515v1) | [PDF](https://arxiv.org/pdf/2602.20515v1)

> In long-context large language model (LLM) inference, the prefill stage dominates computation due to self-attention over the complete input context. Sparse attention significantly reduces self-attenti...

---

### TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence
**Relevance: 93/100 | Hype: 55/100** — Directly about LLM inference hardware acceleration: hybrid ROM-SRAM accelerator co-designed with ternary quantization for edge LLM inference, achieving 3,306 TPS with BitNet-2B. Addresses memory wall with extreme density and QLoRA tunability.
*Authors: Hongyi Guan, Yijia Zhang, Wenqiang Wang et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20662v1) | [PDF](https://arxiv.org/pdf/2602.20662v1)

> The deployment of Large Language Models (LLMs) for real-time intelligence on edge devices is rapidly growing. However, conventional hardware architectures face a fundamental memory wall challenge, whe...

---

### TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence
**Relevance: 93/100 | Hype: 55/100** — Directly about LLM inference hardware acceleration: hybrid ROM-SRAM accelerator co-designed with ternary quantization for edge LLM inference, achieving 3,306 TPS with BitNet-2B. Addresses memory wall with extreme density and QLoRA tunability.
*Authors: Hongyi Guan, Yijia Zhang, Wenqiang Wang et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20662v1) | [PDF](https://arxiv.org/pdf/2602.20662v1)

> The deployment of Large Language Models (LLMs) for real-time intelligence on edge devices is rapidly growing. However, conventional hardware architectures face a fundamental memory wall challenge, whe...

---

### Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
**Relevance: 92/100 | Hype: 55/100** — Directly about tensor parallelism for SSM-based LLM inference across multiple GPUs, with KV cache equivalent (SSM state cache), quantized AllReduce, and throughput/latency benchmarks.
*Authors: Anurag Dutt, Nimit Shah, Hazem Masarani et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21144v1) | [PDF](https://arxiv.org/pdf/2602.21144v1)

> Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often ...

---

### Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
**Relevance: 92/100 | Hype: 55/100** — Directly about tensor parallelism for SSM-based LLM inference across multiple GPUs, with KV cache equivalent (SSM state cache), quantized AllReduce, and throughput/latency benchmarks.
*Authors: Anurag Dutt, Nimit Shah, Hazem Masarani et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21144v1) | [PDF](https://arxiv.org/pdf/2602.21144v1)

> Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often ...

---

### ReviveMoE: Fast Recovery for Hardware Failures in Large-Scale MoE LLM Inference Deployments
**Relevance: 90/100 | Hype: 60/100** — Directly about fast failure recovery in large-scale MoE LLM inference deployments without restarting serving instances, deployed on Huawei Cloud's MaaS platform with disaggregated MoE/attention architectures.
*Authors: Haley Li, Xinglu Wang, Cong Feng et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21140v1) | [PDF](https://arxiv.org/pdf/2602.21140v1)

> As LLM deployments scale over more hardware, the probability of a single failure in a system increases significantly, and cloud operators must consider robust countermeasures to handle these inevitabl...

---

### ReviveMoE: Fast Recovery for Hardware Failures in Large-Scale MoE LLM Inference Deployments
**Relevance: 90/100 | Hype: 60/100** — Directly about fast failure recovery in large-scale MoE LLM inference deployments without restarting serving instances, deployed on Huawei Cloud's MaaS platform with disaggregated MoE/attention architectures.
*Authors: Haley Li, Xinglu Wang, Cong Feng et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21140v1) | [PDF](https://arxiv.org/pdf/2602.21140v1)

> As LLM deployments scale over more hardware, the probability of a single failure in a system increases significantly, and cloud operators must consider robust countermeasures to handle these inevitabl...

---

### OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
**Relevance: 75/100 | Hype: 55/100** — Directly about security vulnerabilities in multi-tenant LLM serving: exploits shared KV caches for prompt leakage. Demonstrates practical attack on production LLM serving infrastructure with up to 12.48x efficiency improvement.
*Authors: Longxiang Wang, Xiang Zheng, Xuhao Zhang et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20595v1) | [PDF](https://arxiv.org/pdf/2602.20595v1)

> Multi-tenant LLM serving frameworks widely adopt shared Key-Value caches to enhance efficiency. However, this creates side-channel vulnerabilities enabling prompt leakage attacks. Prior studies identi...

---

### OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
**Relevance: 75/100 | Hype: 55/100** — Directly about security vulnerabilities in multi-tenant LLM serving: exploits shared KV caches for prompt leakage. Demonstrates practical attack on production LLM serving infrastructure with up to 12.48x efficiency improvement.
*Authors: Longxiang Wang, Xiang Zheng, Xuhao Zhang et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20595v1) | [PDF](https://arxiv.org/pdf/2602.20595v1)

> Multi-tenant LLM serving frameworks widely adopt shared Key-Value caches to enhance efficiency. However, this creates side-channel vulnerabilities enabling prompt leakage attacks. Prior studies identi...

---

### Lagom: Unleashing the Power of Communication and Computation Overlapping for Distributed LLM Training
**Relevance: 72/100 | Hype: 45/100** — Optimizes communication-computation overlap for distributed LLM training with a unified cost model. While focused on training, the communication optimization techniques (co-tuning communication parameters, priority-based search) directly apply to distributed inference as well.
*Authors: Guanbin Xu, ZhenGuo Xu, Yuzhe Li et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20656v1) | [PDF](https://arxiv.org/pdf/2602.20656v1)

> Overlapping communication with computation is crucial for distributed large-model training, yet optimizing it - especially when computation becomes the bottleneck-remains challenging. We present Lagom...

---

### Lagom: Unleashing the Power of Communication and Computation Overlapping for Distributed LLM Training
**Relevance: 72/100 | Hype: 45/100** — Optimizes communication-computation overlap for distributed LLM training with a unified cost model. While focused on training, the communication optimization techniques (co-tuning communication parameters, priority-based search) directly apply to distributed inference as well.
*Authors: Guanbin Xu, ZhenGuo Xu, Yuzhe Li et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20656v1) | [PDF](https://arxiv.org/pdf/2602.20656v1)

> Overlapping communication with computation is crucial for distributed large-model training, yet optimizing it - especially when computation becomes the bottleneck-remains challenging. We present Lagom...

---
