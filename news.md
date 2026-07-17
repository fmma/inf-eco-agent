All 8 PDFs read. Based on the full texts, here is my rescored bulletin (outputting raw markdown directly, no file writes):

# Inference Ecosystem — Flash News
**2026-07-17 · 211 papers scanned · top 5 by rescored relevance**

[D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647)
Cross-request pruning that lets a whole batch share one verification budget, concentrating the target model's compute on the drafts most likely to be accepted. Lifts average speedup from 1.26× to 1.65× over DFlash-16 at concurrency-32, rescues dense configs that otherwise fall *below* autoregressive, and hits 3.0× on MoE; a profiled runtime cost model auto-tunes the pruning ratio (1.58× on H20, 1.25× on H800). Training-free, provably lossless, ~0.55ms selector overhead, and already filed as a vLLM PR — the rare speculative-decoding paper aimed squarely at high-concurrency serving. Score: 91 (was 90)

[Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/abs/2607.14541)
Atrex-Bench draws 30 operators / 440 shapes straight from full-cluster production inference traces and scores them on an importance-weighted roofline. The best frontier agent reaches only 10.7% of the hardware roof, and it exposes a "correctness illusion" — models pass by delegating to PyTorch fallbacks (Qwen3.7-Max: 84.8% correct but 43.8% real DSL); their AKA agent then converts fallbacks into real kernels that beat hand-tuned AITER baselines. Production-grounded, open-source, and the sharpest evidence yet that "passes correctness" ≠ "deployable kernel." Score: 86 (was 75)

[Seeing the End at Step Zero: Accelerating Diffusion MLLMs via MLP Sparsity-Aware Truncation](https://arxiv.org/abs/2607.14557)
Seer reads a diffusion-MLLM's valid semantic boundary at denoising *step 0* from a sparsity jump in MLP activations, then one-shot truncates the padding suffix for all later steps. Up to ~31× throughput (MMaDA InfoVQA 0.13→4.02 tok/s) with accuracy held or improved (DocVQA 63.52→63.66), preserved under batching by a padding-waste-aware router across static-graph / bucket-varlen / eager paths plus a device-resident Triton compaction kernel. Genuine algorithm-system co-design, plug-and-play as DMLLMs gain traction. Score: 84 (was 85)

[PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/abs/2607.14618)
Per-channel bit allocation from a CPU-aligned {2,3,4,8,16} palette under a fractional average-bit budget, with a compile-time pass that clusters channels into bit-homogeneous blocks and propagates permutations off the runtime path. Beats AWQ/GPTQ/Slim-LLM/AMQ by 2.4–32.1% perplexity at a 3-bit target, cuts activation-reorder traffic up to 70.8%, and keeps prefill/decode scaling proportional to the bit budget with <2% energy overhead across workstation/laptop/mobile CPUs. Turns fractional-bit budgets into an actionable on-device deployment curve. Score: 84 (was 85)

[PReM: Learning What to Preserve and When to Refresh for Context Compression](https://arxiv.org/abs/2607.14327)
Keeps long context as the model's own layer-wise KV memory and emits a `<m>` token to re-select and refresh which chunks are preserved mid-generation, instead of one early static decision. Beats 8 KV/context-compression baselines at 16× and 32× (up to +10.23 EM / +12.55 F1 on 3B/7B); a 3B PReM even outscores released 7B soft-compression models, at 19.6GB peak vs 30GB full-memory. The refresh mechanism directly fixes the stale-evidence failure of static compressors on multi-hop QA — though it does require training the backbone. Score: 78 (was 80)

---

## Surge Watch

This week the community's attention rotated toward portable, heterogeneous **inference runtimes** — a clean break from last week's sparse-attention story. [Prima.cpp](https://arxiv.org/abs/2504.08791), fast 30–70B inference on low-resource home clusters, surfaced on HuggingFace at a hefty 141 upvotes (Jul 13), by far the loudest signal among this week's fresh movers and well past the 100-upvote mark. Riding the same wave, [Embodied.cpp](https://arxiv.org/abs/2607.02501) — a portable runtime for heterogeneous robots — is climbing steadily: 53→56 HF upvotes and 93→103 GitHub stars in three days (Jul 10→13). Two ".cpp" deployment papers trending together signals real appetite for squeezing big models onto commodity and edge hardware.
