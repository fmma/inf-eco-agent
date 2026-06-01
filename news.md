The permission system seems to be blocking my attempts. Let me proceed with the detailed abstracts available — they contain substantial technical detail for a solid bulletin.

# Inference Ecosystem — Flash News
**2026-06-01 | 326 papers scanned**

---

### [Speculative Pipeline Decoding: Higher-Accuracy and Zero-Bubble Speculation via Pipeline Parallelism](https://arxiv.org/abs/2605.30852)

SPD rethinks speculative decoding by partitioning the target LLM into *n* pipeline stages, processing *n* tokens in parallel with zero latency bubbles. Unlike standard draft-then-verify, the speculation module aggregates intermediate features across pipeline depths — bounding prediction difficulty and achieving higher acceptance rates than multi-token prediction baselines. Code is released. If your serving stack already uses pipeline parallelism, this is a near-free upgrade path.
**Score: 93 (was 92)**

### [Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection](https://arxiv.org/abs/2602.03216)

Tackles the quadratic attention wall at 128K context with a per-head token-level sparsification that compresses Q/K/V to a reduced set, then decompresses back — letting evicted tokens be reconsidered in later layers (unlike permanent eviction methods). Fully compatible with FlashAttention and composable with existing sparse kernels. 3.23x attention speedup at 128K with <1% accuracy drop. The interleaved selection/decompression design is the key differentiator here — it avoids the irreversible early-layer decisions that plague other approaches.
**Score: 92 (was 90)**

### [StiefAttention: KV Cache Low-Rank Approximation over the Stiefel Manifold](https://arxiv.org/abs/2601.21686)

Post-training KV cache compression that learns orthonormal projection bases by minimizing decoder-layer output reconstruction error — not a proxy SVD objective. Constructs per-layer error-rank profiles for budget-constrained rank allocation. On Llama3-8B at iso-compression, beats EigenAttention by 4.2 perplexity points (C4) and 8.9 points on 0-shot MMLU. The principled Stiefel manifold optimization makes this more robust than heuristic approaches, and the rank allocation mechanism is a practical tool for hitting specific HBM budgets.
**Score: 91 (was 92)**

### [GRKV: Global Regression for Training-Free KV Cache Compression](https://arxiv.org/abs/2605.31105)

Training-free KV cache merging via ridge regression that directly minimizes the gap between compressed-cache and full-cache attention outputs. Addresses a real problem: span-based retention methods concentrate merges on boundary tokens, causing over-merging. GRKV distributes evicted information across all retained tokens with regularization. Only merging method that actually improves overall performance on both LongBench and RULER — no training, minimal overhead. Drop-in upgrade for existing eviction pipelines.
**Score: 90 (was 92)**

### [Reducing the GPU Memory Bottleneck with Lossless Compression for ML](https://arxiv.org/abs/2605.30728)

Invariant Bit Packing (IBP) identifies and eliminates invariant bits across tensor groups, compressing PCIe transfers with GPU-optimized decompression using warp parallelism and async transfers. 24% faster LLM inference, 180% faster DLRM embedding lookup, 74% faster GNN training — all lossless, no accuracy tradeoff. Unlike lossy quantization, this is a pure systems win you can stack on top of existing optimizations. Easy-to-use APIs already integrated into LLM inference frameworks.
**Score: 88 (was 85)**

---

## Surge Watch

[Orthrus](https://arxiv.org/abs/2605.12825) is the standout this cycle — GitHub stars exploded from 13 to 393 in two weeks, with memory-efficient parallel token generation via dual-view diffusion clearly striking a chord as the dLLM inference design space heats up.

[Mamba-3](https://arxiv.org/abs/2603.15569) keeps accelerating: citations jumped another +10 to 43 on 05-30 (with influential now at 5), after the 21→33 leap reported last cycle. SSM-based architectures are being cited at a rate that suggests real design convergence.

[OScaR](https://arxiv.org/abs/2605.19660) (distinct from last cycle's OSCAR — confusingly similar names, different papers) went from 23 to 102 GitHub stars between 05-22 and 05-31. Extreme KV cache quantization via Occam's-razor-style simplification is finding quick adoption.

[Attention Residuals](https://arxiv.org/abs/2603.15031) is building deep academic impact — influential citations doubled from 4 to 8 between 05-22 and 05-30, total citations 19→25. Kimi's architectural contribution is increasingly being built upon, not just cited.

[Continuum](https://arxiv.org/abs/2511.02230) quietly picked up +5 citations (20→25) and its first new influential citation (3→4) between 05-22 and 05-29. KV cache TTL management for multi-turn agents is arriving just as agentic workloads dominate the serving conversation.
