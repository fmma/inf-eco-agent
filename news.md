# Inference Ecosystem — Flash News
**2 April 2026 — 623 papers scanned**

### [MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation](https://arxiv.org/abs/2604.00235v1)

A training-free, model-agnostic decode acceleration that reuses prior attention computations instead of re-streaming the entire KV cache. MAC matches pre-RoPE queries in a short ring buffer, rectifies a small high-mass band near the match boundary, then merges via numerically stable log-domain fusion. On LLaMA with FlashInfer, it cuts KV accesses by up to 99%, delivers 14.3x attention-phase speedup (up to 46x at 256K), and achieves 2.6x end-to-end generation speedup at 128K context — all while matching full-attention quality on LongBench v2, RULER, and LongGenBench. Accepted at MLSys 2026; works with MQA/GQA and MoE models. This is the most exciting long-context decode result this week.
Score: 97 (was 95)

### [TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving](https://arxiv.org/abs/2604.00368v1)

Production data plane from the Mooncake ecosystem that replaces imperative path selection with declarative slice spraying across heterogeneous interconnects (RDMA, NVLink, MNNVL, Ascend UB). TENT decomposes elephant flows into 64KB slices and schedules each to the rail with the lowest estimated completion time via telemetry-driven feedback. On H800 HGX clusters with SGLang HiCache, it achieves 1.36x higher throughput and 26% lower P90 TTFT over Mooncake TE, with sub-50ms self-healing on link failures. Already deployed at multiple industrial sites processing 50M+ tokens/min. Open-sourced at github.com/kvcache-ai/Mooncake. If you run disaggregated serving at scale, this is your new transfer engine.
Score: 96 (was 95)

### [Scheduling LLM Inference with Uncertainty-Aware Output Length Predictions](https://arxiv.org/abs/2604.00499v1)

Instead of predicting a single output length for SJF scheduling, TIE fits a log-t distribution — theoretically justified by power-law tail decay from stochastic EOS sampling. A DeBERTa-v3 predictor estimates (mu, sigma), and a Tail Inflated Expectation score combines the censored expectation with CVaR at alpha=0.9 for risk-adaptive scheduling. Implemented on vLLM with async batched prediction. At 100 RPS on Llama-3-8B, TIE reduces per-token latency by 2.31x over the best baseline (LTR) and improves offline SDG throughput by 1.42x. Generalizes across 8 models including MoE architectures, 3 datasets, and both 8B and 70B scales. A principled fix for a problem every serving team hits.
Score: 93 (was 92)

### [ITQ3_S: High-Fidelity 3-bit LLM Inference via Interleaved Ternary Quantization with Rotation-Domain Smoothing](https://arxiv.org/abs/2603.27914v2)

Fuses FWHT rotation with IQ3_S ternary quantization into a single CUDA kernel — the 256-point inverse Walsh-Hadamard transform runs entirely in shared memory during dequantization with only 2.1% compute overhead. On RTX 5090 Blackwell, ITQ3_S closes 57% of the perplexity gap to FP16 versus baseline IQ3_S (6.52 vs 7.03 on WikiText-2 for LLaMA-3 8B) while fitting a 70B model in 27.3 GiB — single consumer GPU, no sharding. Prefill throughput exceeds 4-bit alternatives by 1.5x via optimized DP4A and Tensor Core scheduling. For anyone running models on consumer hardware, this pushes the practical floor of quantization quality.
Score: 88 (was 95)

---

## Surge Watch

[PackForcing](https://arxiv.org/abs/2603.25730v1) is this week's breakout: zero signals on Mar 28, now sitting at 46 HF upvotes and 152 GitHub stars five days later. Short-to-long video inference via packing is clearly resonating with practitioners.

[Vectorizing the Trie](https://arxiv.org/abs/2602.22647v1) was a sleeper — 4 HF upvotes for over a month, completely flat — then 204 GitHub stars appeared overnight. Practitioners discovered efficient constrained decoding on accelerators without the academic community noticing first. Worth watching whether upvotes follow.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) keeps compounding: 2,888 GitHub stars (+93 in 5 days) and HF upvotes ticked up to 171 (+9). Approaching the 3K star mark with no sign of plateauing. Still the highest-momentum paper in the tracker.

[SpecEyes](https://arxiv.org/abs/2603.23483v1) growth has tapered — only +2 HF upvotes and +6 stars over 5 days after the initial 19→57 surge. The discovery phase is winding down.
