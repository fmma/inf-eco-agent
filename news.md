All eight PDFs read. Based on the full texts, here is my rescored bulletin.

---

# Inference Ecosystem — Flash News
**2026-08-24 · 148 papers scanned · top 5**

Quantization and MoE offloading dominate today's batch — plus a standout on speculative decoding for the linear-attention hybrids everyone is now shipping.

### [TreeWY: Speculative Verification for Gated DeltaNet Hybrids](https://arxiv.org/abs/2608.20961)
Hybrid models (mostly Gated DeltaNet layers + a few softmax) break speculative decoding: verifying a draft needs a full recurrent-state snapshot per draft position, which is memory-infeasible for wide trees. TreeWY rewrites the gated delta rule as a tree-structured WY transform so one triangular solve verifies every node, storing a 128×-smaller pseudo-value matrix and reconstructing only the accepted state on commit. Implemented in vLLM on Qwen3.5-35B/397B (B200), it cuts peak KV usage 2–3× for up to 1.49× throughput and ~40× lower p99 TTFT where memory binds — and it's refreshingly honest that the win is regime-dependent. Score: 91 (was 90)

### [SPICE: Speculative Prefetching with Low-Rank Expert Surrogates for MoE](https://arxiv.org/abs/2608.21240)
MoE offloading is I/O-bound — PCIe expert transfers are 73–88% of per-layer latency. SPICE runs a lightweight draft model with confidence-aware adaptive lookahead to prefetch experts, approximates low-confidence misses with a resident shared-expert + LoRE (low-rank) surrogate, and offloads exact residual work to the CPU in parallel with GPU compute. On DeepSeek-V2-Lite and Qwen2-57B-A14B it hits 2.04–2.70× over AdapMoE (up to 3.12× TPOT at long context) for a 3–4pt accuracy hit, cutting fallback to 3% and H2D traffic 28%. Score: 89 (was 92)

### [Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs](https://arxiv.org/abs/2608.21134)
Graphcore/Arm co-design a sub-3-bit format (S3D8: three signed weights per byte via a shared 5-bit centroid + sign bits) that decodes to INT8 on Arm CPUs in 5 logical ops + 3 table lookups, paired with a data-free QAT pipeline distilling from the model's own generations. Llama 3.2 11B Vision compresses to 3.7 GB (8-bit activations) at only 0.083 avg VQA degradation — far ahead of size-matched INT/student-t/lloyd-max. Real deployment: 3.8 tok/s on a Pixel 8a (where INT8 won't even fit) and a speedup over INT8 on Graviton4, with full open-source C++ for Linux/Android. Score: 86 (was 85)

### [Quantization-Aware Healing: Recovering Compressed, 4-Bit LLMs](https://arxiv.org/abs/2608.20953)
When you both structurally compress and 4-bit quantize, the usual QAD teacher (the recovered bf16 checkpoint) caps the student. QAH distills the 4-bit student straight from the *original* uncompressed model: on GPT-OSS 120B→60B→MXFP4 the healed 4-bit model matches or beats its own bf16 source on 7/9 benchmarks and ties the 120B on LiveCodeBench at ~4× less weight memory — shipped open-weight as Hypernova-60B. It converges ~7× faster than QAT without collapsing, and the deployment lessons (FSDP2 beats DeepSpeed by 8.6pts on GPQA for MXFP4 distillation) alone are worth the read. Score: 82 (was 80)

### [DAOP: Data-Aware Offloading and Predictive Pre-Calculation for MoE](https://arxiv.org/abs/2501.10375)
The pragmatic counterpart to SPICE: since a CPU→GPU expert migration is ~32× slower than a GPU block and activations are ~1/10,000th the size of expert weights, DAOP keeps hot experts on GPU per-sequence (prefill patterns predict decode at ~91% similarity) and pre-computes predicted CPU experts one layer ahead. It beats Fiddler by 35–40% (4.5 tok/s Mixtral-8x7B, 8.2 tok/s Phi-3.5 on an A6000) with minimal accuracy loss, and it's open-source — though on older models and largely incremental over Fiddler. Score: 80 (was 90)

---

## Surge Watch

HuggingFace upvotes went quiet this week — no fresh breakout, and last week's router/edge-MoE spikes never re-accelerated. The action moved to citations, where a few papers are quietly compounding.

[IndexCache](https://arxiv.org/abs/2603.12201) (cross-layer sparse-attention index reuse) is the cleanest curve: **11 → 19 citations** with influential cites climbing **0 → 4** since mid-July — that's adoption, not a launch bump. [Mamba-3](https://arxiv.org/abs/2603.15569) kept pace, crossing **72 citations / 10 influential** (up from 64/8 a month ago) — a state-space line still accelerating rather than plateauing.

Fresh mover worth watching: [MEMENTO](https://arxiv.org/abs/2604.09852) (LLMs managing their own context) jumped **7 → 10 citations in two days** (Aug 18→20), influential ticking 1 → 2 — small, but the slope just turned up.
