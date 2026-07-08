# Inference Ecosystem — Flash News

**2026-07-08 · 841 papers scanned · 5 selected**

Read all eight PDFs. Two clear standouts this week, both attacking the same structural sin: treating the serving instance as the unit of change.

### [Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch](https://arxiv.org/abs/2606.26607)
The best MoE serving paper I've read this year. The insight is almost embarrassingly clean: EP and TP aren't two models, they're two *layouts* of one model over byte-identical expert weights and KV cache — so a switch only moves the slices whose owner changed. Moebius holds both CUDA-graph sets resident at fixed addresses (via a unified memory manager with an N+1 slot offset for safe in-place resharding) and moves bytes with fused CUDA IPC kernels that skip NCCL staging entirely — 152 ms to reshard 235B of experts, 1.49× faster than an All-to-All, >70% of NVLink peak. On 8×H200 / Qwen3-235B-A22B it beats an *oracle* that picks the better static layout per RL rollout step by 1.16–1.25×, because the win comes from switching *within* a step as the burst decays into stragglers. 7,400 LoC on SGLang, ~200 lines touched. 2.4% memory overhead, funded by shrinking KV rather than adding memory. If you run MoE rollouts, this is the paper. **Score: 97 (was 98)**

### [KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding](https://arxiv.org/abs/2606.29207)
Disaggregates *within* the decode step: weight nodes keep projection/FFN, weightless attention nodes hold token-range KV partitions and scale on demand. The systems trick is real — a CPU polling loop reads host-visible `WriteValue32` readiness flags out of an unmodified CUDA Graph and posts pre-registered UCX sends, so a scale event is a routing-table edit, not a recapture. Prepared route install: **7.2 µs**, versus 1.1 s for ServerlessLLM and 10.8 s for a cold start. Query-first attention dispatches Q before K/V projection finishes, and inter-layer microbatch pipelining hits 1.90× of the 2× bound — disaggregated MHA decode ends up *faster* than the non-disaggregated reference (0.96×). Flat p99 TPOT (~34 ms on H100) at 100% SLO attainment, 27–61% lower $/Mtok. Weights and growing KV state should not share an elastic unit. **Score: 96 (was 98)**

### [DiLaServe: High SLO Attainment Serving for Diffusion Language Models](https://arxiv.org/abs/2606.29094)
Venkataraman's group brings real serving discipline to dLLMs, and the key move is recognizing the confidence threshold as a *load-control knob*, not just a quality dial: dropping 0.9→0.7 cuts denoising steps 38%, buying 1.61× capacity for 1.5% accuracy. Per-request SLO-aware threshold selection alone gives +70.8pp SLO attainment, but adding aggregate load control (which caps each request's max threshold so worst-case cluster load stays within capacity) adds another +42.4pp — the two-level design is the paper. A two-stage ILP retunes TP mix as load shifts, and migration is restricted to recompute steps (arbitrary-step migration costs up to 38% at 16 instances). Denoising steps being near-stateless makes tens-of-KB migration viable. 56.6pp SLO gain, 46% latency cut, <1% quality drop. **Score: 93 (was 97)**

### [KernelSight-LM: A Kernel-Level LLM Inference Simulator](https://arxiv.org/abs/2606.28565)
Roofline × learned-efficiency per kernel family, fed into a line-by-line reimplementation of vLLM v1's scheduler (Spearman +0.985 on launch order). Predicts held-out **GB200** from datasheet specs alone at 12.1% per-kernel error; one microbenchmark sweep sharpens it to 3.8% — 7.3× better than AIConfigurator, which routes RMSNorm/RoPE/KV-write through a single `bytes/(0.8·BW)+3µs` shortcut and eats 29–64% error there. End-to-end p50: 3.0% throughput, 6.2% TPOT. The honesty is what earns the score: Appendix B shows the attention efficiency factor is *both* the largest (η≈3–3.5) and the least portable (3.8× cross-device spread) — exactly the family where the model matters most is where it transfers worst. TTFT also blows up to 74% at ρ≈1.2. Use it for capacity planning below saturation, not for tail-latency claims. **Score: 92 (was 96)**

### [Ranking Before Serving: Low-Latency LLM Serving via Pairwise Learning-to-Rank](https://arxiv.org/abs/2510.03243)
The 15.7× headline is per-token latency vs. FCFS under overload — read it as HOL-blocking relief, not a kernel speedup. What holds up is the framing: response lengths are stochastic (~20% relative variance across reruns at temp 0.7), so pointwise regression and listwise ranking train on noise. PARS filters to pairs differing ≥20% and trains BERT with margin ranking loss — Kendall's τ jumps from 0.09 to 0.50 on LMSYS/R1. A GPT-4-trained predictor transfers to Llama and R1 without retraining, and throughput *rises* (2.57→2.87 req/s) because same-length batches decode more homogeneously. ~1,000 lines on vLLM 0.8.5, no CUDA changes, open source. Costs 1 GB of GPU for the predictor. **Score: 85 (was 98)**

**Cut on full text:** PersistentKV (single-author RTX 3060; the calibrated router honestly routes B4 and G≠4 *back to FlashInfer* — a scheduling study, not a kernel win) and Cache-Resident LLM Inference (the 11.51× is vs. llama.cpp at batch 1; end-to-end stops at 7B, the rest is analytical extrapolation, and WA separation itself only buys 1.00–1.16×).

---

## Surge Watch

[TokenPilot](https://arxiv.org/abs/2606.17016) is this cycle's breakout: 4 → 16 HF upvotes and 0 → 36 GitHub stars in three weeks, starting from nothing. Cache-efficient context management for agents is exactly the pain point everyone shipping long-horizon agent loops is hitting right now.

[Domino](https://arxiv.org/abs/2605.29707) has flipped modes. HF upvotes plateaued (145 → 152), but GitHub stars nearly doubled — 64 → 114. The hype phase is over and the "people are actually integrating it" phase has begun. That's the healthier signal.

[Mamba-3](https://arxiv.org/abs/2603.15569) is compounding academically: 50 → 61 citations with influential citations jumping 5 → 8. Almost no social buzz (6 HF upvotes, ever) — this is pure researcher-to-researcher adoption.

[SPEED-Bench](https://arxiv.org/abs/2604.09557) crossed 3K GitHub stars (2,934 → 3,157) and picked up its first influential citation. Speculative decoding is getting a standard yardstick, which usually precedes a wave of comparable papers.

[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) has cooled — 131 → 150 upvotes over three weeks, after gaining 48 in three days. Strong debut, normal decay. Stars still climbing (293 → 371), so the interest converted.
