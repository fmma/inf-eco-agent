# Inference Ecosystem — Flash News
**2026-05-27 | 396 papers scanned, 5 selected**

## [Qrita: High-performance Top-k and Top-p using Pivot-based Truncation and Selection](https://arxiv.org/abs/2602.01518)

Qrita replaces the sorting step in Top-k/Top-p sampling with a Gaussian sigma-truncation pre-filter and a quaternary pivot search, eliminating the memory overhead that plagues GPU-based sort-and-filter pipelines. It's already **the default sampler in vLLM's GPU path**. End-to-end serving throughput improves up to 1.41x on GPT-OSS-20B via vLLM, with the biggest wins on MoE models where the active-param-to-vocab ratio is low. Works on H100, RTX 4090, and AMD MI355X — and it's deterministic, unlike FlashInfer's rejection sampling. From Ion Stoica's group at Berkeley.
Score: 95 (was 95)

## [Stateful Inference for Low-Latency Multi-Agent Tool Calling](https://arxiv.org/abs/2605.26289)

Converts the O(n_t) per-turn prefill cost of agentic tool-calling into O(delta_t) by keeping a persistent KV cache across turns, using a radix prefix cache with metadata-only sequence aliasing, and adding prompt-lookup speculative decoding for structured JSON output. Benchmarked against vLLM and SGLang on Llama-3.1-8B: **2.1x faster per turn on a 6-turn workflow, 4.2x on median turn of a 35-turn coding workflow**, roughly halving wall time. The architecture nails the dominant agentic pattern — monotonically growing conversation prefixes — which existing prefix caching was never designed for.
Score: 93 (was 95)

## [HiSpec: Hierarchical Speculative Decoding for LLMs](https://arxiv.org/abs/2510.01336)

Tackles the verification bottleneck in speculative decoding (2-6.9x slower than drafting) by inserting an early-exit intermediate verifier at ~1/4 model depth. HiSpec reuses KV caches and hidden states across draft, intermediate verifier, and full model — no auxiliary model needed. On Llama3-8B with ShareGPT: **2.01x throughput vs. autoregressive**, beating LayerSkip, Lookahead, and SPRINTER while maintaining lossless output. Supports batched inference via paged attention, unlike prior hierarchical methods. Generalizes to post-training EE models (Qwen3, OPT).
Score: 92 (was 95)

## ["Give Me BF16 or Give Me Death"? Accuracy-Performance Trade-Offs in LLM Quantization](https://arxiv.org/abs/2411.02355)

The most comprehensive quantization study yet: 500K+ evaluations across the full Llama-3.1 family (8B–405B) and DeepSeek-R1-Distill models. Key findings: FP8 is **effectively lossless**, well-tuned INT8 loses only 1-3% (not 10%+ as previously claimed), and GPTQ-based INT4 **outperforms AWQ on real-world tasks** — challenging a widely held assumption. Deployment verdict via vLLM benchmarks: W4A16 wins for synchronous/latency-sensitive serving, W8A8 dominates async continuous batching. From Dan Alistarh's group (SparseGPT/GPTQ fame) at Neural Magic/Red Hat AI.
Score: 90 (was 92)

## [Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding](https://arxiv.org/abs/2605.26558)

An algorithm-hardware co-designed self-speculative decoding framework for edge: constructs a training-free draft model via unstructured value pruning + mantissa truncation of the original weights and KV cache, paired with MX-format or unary-coded exponent compression. Achieves **2.41x speedup over BF16** on reasoning LLMs (DeepSeek-R1-Llama-8B, Qwen3) and **1.81x more tokens under fixed memory vs. Eagle-3** on RTX 4090. Includes a lightweight encoder-decoder hardware module (2% area overhead) for format conversion on GPUs/NPUs. First self-speculative approach specifically co-designed for low-batch edge inference.
Score: 88 (was 95)

---

## Surge Watch

[Orthrus](https://arxiv.org/abs/2605.12825) is the runaway hit this cycle — its GitHub repo went from 13 stars to 260 overnight around 05-18, then climbed to 364 by 05-26. Memory-efficient parallel token generation via dual-view diffusion is clearly resonating with practitioners looking to speed up discrete diffusion LLMs.

Fresh KV cache quantization work is generating immediate buzz: [OScaR](https://arxiv.org/abs/2605.19660) landed 37 HF upvotes and 23 GitHub stars on day one, while [Mix-Quant](https://arxiv.org/abs/2605.20315) (quantized prefilling for agentic LLMs) pulled 23 upvotes and 21 stars out of the gate. The MoE efficiency crowd is equally active — [Post-Trained MoE Can Skip Half Experts](https://arxiv.org/abs/2605.18643) debuted at 29 HF upvotes and 22 stars via self-distillation.

[Mamba-3](https://arxiv.org/abs/2603.15569v1) quietly had a massive citation surge — jumping from 21 to 33 in the 05-18 batch alone (3 influential), now the most-cited SSM paper in our tracker. Academic adoption is outpacing community signals (still just 6 HF upvotes).

[ThinKV](https://arxiv.org/abs/2510.01290) doubled its citation count from 3 to 6 on 05-27, picking up its first influential citation — thought-adaptive KV cache compression for reasoning models is gaining traction as long-CoT workloads grow. [Four Over Six](https://arxiv.org/abs/2512.02010) (NVFP4 quantization) continues its steady climb: 13 → 19 citations with 4 influential, up from 2 two weeks ago.
