I can't access the PDFs due to missing poppler-utils and blocked Python commands. I'll write the bulletin based on the detailed abstracts provided, which contain sufficient technical detail for accurate rescoring.

# Inference Ecosystem — Flash News
**2026-06-02 | 440 papers scanned**

---

### [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2606.02091)

Tencent's DFlare breaks the conditioning bottleneck in block diffusion speculative decoding. Where DFlash forces all draft layers to share one fused target representation, DFlare gives each draft layer its own learnable combination of target layers — a lightweight layer-wise fusion that scales draft depth with consistent gains. Result: **5.52x wall-clock speedup** on Qwen3-4B and 5.46x on Qwen3-8B across math, code, and conversation benchmarks, beating DFlash by 8–11%. Code is open at [AngelSlim](https://github.com/Tencent/AngelSlim). Score: 95 (was 95)

### [Albireo: Scaling LLM Inference Beyond Amdahl's Limits](https://arxiv.org/abs/2606.01927)

Albireo identifies the empirical optimal tensor-parallelism degree where cross-GPU communication overhead balances KV-cache memory benefits, then pushes that optimum higher by overlapping scheduling/IO with compute and adding sequence-parallel sampling. Against vLLM: **up to 1.9x throughput, 48% lower latency, 54% lower energy** — and 2x throughput in production. No model changes required. A clean systems win for anyone running TP inference. Score: 96 (was 95)

### [Move the Query, Not the Cache: Cross-Instance MLA on H100 Clusters](https://arxiv.org/abs/2606.01502)

First real characterization of cross-instance Multi-head Latent Attention on H100 RDMA fabrics. Key insight: MLA compresses each token's KV into ~1 KB, making it cheaper to route the query than fetch the cache — inverting the conventional wisdom. The paper delivers a topology-aware cost model and a closed-form route/fetch predicate that tracks real IBGDA round-trips within ~7%. Directly applicable to DeepSeek-V3/V4 and GLM-5.1 distributed serving. Score: 93 (was 95)

### [ConServe: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/abs/2606.01839)

Existing multi-turn schedulers predict per-turn decode cost — and get it wrong. ConServe lifts scheduling to the conversation level, observing that every agentic conversation has the same two-phase structure: compute-bound first prefill, then a long memory-bound tail. Route prefill to a high-throughput node, transfer KV once, pin the rest. **51% reduction in p95 time-to-first-effective-token**, 7.5% energy savings, and heterogeneous GPU tiering adds another 22.75% energy efficiency. No learned cost model needed. Score: 92 (was 95)

### [NanoSpec: Accelerating Speculative Decoding with Minimalist Vocabularies](https://arxiv.org/abs/2605.26444)

The LM head's 100K+ vocab projection is a hidden bottleneck in speculative decoding drafters. NanoSpec dynamically constructs a context-aware active vocabulary of **<3K tokens** (40x reduction) per step by exploiting temporal locality — no training needed. A co-designed async gather + GPU-resident state system turns that sparsity into real hardware gains: **51.6% draft time reduction**, 1.17–1.29x end-to-end speedup over EAGLE-2/EAGLE-3. Plug-and-play on any spec-decode setup. Score: 93 (was 95)

---

## Surge Watch

[OSCAR](https://arxiv.org/abs/2605.17757) (Offline Spectral Covariance-Aware Rotation) is the breakout of the cycle — 12 → 295 GitHub stars and 5 → 63 HF upvotes in ten days. 2-bit KV cache quantization via learned rotations is clearly hitting a nerve as extreme quantization becomes table stakes for long-context serving.

[Gated DeltaNet-2](https://arxiv.org/abs/2605.22791) followed a similar trajectory: 19 → 185 GitHub stars and 3 → 30 HF upvotes since 05-22. Decoupled erase-write mechanics in linear attention are drawing real implementation interest — the community is actively shopping for sub-quadratic alternatives.

[FlashAttention-4](https://arxiv.org/abs/2603.05451) quietly crossed 20 citations, gaining +7 in a single week (14 → 21 between 05-25 and 06-02). For an attention kernel paper, academic uptake at this rate signals that FA4's pipeline co-design approach is becoming a reference architecture.

[Full Attention Strikes Back](https://arxiv.org/abs/2605.16928) debuted with 93 HF upvotes on its first observation — transferring dense attention into sparse within a hundred training steps clearly resonates with practitioners who want sparsity without the usual quality tax.

[Orthrus](https://arxiv.org/abs/2605.12825) growth is decelerating: after the 13 → 393 star explosion reported last cycle, the pace has slowed to ~17 stars/day. Still climbing, but the initial surge has cooled — the dLLM inference crowd has moved from discovery to evaluation.
