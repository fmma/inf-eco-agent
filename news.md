PDF extraction tools aren't available in this environment, so I'll rescore based on the detailed abstracts provided and write the bulletin.

# Inference Ecosystem — Flash News
**2026-04-09** | 519 papers scanned

## [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/abs/2604.06664)

Cold-start just got solved. Foundry (UC Berkeley, Ion Stoica) persists CUDA graph topology and execution context offline, then reconstructs executable graphs with negligible overhead at startup. The key trick: deterministic memory layouts plus topology-based templating that lets a single-GPU offline capture generate templates for multi-GPU deployments by patching only rank-dependent NCCL state. Result: Qwen3-235B-A22B initialization drops from **10 minutes to 3.9 seconds** — a 99% reduction — while preserving full CUDA graph throughput gains. If you're running autoscaling or parallelism reconfiguration in production, this is the paper to read this week.
Score: 96 (was 95)

## [Fast-dVLM: Efficient Block-Diffusion VLM via Direct Conversion from Autoregressive VLM](https://arxiv.org/abs/2604.06832)

Song Han's group converts autoregressive VLMs to block-diffusion models that decode multiple tokens in parallel — no separate draft model needed. Direct one-stage conversion from an already-aligned AR VLM outperforms the two-stage approach, and a suite of multimodal adaptations (block size annealing, causal context attention, auto-truncation masking) makes it work for vision-language. With SGLang integration and FP8 quantization, Fast-dVLM hits **6x end-to-end inference speedup** over the AR baseline while matching quality across 11 benchmarks. Particularly relevant for edge/robotics where batch-1 AR decoding is memory-bandwidth-bound.
Score: 93 (was 90)

## [ForkKV: Scaling Multi-LoRA Agent Serving via Copy-on-Write Disaggregated KV Cache](https://arxiv.org/abs/2604.06370)

Multi-LoRA agent workflows break prefix caching because each adapter's activations cause KV divergence. ForkKV borrows the OS fork+CoW paradigm: a DualRadixTree physically splits KV cache into a massive shared base-model component and lightweight per-adapter deltas, with a custom ResidualAttention kernel that reconstructs the full cache in on-chip SRAM. Up to **3x throughput** over SOTA multi-LoRA systems with negligible quality impact. If you're co-hosting specialized agents on shared infrastructure, this is the architecture to study.
Score: 92 (was 95)

## [Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics](https://arxiv.org/abs/2604.07144)

A paradigm paper: instead of hand-engineering static scheduling and rescheduling policies, let an LLM continuously synthesize and rewrite serving policy code based on observed runtime dynamics. Autopoiesis treats scheduling algorithms as "living code" that evolves as workload patterns and cluster topology shift. The results are real — **up to 53% and average 34% improvement** over SOTA serving systems across diverse runtime conditions. The implication is provocative: the optimal serving policy is workload-specific and time-varying, so static human-designed policies are fundamentally limited.
Score: 88 (was 95)

## [InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models](https://arxiv.org/abs/2604.07173)

As MoE architectures balloon LoRA memory costs (every expert needs its own adapter weights), InfiniLoRA decouples LoRA execution into a shared LoRA Server with parallelism-aware execution and SLO-driven provisioning. GPU-initiated communication and hardware-specialized kernels keep it on the critical path. Result: **3.05x serviceable request rate** under strict latency SLOs and 54% more adapters meeting their targets. A complementary approach to ForkKV — one tackles KV cache sharing, this tackles compute disaggregation.
Score: 85 (was 92)

---

## Surge Watch

[TriAttention](https://arxiv.org/abs/2604.04921v1) has its third data point and the verdict is sustained: 82 HF upvotes and 284 GitHub stars, up from 73/194 yesterday. That's +90 stars overnight — the KV cache compression angle is clearly resonating with practitioners, not just paper-scrollers.

[MegaTrain](https://arxiv.org/abs/2604.05091v1) — "full-precision 100B+ training on a single GPU" — went from 4 to 26 HF upvotes and 4 to 99 GitHub stars overnight. The premise is audacious enough to drive clicks on its own, but the early velocity suggests real curiosity. Only two data points; next reading will separate hype from staying power.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) is cooling off: star growth halved to ~15/day (3,042 total), citations flat at 6. The viral-to-infrastructure transition flagged last time appears to be settling into steady state rather than accelerating further.

Everything else is flat. [TAPS](https://arxiv.org/abs/2603.27027v1) enters week two frozen at 141 upvotes / 4 stars — the follow-through gap is now structural.
