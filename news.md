# Inference Ecosystem — Flash News
**2026-05-25 | 176 papers scanned**

### [AlignedServe: Orchestrating Prefix-aware Batching for High-throughput LLM Serving](https://arxiv.org/abs/2605.23389)
A SIGMOD 2026 paper that tackles a problem hiding in plain sight: tokens in the same decode batch have wildly different costs because their KV-cache lengths differ, creating iteration-level bubbles nobody else addresses. AlignedServe groups requests by prefix length using a quad-tree-based Density First Search, offloads KV-cache to CPU memory, and introduces a GPU-Prefetch-For-GPU architecture that shuttles cache via NVLink instead of PCIe. On H100s with real Azure/ShareGPT traces, it delivers **1.98x throughput** and **7.4x latency reduction** over vLLM, DistServe, and FastGen. The first work to seriously optimize within-iteration compute imbalance.
Score: 93 (was 95)

### [FastKernels: Benchmarking GPU Kernel Generation in Production](https://arxiv.org/abs/2605.23215)
Snowflake AI Research delivers a sobering reality check for the LLM-writes-CUDA hype. FastKernels is both a benchmark and a minimalistic inference framework covering 46 architectures across 8 categories (96.2% of HuggingFace Transformers), with interfaces matching vLLM/SGLang modules for direct deployment. The key finding: even the best kernel agent (OpenAI Codex) achieves only **0.94x aggregate speedup** against production baselines — gains evaporate once you compare against cuBLAS/FlashAttention3 instead of PyTorch eager. Includes the first multi-GPU communication kernel benchmarks. Essential reading for anyone building kernel agents.
Score: 92 (was 90)

### [ZipMoE: Lossless Compression for On-Device MoE Serving](https://arxiv.org/abs/2601.21198)
An ICML 2026 paper that cracks on-device MoE inference without lossy quantization. ZipMoE exploits the low-entropy exponent bits of BF16 parameters for lossless compression, then orchestrates CPU-parallel decompression overlapped with SSD I/O on unified-memory edge SoCs (Jetson AGX Orin). A cache-affinity scheduler with provable constant-factor approximation manages hierarchical cache pools across compression states. Results: **72.77% latency reduction** and **6.76x throughput** over MoE-Infinity and DeepSpeed on DeepSeekV2-Lite and Qwen1.5-MoE. Shifts MoE inference from I/O-bound to compute-centric on edge hardware.
Score: 91 (was 92)

### [PBS-Attn: Sparser Block-Sparse Attention via Token Permutation](https://arxiv.org/abs/2510.21270)
An ICML 2026 paper with an elegant insight: attention is permutation-invariant, so instead of passively selecting blocks from a chaotic attention matrix, actively restructure it. PBS-Attn sorts keys by global importance within segments to cluster "heavy hitter" tokens into contiguous blocks, using a segmented permutation strategy that preserves inter-segment causality. Custom permuted-FlashAttention Triton kernels achieve **up to 2.75x end-to-end prefilling speedup** on Llama-3.1-8B and Qwen-2.5-7B while closely matching full attention on LongBench, LongBenchv2, and RULER. Plug-and-play — works on top of any block selection method.
Score: 90 (was 88)

### [AMS: Adaptive Mass-Segmented KV Compression for Long-Context Reasoning](https://arxiv.org/abs/2605.23200)
Identifies "Region Wipe-out" — where global top-k KV eviction annihilates entire reasoning blocks under tight budgets, causing problem drifting and repetition collapse. AMS shifts from token-level competition to region-aware quota allocation: attention mass defines adaptive segments, each gets a guaranteed minimum quota, then any existing scorer (TOVA, TriAttention, KeyDiff, R-KV) selects locally. On DeepSeek-R1-Distill-Qwen-7B, AMS-Expected beats AdaKV-ExpE2 by **+16 points** on MATH500 at budget 256 and even surpasses uncompressed Full KV at budgets 512/1024. Compatible with vLLM paged-KV serving at the same memory footprint as gather-based methods.
Score: 88 (was 92)

---

## Surge Watch

[MinT](https://arxiv.org/abs/2605.13779) (Mind Lab) is the week's attention magnet — 202 HF upvotes on arrival (05-16), climbing to 216 by 05-22. A managed infrastructure system for training and serving millions of LLMs is clearly hitting a nerve with practitioners. GitHub stars growing from 32 to 37.

[FlashAttention-4](https://arxiv.org/abs/2603.05451v1) continues a quiet but steady citation climb — 10 → 13 → 14 over the past two weeks, including a +3 batch jump on 05-18. Still only 1 HF upvote, but the algorithm/kernel co-design paper is becoming a standard academic reference without any community fanfare.

[Prefill-as-a-Service](https://arxiv.org/abs/2604.15039v1) went from 0 to 5 citations in a month, picking up +2 in a single batch on 05-18. Cross-datacenter KV cache transfer is carving out a distinct research niche.

[DiffAdapt](https://arxiv.org/abs/2510.19669) nearly doubled its citations — 5 to 10 between 05-14 and 05-25, with a +4 batch jump on 05-18. Difficulty-adaptive reasoning for token-efficient inference is getting picked up fast.

Previous breakouts have cooled: [Orthrus](https://arxiv.org/abs/2605.12825) stabilized around 348 stars after its explosive +247 single-day surge, [Mamba-3](https://arxiv.org/abs/2603.15569v1) flat at 33 citations, and [Adaptive Block-Scaled Data Types](https://arxiv.org/abs/2603.28765v1) unchanged at 187 stars.
