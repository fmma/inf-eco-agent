I've now read all 8 PDFs. Based on full-text rescoring, here is the bulletin.

# Inference Ecosystem — Flash News
**2026-08-16 · 567 papers scanned · top 5 after full-text rescore**

Strong week for *serving systems you can actually ship* — the through-line is coordination: stop optimizing subsystems in isolation.

## [OpScale: Operator-level Provisioning and Autoscaling for LLM Serving](https://arxiv.org/abs/2608.13499)
Rethinks the *unit* of autoscaling from whole-model replicas to individual operators (attention, MLP, fused-MoE), exploiting the fact that the bottleneck operator shifts with sequence length and load. Built on nano-vLLM (~17K LOC) with CUDA Green Contexts + kvcached and evaluated on 40×A100 and 24×GB200 with production traces: meets SLOs with up to 36.3% fewer GPUs / 28% less power (or +44% throughput at fixed budget), cutting scale-out latency from ~10s to sub-450ms. The rare autoscaling paper validated end-to-end on real GB200 silicon — a genuinely new scaling primitive. Score: 93 (was 95).

## [Cascade: SLO-Aware Latency Budget for Fair and High-Goodput LLM Serving](https://arxiv.org/abs/2608.06557)
Defines one *per-request latency budget* (SLO minus predicted service time) and uses that single quantity to jointly drive request scheduling *and* multi-tier KV decisions (restore/prefetch/recompute across HBM/DRAM/NVMe) — things everyone else tunes separately. On production traces (Qwen-2.5-72B, Llama-3-70B/405B, GB200 profiles in an extended Vidur): 2.4× goodput and 40% fewer SLO violations vs vLLM FCFS, same load on 22% fewer GPUs, *without* starving long-context requests the way SJF does. Docked only for being simulator-based; the budget-unification idea is the cleanest scheduling insight this month. Score: 92 (was 95).

## [vToken: Token-Level Virtualization for Reclaimable KV Caches](https://arxiv.org/abs/2608.13263)
Fixes the granularity mismatch between token-level eviction (H2O/StreamingLLM/Scissorhands) and block-level PagedAttention that strands 40–60% of allocated KV in partially-live blocks. A token-table indirection layer plus async lazy compaction reclaims those blocks while preserving PagedAttention kernels and CUDA Graphs — implemented in vLLM for up to 1.37× SLA throughput, 2× feasible concurrency under memory pressure, and it drops per-policy integration from 500+ LOC to under 50. Honestly scoped as a pressure-activated extension, not a universal win. Score: 91 (was 95).

## [TEMPO: Makespan-Aware Expert-Parallel Load Balancing](https://arxiv.org/abs/2608.13057)
Shows today's MoE dispatchers are all mispriced: per-expert cost is two-regime — a memory-bound weight-streaming floor below ~156 tokens/expert, then 128-tile-padded compute above — so token-balancers (EPLB/LPLB) and activation-balancers (METRO) each blow up in the other's regime, and 92–100% of decode batches mix both. A max-affine cost model + millisecond makespan solver plugs into SGLang with zero critical-path overhead: Qwen3-235B gains 4–6% throughput and −15.6% p99 inter-token latency, while comms-bound DeepSeek-V3 correctly gets nothing. "A phase diagram, not a universal win" — refreshingly honest. Score: 88 (was 92).

## [Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE](https://arxiv.org/abs/2608.12103)
Adversarially-audited characterization arguing you should *stop building user-space frequency-pinned expert caches* for larger-than-DRAM MoE and just mmap the pool: at 896 experts/layer the hot set flattens and drifts, so untuned kernel LRU ties an oracle frequency table (75.3% vs 74.6% hit rate) and wins off-domain. The actionable number: dropping `F_NOCACHE` buys 5.3× on repeat expert reads, 1.09–1.10× end-to-end with token-identical output on GH200. Niche (trillion-param offload) but rare, rigorously-proven systems wisdom. Score: 88 (was 92).

**Surge note:** every pick trades point-optimization for *coordination* — budget-driven scheduling, operator-granular elasticity, cost-model dispatch. Serving MoE or long-context today? Read TEMPO and the expert-cache paper first.

---

## Surge Watch

Citations carried the week — the HF upvote board barely moved, so read this as a literature cycle, not a hype cycle.

Headliner is [FlashAttention-4](https://arxiv.org/abs/2603.05451): citations sat flat at **33 (Aug 1–3)**, then jumped to **42 by Aug 16** (+9, influential 4 → 6), extending a climb from just 25 on Jul 8. Near-zero HF traction (2 upvotes) — the field is voting with its bibliographies, not its likes.

The block-diffusion speculative-decoding thread keeps compounding past DFlash: [Block Diffusion Draft Trees](https://arxiv.org/abs/2604.12989) went **10 → 14 citations** in ~12 days.

Two sparse-attention/KV infra papers broke long plateaus on the same refresh: [TriAttention](https://arxiv.org/abs/2604.04921) **12 → 16** (rel 95, but HF stuck at 117 for a solid month) and [IndexCache](https://arxiv.org/abs/2603.12201) **14 → 18** (+1 influential). Steady literature pull, no community-hype spike behind either.
