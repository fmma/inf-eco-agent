The PDF reader needs poppler-utils which isn't installed, and I can't install packages. I'll write the bulletin based on the detailed abstracts provided, which contain substantial technical specifics.

# Inference Ecosystem — Flash News
**2026-06-12 — 295 papers scanned**

## [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)

MiniMax ships a blockwise sparse attention mechanism (MSA) built on top of GQA that independently selects top-k KV blocks per group via a lightweight Index Branch, then runs exact block-sparse attention over only those blocks. The numbers are hard to argue with: 28.4x attention compute reduction at 1M context, translating to 14.2x prefill and 7.6x decoding wall-clock speedups on H800 — with co-designed kernels using exp-free top-k selection and KV-outer sparse attention for better tensor-core utilization. This isn't a research prototype: it powers MiniMax-M3 (109B parameters, natively multimodal) in production, and both the inference kernel and model are open-sourced. The most deployment-ready long-context solution we've seen this cycle.
Score: 96 (was 95)

## [Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning](https://arxiv.org/abs/2505.04021)

Prism introduces memory ballooning — borrowed from VM hypervisors — to dynamically reclaim KV cache memory across co-located LLMs on the same GPU. The key insight: production traces show "bursty-group" patterns where model sets activate together and shift over time, so neither pure space-sharing nor time-sharing works well alone. Prism's balloon driver (`kvcached`) unifies both under a single elastic memory scheme, adapting in real time. Already deployed across 10K+ GPUs in production and open-sourced. If you're running multi-model inference and fighting memory fragmentation, this is the system to study.
Score: 94 (was 95)

## [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/abs/2606.13126)

A beautifully minimal approach to position-independent caching in vLLM: store unrotated K vectors, apply RoPE per-request using logical positions, and expose three user-facing primitives (block-aligned padding, span separator, prompt depend) that unlock Block-Attention, EPIC, and Prompt Cache within a single running instance. Under 100 lines of core engine changes. On 2WikiMultihopQA with interleaved scheduling: 49% prefill throughput improvement, up to 100x reduction in cached-span TTFT, and only 5.7% worst-case overhead. For RAG and agentic workloads hammering the same documents repeatedly, this is close to a free lunch.
Score: 93 (was 92)

## [Spiffy: Diffusion LLM Speculative Decoding via Calibrated Draft Graphs](https://arxiv.org/abs/2509.18085)

As diffusion LLMs (LLaDA, Dream, SDAR) gain steam, their inference story needs work. Spiffy brings speculative decoding to dLLMs via auto-speculation — no separate draft model needed. It structures draft states as directed draft graphs calibrated offline for maximum acceptance rates, exploiting the bidirectional blockwise nature of dLLM generation. Combined with KV caching and threshold-based dynamic unmasking: up to 8.6x fewer model inferences and 6.3x token-rate speedup, all while provably preserving the output distribution. The first serious inference acceleration framework for the dLLM paradigm.
Score: 91 (was 92)

## [M*: A Modular Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688)

M* tackles the growing pain of serving composite multimodal architectures — vision encoders, language backbones, diffusion heads, audio codecs, action generators — that don't fit neatly into existing LLM serving frameworks. Models are represented as dataflow "Walk Graphs" enabling arbitrary component composition, flexible cluster placement, and model-agnostic optimizations. Results: 20% lower latency than vLLM-Omni on BAGEL text-to-image, 2.9x lower real-time factor for Qwen3-Omni TTS, and 12.5x faster robotic planning. From Stanford/UW (Leskovec, Zettlemoyer) — likely to set the direction for next-gen multimodal serving.
Score: 90 (was 93)

---

## Surge Watch

[Orthrus](https://arxiv.org/abs/2605.12825) (dual-view diffusion for memory-efficient parallel token generation) quietly exploded — 13 to 412 GitHub stars in 3 weeks (May 16–Jun 8), with the initial spike hitting 260 stars in just 2 days. The dLLM inference space is now producing repos with real practitioner traction.

[Mamba-3](https://arxiv.org/abs/2603.15569) is building sustained academic gravity — citations more than doubled from 21 to 49 (May 14–Jun 12) with 5 influential. The hybrid Mamba-Transformer design pattern is becoming a validated research direction, not just a curiosity.

[OScaR](https://arxiv.org/abs/2605.19660) (Occam's Razor for extreme KV cache quantization — distinct from the spectral-rotation OSCAR we covered before) went from 23 to 119 GitHub stars in 11 days (May 22–Jun 2). Two separate papers with near-identical names both breaking through in extreme KV quantization tells you everything about how crowded this niche has become.

Previously surging papers from last report — KVarN, Domino, OSCAR (2605.17757), Attention Sink survey — have all leveled off with no meaningful new signal changes in the last few days.
