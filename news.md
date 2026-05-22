# Inference Ecosystem — Flash News
**2026-05-22 | 346 papers scanned**

### [WarmServe: Enabling One-for-Many GPU Prewarming for Multi-LLM Serving](https://arxiv.org/abs/2512.09472)
Published at ICML 2026, WarmServe tackles the cold-start TTFT problem in multi-model serving clusters by proactively loading weights from multiple models onto the same GPU based on workload forecasts. The system uses CUDA VMM page-table tricks to switch between prewarmed models near-instantly, a KV cache reservation strategy to prewarm into idle cache space on still-active GPUs, and a placement algorithm that isolates high-priority models to avoid cross-eviction. Evaluation on Azure production traces shows up to 50.8x tail TTFT reduction vs. ServerlessLLM-GPU and 2.5x higher throughput vs. MuxServe. Built on vLLM, open-sourced.
Score: 93 (was 95)

### [Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants](https://arxiv.org/abs/2511.02043)
Published at MLSys 2026, Flashlight extends TorchInductor to auto-generate fused FlashAttention-style Triton kernels from plain PyTorch attention code — no templates, no special APIs. It introduces unified reduction IR, algebraic fusion (online softmax derivation via homomorphism), and tiling-aware dimension elimination to fuse entire matmul-softmax-matmul chains into a single kernel. Critically, it handles attention variants FlexAttention cannot: differential attention, Evoformer (5x+ speedup on gated self-attention), and Invariant Point Attention. Just pass `enable_flashlight=True` to `torch.compile`.
Score: 93 (was 92)

### [STAND: Accelerated Test-Time Scaling with Model-Free Speculative Sampling](https://arxiv.org/abs/2506.04708)
STAND exploits the massive n-gram redundancy in reasoning trajectories (97% bigram overlap across 16 trajectories) to build a model-free speculative decoder that needs no draft model. The key insight: stochastic drafting from stored logit distributions yields 5-8% higher acceptance rates than deterministic lookup. Combined with Gumbel-Top-K sampling and data-driven tree optimization, STAND cuts inference latency 60-65% on AIME/GPQA/LiveCodeBench while preserving accuracy. Works as a plug-and-play accelerator on any reasoning LLM — tested on DeepSeek-R1-Distill-Qwen 7B/14B.
Score: 92 (was 93)

### [CacheClip: Accelerating RAG with Effective KV Cache Reuse](https://arxiv.org/abs/2510.10129)
CacheClip solves the RAG TTFT bottleneck by precomputing per-chunk KV caches and selectively recomputing only the ~20% of tokens that matter for cross-chunk attention. The clever trick: a tiny auxiliary LLM (SmolLM2-135M) running on CPU identifies which tokens to recompute better than the primary model's own early layers — its last-layer attention has higher Jaccard overlap with the 14B model's deep layers. With shared-prefix calibration and sliding-window grouping, CacheClip retains 85-91% of full-attention quality while achieving 3.33x prefill speedup on Qwen2.5-14B.
Score: 88 (was 90)

### [EdgeRazor: Mixed-Precision Quantization-Aware Distillation for LLMs](https://arxiv.org/abs/2605.04062)
EdgeRazor pushes sub-2-bit LLM quantization to practical territory with three modules: super-group mixed-precision allocation (provably optimal discrepancy for training-time salience drift), adaptive feature distillation via structural similarity, and entropy-aware KL divergence that works with any data recipe. The 1.58-bit Qwen3-0.6B shrinks from 1.11GB to 0.19GB and decodes at 317 tok/s on Apple M4 Pro (15.16x over BF16), while the 1.88-bit variant beats all 2-bit and even 3-bit baselines across 14 tasks. Models and code released on GitHub and HuggingFace.
Score: 87 (was 85)

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569v1) is on a citation tear — jumped from 21 to 33 citations between May 17–18, a +57% spike in a single reporting window. Now at 33 citations with 3 influential. The SSM community is clearly building on this one fast.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) from the Kimi team saw a similar citation surge: 13 → 19 citations (and 3 → 4 influential) in the same May 17–18 window. Steady GitHub stars (~3.3k) and 185 HF upvotes provide the base, but the academic pickup is accelerating.

[Orthrus](https://arxiv.org/abs/2605.12825) exploded on GitHub — from 13 stars on May 16 to 348 today. A dual-view diffusion approach to parallel token generation clearly struck a nerve with practitioners. Worth watching if this translates into citations.

[MinT](https://arxiv.org/abs/2605.13779) (Mind Lab's managed LLM infrastructure paper) continues to hold one of the highest HF upvote counts in the tracker at 216, climbing steadily from 202 since May 16. Strong industry interest in production serving infrastructure.

[Mamba-3](https://arxiv.org/abs/2603.15569v1)'s citation velocity in particular suggests it's becoming a key reference for hybrid architecture work — 10 → 33 citations in the last month with most of that growth concentrated in the last week.
