# Inference Ecosystem — Flash News
**2026-03-03** | 247 new papers scanned

**RL-optimized speculative decoding beats Eagle3 by 36%.** Microsoft's [Learning to Draft](https://arxiv.org/abs/2603.01639v1) trains co-adaptive draft+verify policies via RL to directly maximize wall-clock throughput—not proxy metrics. Result: 2.24–4.32x speedup across 5 LLMs, establishing a new SOTA for adaptive speculative decoding. Score: 95

**MLRA fixes MLA's tensor parallelism blind spot.** DeepSeek's MLA can't shard its single latent head across TP ranks, forcing redundant KV cache loads. [MLRA](https://arxiv.org/abs/2603.02188v1) makes latent states partitionable, delivering 2.8x decoding speedup over MLA with matching perplexity. Pretrained weights on HuggingFace. Score: 94

**Quasar quantizes the verification bottleneck.** [Quasar](https://arxiv.org/abs/2603.01399v1) applies low-bit quantization to the verification phase of speculative decoding—the part everyone ignored. Halves memory traffic, 1.28x throughput on Qwen3, training-free, orthogonal to any draft strategy. Score: 90

**KVSlimmer derives closed-form KV cache compression.** [KVSlimmer](https://arxiv.org/abs/2603.00907v1) grounds asymmetric KV merging in spectral theory and produces a gradient-free, forward-pass-only compression algorithm. On Llama3.1-8B: 29% memory reduction, 28% latency reduction, better LongBench scores than prior methods. Score: 90

**TriMoE adds a third compute tier for MoE offloading.** [TriMoE](https://arxiv.org/abs/2603.01058v1) maps MoE experts to GPU/CPU/NDP by temperature (hot/warm/cold), using AMX-enabled CPUs for the warm experts that fall through the cracks. 2.83x over SOTA. Requires DIMM-NDP hardware, but the scheduling ideas are broadly applicable. Score: 88

---

## Hype Watch
[DynaMoE](http://arxiv.org/abs/2603.01697v1) just picked up its first HuggingFace upvote — early days, but worth flagging. The paper proposes dynamic token-level expert activation with layer-wise adaptive capacity for MoE models, tackling the perennial problem of compute waste in sparse architectures. With MoE deployments scaling up across the industry, anything that promises smarter routing at the token level has a natural audience. One upvote doesn't make a trend, but first traction on a 72-relevance paper about MoE efficiency is the kind of signal that sometimes precedes a wave of interest. Keep an eye on this one.
