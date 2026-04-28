# Inference Ecosystem — Flash News

**2026-04-28** — 554 new papers scanned

### [Kwai Summary Attention: Compressing KV Cache with Learnable Summary Tokens](https://arxiv.org/abs/2604.24432)

KSA introduces learnable summary tokens at chunk boundaries to compress the KV cache to O(n/k), orthogonal to GQA and MLA — composing KSA+MLA yields a 0.22% cache ratio while Hybrid-KSA trained from scratch beats full attention on RULER-128K by +16.6 points. Open-sourced training scripts from Kwai's OneRec team, with sliding chunk attention to avoid boundary information loss. **Rescored: 88**

### [Characterizing Expert Activation Patterns for Scalable Mixture-of-Experts Inference](https://arxiv.org/abs/2604.23150)

Georgia Tech and Meta profile 100k+ expert activation traces across Llama 4 Maverick, DeepSeek V3, and Qwen3-MoE, finding that workload-aware micro-batch grouping and expert placement can reduce all-to-all communication by up to 20%. Prefill-decode activation correlation is 0.82 for Maverick, and request type can be classified from expert activations with >94% accuracy — actionable data for multi-node MoE serving. **Rescored: 85**

### [HyLo: Long-Context Aware Upcycling for Hybrid LLM Scaling](https://arxiv.org/abs/2604.24715)

AMD's HyLo converts pretrained Transformers (Llama, Qwen) into MLA+Mamba2/GDN hybrids via distillation-based upcycling, cutting KV-cache memory by 90%+ and enabling 2M-token prefill/decoding in their vLLM integration on 8 MI300X GPUs. At 1B-3B scale, HyLo-Qwen-1.7B trained on only 10B tokens outperforms JetNemotron (400B tokens) on GSM8K and RULER-64K — a practical recipe for long-context serving without training from scratch. **Rescored: 85**

### [Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/abs/2604.23466)

First independent cross-architecture evaluation of NVIDIA's CuTile: on datacenter Blackwell (B200), a 60-line Python fused attention kernel hits 1,007 TFLOP/s — 2.5x faster than FlashAttention-2 — but the same kernel achieves only 53% of FA2 on workstation Blackwell (RTX PRO 6000), exposing a 5.6x cross-GPU gap from compiler immaturity. Triton remains the safer bet for mixed fleets at 62-101% of cuBLAS with no architecture-specific tuning. **Rescored: 80**

### [DepthKV: Leveraging Layer Sensitivity for Adaptive KV Cache Pruning](https://arxiv.org/abs/2604.24647)

DepthKV uses a permutation-test framework (p<0.05) to quantify per-layer sensitivity to KV cache pruning and allocates budget via an InfoNCE-guided metric (MGA). At a 60% global pruning ratio, layer-dependent allocation consistently outperforms uniform pruning across Gemma-7B, LLaMA-3.1-8B, and Qwen2.5-7B on summarization, QA, and reasoning tasks. **Rescored: 78**

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569) is quietly building academic momentum. After plateauing at 12 citations for two weeks, it jumped to 16 in the last 7 days — a 33% week-over-week increase. Still only 6 HF upvotes, so this is purely researcher-driven: the SSM community is actively building on the improved state space model architecture.

[Understanding the Physics of Key-Value Cache Compression](https://arxiv.org/abs/2603.01426) is another sleeper waking up. After nearly two months of absolute zero across all signals, it picked up 3 citations (1 influential) starting mid-April. A theoretical KV cache paper attracting influential citations suggests it's being used as foundational reference in new compression work.

[IceCache](https://arxiv.org/abs/2604.10539) saw its first real developer interest: 3→15 GitHub stars in 6 days. Small numbers, but a 5x jump on a memory-efficient KV cache paper published just two weeks ago — worth tracking whether this is the start of adoption or a one-off spike.

Previous hot signals are all stabilizing as expected. TriAttention, Block Diffusion Draft Trees, and Mixture-of-Depths Attention are adding single-digit stars per week — the initial surges are over.
