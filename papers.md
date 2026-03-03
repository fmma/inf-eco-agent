# LLM inference systems and I/O

Automatically discovered papers scored for relevance to: Serving, optimizing, and scaling large language model inference. Includes KV cache management, speculative decoding, continuous batching, PagedAttention, model quantization for inference, inference frameworks (vLLM, TensorRT-LLM, SGLang, TGI, llama.cpp), inference throughput/latency optimization, distributed inference, inference hardware, and I/O optimization (disk I/O, network I/O, memory bandwidth, data loading, storage systems, NVMe, RDMA, interconnects) as it relates to LLM inference and serving.

**56** papers above threshold (70/100) out of **919** total scanned.

---

### Multi-Head Low-Rank Attention
**Relevance: 95/100 | Hype: 82/100** — Directly addresses KV cache loading bottleneck in LLM inference decoding, proposes a new attention mechanism (MLRA) enabling efficient tensor parallelism with 2.8x decoding speedup over MLA.
*Authors: Songtao Liu, Hongwu Peng, Zhiwei Zhang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.02188v1) | [PDF](https://arxiv.org/pdf/2603.02188v1)

MLRA decomposes MLA's single latent KV head into four independent low-rank branches that can be sharded across devices, solving MLA's tensor parallelism bottleneck during decoding. At 2.9B scale, MLRA-4 achieves state-of-the-art perplexity (13.672 vs 13.727 for MLA) and 58.84% zero-shot accuracy while delivering 1.05-1.26x speedup over GQA and 2.8x over MLA in long-context decoding latency on H100 GPUs. Published at ICLR 2026 with code and pretrained weights available.

> Long-context inference in large language models is bottlenecked by Key--Value (KV) cache loading during the decoding stage, where the sequential nature of generation requires repeatedly transferring t...

---

### Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning
**Relevance: 95/100 | Hype: 82/100** — Directly about speculative decoding optimization for LLM inference — proposes RL-trained co-adaptive policies to dynamically control draft depth and verification size, directly maximizing inference throughput.
*Authors: Jiebin Zhang, Zhenghan Yu, Liang Wang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01639v1) | [PDF](https://arxiv.org/pdf/2603.01639v1)

LTD (Learning to Draft) formulates speculative decoding as an RL environment with two co-adaptive MLP policies: a depth policy controlling draft tree expansion and a size policy selecting verification token count, both optimized via PPO with per-cycle throughput as reward. Built on Eagle3, it achieves 2.24x–4.32x speedups across five LLMs (Llama-3-8B, Vicuna-13B, DeepSeek-R1-Distill-8B, Qwen3-14B/32B), outperforming Eagle3 by up to 36.4% on Qwen3-32B with under 1.5% policy overhead.

> Speculative decoding accelerates large language model (LLM) inference by using a small draft model to generate candidate tokens for a larger target model to verify. The efficacy of this technique hing...

---

### LK Losses: Direct Acceptance Rate Optimization for Speculative Decoding
**Relevance: 95/100 | Hype: 75/100** — Directly proposes novel training losses (LK losses) for speculative decoding draft models that directly optimize acceptance rate instead of KL divergence, a core LLM inference acceleration technique.
*Authors: Alexander Samarin, Sergei Krutikov, Anton Shevtsov et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.23881v1) | [PDF](https://arxiv.org/pdf/2602.23881v1)

Proposes LK losses — a likelihood-based loss and a hybrid KL+TV loss with adaptive blending — for training speculative decoding draft models to directly maximize token acceptance rate instead of using KL divergence as a proxy. Experiments across four draft architectures (EAGLE-3, MEDUSA, MLP speculator, DeepSeek MTP) and six target models (8B–685B) show consistent gains of up to 8–10% in average acceptance length, with larger improvements for capacity-constrained drafters and stochastic sampling (T=1). The method is a drop-in replacement requiring no extra compute.

> Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to propose candidate tokens that are then verified in parallel by the target mod...

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

### Data Driven Optimization of GPU efficiency for Distributed LLM Adapter Serving
**Relevance: 92/100 | Hype: 55/100** — Directly addresses GPU efficiency optimization for distributed LLM adapter serving, with detailed analysis of KV cache, continuous batching, vLLM internals, and throughput/latency tradeoffs.
*Authors: Ferran Agullo, Joan Oliveras, Chen Wang et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.24044v1) | [PDF](https://arxiv.org/pdf/2602.24044v1)

Proposes a data-driven pipeline for optimizing GPU utilization in distributed LLM-adapter (LoRA) serving. The system combines a Digital Twin that emulates vLLM's continuous batching and KV-cache dynamics (achieving <5% throughput error at 90x speedup over real benchmarking), distilled ML models for throughput/starvation prediction, and a greedy placement algorithm that minimizes GPU count while avoiding memory errors. Evaluated on H100 GPUs with Llama-3.1-8B and Qwen-2.5-7B, the pipeline consistently finds optimal adapter packing points and outperforms baselines including dLoRA.

> Large Language Model (LLM) adapters enable low-cost model specialization, but introduce complex caching and scheduling challenges in distributed serving systems where hundreds of adapters must be host...

---

### Scaling State-Space Models on Multiple GPUs with Tensor Parallelism
**Relevance: 92/100 | Hype: 55/100** — Directly about tensor parallelism for SSM-based LLM inference across multiple GPUs, with KV cache equivalent (SSM state cache), quantized AllReduce, and throughput/latency benchmarks.
*Authors: Anurag Dutt, Nimit Shah, Hazem Masarani et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.21144v1) | [PDF](https://arxiv.org/pdf/2602.21144v1)

> Selective state space models (SSMs) have rapidly become a compelling backbone for large language models, especially for long-context workloads. Yet in deployment, their inference performance is often ...

---

### Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification
**Relevance: 92/100 | Hype: 52/100** — Directly targets LLM inference acceleration by applying W8A8 quantization to the verification phase of speculative decoding, reducing memory bandwidth by ~50% — core inference optimization.
*Authors: Guang Huang, Zeyi Wen*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01399v1) | [PDF](https://arxiv.org/pdf/2603.01399v1)

Quasar applies W8A8 quantization (via enhanced SmoothQuant) specifically to the verification stage of self-speculative decoding, halving memory traffic during the parallel forward pass. Evaluated on Qwen3-8B and OpenPangu-7B across MT-bench, HumanEval, GSM8K, Alpaca, and CNN/DM, it achieves up to 1.64x speedup on GSM8K and 1.28x overall end-to-end throughput improvement with negligible accuracy loss (<3.1% average delta). The approach is orthogonal to drafting strategies, making it a drop-in enhancement for any speculative decoding pipeline.

> Speculative Decoding (SD) has emerged as a premier technique for accelerating Large Language Model (LLM) inference by decoupling token generation into rapid drafting and parallel verification. While r...

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

### TriMoE: Augmenting GPU with AMX-Enabled CPU and DIMM-NDP for High-Throughput MoE Inference via Offloading
**Relevance: 88/100 | Hype: 52/100** — Directly addresses MoE inference optimization via a novel GPU-CPU-NDP offloading architecture with expert scheduling and data placement policies.
*Authors: Yudong Pan, Yintao He, Tianhua Han et al.*
*Published: 2026-03-01*
[arXiv](https://arxiv.org/abs/2603.01058v1) | [PDF](https://arxiv.org/pdf/2603.01058v1)

TriMoE introduces a three-way heterogeneous architecture (GPU + AMX-enabled CPU + DIMM-NDP) for single-GPU MoE inference, classifying experts as hot/warm/cold and mapping each to the compute domain where it runs most efficiently. It includes a bottleneck-aware greedy makespan scheduler and a prediction-driven dynamic relayout/rebalancing scheme using EMA-based load prediction. Evaluated on DeepSeek-V2, Qwen3-235B, and GLM-4.5-Air, TriMoE achieves 2.12–2.83x decode speedup and 2.09–2.78x end-to-end throughput improvement over state-of-the-art offloading baselines.

> To deploy large Mixture-of-Experts (MoE) models cost-effectively, offloading-based single-GPU heterogeneous inference is crucial. While GPU-CPU architectures that offload cold experts are constrained ...

---

### KVSlimmer: Theoretical Insights and Practical Optimizations for Asymmetric KV Merging
**Relevance: 88/100 | Hype: 52/100** — Directly addresses KV cache compression for LLM inference via a novel merging algorithm with theoretical grounding, reducing memory and latency during serving.
*Authors: Lianjun Liu, Hongli An, Weiqi Yan et al.*
*Published: 2026-03-01*
[arXiv](https://arxiv.org/abs/2603.00907v1) | [PDF](https://arxiv.org/pdf/2603.00907v1)

KVSlimmer introduces a theoretically grounded asymmetric KV cache merging framework. It explains Key/Value asymmetry via spectral energy analysis of projection weights, then derives an exact Hessian formulation with a closed-form, gradient-free solution using only forward-pass variables. On Llama3.1-8B-Instruct with LongBench, it improves average score by 0.92 over AsymKV while reducing memory by 29% and latency by 28%.

> The growing computational and memory demands of the Key-Value (KV) cache significantly limit the ability of Large Language Models (LLMs). While KV merging has emerged as a promising solution, existing...

---

### KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning
**Relevance: 88/100 | Hype: 52/100** — Directly addresses KV cache management and inference latency optimization (TTFT reduction) for LLM serving, with a novel static-dynamic memory construction, multi-hop KV recomputation, and layer-balanced loading pipeline — all core inference systems concerns. Built on vLLM. Docked slightly because the application domain is embodied planning rather than general LLM serving.
*Authors: Zebin Yang, Tong Xie, Baotong Lu et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.23592v1) | [PDF](https://arxiv.org/pdf/2602.23592v1)

KEEP is a KV-cache-centric memory management system that accelerates LLM inference for embodied planning agents. It introduces three techniques: (1) static-dynamic memory construction that groups memory segments by update frequency to minimize KV cache invalidation, (2) multi-hop memory recomputation that uses attention-based importance propagation to selectively recompute KV states for critical memory segments, and (3) layer-balanced memory loading that redistributes KV loading across transformer layers to eliminate pipeline bubbles. Evaluated on ALFRED and WAH-NL benchmarks using Qwen-2.5 models atop vLLM, KEEP achieves up to 2.68x TTFT speedup over full recomputation and 1.90x TTFT reduction over CacheBlend with negligible accuracy loss.

> Memory-augmented Large Language Models (LLMs) have demonstrated remarkable capability for complex and long-horizon embodied planning. By keeping track of past experiences and environmental states, mem...

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

### Divide and Conquer: Accelerating Diffusion-Based Large Language Models via Adaptive Parallel Decoding
**Relevance: 82/100 | Hype: 62/100** — Directly addresses inference acceleration for diffusion-based LLMs via a training-free parallel decoding method (DiCo), with detailed throughput measurements and latency reduction results.
*Authors: Xiangzhong Luo, Yilin An, Zhicheng Yu et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.23792v1) | [PDF](https://arxiv.org/pdf/2602.23792v1)

Proposes DiCo, a training-free adaptive parallel decoding approach for diffusion-based LLMs (dLLMs) like LLaDA and Dream. It uses a three-phase divide-and-conquer paradigm: identifying seed tokens and forming local clusters of conditionally independent masked tokens, performing adaptive parallel decoding within clusters, and finalizing with compound decoding using logit margins. Achieves 3.4-7.9x inference speedups over vanilla decoding on GSM8K, Math-500, MBPP, and HumanEval while often improving accuracy, evaluated on NVIDIA RTX 4090.

> Diffusion-based large language models (dLLMs) have shown promising performance across various reasoning tasks, establishing themselves as an alternative to autoregressive large language models (LLMs)....

---

### Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics
**Relevance: 82/100 | Hype: 55/100** — Directly analyzes KV cache compression for LLM inference, proposing structural metrics (GER, consensus) and identifying failure modes (erasure, rigidity) under compression — core inference optimization topic.
*Authors: Samhruth Ananthanarayanan, Ayan Sengupta, Tanmoy Chakraborty*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01426v1) | [PDF](https://arxiv.org/pdf/2603.01426v1)

Proposes a physics-inspired framework for understanding KV cache compression as a perturbation of token-level attention routing, rather than simple memory reduction. Introduces the Global Eviction Ratio (GER) metric and identifies two failure modes — representational erasure and representational rigidity — with a universal 'safety cliff' near 90% compression across LLaMA and Qwen architectures. Uses synthetic datasets to show that moderate compression preserves accuracy despite internal degradation, while extreme compression triggers phase-transition-like hallucination spikes correlated with GER.

> As context windows in LLMs scale to 100K+ tokens, the key-value (KV) cache becomes the dominant memory bottleneck, with recent methods claiming 80-90% savings and minimal benchmark degradation. We arg...

---

### SLA-Aware Distributed LLM Inference Across Device-RAN-Cloud
**Relevance: 82/100 | Hype: 55/100** — Empirical study of distributed LLM/VLM inference across device-edge-cloud tiers using vLLM on a 5G AI-RAN testbed, with detailed latency/SLA measurements for quantized model variants and MIG GPU isolation.
*Authors: Hariz Yet, Nguyen Thanh Tam, Mao V. Ngo et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.23722v1) | [PDF](https://arxiv.org/pdf/2602.23722v1)

Presents end-to-end measurements of SLA-aware VLM inference (Qwen2.5-VL 3B/7B) across on-device (Jetson Orin NX), RAN-edge (GH200 with MIG), and cloud (H100) tiers on a 5G SA testbed. Shows that quantized variants (AWQ, W4A16, W8A8) achieve sub-0.5s edge latency with 97-99% hit-rate, while on-device remains multi-second and cloud is unreliable under strict SLAs due to WAN tail latency. Demonstrates that MIG isolation preserves RAN baseband timing health under up to 20 concurrent inference clients.

> Embodied AI requires sub-second inference near the Radio Access Network (RAN), but deployments span heterogeneous tiers (on-device, RAN-edge, cloud) and must not disrupt real-time baseband processing....

---

### Whisper-MLA: Reducing GPU Memory Consumption of ASR Models based on MHA2MLA Conversion
**Relevance: 82/100 | Hype: 50/100** — Whisper-MLA reduces KV cache size by up to 87.5% for ASR inference by converting Multi-Head Attention to Multi-Head Latent Attention, directly about inference memory optimization.
*Authors: Sen Zhang, Jianguo Wei, Wenhuan Lu et al.*
*Published: 2026-02-28*
[arXiv](https://arxiv.org/abs/2603.00563v1) | [PDF](https://arxiv.org/pdf/2603.00563v1)

> The Transformer-based Whisper model has achieved state-of-the-art performance in Automatic Speech Recognition (ASR). However, its Multi-Head Attention (MHA) mechanism results in significant GPU memory...

---

### SageBwd: A Trainable Low-bit Attention
**Relevance: 80/100 | Hype: 70/100** — Low-bit INT8 attention for both training and inference acceleration, builds on SageAttention which is a key inference optimization technique.
*Authors: Jintao Zhang, Marco Chen, Haoxu Wang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.02170v1) | [PDF](https://arxiv.org/pdf/2603.02170v1)

> Low-bit attention, such as SageAttention, has emerged as an effective approach for accelerating model inference, but its applicability to training remains poorly understood. In prior work, we introduc...

---

### KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models
**Relevance: 80/100 | Hype: 55/100** — Speculative decoding acceleration for Vision-Language-Action models, uses Kalman Filter to rectify SD errors avoiding costly re-inference, achieves 27-37% acceleration.
*Authors: Zihao Zheng, Zhihao Mao, Maoliang Li et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01581v1) | [PDF](https://arxiv.org/pdf/2603.01581v1)

> Vision-Language-Action (VLA) models build a token-domain robot control paradigm, yet suffer from low speed. Speculative Decoding (SD) is an optimization strategy that can boost inference speed. Two ke...

---

### pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training
**Relevance: 80/100 | Hype: 55/100** — Low-bit quantization-aware training for LLMs with 1-bit dominant branch and high-precision branch; directly enables efficient LLM inference via extreme quantization for edge deployment.
*Authors: Wenzheng Zhang, Bingzheng Liu, Yang Hu et al.*
*Published: 2026-02-26*
[arXiv](https://arxiv.org/abs/2602.22592v1) | [PDF](https://arxiv.org/pdf/2602.22592v1)

> Quantization-Aware Training from scratch has emerged as a promising approach for building efficient large language models (LLMs) with extremely low-bit weights (sub 2-bit), which can offer substantial...

---

### Task-Centric Acceleration of Small-Language Models
**Relevance: 80/100 | Hype: 52/100** — Directly addresses LLM/SLM inference acceleration with two concrete methods: tokenizer augmentation (TASC-ft) reducing decoding steps, and n-gram speculative decoding (TASC-spec) achieving up to 3.15x speedup — both squarely in inference optimization territory.
*Authors: Dor Tsur, Sharon Adar, Ran Levy*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.24174v1) | [PDF](https://arxiv.org/pdf/2602.24174v1)

Proposes TASC, a two-pronged framework for accelerating small language model inference on task-specific workloads. TASC-ft enriches the tokenizer with high-frequency output n-grams during fine-tuning to reduce decoding steps (up to 2.1x speedup), while TASC-spec constructs a training-free n-gram draft model mixing corpus and prompt statistics for speculative decoding (up to 3.15x speedup). Evaluated on medical QA, multi-label classification, and slot-filling tasks using Qwen2.5 and Llama-3-8B models.

> Small language models (SLMs) have emerged as efficient alternatives to large language models for task-specific applications. However, they are often employed in high-volume, low-latency settings, wher...

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

### FreeAct: Freeing Activations for LLM Quantization
**Relevance: 78/100 | Hype: 55/100** — Quantization framework for LLMs addressing dynamic activation patterns across diffusion LLMs and multimodal LLMs, up to 5.3% improvement - directly about inference optimization through quantization.
*Authors: Xiaohao Liu, Xiaobo Xia, Manyi Zhang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01776v1) | [PDF](https://arxiv.org/pdf/2603.01776v1)

> Quantization is pivotal for mitigating the significant memory and computational overhead of Large Language Models (LLMs). While emerging transformation-based methods have successfully enhanced quantiz...

---

### 3BASiL: An Algorithmic Framework for Sparse plus Low-Rank Compression of LLMs
**Relevance: 78/100 | Hype: 55/100** — Sparse plus low-rank decomposition for LLM compression with 2:4 sparsity + rank 64 configuration, achieving 2.5x faster compression on A100 GPU - directly about model compression for inference.
*Authors: Mehdi Makni, Xiang Meng, Rahul Mazumder*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01376v1) | [PDF](https://arxiv.org/pdf/2603.01376v1)

> Sparse plus Low-Rank $(\mathbf{S} + \mathbf{LR})$ decomposition of Large Language Models (LLMs) has emerged as a promising direction in model compression, aiming to decompose pre-trained model weights...

---

### AdaPonderLM: Gated Pondering Language Models with Token-Wise Adaptive Depth
**Relevance: 78/100 | Hype: 50/100** — Token-wise adaptive depth for inference via learned early exiting with KV reuse mechanism, directly reduces inference compute by ~10% while maintaining perplexity.
*Authors: Shixiang Song, He Li, Zitong Wang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01914v1) | [PDF](https://arxiv.org/pdf/2603.01914v1)

> Test-time scaling via recurrent/iterative Transformers enables large language models to spend more computation at inference, but most pretrained recurrent LMs run a fixed number of iterations, wasting...

---

### PonderLM-3: Adaptive Token-Wise Pondering with Differentiable Masking
**Relevance: 75/100 | Hype: 55/100** — PonderLM-3 introduces token-wise adaptive computation at inference time, allocating compute per-token based on difficulty - directly optimizes inference FLOPs.
*Authors: He Li, Feichen Song, Boyi Zeng et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.02023v1) | [PDF](https://arxiv.org/pdf/2603.02023v1)

> Test-time scaling has shown that allocating more additional computation at inference can improve generation quality, motivating a natural follow-up question: where should this computation be spent? Bu...

---

### OptiLeak: Efficient Prompt Reconstruction via Reinforcement Learning in Multi-tenant LLM Services
**Relevance: 75/100 | Hype: 55/100** — Directly about security vulnerabilities in multi-tenant LLM serving: exploits shared KV caches for prompt leakage. Demonstrates practical attack on production LLM serving infrastructure with up to 12.48x efficiency improvement.
*Authors: Longxiang Wang, Xiang Zheng, Xuhao Zhang et al.*
*Published: 2026-02-24*
[arXiv](https://arxiv.org/abs/2602.20595v1) | [PDF](https://arxiv.org/pdf/2602.20595v1)

> Multi-tenant LLM serving frameworks widely adopt shared Key-Value caches to enhance efficiency. However, this creates side-channel vulnerabilities enabling prompt leakage attacks. Prior studies identi...

---

### HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC
**Relevance: 75/100 | Hype: 52/100** — Directly addresses LLM inference orchestration on mobile SoCs with heterogeneous accelerator scheduling, bandwidth-aware concurrency control, and latency optimization—core inference systems concerns—but scoped narrowly to on-device RAG pipeline orchestration rather than general LLM serving.
*Authors: Maoliang Li, Jiayu Chen, Zihao Zheng et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01661v1) | [PDF](https://arxiv.org/pdf/2603.01661v1)

HeRo is a heterogeneous-aware scheduling framework for agentic RAG workflows on mobile SoCs (Snapdragon 8 Gen 3/4). It uses profiling-based performance models capturing per-stage accelerator affinity, workload shape sensitivity, and DRAM bandwidth contention, combined with an online scheduler that performs shape-aware sub-stage partitioning, criticality-based CPU/GPU/NPU mapping, and bandwidth-aware concurrency control. Evaluated on Qwen3 and LLaMA3 model families across four RAG datasets, HeRo achieves up to 10.94x latency reduction over single-accelerator baselines and 1.5x over static multi-accelerator mapping.

> With the increasing computational capability of mobile devices, deploying agentic retrieval-augmented generation (RAG) locally on heterogeneous System-on-Chips (SoCs) has become a promising way to enh...

---

### Boosting Entropy with Bell Box Quantization
**Relevance: 75/100 | Hype: 50/100** — Quantization-aware pre-training method that improves low-bit model quality, directly reduces compute and memory overhead for inference on edge devices.
*Authors: Ningfeng Yang, Tor M. Aamodt*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01599v1) | [PDF](https://arxiv.org/pdf/2603.01599v1)

> Quantization-Aware Pre-Training (QAPT) is an effective technique to reduce the compute and memory overhead of Deep Neural Networks while improving their energy efficiency on edge devices. Existing QAP...

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

### KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models
**Relevance: 72/100 | Hype: 60/100** — Knowledge distillation framework using SGLang for teacher inference and FSDP2 for student training, bridges inference efficiency of SGLang with training - directly relevant to inference-efficient distillation.
*Authors: Songming Zhang, Xue Zhang, Tong Zhang et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01875v1) | [PDF](https://arxiv.org/pdf/2603.01875v1)

> Knowledge distillation (KD) is an essential technique to compress large language models (LLMs) into smaller ones. However, despite the distinct roles of the student model and the teacher model in KD, ...

---

### Towards Privacy-Preserving LLM Inference via Collaborative Obfuscation (Technical Report)
**Relevance: 72/100 | Hype: 60/100** — Privacy-preserving LLM inference via collaborative obfuscation, tested on DeepSeek-V3.1 671B parameters with equivalent efficiency to plaintext inference - directly about inference serving.
*Authors: Yu Lin, Qizhi Zhang, Wenqiang Ruan et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.01499v1) | [PDF](https://arxiv.org/pdf/2603.01499v1)

> The rapid development of large language models (LLMs) has driven the widespread adoption of cloud-based LLM inference services, while also bringing prominent privacy risks associated with the transmis...

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

### Beyond Microservices: Testing Web-Scale RCA Methods on GPU-Driven LLM Workloads
**Relevance: 72/100 | Hype: 50/100** — Evaluates root cause analysis methods on LLM inference deployments, directly tests on GPU-driven LLM inference workloads with controlled failure injections.
*Authors: Dominik Scheinert, Alexander Acker, Thorsten Wittkopp et al.*
*Published: 2026-03-02*
[arXiv](https://arxiv.org/abs/2603.02057v1) | [PDF](https://arxiv.org/pdf/2603.02057v1)

> Large language model (LLM) services have become an integral part of search, assistance, and decision-making applications. However, unlike traditional web or microservices, the hardware and software st...

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

### Learning Generation Orders for Masked Discrete Diffusion Models via Variational Inference
**Relevance: 70/100 | Hype: 45/100** — Variational inference for learning parallel generation orders in masked diffusion LLMs, achieving competitive accuracy with only 4 generation steps; directly relevant to parallel token generation efficiency.
*Authors: David Fox, Sam Bowyer, Song Liu et al.*
*Published: 2026-02-27*
[arXiv](https://arxiv.org/abs/2602.23968v1) | [PDF](https://arxiv.org/pdf/2602.23968v1)

> Masked discrete diffusion models (MDMs) are a promising new approach to generative modelling, offering the ability for parallel token generation and therefore greater efficiency than autoregressive co...

---
