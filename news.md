I've read all 8 PDFs. After rescoring against the full texts, the standouts are AgentSpec (strong multi-model vLLM eval, solves spec-decoding's large-batch collapse), ResiSpec (exact, composable), and PuzzleKV (training-free, reproducible). Minima-KV drops sharply — its evidence is self-reported, unreconciled across profiles, shows quality regressions, and isn't reproducible. Here's the bulletin:

# Inference Ecosystem — Flash News
**2026-08-26 · 5 papers from 258 scanned**

### [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://arxiv.org/abs/2608.24004)
Every mainstream speculative decoder (EAGLE-3, NGram, SuffixDecoding) drops *below* autoregressive throughput once batch size passes ~32 on agent workloads — exactly the regime production serving lives in. AgentSpec fixes this with structure-isolated drafting (speculate only within a semantic block, cutting rejection from 53%→26%) plus redundancy-aware budget allocation, and is the only method that stays faster than AR at batch 256, reaching up to 2.02× speedup and 104% higher goodput than the best baseline across 4 model families in vLLM — even beating MTP on MiMo-7B. This is the rare spec-decoding paper that targets the batch sizes engineers actually run. Score: 91 (was 90)

### [ResiSpec: Multi-Candidate Speculative Sampling via Residual Distribution Shaping](https://arxiv.org/abs/2608.24411)
Multi-candidate/tree speculation hits a scaling wall the authors name "Residual Drift": after early candidates are rejected, the residual target distribution slides into the draft model's blind spots, so every later candidate in the tree is wasted. ResiSpec reshapes the verification proxy to keep residuals anchored in the draft's high-confidence zone — provably exact (KL ~1e-10) — for up to 1.92× over SpecInfer and drops in as an add-on to Sequoia (+1.31×) and EAGLE (+1.15×). Clean, exact, composable; docked only because the eval is a single RTX 3090 with Llama-2-7B + a 68M draft. Score: 88 (was 92)

### [PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression](https://arxiv.org/abs/2608.23843)
PuzzleKV reinterprets the PagedAttention page as the compression unit — training/calibration-free per-page truncated SVD, mixed attention over dense and factorized pages via online softmax, converted incrementally during decode. At ~60% KV storage it retains >96% of Full-KV quality on RULER/LongBench (Qwen3-8B, Llama-3.1-8B) and buries sequence-level Global SVD where a shared basis collapses (NIAH-S1: 100 vs 3.6); +INT4 reaches 18.7% storage at >93% quality with just 0.18% TPOT overhead. The page-granularity insight and vLLM-native abstraction make this the most deployable KV-compression paper here. Score: 86 (was 88)

### [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression](https://arxiv.org/abs/2608.23962)
A profiled-simulator study (A100/A40/H100) that puts tensor parallelism (TP1–8) and KV compression (16/8/4-bit) on one cost-per-Mtoken axis and finds no crossover: compression is 1.2–2.0× cheaper at every matched memory-relief level. The sharper result is the real decision boundary — not context length or batch, but model-size-vs-device-memory (~36B on an 80GB card): below it compress and extra GPUs are wasted spend, above it TP is mandatory because weights, not KV, bind. Useful capacity-planning framing, but simulation-only with no quality axis and no dequant-latency model, so read the "compression wins" as a best case. Score: 84 (was 92)

### [Serving Masked Diffusion LLMs: Characterization from Real Hardware](https://arxiv.org/abs/2608.23807)
The first measurement-grounded look at diffusion-LLM serving under load (LLaDA-8B + D2F, H200), and it breaks several AR-carryover assumptions: request difficulty is discrete (11 fixed denoising-step tiers) and unpredictable at admission (R²<0.15), and — most striking — only 24% of single-request wall-clock is GPU compute, with 76% CPU-side dispatch. Synchronized step-level batching amortizes that fixed cost for 16× throughput at batch 16, pointing dLLM serving toward CUDA Graphs and tight CPU-GPU coupling rather than kernel tuning. Forward-looking and rigorous for an emerging serving class. Score: 84 (was 88)

---

## Surge Watch

[FreeToken](https://arxiv.org/abs/2608.16157) went supernova. The bandwidth-adaptive edge-MoE paper I flagged last week didn't just keep climbing on HuggingFace (**61 → 94 upvotes**) — its GitHub repo detonated from **67 to 7,304 stars**, a >100× jump that's easily the loudest signal on the board this cycle. That's not launch buzz; someone shipped code the community had been waiting for.

[LLMRouter](https://arxiv.org/abs/2608.06867), by contrast, is cooling: upvotes have flatlined at **109** (the 97→109 run is over) while stars keep a slow drip to **2,536**. Classic post-launch plateau settling into a long tail.

On the citation side, [FlashAttention-4](https://arxiv.org/abs/2603.05451) is the quiet compounder — **42 → 46 citations and influential cites 6 → 7 in ten days**. Flagship-kernel adoption, not hype. DSpark and DFlash, last week's citation names, have both gone flat.
