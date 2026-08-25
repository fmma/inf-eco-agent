I've read all 8 PDFs. After rescoring on full text, here's the bulletin:

# Inference Ecosystem — Flash News
**2026-08-25 · 5 papers · 305 scanned**

### [NOVA: Technology-Architecture Co-Design of Near-Memory Processing for Attention-SSM-MoE Hybrid LLM Inference](https://arxiv.org/abs/2608.22613)
MICRO 2026's most ambitious inference-hardware paper: a 2-tier near-memory processor (peri-die + base-die) on 4F² VCT DRAM with peri-over-cell stacking that doubles memory density and runs GQA, SSM, and MoE decode entirely in memory. It averages 4.5× throughput, 69.8% lower latency, and 5× better energy efficiency over an H100 across Nemotron-3-Nano/Super, Falcon-H1R, and Qwen3 — at 3.9% area overhead — and is the *only* design that survives 256K context without OoM. Not deployable today, but the clearest signal yet of where silicon is heading for the hybrid models everyone is now shipping. Score: 93 (was 95).

### [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](https://arxiv.org/abs/2608.22643)
Nails the brutal "model-exceeds-memory" edge regime with one sharp observation: 82–85% of active MLP neurons persist token-to-token, so only the delta must cross the NVMe boundary. A single post-layer-0 predictor (2.86% of params) exposes the entire sparse-layer I/O plan up front, replacing reactive OS demand paging with scheduled io_uring reads. Result: 7.9–12.0× over llama.cpp on a Jetson AGX Orin (3.22 vs 0.34 tok/s at 14G), in a setting where 12 of 20 tested engines never even reach generation. Score: 89 (was 92).

### [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)
Exposes a prefill/decode attention mismatch — prefill fixates on the audio start (sink effect), decode spreads broadly, top-K overlap only ~0.19 — that dooms any prefill-only KV eviction. WnW triages KV-heads into anchor/tidal/fixed roles: anchors observe decode-time importance while tidal heads recall audio chunks from CPU on demand. It stays within ~1.6 WER of full cache at 20% GPU tokens on Voxtral/Qwen2.5-Omni, where prefill-only baselines fail to terminate; the recallable-eviction insight generalizes well beyond speech. Score: 87 (was 90).

### [Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time](https://arxiv.org/abs/2608.22761)
The empirical backing for the DRY sampler already shipping in llama.cpp, ExLlamaV2, and text-generation-webui. By penalizing only tokens that extend a suffix seen earlier in context (with breakers protecting chat/format tokens), DRY cuts the loop rate ~47% while preserving MT-Bench, MMLU, and GSM8k on 70B/120B AWQ models — exactly where repetition penalties and no-repeat n-gram blocking lose measurable ground. Under 3% overhead out to 128K context; safe to leave on by default. Score: 87 (was 85).

### [XTC: Head-Aware Sampling by Excluding Top Choices](https://arxiv.org/abs/2608.22758)
Companion to DRY (same team, also merged into llama.cpp/ExLlamaV2/text-gen-webui): a decoding operator that fires only when ≥2 tokens clear an absolute plausibility floor, then removes the dominant ones and keeps the underdog. Across 60 experiments and a 150-rater human study it delivers 11–15% Distinct-2 gains and 27–47% fewer repeat trigrams, costing just −1.7 pp on IFEval versus −8.8 pp for a diversity-matched temperature bump. It targets the head, so it composes cleanly with min-p and temperature. Score: 87 (was 85).

---

## Surge Watch

HuggingFace woke back up this week after last week's lull — two fresh breakouts led the charge.

[FreeToken](https://arxiv.org/abs/2608.16157) (bandwidth-adaptive edge-MoE serving) is the cleanest spike: **26 → 61 HF upvotes in a single day** (Aug 19→20), the sharpest acceleration on the board. [LLMRouter](https://arxiv.org/abs/2608.06867) is the heavyweight — **97 → 109 upvotes and 2,355 → 2,434 GitHub stars** in under a week; a router-infra megarepo that's clearly caught fire, even if it reads more as launch hype than research signal.

On citations, [DSpark](https://arxiv.org/abs/2607.05147) (semi-AR speculative decoding) is quietly compounding: **8 → 18 citations, influential cites 2 → 6** since early August — adoption, not a launch bump. [DFlash](https://arxiv.org/abs/2602.06036) keeps its streak alive too, **67 → 72 citations and ~+300 GitHub stars (now ~5.9k)** in ten days. Last week's citation names (IndexCache, Mamba-3, MEMENTO) have all flattened.
