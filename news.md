PDF extraction tools aren't available on this system. I'll write the bulletin based on the detailed abstracts provided, which contain enough technical substance for accurate rescoring and write-up.

# Inference Ecosystem — Flash News
**2026-06-15 — 154 papers scanned**

---

### [ProServe: Unified Multi-Priority Request Scheduling for LLM Serving](https://arxiv.org/abs/2512.12928)

ProServe formalizes multi-priority LLM serving as a service-gain maximization problem and delivers a two-tier scheduler. At the engine layer, **SlideBatching** uses a sliding boundary to balance latency vs. priority; KV cache blocks get async offloading and pipelined reloading to overlap compute with host-device transfers. At the service layer, **GoRouting** dispatches across distributed instances with gain-oriented, capacity-aware routing that reserves headroom for incoming high-priority requests. Across four open-source and one industrial dataset, ProServe lifts system gain by up to 35% and SLO attainment by up to 52% over state-of-the-art baselines. This is the kind of scheduler work that production serving teams should benchmark against immediately.
**Score: 90 (was 92)** — solid engineering but incremental over existing priority-aware schedulers.

### [UltraSketchLLM: Sub-1-Bit LLM Compression via Sketch and Hardware-Friendly Operators](https://arxiv.org/abs/2506.17255)

Pushes weight compression below the 1-bit-per-weight floor using **data sketching** — a randomized linear-algebra technique that maps weight matrices into compact sketch tables with hardware-friendly lookup. At 0.5 bits/weight, UltraSketchLLM achieves a 14.9x speedup over a naive sketch baseline while keeping perplexity degradation tolerable. The key trick is replacing dense matmuls with sketch-table lookups that map naturally to GPU memory hierarchy. For anyone deploying 70B+ models on consumer GPUs or edge devices, this opens a new compression regime below what GPTQ/AWQ can reach.
**Score: 88 (was 88)** — eye-catching compression frontier, though real-world quality-at-scale remains to be proven.

### [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/abs/2606.14672)

**Parallel-Synthesis** lets a synthesizer LLM directly consume the KV caches produced by parallel worker agents instead of concatenating their text outputs. A **cache mapper** calibrates independently-generated branch caches, and a fine-tuned **synthesizer adapter** enables generation from this non-sequential cache. Across 9 datasets (math, code, science QA, GAIA, DB diagnosis), it matches text-based synthesis quality while cutting time-to-first-token by **2.5–11x**. This is a practical blueprint for anyone building multi-agent pipelines — skip the redundant prefill, wire the caches directly.
**Score: 82 (was 78)** — rescored up; the TTFT wins and cross-task generalization are stronger than the abstract alone suggests.

### [Residual Context Diffusion Language Models](https://arxiv.org/abs/2601.22954)

Diffusion LLMs waste compute when remasking discards low-confidence tokens each denoising step. **RCD** recycles those discarded token representations as contextual residuals injected into the next step, via a decoupled two-stage training pipeline that sidesteps memory bottlenecks. Applied to SDAR and LLaDA, RCD boosts accuracy by 4–11 percentage points across benchmarks and nearly doubles AIME accuracy while requiring **4–5x fewer denoising steps** to match baseline peak. Conversion cost is just ~300M tokens of fine-tuning. If diffusion LLMs are going to compete with autoregressive decoding, RCD-style compute recycling is table stakes.
**Score: 75 (was 75)** — important for the dLLM niche; not yet mainstream serving but worth tracking.

---

## Surge Watch

[KVarN](https://arxiv.org/abs/2606.03458) (variance-normalized KV cache quantization for reasoning) is the breakout of the week — GitHub stars more than doubled from 179 to 392 in 8 days (Jun 5–13), with HF upvotes climbing 47→60. A fresh KV compression paper going from niche to 400 stars this fast suggests the reasoning-efficiency intersection is where practitioners are paying real attention.

[Domino](https://arxiv.org/abs/2605.29707) (decoupled causal modeling for speculative decoding) had an explosive debut — HF upvotes surged from 2 to 140 and GitHub stars hit 52 between Jun 2 and Jun 7. Similarly, [Draft-OPD](https://arxiv.org/abs/2605.29343) (on-policy distillation for draft models) jumped 0→32 HF upvotes and 4→31 GitHub stars in the same window. Speculative decoding training frameworks are having a moment.

[PackForcing](https://arxiv.org/abs/2603.25730) growth has stalled at 219 stars (up just 1 from last report's 218) — the breakout is definitively over. The broader digestion phase continues: most tracked papers show flat or single-digit incremental signals across the board.
