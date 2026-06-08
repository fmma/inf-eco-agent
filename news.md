# Inference Ecosystem Flash News — 2026-06-08 (189 papers scanned)

**[Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://arxiv.org/abs/2606.07362)** (MLSys 2026)
First systematic dissection of vLLM startup latency across 22 models and v0.3–v0.11 releases. The six-step breakdown reveals startup is overwhelmingly CPU-bound — swapping an H100 for an L40S changes total time by just 3%, while a different CPU shifts it by 35%. A lightweight white-box predictor trained on per-step linear regressions hits 2.4s MSE on held-out models, directly actionable for serverless autoscalers like NVIDIA Dynamo. Open-sourced profiler and all datasets at github.com/upb-cn/vllm-startup-profiler.
Relevance: 88

**[PolarQuant: Polar Coordinate Key Cache Quantization](https://arxiv.org/abs/2502.00527)** (NeurIPS 2025)
Reframes the key-cache outlier problem through polar coordinates: RoPE-paired dimensions form stable circles whose radius and angle are both smooth — turning a hard channel-outlier quantization into a clean (r, t)-bit encoding. A custom Triton kernel replaces the QK dot product with a lookup table over the 2^(r+t) quantized states, delivering up to 3.18x decoding throughput at 32K context on Llama-3.1-8B with negligible quality loss. At 3-bit on Llama-3.1-8B, PolarQuant actually *improves* LongBench average over the BF16 baseline (+0.27).
Relevance: 85

**[OffQ: Taming Structured Outliers in W4A4KV4 Quantization by Offsetting](https://arxiv.org/abs/2606.07116)**
Exploits the finding that LLM activation outliers live in a 1-D subspace shared across layers and tokens. A "top-1 PCA" isolates that direction, a Hadamard rotation converts it into a per-group constant offset absorbed by the zero-point — no mixed precision, no non-uniform grids, all matrix multiplies stay in uniform INT4. On Llama-3-8B W4A4KV4, OffQ reaches 6.98 WikiText PPL (vs. 6.1 FP16) and 65.5% zero-shot average, beating SpinQuant, KurTail, and ResQ across Llama and Qwen 2.5 families up to 72B.
Relevance: 82

**[Sparsely Gated Tiny Linear Experts (sgatlin)](https://arxiv.org/abs/2606.07414)**
Pushes MoE granularity to the extreme: each "expert" is a single rank-1 linear neuron, <0.1% of feedforward params are active per token, and — counterintuitively — removing the activation function *helps*. In isoflop comparisons up to 6e18 FLOPs on SlimPajama, sgatlin beats MLP, SwiGLU, coarse MoE, and matches PEER. The linearity payoff extends to interpretability: gating weights form a semantic metric space where nearest-neighbor circuits share meaning, and causal patching confirms feedforward circuits encode factual associations.
Relevance: 80

**[MAGE: Sparse Attention for Block Diffusion LLMs](https://arxiv.org/abs/2602.14209)**
Block diffusion models (LLaDA 2.0, SDAR, Fast-dLLM v2) force all B tokens in a block to share one KV subset — existing sparse estimators like Quest lose up to 25% recall under this constraint. MAGE discovers that the all-[MASK] block at step 1 already reveals the per-block oracle (84%+ recall at k=512), a property induced by the block-diffusion training objective itself. One exact attention pass at step 1, reused across all remaining denoising steps, yields near-lossless accuracy and up to 6.82x end-to-end speedup at 128K context.
Relevance: 78

---

## Surge Watch

Two KV cache quantization papers are surging simultaneously. [OSCAR](https://arxiv.org/abs/2605.17757) (offline spectral covariance-aware rotation for 2-bit KV) exploded from 5 to 63 HF upvotes and 12 to 295 GitHub stars in 10 days — by far the biggest community spike this cycle. [OScaR](https://arxiv.org/abs/2605.19660) (Occam's Razor for extreme KV quant) saw GitHub quintuple from 23 to 119 in the same window. Two independent papers hitting this hard at once signals real demand for sub-4-bit KV compression.

[Draft-OPD](https://arxiv.org/abs/2605.29343) (on-policy distillation for speculative decoding drafts) went from zero to 32 HF upvotes and 31 GitHub stars in a week — fast early traction for a training-focused approach to improving draft model quality.

[Continuum](https://arxiv.org/abs/2511.02230) (KV cache TTL scheduling for multi-turn LLM agents) quietly climbed from 20 to 29 citations over three weeks, with influential citations doubling from 3 to 6. As agentic serving heats up, this is building the kind of steady academic pickup that precedes framework adoption.
