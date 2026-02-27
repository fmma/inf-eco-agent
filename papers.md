# LLM inference systems and I/O

Automatically discovered papers scored for relevance to: Serving, optimizing, and scaling large language model inference. Includes KV cache management, speculative decoding, continuous batching, PagedAttention, model quantization for inference, inference frameworks (vLLM, TensorRT-LLM, SGLang, TGI, llama.cpp), inference throughput/latency optimization, distributed inference, inference hardware, and I/O optimization (disk I/O, network I/O, memory bandwidth, data loading, storage systems, NVMe, RDMA, interconnects) as it relates to LLM inference and serving.

**38** papers above threshold (70/100) out of **654** total scanned.

---

### DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference
**Relevance: 95/100 | Hype: 75/100** — DualPath directly addresses KV-Cache storage I/O bottleneck in agentic LLM inference with disaggregated architecture, dual-path loading via RDMA, 1.87x throughput improvement.
*Authors: Yongtong Wu, Shaoyuan Chen, Yinmin Zhong et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.21548v1) | [PDF](https://arxiv.org/pdf/2602.21548v1)

> The performance of multi-turn, agentic LLM inference is increasingly dominated by KV-Cache storage I/O rather than computation. In prevalent disaggregated architectures, loading the massive KV-Cache f...

---

### FLYING SERVING: On-the-Fly Parallelism Switching for Large Language Model Serving
**Relevance: 95/100 | Hype: 70/100** — Online DP-TP parallelism switching for LLM serving without worker restarts; vLLM-based system with zero-copy model weights, KV cache adaptation, and deadlock-free scheduling. Directly about LLM serving infrastructure.
*Authors: Shouwei Gao, Junqi Yin, Feiyi Wang et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22593v1) | [PDF](https://arxiv.org/pdf/2602.22593v1)

> Production LLM serving must simultaneously deliver high throughput, low latency, and sufficient context capacity under non-stationary traffic and mixed request requirements. Data parallelism (DP) maxi...

---

### KnapSpec: Self-Speculative Decoding via Adaptive Layer Selection as a Knapsack Problem
**Relevance: 95/100 | Hype: 70/100** — Self-speculative decoding via adaptive layer selection formulated as knapsack problem; directly about LLM inference acceleration with up to 1.47x speedup on Qwen3 and Llama3.
*Authors: Seongjin Cha, Gyuwan Kim, Dongsu Han et al.*
*Published: 2026-02-23*
[arXiv](https://arxiv.org/abs/2602.20217v1) | [PDF](https://arxiv.org/pdf/2602.20217v1)

> Self-speculative decoding (SSD) accelerates LLM inference by skipping layers to create an efficient draft model, yet existing methods often rely on static heuristics that ignore the dynamic computatio...

---

### LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure
**Relevance: 95/100 | Hype: 65/100** — Unified simulator for heterogeneous and disaggregated LLM serving infrastructure with hardware-aware modeling of batching, routing, offloading, memory, and power; directly about LLM serving systems.
*Authors: Jaehong Cho, Hyunmin Choi, Guseul Heo et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.23036v1) | [PDF](https://arxiv.org/pdf/2602.23036v1)

> Large language model (LLM) serving infrastructures are undergoing a shift toward heterogeneity and disaggregation. Modern deployments increasingly integrate diverse accelerators and near-memory proces...

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

### S2O: Early Stopping for Sparse Attention via Online Permutation
**Relevance: 93/100 | Hype: 65/100** — Early stopping for sparse attention via online permutation achieving 7.51x attention speedup and 3.81x end-to-end speedup on 128K context Llama-3.1-8B; directly about LLM inference optimization for long contexts.
*Authors: Yu Zhang, Songwei Liu, Chenqian Yan et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22575v1) | [PDF](https://arxiv.org/pdf/2602.22575v1)

> Attention scales quadratically with sequence length, fundamentally limiting long-context inference. Existing block-granularity sparsification can reduce latency, but coarse blocks impose an intrinsic ...

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

### ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?
**Relevance: 92/100 | Hype: 70/100** — Benchmark for coding agents optimizing real-world LLM inference workloads from vLLM and SGLang; directly about LLM inference optimization with 54 tasks from actual serving framework PRs.
*Authors: Ayush Nangia, Shikhar Mishra, Aman Gokrani et al.*
*Published: 2026-02-23*
[arXiv](https://arxiv.org/abs/2602.19594v1) | [PDF](https://arxiv.org/pdf/2602.19594v1)

> We introduce ISO-Bench, a benchmark for coding agents to test their capabilities on real-world inference optimization tasks. These tasks were taken from vLLM and SGLang, two of the most popular LLM se...

---

### InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models
**Relevance: 92/100 | Hype: 60/100** — Hardware-aware KV cache quantization for LLM inference with inner-dimension grouping, up to 22% speedup over prior work and 88% over FP16; directly about LLM inference optimization.
*Authors: Sayed Mohammadreza Tayaranian Hosseini, Amir Ardakani, Warren J. Gross*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.23200v1) | [PDF](https://arxiv.org/pdf/2602.23200v1)

> Reducing the hardware footprint of large language models (LLMs) during decoding is critical for efficient long-sequence generation. A key bottleneck is the key-value (KV) cache, whose size scales with...

---

### SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning
**Relevance: 92/100 | Hype: 60/100** — Model-driven KV cache compression for long-horizon agentic reasoning, reducing peak token usage by 65%; leverages the LRM itself for cache management. Directly about LLM inference memory optimization.
*Authors: Sanjay Kariyappa, G. Edward Suh*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22603v1) | [PDF](https://arxiv.org/pdf/2602.22603v1)

> Long-running agentic tasks, such as deep research, require multi-hop reasoning over information distributed across multiple webpages and documents. In such tasks, the LLM context is dominated by token...

---

### Multi-Layer Scheduling for MoE-Based LLM Reasoning
**Relevance: 92/100 | Hype: 60/100** — Directly about multi-layer scheduling for MoE-based LLM serving/inference, addressing request-level, engine-level, and expert-level scheduling with vLLM comparisons, TTFT/TPOT latency optimization.
*Authors: Yifan Sun, Gholamreza Haffar, Minxian Xu et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.21626v1) | [PDF](https://arxiv.org/pdf/2602.21626v1)

> Large Language Models (LLMs) have achieved remarkable success across a wide range of tasks, but serving them efficiently at scale remains a critical challenge due to their substantial computational an...

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

### Accelerating Local LLMs on Resource-Constrained Edge Devices via Distributed Prompt Caching
**Relevance: 90/100 | Hype: 50/100** — Distributed prompt caching for LLM inference on edge devices, reducing TTFT by 93% and TTLT by 50%; directly about accelerating LLM inference on resource-constrained hardware.
*Authors: Hiroki Matsutani, Naoki Matsuda, Naoto Sugiura*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22812v1) | [PDF](https://arxiv.org/pdf/2602.22812v1)

> Since local LLM inference on resource-constrained edge devices imposes a severe performance bottleneck, this paper proposes distributed prompt caching to enhance inference performance by cooperatively...

---

### Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators
**Relevance: 88/100 | Hype: 75/100** — Efficient constrained decoding for LLM-based generative retrieval on TPUs/GPUs using sparse matrix operations; 948x speedup over CPU trie, first production-scale deployment at YouTube.
*Authors: Zhengyang Su, Isay Katsman, Yueqi Wang et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22647v1) | [PDF](https://arxiv.org/pdf/2602.22647v1)

> Generative retrieval has emerged as a powerful paradigm for LLM-based recommendation. However, industrial recommender systems often benefit from restricting the output space to a constrained subset of...

---

### A Replicate-and-Quantize Strategy for Plug-and-Play Load Balancing of Sparse Mixture-of-Experts LLMs
**Relevance: 85/100 | Hype: 60/100** — Directly addresses inference-time load balancing for Sparse MoE LLMs via replication and quantization; training-free framework achieving 1.4x imbalance reduction within original memory budget.
*Authors: Zijie Liu, Jie Peng, Jinhao Duan et al.*
*Published: 2026-02-23*
[arXiv](https://arxiv.org/abs/2602.19938v1) | [PDF](https://arxiv.org/pdf/2602.19938v1)

> Sparse Mixture-of-Experts (SMoE) architectures are increasingly used to scale large language models efficiently, delivering strong accuracy under fixed compute budgets. However, SMoE models often suff...

---

### Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference
**Relevance: 85/100 | Hype: 55/100** — ReMix introduces continuous mixing state for efficient diffusion LLM inference, achieving 2-8x speedup without quality loss; training-free method directly targeting DLLM inference efficiency.
*Authors: Yushi Ye, Feng Hong, Huangjie Zheng et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22868v1) | [PDF](https://arxiv.org/pdf/2602.22868v1)

> Diffusion Large Language Models (DLLMs) promise fast non-autoregressive inference but suffer a severe quality-speed trade-off in parallel decoding. This stems from the ''combinatorial contradiction'' ...

---

### pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training
**Relevance: 80/100 | Hype: 55/100** — Low-bit quantization-aware training for LLMs with 1-bit dominant branch and high-precision branch; directly enables efficient LLM inference via extreme quantization for edge deployment.
*Authors: Wenzheng Zhang, Bingzheng Liu, Yang Hu et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22592v1) | [PDF](https://arxiv.org/pdf/2602.22592v1)

> Quantization-Aware Training from scratch has emerged as a promising approach for building efficient large language models (LLMs) with extremely low-bit weights (sub 2-bit), which can offer substantial...

---

### DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs
**Relevance: 78/100 | Hype: 72/100** — DySCO is a training-free decoding algorithm that dynamically rescales attention weights during inference using retrieval heads, directly optimizing long-context inference quality.
*Authors: Xi Ye, Wuwei Zhang, Fangcong Yin et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.22175v1) | [PDF](https://arxiv.org/pdf/2602.22175v1)

> Understanding and reasoning over long contexts is a crucial capability for language models (LMs). Although recent models support increasingly long context windows, their accuracy often deteriorates as...

---

### Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?
**Relevance: 78/100 | Hype: 60/100** — Directly addresses why diffusion language models converge to autoregressive-like decoding and proposes NAP for genuinely parallel non-autoregressive generation; core inference paradigm research.
*Authors: Pengxiang Li, Dilxat Muhtar, Lu Yin et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.23225v1) | [PDF](https://arxiv.org/pdf/2602.23225v1)

> Diffusion Language Models (DLMs) are often advertised as enabling parallel token generation, yet practical fast DLMs frequently converge to left-to-right, autoregressive (AR)-like decoding dynamics. I...

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

### Confidence-Driven Multi-Scale Model Selection for Cost-Efficient Inference
**Relevance: 75/100 | Hype: 50/100** — Directly about cost-efficient LLM inference via confidence-driven dynamic model selection, routing between smaller and larger models to reduce compute costs.
*Authors: Bo-Wei Chen, Chung-Chi Chen, An-Zi Yen*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.22090v1) | [PDF](https://arxiv.org/pdf/2602.22090v1)

> Large Language Models (LLMs) have revolutionized inference across diverse natural language tasks, with larger models performing better but at higher computational costs. We propose a confidence-driven...

---

### Sustainable LLM Inference using Context-Aware Model Switching
**Relevance: 75/100 | Hype: 35/100** — Context-aware model switching for sustainable LLM inference, reducing energy by 67.5% with 93.6% quality; directly about LLM inference efficiency through dynamic model selection.
*Authors: Yuvarani, Akashdeep Singh, Zahra Fathanah et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.22261v1) | [PDF](https://arxiv.org/pdf/2602.22261v1)

> Large language models have become central to many AI applications, but their growing energy consumption raises serious sustainability concerns. A key limitation in current AI deployments is the relian...

---

### Interleaved Head Attention
**Relevance: 72/100 | Hype: 60/100** — Interleaved Head Attention proposes cross-head mixing in MHA to improve multi-step reasoning, directly modifying the attention mechanism used during inference with modest parameter overhead.
*Authors: Sai Surya Duvvuri, Chanakya Ekbote, Rachit Bansal et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21371v1) | [PDF](https://arxiv.org/pdf/2602.21371v1)

> Multi-Head Attention (MHA) is the core computational primitive underlying modern Large Language Models (LLMs). However, MHA suffers from a fundamental linear scaling limitation: $H$ attention heads pr...

---

### Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching
**Relevance: 72/100 | Hype: 55/100** — Test-time scaling with diffusion language models using step-level recombination and process reward models; achieves 1.8x latency reduction over diffusion models while improving accuracy. Directly about LLM inference efficiency.
*Authors: Roy Miles, Aysim Toker, Andreea-Maria Oncescu et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22871v1) | [PDF](https://arxiv.org/pdf/2602.22871v1)

> Reasoning with large language models often benefits from generating multiple chains-of-thought, but existing aggregation strategies are typically trajectory-level (e.g., selecting the best trace or vo...

---

### Sparsity Induction for Accurate Post-Training Pruning of Large Language Models
**Relevance: 72/100 | Hype: 50/100** — Post-training pruning/sparsity for LLMs to reduce computational and memory costs at inference time, directly relevant to inference efficiency.
*Authors: Minhao Jiang, Zhikai Li, Xuewen Liu et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.21652v1) | [PDF](https://arxiv.org/pdf/2602.21652v1)

> Large language models have demonstrated capabilities in text generation, while their increasing parameter scales present challenges in computational and memory efficiency. Post-training sparsity (PTS)...

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

### Pyramid MoA: A Probabilistic Framework for Cost-Optimized Anytime Inference
**Relevance: 72/100 | Hype: 45/100** — Hierarchical Mixture-of-Agents architecture with dynamic query routing for cost-optimized LLM inference; achieves 61% compute cost reduction while maintaining accuracy.
*Authors: Arindam Khaled*
*Published: 2026-02-23*
[arXiv](https://arxiv.org/abs/2602.19509v1) | [PDF](https://arxiv.org/pdf/2602.19509v1)

> Large Language Models (LLMs) face a persistent trade-off between inference cost and reasoning capability. While "Oracle" models (e.g., Llama-3-70B) achieve state-of-the-art accuracy, they are prohibit...

---

### Ruyi2 Technical Report
**Relevance: 72/100 | Hype: 40/100** — Adaptive early-exit LLM architecture with variable-depth computation and 3D parallel training; directly about efficient LLM inference via adaptive computation.
*Authors: Huan Song, Shuyu Tian, Junyi Hao et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22543v1) | [PDF](https://arxiv.org/pdf/2602.22543v1)

> Large Language Models (LLMs) face significant challenges regarding deployment costs and latency, necessitating adaptive computing strategies. Building upon the AI Flow framework, we introduce Ruyi2 as...

---

### CCCL: Node-Spanning GPU Collectives with CXL Memory Pooling
**Relevance: 70/100 | Hype: 55/100** — CXL shared memory pool for cross-node GPU collective communications; relevant to LLM infrastructure with interconnect optimization and LLM training speedup demonstrated.
*Authors: Dong Xu, Han Meng, Xinyu Chen et al.*
*Published: 2026-02-25*
[arXiv](https://arxiv.org/abs/2602.22457v1) | [PDF](https://arxiv.org/pdf/2602.22457v1)

> Large language models (LLMs) training or inference across multiple nodes introduces significant pressure on GPU memory and interconnect bandwidth. The Compute Express Link (CXL) shared memory pool off...

---
