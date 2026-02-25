# LLM inference systems and I/O

Automatically discovered papers scored for relevance to: Serving, optimizing, and scaling large language model inference. Includes KV cache management, speculative decoding, continuous batching, PagedAttention, model quantization for inference, inference frameworks (vLLM, TensorRT-LLM, SGLang, TGI, llama.cpp), inference throughput/latency optimization, distributed inference, inference hardware, and I/O optimization (disk I/O, network I/O, memory bandwidth, data loading, storage systems, NVMe, RDMA, interconnects) as it relates to LLM inference and serving.

**7** papers above threshold (70/100) out of **106** total scanned.

---

### FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill
**Score: 100/100** — Directly addresses LLM inference prefill acceleration with sparse attention on FPGA, targeting TTFT and energy efficiency.
*Authors: Rakshith Jayanth, Viktor Prasanna*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20515v1) | [PDF](https://arxiv.org/pdf/2602.20515v1)

> In long-context large language model (LLM) inference, the prefill stage dominates computation due to self-attention over the complete input context. Sparse attention significantly reduces self-attenti...

---

### Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
**Score: 90/100** — Presents tensor parallelism for SSM-based LLM inference with SSM state caching, quantized AllReduce, and multi-GPU throughput scaling.
*Authors: Anurag Dutt, Nimit Shah, Hazem Masarani*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21144v1) | [PDF](https://arxiv.org/pdf/2602.21144v1)

> Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often ...

---

### ReviveMoE: Fast Recovery for Hardware Failures in Large-Scale MoE LLM Inference Deployments
**Score: 90/100** — Directly targets failure recovery in production LLM inference serving (MaaS), avoiding costly model reload and recompilation during inference.
*Authors: Haley Li, Xinglu Wang, Cong Feng*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21140v1) | [PDF](https://arxiv.org/pdf/2602.21140v1)

> As LLM deployments scale over more hardware, the probability of a single failure in a system increases significantly, and cloud operators must consider robust countermeasures to handle these inevitabl...

---

### CHESS: Context-aware Hierarchical Efficient Semantic Selection for Long-Context LLM Inference
**Score: 90/100** — Algorithm-system co-design for KV cache management in long-context LLM inference, achieving 4.56x throughput improvement with 1% KV cache.
*Authors: Chao Fei, Guozhong Li, Chenxi Liu*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20732v1) | [PDF](https://arxiv.org/pdf/2602.20732v1)

> Long-context LLMs demand accurate inference at low latency, yet decoding becomes primarily constrained by KV cache as context grows. Prior pruning methods are largely context-agnostic: their token sel...

---

### TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence
**Score: 90/100** — Hardware accelerator co-designed with ternary quantization for edge LLM inference, addressing the memory wall with hybrid ROM-SRAM architecture.
*Authors: Hongyi Guan, Yijia Zhang, Wenqiang Wang*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20662v1) | [PDF](https://arxiv.org/pdf/2602.20662v1)

> The deployment of Large Language Models (LLMs) for real-time intelligence on edge devices is rapidly growing. However, conventional hardware architectures face a fundamental memory wall challenge, whe...

---

### Lagom: Unleashing the Power of Communication and Computation Overlapping for Distributed LLM Training
**Score: 72/100** — Lagom optimizes communication-computation overlap for distributed LLM training with 1.07-1.33x speedup; directly addresses communication/computation co-optimization relevant to distributed LLM systems and I/O.
*Authors: Guanbin Xu, ZhenGuo Xu, Yuzhe Li et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20656v1) | [PDF](https://arxiv.org/pdf/2602.20656v1)

> Overlapping communication with computation is crucial for distributed large-model training, yet optimizing it - especially when computation becomes the bottleneck-remains challenging. We present Lagom...

---

### OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
**Score: 70/100** — Exposes side-channel vulnerabilities in shared KV cache architectures used by multi-tenant LLM serving frameworks.
*Authors: Longxiang Wang, Xiang Zheng, Xuhao Zhang*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20595v1) | [PDF](https://arxiv.org/pdf/2602.20595v1)

> Multi-tenant LLM serving frameworks widely adopt shared Key-Value caches to enhance efficiency. However, this creates side-channel vulnerabilities enabling prompt leakage attacks. Prior studies identi...

---
