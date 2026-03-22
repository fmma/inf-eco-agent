# Inference Ecosystem — Flash News
2026-03-22 | 548 papers scanned

## [SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding](https://arxiv.org/abs/2603.18567)

The biggest practical blocker for speculative decoding adoption is not the algorithm; it is the absence of high-quality draft models. SpecForge attacks this directly with a production-grade EAGLE-3 training framework that decouples target and draft model parallelism (SGLang for inference on the target, FSDP for training the draft), achieving up to 9.9x faster training on Qwen3-235B-A22B. The released SpecBundle draft models cover Llama-3/4, Qwen-3, GPT-OSS, and Kimi K2, delivering up to 4.48x end-to-end inference speedup on SGLang, with 1.3x gains over existing open-source drafts. A systematic study also finds that dense drafts consistently outperform MoE drafts and that data regeneration yields a 5.3% throughput lift across benchmarks. Score: 95 (was 93)

## [FlashSampling: Fast and Memory-Efficient Exact Sampling](https://arxiv.org/abs/2603.15854)

Fuses categorical sampling into the LM-head matmul via Gumbel-Max decomposition over vocabulary tiles, never materializing the [B,V] logits tensor in HBM. The method is mathematically exact (confirmed by chi-squared tests against PyTorch reference) and extends cleanly to top-k, tensor-parallel, and online settings through hierarchical Gumbel factorization. End-to-end vLLM integration on B200 shows up to 19% TPOT reduction on Qwen3-1.7B; gains are proportional to the LM-head's share of decode time, so smaller models benefit most. Already open-source with benchmarks across H100, H200, B200, and B300. Score: 93 (was 95)

## [Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective](https://arxiv.org/abs/2603.16104)

Helium reframes agentic LLM serving as query optimization: workflows become DAGs of LLM-as-operators, enabling proactive KV cache pre-warming, common subgraph elimination across agent calls, and cache-aware scheduling via a templated radix tree. On a 19-agent financial trading workflow (88 LLM operators), Helium achieves up to 39.5x speedup over naive vLLM and 1.56x over KVFlow, with scheduling overhead under 230 ms even at 16 parallel branches. The key insight: per-call optimizations leave massive cross-call reuse on the table, and a global query planner can recover it. Score: 90 (was 95)

## [EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models](https://arxiv.org/abs/2603.18489)

Diffusion LLMs (LLaDA, Dream) require full forward passes at every denoising step because bidirectional attention invalidates standard KV caching. EntropyCache uses a single O(V) scalar, the max entropy of newly decoded token distributions, as a constant-cost proxy for cache staleness, triggering full recomputation only when needed. Combined with recomputation of the k most recently decoded tokens to handle multi-step feature volatility, this achieves 15.2-26.4x speedup on standard benchmarks and up to 107x on BBH 3-shot (Dream), with decision overhead at 0.5% of inference time. As dLLMs gain traction, this is the caching method to watch. Score: 88 (was 92)

## [Multi-stage Flow Scheduling for LLM Serving](https://arxiv.org/abs/2603.17456)

In disaggregated serving, generating the first token involves three overlapping communication stages (KV-cache reuse, collective allreduce, P2D transfer) that contend on shared links. MFS introduces Defer-and-Promote scheduling via a Reverse Multi-Level Queue: last-stage flows are deferred to yield bandwidth, then promoted just in time as laxity diminishes. Integrated as a pluggable vLLM module and evaluated on a 32-GPU testbed with Mixtral 8x7B, MFS improves TTFT SLO attainment by 1.2-2.4x over Fair Sharing, SJF, and EDF baselines. The approach is orthogonal to compute-side optimizations and addresses a networking bottleneck that most serving papers ignore. Score: 88 (was 93)

---

## Surge Watch



[Attention Residuals](https://arxiv.org/abs/2603.15031v1) is the standout this cycle. In five days: 53 → 134 HF upvotes, 1,067 → 2,419 GitHub stars, and picked up its first influential citation. Kimi Team's approach to residual-based attention is generating the kind of broad, fast traction that most inference papers never see.

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619v1) is on a similar trajectory at smaller scale: 41 → 73 HF upvotes and 70 → 135 GitHub stars since first appearing on 03-17. Token-level depth routing for attention clearly has an audience.

[GradMem](https://arxiv.org/abs/2603.13875v1) went from zero signals to 30 HF upvotes and 20 GitHub stars in five days. Test-time gradient descent into memory is a novel enough angle that the initial burst warrants tracking.

[Qwen3-Coder-Next](https://arxiv.org/abs/2603.00729v1) woke back up after the plateau flagged last time: 48 → 58 HF upvotes and 2 → 4 citations over the past week. Not explosive, but the flatline has ended.

[IndexCache](https://arxiv.org/abs/2603.12201v1) growth has decelerated: only 48 → 51 HF upvotes in five days after the 37 → 48 burst. GitHub stars still climbing (35 → 53) but the initial wave appears to be tapering.
