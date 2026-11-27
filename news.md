All 8 PDFs read. Final full-text rescores: DFly2 95, RankCast 94, Ostinato 94, PipeAxes 92, LEGOSpec 90, HSM 89, AsymSpec 87, MixMoMo 84. Top 5 (all ≥90) selected — a clean spread across long-context spec decoding, MoE EP balancing, edge MoE agents, pipeline parallelism, and spec-draft design.

# Inference Ecosystem — Flash News

**2026-11-27 · 5 papers worth your attention** (235 scanned)

### [DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity](https://arxiv.org/abs/2611.34776)
A block-parallel drafter that rides the target's own native sparsity — reusing its KV cache and indexer positions instead of keeping a separate cache or scoring pass. On DeepSeek-V4.1-Flash, GLM-5.3-Flash and Hunyuan-flash, its accepted-length margin over DSpark widens to 10–31% on long-context/agentic work, yielding **+62% (long-context) and +81% (agentic) throughput at 64K**. If you serve natively-sparse flash models, this is the spec-decoding design to copy right now.
*Score: 95 (was 96)*

### [Phase-Aware Rank Balancing in MoE Serving](https://arxiv.org/abs/2611.33542)
RankCast treats prefill (compute-bound on the busiest rank) and decode (memory-bound on active-expert count) as *different* balancing problems, redistributing expert load per-phase over DeepEP in SGLang. On Qwen3-235B-A22B (EP=8) and Qwen3.5-397B-A17B (EP=16) it removes >75% of busiest-rank excess prefill load for **+16–19% prefill throughput and +6–11% decode 1/TPOT, beating EPLB by 2.7–6.8 points** at <1pp quality cost. EP load imbalance is *the* large-MoE serving tax, and this beats the de facto baseline.
*Score: 94 (was 95)*

### [Ostinato: Low-Latency CPU–GPU MoE Inference for Local Agents](https://arxiv.org/abs/2611.11533)
One static cross-layer GPU expert pool, reused every forward pass, so short agent tool-turns copy **zero** expert weights from host DRAM; multi-GPU decode is captured as a device-side zero-slot CUDA graph. Built on llama.cpp and tested on SWE + τ²-bench across DeepSeek-V4-Flash, GLM-5.3-Flash and Qwen3.8-Flash-Next, it cuts median tool-turn waits **2.5–6.6×** and runs full sessions **1.36–3.83× faster** (up to 4× RTX 4090D), beating KTransformers and ik_llama.cpp. The most thorough paper in the batch, aimed squarely at the booming local-agent-on-consumer-GPU space.
*Score: 94 (was 95)*

### [Decoupling Compute and Communication Granularities for Pipeline-Parallel LLM Serving](https://arxiv.org/abs/2611.34615)
PipeAxes slices wide prefill batches a few layers at a time so decodes interleave between slices, over a fused Triton Hadamard-INT4 codec (7.53× compression, <0.03% perplexity hit), all in vLLM. On a 4-stage MoE it delivers **23.3× SLO goodput** over calibrated Revisit-PP, and on mixed 64K traffic drops short-request p95 TTFT from **129.8s to 512ms**. Niche (PCIe/WAN heterogeneous clusters) — but if that's your hardware, the gains are enormous.
*Score: 92 (was 95)*

### [LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training](https://arxiv.org/abs/2611.33004)
Decomposes drafts into Context/Backbone/Proposal/Objective and runs matched-condition ablations to isolate what *actually* drives acceptance — then ships DFlux (SWA–GQA hybrid + convolution + Residual Corrector + hierarchical supervision). Across Qwen and Gemma, DFlux beats the strongest baseline by **+19.7% (regular) / +34.7% (long-context) acceptance** and **1.57–5.62× SGLang throughput over AR**, while the training stack adds +79% throughput and 3.11× faster offline supervision vs SpecForge. Finally disentangles the spec-draft choices everyone's been tuning blind.
*Score: 90 (was 90)*

---

## Surge Watch

**The SSD-MoE repo gave back its surge.** [The Other Half of the Memory Wall](https://arxiv.org/abs/2609.18063) *lost* ~1,500 GitHub stars Nov 22→27 (12,186 → 10,691) — the first drop after weeks of thousand-a-day gains, with HF upvotes slipping 37→36. De-star wave or spam purge, the vertical climb I flagged as cooling is now clearly over.

**Two inference papers crossed 100 citations.** [Continuum](https://arxiv.org/abs/2511.02230) (KV-cache-TTL agent scheduling) went 91→101 and [VLASH](https://arxiv.org/abs/2512.01031) (real-time VLAs) went 95→106 over Nov 22→27, each with a fresh influential-citation bump (+3, +4) — agentic serving and real-time robotics are both indexing hard.

**Linear-attention citations keep compounding.** [Gated DeltaNet-2](https://arxiv.org/abs/2605.22791) added +12 in five days (50→62, influential 9→12) and [HiSparse](https://arxiv.org/abs/2608.07009) jumped 9→15 (influential 1→6) — the architecture and sparse-decoding backbones haven't slowed since last week.
