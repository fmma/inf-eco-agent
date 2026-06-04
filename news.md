# Inference Ecosystem — Flash News
**2026-06-04 | 761 papers scanned, 5 featured**

## [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.04511)

NVIDIA and Song Han's group introduce a fourth per-layer projection — the Forecast — that predicts which KV blocks the *next* layer needs, decoupling sparse selection from attention and enabling asynchronous CPU-to-GPU prefetch via a persistent UVA Triton kernel. On MiniCPM4.1-8B and NOSA-8B at 128K context, SparDA delivers 1.25x prefill speedup, 1.7x decode speedup over sparse-offload baselines, and up to 5.3x higher decode throughput by unlocking larger feasible batch sizes on a single GPU. Only 0.41% extra parameters; code at NVlabs/SparDA. This reframes sparsity from a compute trick into an offloading-friendly memory-access schedule — the direction long-context serving needs.
**Score: 96 (was 95)**

## [KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks](https://arxiv.org/abs/2606.03458)

Huawei identifies that KV-cache quantization errors accumulate across autoregressive timesteps because of incorrect per-token scaling — the top 5% of outlier errors cause more end-to-end KL divergence than the other 95%. KVarN applies Hadamard rotation plus a calibration-free Sinkhorn dual-scaling variance normalization, crushing token-magnitude errors at 2-bit precision. New SOTA on MATH500, AIME24, and HumanEval across Qwen3-4B, Llama-3.1-8B, and Phi-4-14B, with only 0.18% measured quantization overhead in vLLM. If you're running reasoning models with long chain-of-thought, this is the 2-bit KV method to beat.
**Score: 94 (was 95)**

## [SSSD: Simply-Scalable Speculative Decoding](https://arxiv.org/abs/2411.05894)

Huawei's training-free speculative decoding combines a CPU-side suffix-array datastore with prompt/self-output n-gram matching and a roofline-derived hardware-aware speculation length rule (sq = I_knee / batch_size). Up to 2.9x latency reduction on Llama-3.3-70B coding tasks, matching or beating EAGLE-3 on math and German-language benchmarks while requiring zero data prep, training, or tuning. Cold-start from an empty datastore still gives 1.1-1.23x speedup; after 1K conversations it hits 1.6-1.8x for non-English languages. The deployability story — just point it at your serving stack — is the real differentiator over trained drafters.
**Score: 93 (was 95)**

## [FlashMLA-ETAP: Efficient Transpose Attention Pipeline for Accelerating MLA Inference on NVIDIA H20 GPUs](https://arxiv.org/abs/2506.01969)

A clever dimension-swap trick for DeepSeek-R1 671B on memory-constrained H20 GPUs: ETAP transposes attention computation so the KV context length aligns with the M-dimension in WGMMA ops, eliminating the 75%+ redundant padding that plagued FlashMLA when 128 heads are split across 8 GPUs. Result: 2.78x over FlashMLA at 64K (batch 16), 5.24x over FlashAttention-3, with 15.2x lower RMSE. Directly addresses the "how do I actually run R1-671B on my H20 box" question many teams face right now.
**Score: 88 (was 95)**

## [Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding](https://arxiv.org/abs/2606.01019)

Tackles the runtime decision problem in speculative decoding: should you verify a cache-based draft or fall back to a model-based drafter like EAGLE3? A lightweight MLP predicts the accepted length of each cache draft *before* verification, routing high-payoff drafts to cache verification and low-payoff ones to EAGLE3. Across 3 LLMs and 16 datasets, it averages 2.73x speedup on agentic workloads — beating EAGLE3 in every agentic setting tested. The insight that high-payoff cache drafts concentrate in <9% of decoding states, and a small predictor can find them, points toward runtime draft selection as the next frontier for spec decode.
**Score: 88 (was 93)**

---

## Surge Watch

[Continuum](https://arxiv.org/abs/2511.02230) (KV Cache TTL for multi-turn agents) is this cycle's standout — flat at 20 citations through 05-22, then surged to 29 by 06-04 with influential citations doubling from 3 to 6. Multi-turn agent scheduling is clearly becoming a reference problem, and this paper is consolidating as the canonical formulation.

[Mamba-3](https://arxiv.org/abs/2603.15569) continues its relentless climb: 46 citations (5 influential), up from 33 just two weeks ago. For a state space model paper, that pace of academic uptake signals SSM-transformer hybrids are no longer niche — they're entering the production conversation.

[TokenCake](https://arxiv.org/abs/2510.18586) (KV-Cache-centric multi-agent serving) quietly doubled from 5 to 9 citations in two weeks — the multi-agent serving stack is drawing sustained implementation interest beyond Continuum.

Previous cycle's breakouts are settling into plateau: OSCAR, Gated DeltaNet-2, and Orthrus all returned empty signal data on 06-04, consistent with the discovery-to-evaluation transition noted last time. The initial attention spikes have passed; now it's about who ships integrations.
