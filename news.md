All 8 PDFs read. After reading the full texts, here's my rescored bulletin. Notable adjustments: I revised the single-model TensorRT-LLM bit-width paper (2608.28003) down below threshold (narrow 1B/single-framework scope), trimmed the hardware survey (strong but reference-material, not news), and confirmed the top tier. One correction worth flagging — HyQuant's text claims "only method at batch-32" but its own Table 6 shows all methods OOM at 32 and HyQuant alone surviving at batch-16, so I report the table's number.

# Inference Ecosystem — Flash News
**2026-08-31 · 174 papers scanned · top 5**

Speculative decoding, KV eviction, and low-bit attention dominate this batch, plus a rigorous energy-accounting study every serving team should read.

## [TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding](https://arxiv.org/abs/2608.26112)
TreeGraft lets a near-free n-gram drafter and a stronger neural "middle" drafter jointly build one shared draft tree, using non-destructive grafting (never overwriting branches the target might still accept) and a distilled value-guided scheduler to decide when the expensive drafter is worth calling. It hits 1.60× average speedup across 10 model pairs and 6 benchmarks — 15.1% over the better fixed-drafter endpoint, up to 26.6% — and is fully training-free with open code. Immediately actionable for anyone running tree-based speculative decoding. Score: 89 (was 91)

## [A Probabilistic Interpretation of KV Cache Eviction](https://arxiv.org/abs/2608.28293)
Van den Broeck & Grover's group proves KV eviction is NP-complete, then reframes it as expectation estimation: H2O, SnapKV, TOVA, and StreamingLLM are all just zero-variance, unbounded-bias estimators. The payoff is decode-time correction via self-normalized importance sampling — a previously ignored failure mode — giving more robust accuracy across LongBench and RULER at the same compression budget on Llama3.2-3B and Qwen3-4B. The mental model to have before shipping any KV-compression scheme. Score: 88 (was 90)

## [Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms](https://arxiv.org/abs/2608.28044)
A careful H100/H200 study showing request energy and token energy move in opposite directions: on Llama-3.2-1B (batch-16, 4K context), growing output 10→512 tokens cuts J/token ~10× (7.46→0.72) while total window energy rises ~5× (1.19→5.93 kJ). Batching gains are context-bounded (6.31× at 512 ctx collapses to 1.17× at 4K), and MoE routing makes low-concurrency serving especially wasteful. If you tune batch/context/output knobs for cost, this reframes "efficient." Score: 87 (was 90)

## [Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation](https://arxiv.org/abs/2608.28276)
PASK reuses the parser transitions that constrained decoding already computes to decide which generated KV entries persist — protecting schema-critical tokens (required fields, arguments, boundaries) that model-side attention saliency misses. At a 0.33 KV budget it beats the strongest compressed baseline by 17.39 pp on BFCL function-calling, with up to 2.2× throughput, 3.3× lower TPOT, and 0.53× peak GPU memory vs Full KV. A sharp, agent-timely angle on KV compression. Score: 86 (was 88)

## [HyQuant: Hybrid-Precision Quantization for LLM Attention](https://arxiv.org/abs/2608.27875)
HyQuant keeps a tiny set of persistent "vertical-line" tokens (<5%) plus a recent window in FP16 and quantizes the rest to 4-bit, fusing dequant into a FlashAttention-style kernel across both prefill and decode. It delivers 1.32×–3.58× decode-kernel speedup (1.04–1.17× end-to-end) with near-lossless accuracy on Qwen3/Llama/GLM across LongBench, GSM8K, and MATH500, and alone sustains batch-16 on a single H100 (231.6 tok/s while FA2/KIVI/KVTuner OOM). Score: 85 (was 88)

---

## Surge Watch

No fresh community-upvote breakout this week — momentum has shifted to the **citation** charts, where a few papers are compounding fast.

**[FlashAttention-4](https://arxiv.org/abs/2603.05451)** is the standout: citations nearly doubled, 28 → 47 in a month (Jul 27→Aug 27), with influential citations up 4 → 7. Barely any HF buzz (2 upvotes), but the kernel-pipelining co-design is being adopted fast where it counts — in other papers' references.

**[Mamba-3](https://arxiv.org/abs/2603.15569)** keeps compounding academically: citations 64 → 73 and influential citations 8 → 10 over the past five weeks, even as HF upvotes stay frozen at 6-7 — a clean case of research traction outrunning community hype.

On the inference-native side, **[IndexCache](https://arxiv.org/abs/2603.12201)** (cross-layer sparse-attention index reuse) is building a rare dual signal: citations 12 → 20 (influential 1 → 4) since late July, plus a late-August HF tick from 64 → 69 upvotes — one to keep an eye on.
