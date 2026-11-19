# Inference Ecosystem — Flash News
**2026-11-19 · 5 papers · 247 scanned**

Serving systems and speculative decoding own today's batch — with production-scale receipts from Meta and NVIDIA, and looped-transformer decoding maturing fast.

## [Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity](https://arxiv.org/abs/2611.24891)
Meta's production traffic shaper ports congestion control to inference dispatch: a fail-fast CAP refuses work at the saturated replica (HTTP 429), and the TRACK dispatcher probes the ceiling from refusals alone — no output-length prediction, no fleet-rate retuning. In same-traffic A/Bs it served a classifier on **43% fewer H100s** than its fixed-rate precursor and kept vLLM batches a median 124/128 full vs 41; the system carries 300M+ requests/day (1.1B in its busiest 24h). If you operate a serving fleet, this is the most actionable systems paper of the day. Score: 91 (was 90)

## [NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding](https://arxiv.org/abs/2611.23835)
NVIDIA shows a feature-conditioned draft's entire residual stream can run at half or quarter of the target width while largely preserving acceptance (≤3% loss at half) — and for DFlash the trained output adapter folds into the borrowed LM head, leaving logits exact up to rounding. Tested on DFlash/EAGLE-3 × Qwen3-8B/GPT-OSS-20B in SGLang: **1.06–1.12× end-to-end on B200, 1.13–1.44× on GB10** at batch 1, holding at or above parity through batch 512. Draft width is now a first-class knob — tune it for your GPU instead of inheriting it from the target. Score: 89 (was 90)

## [Towards Fair Resource Sharing in Agentic LLM Serving](https://arxiv.org/abs/2611.23558)
Duru defines agent-level fairness as slowdown relative to standalone execution and coordinates slowdown-aware routing, starvation admission exceptions, and SLO-driven autoscaling across the full stack. On Qwen3-Coder-30B, Llama-3.3-70B and DeepSeek-V4-Flash (NVIDIA + AMD, real Azure/TraceLab/AgentX traces) it cuts p99 normalized slowdown by a geomean **44.4% (up to 79.5%)** at 91.8–127.4% of baseline throughput, beating NVIDIA Dynamo and llm-d. Agentic serving fairness is heating up, and this is the most complete cross-layer treatment yet. Score: 87 (was 90)

## [Late Entry in Looped Language Models](https://arxiv.org/abs/2611.24576)
A rigorous answer to "which passes should a token run?" in looped LMs: skip the early passes and enter the final K<T passes over a deep context cache, completing true 1→T KV states as piggybacked batch rows at zero extra serial calls. "Wake verification" unifies greedy-exact (τ=0), margin-gated, and lossy decoding in one static CUDA graph — **5.2× on Ouro-2.6B and up to 8.4× greedy-exact / 12.5× lossy on Huginn-3.5B**, with rollbacks dropping 21.5× as recurrence deepens. Proves cached-context depth beats token-local early passes and backs it with a calibrated Roofline law. Score: 84 (was 88)

## [LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers](https://arxiv.org/abs/2611.24301)
LoopCache kills the R× KV-traffic blowup of wave-style loop decoders via cyclic loop KV scheduling (one loop's cache per step) plus confidence-guided dynamic draft updating, keeping independent KV only for a few loop-sensitive shallow layers. Across six looped models and long-context benchmarks it reaches **10.25× / 14.56× over WFD / LoopSpec** and 5.12× / 2.52× over AR / DtV — losslessly. The practical fix that makes looped-transformer speculation viable past a few thousand tokens. Score: 82 (was 88)

---

## Surge Watch

**Speculative decoding is this cycle's citation magnet.** [DFlash](https://arxiv.org/abs/2602.06036) vaulted 127→202 citations in a single week (influential 53→80), the biggest move on the board outside the DeepSeek flagship — and [DSpark](https://arxiv.org/abs/2607.05147) flat-out doubled right alongside it (42→84 citations, 19→41 influential). The block-diffusion speculative-draft line is compounding hard.

**FreeToken graduates from GitHub darling to cited work.** [FreeToken](https://arxiv.org/abs/2608.16157) has stacked ~7.3K→17K stars since August and just logged its first real academic pickup — citations 3→13 with influential citations finally appearing (0→5). Bandwidth-adaptive edge MoE serving is now the adoption story to watch alongside the SSD-served MoEs.

**First-traction alert:** [Evolving Infra](https://arxiv.org/abs/2611.12304) (agent-adaptive serving, from the Continuum/ThunderAgent crowd) went 0→106 GitHub stars and 0→13 HF upvotes in barely two days — worth a bookmark if the curve holds.
