# Inference Ecosystem — Flash News

> 2026-05-15 · 999 new papers scanned, 20 scored, 8 read in full

### [EEP: Surviving Partial Rank Failures in Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670)
Mutable-membership protocol for expert-parallel MoE serving that recovers from GPU rank failures in 11 seconds versus 348 seconds for a full restart. Integrated into SGLang and DeepEP, evaluated on DeepSeek-V3 671B across up to 32 GPUs. The key idea is redistributing orphaned experts to surviving ranks via a lightweight coordination layer, maintaining throughput within 5% of the healthy baseline during degraded operation. **Rescored: 94**

### [Test-Time Speculation: Speculative Decoding with Adaptive Draft Models](https://arxiv.org/abs/2605.09329)
Identifies a previously overlooked problem — speculative decoding acceptance rates decay as output length grows because the draft model drifts from the target's evolving distribution. TTS fixes this with online distillation: the draft model is fine-tuned on accepted tokens during inference using a stride schedule (every S tokens). On Qwen3.5-122B with Qwen3.5-3B draft, TTS achieves 1.54× throughput over vanilla speculative decoding, with acceptance-length improvements up to 72%. **Rescored: 93**

### [Patterns behind the Chaos: A Characterization of MoE Data Movement](https://arxiv.org/abs/2510.05497)
ISCA 2026 paper profiling all-to-all data movement across four MoE models (235B–1000B parameters) and extracting six architectural insights — including that >60% of expert transfers are intra-node and token-to-expert mappings exhibit strong temporal locality. Guided by these patterns, a wafer-scale GPU prototype achieves 6.6× speedup over 8×H100 baselines, while even conventional multi-GPU setups gain 1.25× from locality-aware scheduling. Trace datasets are publicly released. **Rescored: 92**

### [Sieve: Dynamic Expert-Aware PIM Acceleration for MoE](https://arxiv.org/abs/2605.11277)
Stanford group exploits the bimodal distribution of MoE token-to-expert assignments — a few "hot" experts handle most tokens while many "cold" experts see sparse traffic. Sieve dynamically routes hot experts to GPU and cold experts to Processing-in-Memory (PIM) units, achieving 1.3–1.6× latency improvement on Qwen3.5, GPT-OSS, and Qwen3 models. The scheduling algorithm adapts per-layer and per-iteration with <1% overhead. **Rescored: 85**

### [CATS: Cascaded Speculative Decoding for Edge Devices](https://arxiv.org/abs/2605.11186)
Three-stage self-speculative pipeline (aggressive → conservative → verification) tuned to fit within edge DRAM budgets. Evaluated on Jetson AGX Orin with Llama-3 8B and Qwen2.5 7B, CATS delivers up to 5.08× wall-clock speedup by cascading increasingly selective draft stages, each gated by a lightweight confidence threshold. No auxiliary draft model needed — all stages reuse subsets of the target model's own layers. **Rescored: 82**

---

## Surge Watch

[Adaptive Block-Scaled Data Types](https://arxiv.org/abs/2603.28765v1) just broke out of two months of complete silence — 0 → 180 GitHub stars overnight on May 15. After being tracked since early April with zero signals across the board, something clearly surfaced this paper to the community. Worth watching whether this sustains or was a single-event spike.

[ServeGen](https://arxiv.org/abs/2505.09999) already carried serious academic weight (24 citations, 6 influential) but had no community presence until today — 127 GitHub stars appeared in a single day. Production LLM workload characterization hitting the practitioner radar after quietly accumulating researcher attention.

[Continuum](https://arxiv.org/abs/2511.02230), the KV cache TTL paper for multi-turn agents, is following a similar pattern: 20 citations and 3 influential already in the bag, now 75 GitHub stars materialized on first tracking. Academic-to-practitioner crossover in progress.

[Memory-Efficient Looped Transformer](https://arxiv.org/abs/2605.07721) landed with 26 HF upvotes on day one — a strong debut for a paper decoupling compute from memory in looped architectures. Early signal only, but the topic is timely.
