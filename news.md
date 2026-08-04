All 8 PDFs read. After rescoring on full-text contribution, novelty, and practical impact for inference engineers, here's the bulletin.

# Inference Ecosystem — Flash News
**2026-08-04 · 402 papers scanned · 5 picks**

This batch is dominated by KV-cache systems work — offloading, eviction, compaction, and placement — plus a standout on speculative decoding for the hybrid-attention models everyone's now shipping.

### [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633)
Block-diffusion LLMs decode B tokens over T denoising steps, and HERALD (Stoica et al., SNU/Berkeley) exploits the fact that sparse inference splits into a KV *selection* phase (full cache, once per block) and a *denoising* phase (critical cache, T times) — so it runs selection on the CPU and denoising on the GPU, crossing PCIe only once per block and lifting the fetch ceiling by T×. Two neat tricks make it work: draft-based lookahead (build a draft prefix from step-0 logits to overlap phases) and representative-query selection (one center [MASK] query replaces B, 8× faster CPU kernel). On SDAR-8B and LLaDA 2.0-mini 16B it stays near-lossless at a 5% KV budget and hits up to 2.28× GPU-only decode throughput at 32K, with gains widening as context grows. The first offloading system purpose-built for the diffusion-serving era. **Score: 95 (was 95)**

### [Bole: Efficient Tree Speculation for Hybrid-Attention Language Models](https://arxiv.org/abs/2608.01651)
Tree speculative decoding never worked cleanly on gated-delta linear attention because the recurrence exposes no attention matrix to mask — Bole derives an exact closed form (a finite Neumann series over an ancestor-masked system) that verifies every proposal node in parallel from one pre-tree state, accelerating linear-attention tree verification 3.4–7.7×. Its factorized state lifecycle keeps a single committed state plus token-scale factors, slashing transient state memory 82–99× and freeing that capacity for KV cache. Integrated into SGLang with a hardware-aware batch-wide budget, it delivers up to 4.72× AR decode throughput and 2.03× over the strongest tree-spec baseline, cutting agent TTFT/TPOT by up to 67.6%/49.9%. If you're serving Qwen3.5- or Kimi-Linear-style hybrids, this closes a real gap. **Score: 93 (was 93)**

### [RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cache Eviction](https://arxiv.org/abs/2608.01247)
Every eviction method just picks which original KV pairs to keep; RestoreKV instead *generates* a tiny context-conditioned "restore cache" — 8 restore tokens attend to the full cache in one LoRA-adapted pass before eviction — under the same total budget. It's a pure plug-in: base scorer and eviction rule unchanged, adapters disabled after construction, <0.5% one-time overhead and zero added query-time cost. At a 5% budget it lifts KVzip from 38.2 to 73.2 on RULER-4K, and KVzip+ reaches 86.4 at 16× compression, holding across four backbones and five eviction methods. A genuinely fresh "restore, don't just select" angle on a crowded problem. **Score: 89 (was 90)**

### [Energy-Efficient LLM Serving via Disaggregated Attention–FFN and Flexible Frequency Scaling](https://arxiv.org/abs/2608.01891)
AFlex finds that Attention and FFN have *different* energy-optimal GPU frequencies that shift with phase, batch size, and TP degree — so it disaggregates the two operators and runs operator-level DVFS via a global ILP scheduler plus a millisecond-granularity local controller, with an interleaved A/F pipeline to kill bubbles. On A800s in SGLang with Qwen3-32B and Mixtral-8×7B under production traces, it cuts energy per token by up to 49% versus SOTA disaggregated serving and 48% versus phase-level frequency scaling, all while meeting TTFT/TPOT SLOs. Operator-level (not phase-level) DVFS is the insight worth stealing as energy becomes a first-class serving cost. **Score: 88 (was 92)**

### [Practical Online KV Cache Compaction for LLM Agents: An Empirical Study](https://arxiv.org/abs/2608.00902)
A clear-eyed empirical study of KV compaction *inside the agent loop*, where you must compress a turn before you know what future turns will need. The takeaways are directly actionable: immediate compaction often hurts, but delaying a few turns to reuse the agent's own future queries recovers most of the gap, and plain token eviction is surprisingly more robust than fancier attention matching under imperfect proxies. On Qwen3.5-27B/Gemma-4-31B, TE preserves most accuracy while cutting KV 80% and lifting throughput up to 4.2×. Proxy-query choice, not the compaction algorithm, is the real design lever. **Score: 87 (was 90)**

Also strong but just outside the cut: **Celty** (spMspV kernel + SIMT co-design, real 2.8× over cuBLAS but headline 5.3× rides on simulated hardware) and Buyya et al.'s **PrefixPlace**/**PrefixShield** prefix-cache placement and multi-tenant fairness work — practical for operators, but narrower than the picks above.

---

## Surge Watch

Quiet week on the board — most of July's surgers have gone flat, and the only real momentum is one speculative-decoding paper.

[DSpark](https://arxiv.org/abs/2607.05147) is the standout: it's compounding on both axes with no single-day spike — citations **2 → 8 since Jul 10** (6 → 8 this past week, 2 now influential) and HF upvotes **26 → 41** (37 → 41 since Jul 27). In an otherwise stalled field, it's the steadiest dual-signal climb going.

[Unlimited OCR Works](https://arxiv.org/abs/2606.23050) still leads and hasn't broken stride on stars — **20,412 → 21,883 (Jul 30 → Aug 4)**, ~290/day — but HF upvotes have leveled off at **75**, so the social side is topping out even as the repo keeps drawing stars. Star-driven now, not hype-driven.

Closing last week's call: [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392), the "fastest citation pickup" pick, has frozen at **6 citations** since Jul 31 with HF flat at 153. That surge is spent.
