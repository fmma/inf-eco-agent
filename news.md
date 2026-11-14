All eight PDFs are read. Final full-text rescore, then the bulletin.

Rescore summary (abstract → full-text): Cairn 92→92, MegaOps 90→90, GC-MoE 90→88 (niche hardware + batch-256 HBM-bound caveat), Batch Makespan 85→87 (production-validated, timely), DRAMA 85→85, LazyWeights 85→80 (ASIC speedups are projections), Olifant 86→78 (consumer HW/bs=1/domain-matched only), OBM 90→72 (80k-accelerator custom-optics research horizon). Top 5 ≥85 selected.

# Inference Ecosystem — Flash News

**2026-11-14** · 174 papers scanned · top 5 after full-text rescore

### [Fast Serverless LLM Cold Starts by Sharing and Prewarming Startup Work](https://arxiv.org/abs/2611.16180)
Cairn dissects the serverless cold start and finds weight loading is only 5–11% of a 57–85s startup — the rest is compilation, engine init, and KV profiling. It publishes the compile cache and engine artifacts to a shared CXL memory pool and prewarms model-agnostic setup in zygote containers, cutting cold starts 4.1–5.2× (to 11–21s), median TTFT 64%, and timeout rate from 15.6% to 2.1% at 3.2 req/s on ServerlessLLM+vLLM. If you autoscale LLMs, this reframes what "cold start" even means. Score: 92 (was 92)

### [MegaOps: A Kernel Overlapping Framework with PyTorch-like Modularity and Megakernel Performance](https://arxiv.org/abs/2611.16248)
The key insight: you can kill kernel-launch barriers without fusing everything into a megakernel — just run dependent kernels on separate CUDA streams and synchronize on data tiles instead of whole tensors. MegaOps matches hand-tuned ThunderKittens megakernels (0.89–1.15×) and beats vLLM by 1.27× on short-context decode (H100), at only 2.09× the LoC of plain PyTorch while reusing Triton/cuBLAS/cuDNN. Megakernel-class latency without the megakernel maintenance tax. Score: 90 (was 90)

### [GC-MoE: Expert-Parallel MoE Decoding on Consumer Blackwell](https://arxiv.org/abs/2611.16219)
A hand-engineered expert-parallel MoE decode kernel for SM120 (RTX PRO 5000) over PCIe, using block-scaled FP8×FP4 QMMA, a swap-AB mainloop, and expert-granular streaming dispatch. It wins 18/18 configs: 1.52× over FlashInfer's W4A8 MegaMoE and 1.39× over Cake, with cosine ≥0.99999976 numerics on GLM5.2 and DSV4.1-Flash. The catch is honest — at batch 256 it goes HBM-bound and the margin collapses to 1.02× — but for workstation-class MoE serving this is the new bar. Score: 88 (was 90)

### [Reducing Batch Makespan for LLM Agent Workloads through Inference–Environment Coordination](https://arxiv.org/abs/2611.16661)
Ant's Ling team targets a bottleneck everyone doing RL rollouts and agent evals feels: batch makespan, not per-request latency. They add workload-aware KV/recurrent-state cache partitioning for hybrid models, trajectory-affinity routing (LBCH), and Chain-Advancing Action Scheduling that advances long tool-use chains to shorten the tail — 10.4–65.0% makespan cuts on BFCL/SWE-bench/WideSearch/MCP-Atlas, already shipping in Ling-3.x development. Built on SGLang and production-validated. Score: 87 (was 85)

### [DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models](https://arxiv.org/abs/2611.16345)
A measurement-first, training-free accelerator for multimodal diffusion LLMs: spatial visual-token pruning (attention concentrates on ~1–2 patches) plus sufficiency-guided adaptive stopping (denoising plateaus early). On LLaDA-V the balanced variants hit ~9.5× at −1.9pp accuracy, while aggressive FG Uni pushes 18.67× avg across six VL benchmarks, lifting throughput from an unusable 2.6 to 51.9 tok/s. No retraining, no architecture change — if you serve dLLMs, it's a drop-in. Score: 85 (was 85)

---

## Surge Watch

**[Flide](https://arxiv.org/abs/2610.42148) looks like the first fresh breakout since REAP/Continuum.** The exact-state-forking decode paper (relevance 88) went from nothing in our tracking to **486 GitHub stars + 36 HF upvotes** by Nov 14. Caveat: a star count that large appearing in one shot usually means we just linked an already-popular repo rather than two-day growth, so I'd want a second reading to confirm it's live traction — but it's easily the liveliest debut on the board.

Ignore the top of the citation gain list: it's a *second* synchronized Semantic Scholar backfill, bigger than the Nov 12 one. [FlashAttention-4](https://arxiv.org/abs/2603.05451) leapt 77→111 and [Mamba-3](https://arxiv.org/abs/2603.15569) 105→133 overnight, with a couple dozen unrelated papers (Qwen3-Coder, IndexCache, Nemotron 3 Super…) all jumping citations in lockstep on the same day. Bookkeeping, not momentum.

Organic HF upvotes stay flat-to-down from the early-November reset — [D3D](https://arxiv.org/abs/2611.06425) doubling 10→20 is the only flicker, and off too small a base to count. The Memory Wall SSD-MoE repo has no new reading since Nov 13, so nothing to add there this round.
