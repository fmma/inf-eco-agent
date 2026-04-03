# Inference Ecosystem — Flash News
**2026-04-03 | 597 papers scanned**

### [DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72](https://arxiv.org/abs/2604.01621)

NVIDIA introduces DWDP, a new inference parallelism strategy that eliminates inter-rank synchronization from MoE serving by offloading expert weights across peer GPUs and fetching them on demand via copy-engine-based P2P transfers. Implemented in TensorRT-LLM and evaluated with DeepSeek-R1 on GB200 NVL72, it improves end-to-end output TPS/GPU by 8.8% at comparable TPS/user in the 20-100 TPS/user range. The key insight: synchronization overhead hits ~12% under realistic workload imbalance (20% CV in sequence lengths), and DWDP's fully asynchronous execution sidesteps it entirely. The paper also includes a detailed analysis of power-induced frequency throttling from communication-computation overlap — a real concern on Blackwell. Score: 94 (was 95)

### [Goose: Anisotropic Speculation Trees for Training-Free Speculative Decoding](https://arxiv.org/abs/2604.02047)

GOOSE formalizes an overlooked asymmetry in training-free speculative decoding: context-matched tokens (from n-gram lookup) are accepted 2-18x more often than transition tokens (from logit statistics). The optimal tree is therefore *anisotropic* — a deep spine of reliable tokens with wide branches of low-confidence alternatives. This is proven to dominate balanced trees (Sequoia-style) and achieves 1.9-4.3x lossless speedup on 7B-33B models across five benchmarks, outperforming isotropic baselines by 12-33% under equal node budgets. Zero training required, <7 MB memory overhead, <1% wall-clock tree construction cost. The confidence-adaptive bypass mode automatically switches to linear verification when match quality is high. Score: 93 (was 95)

### [FlatAttention: Dataflow and Fabric Collectives Co-Optimization for Tile-Based Accelerators](https://arxiv.org/abs/2604.02110)

FlatAttention proposes a new attention dataflow for emerging tile-based many-PE accelerators that exploits hardware multicast and reduction primitives in the on-chip NoC fabric. On a 32x32 tile configuration matching GH200's peak FP16 performance, it achieves 86% average utilization for compute-bound attention and 78% HBM bandwidth utilization for memory-bound cases — averaging 1.9x over FlashAttention-3/FlashMLA on GH200. End-to-end DeepSeek-v3 FP8 decoding on a 64-chip wafer-scale system shows 1.9x throughput improvement over 96 H800 GPUs despite 1.5x lower peak performance. A forward-looking paper for anyone tracking post-GPU inference hardware. Score: 85 (was 92)

### [AA-SVD: Anchored and Adaptive SVD for LLM Compression](https://arxiv.org/abs/2604.02119)

AA-SVD tackles a blind spot in SVD-based LLM compression: existing methods either optimize on original activations (ignoring upstream compression drift) or on shifted activations (risking divergence from original behavior). AA-SVD does both via a closed-form solution that anchors to original outputs while conditioning on shifted inputs, plus a block-level refinement step that lets compressed layers jointly compensate for each other's errors. On LLaMA-7B at 0.6 compression ratio, it achieves 8.35 WikiText2 perplexity vs. 13.11 for SVD-LLM — and at 0.4 ratio, it's the only SVD method that doesn't collapse. Particularly strong on compact architectures like LLaMA-3-1B where SVD-LLM's perplexity blows up 3x. Score: 82 (was 88)

---

## Surge Watch

[TAPS](https://arxiv.org/abs/2603.27027v1) is the new arrival to watch: 137 HF upvotes within days of appearing on the tracker, making it the strongest debut since Attention Residuals. Task-aware proposal distributions for speculative sampling from KAUST — the community clearly has appetite for practical spec-decode improvements.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) is finally decelerating: +33 GitHub stars over the last day to 2,921, down from the +93-in-5-days pace reported last time. HF upvotes have stalled at 171. Still the most-starred paper in the tracker, but the discovery phase is winding down.

[PackForcing](https://arxiv.org/abs/2603.25730v1) continues on GitHub — 191 stars (+39 since last report) — but HF upvotes flatlined at 47. Practitioners are starring the repo; the academic side has moved on.

[Vectorizing the Trie](https://arxiv.org/abs/2602.22647v1) follow-up: the overnight GitHub surge didn't sustain — only +2 stars to 206, and HF upvotes never followed at all. One-time discovery, not a trend.
