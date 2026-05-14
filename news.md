# Inference Ecosystem — Flash News

**2026-05-14** — 999 papers scanned · 8 read in full · 5 featured

---

### [ThinKV: Thought-Adaptive KV Cache Compression for Reasoning LLMs](https://arxiv.org/abs/2510.01290)

ICLR 2026 from Georgia Tech and NVIDIA. Decomposes chain-of-thought into thought types (retrieval, exploration, thinking) and assigns per-type precision — important reasoning tokens get full precision while filler gets aggressively quantized or evicted. Achieves <5% KV cache retention with 5.8x throughput gain by extending PagedAttention with a "Continuous Thinking" kernel. If you're serving reasoning models, this is the first production-grade approach to taming their exploding KV footprint. **Rescored: 95**

### [Continuum: Optimizing Multi-Turn Agent Serving with KV Cache TTL](https://arxiv.org/abs/2511.02230)

UC Berkeley (Ion Stoica, Joseph Gonzalez). Introduces a KV cache TTL mechanism that models both reload cost and per-turn queueing delay for multi-turn agent workloads — the kind where an agent calls tools 10+ times per task. Built on vLLM, delivers 8x improvement on SWE-Bench and BFCL traces. The agentic serving problem is heating up fast, and this is the first system to properly formalize the cache-or-evict tradeoff for multi-turn conversations. **Rescored: 93**

### [PARD-2: Dual-Mode Speculative Decoding with Confidence-Adaptive Optimization](https://arxiv.org/abs/2605.08632)

AMD's single drafter supports both target-dependent and target-independent speculative decoding, switching modes on the fly. Confidence-Adaptive Token (CAT) optimization prunes low-confidence draft tokens before verification. Hits 6.94x lossless speedup on Llama3.1-8B, surpassing EAGLE-3 by 1.9x. The dual-mode flexibility matters — you get EAGLE-class accuracy when the target model is available and Medusa-class independence when it's not. **Rescored: 92**

### [RDKV: Rate-Distortion Optimized KV Cache Compression](https://arxiv.org/abs/2605.08317)

ETH Zurich brings information-theoretic rigor to KV cache compression. Frames joint eviction and quantization as a reverse water-filling problem, allocating bits where attention mass concentrates. TriZone packed decode layout enables 4.5x decode speedup and 1.9x memory reduction at 128K context on A100. The cleanest theoretical foundation for KV compression yet — and unlike most theory papers, the speedups are real. **Rescored: 90**

### [TAPER: Per-Step Admission Control for Branch Parallelism in LLM Serving](https://arxiv.org/abs/2605.06914)

Stanford and NVIDIA formalize "branch externality" — the throughput tax that intra-request parallelism (best-of-N, tree search, tool fan-out) imposes on co-located requests. TAPER's per-step admission controller achieves 1.77x goodput over naive IRP and >95% SLO attainment on Qwen3-32B. As agentic workloads drive more branching patterns, this is the scheduling primitive serving systems have been missing. **Rescored: 88**

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569v1) is quietly becoming the most-cited paper in this tracker's recent batch — now at 21 citations with a second influential citation, up from 17 ten days ago. SSM architectures keep accumulating academic interest even without HuggingFace buzz.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) (Kimi team) saw a citation burst from 8 to 13 in the last ~10 days, the sharpest recent jump in this cohort. Stars and upvotes are flat at 3.2k/184 — this is purely researcher-driven adoption, not community hype.

[UniPrefill](https://arxiv.org/abs/2605.06221) from the FlashPrefill authors landed with 20 HF upvotes and 31 GitHub stars on its first day of tracking — the strongest day-one signal we've seen in weeks for a prefill optimization paper.

Meanwhile, the papers that dominated earlier cycles — [TriAttention](https://arxiv.org/abs/2604.04921v1) (713 stars), [MegaTrain](https://arxiv.org/abs/2604.05091v1) (566 stars), [DMax](https://arxiv.org/abs/2604.08302v1) (113 stars) — have all visibly plateaued. Growth curves flattened across the board over the past two weeks.
