All eight PDFs read. After full-text review, three papers moved: **MoA-Structured Decode Attention** drops sharply (82→58) — it's a rigorous MoA re-derivation of decode/GQA memory bounds that FlashAttention already achieves in practice, with only tiny reference kernels; **Harmonia** (88→81) and **LaCache** (86→80) are solid but narrower (custom-silicon co-design; diffusion-LLM caching whose standalone gain is only ~1.3×). The top five are the serving/systems/security papers with immediate practitioner impact.

# Inference Ecosystem — Flash News
**2026-07-23 · 327 papers scanned · 5 featured**

The M5 launch and agentic serving dominate this cycle — plus a KV-reuse attack every serving team should read.

### [BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators](https://arxiv.org/abs/2607.19438)
Base Compute's framework-free Metal runtime adds hand-written Metal 4 cooperative-tensor kernels (dense + MoE GEMM, fused gate/up, flash-attention prefill) that route compute-bound matmuls through the M5's per-core Neural Accelerators while leaving memory-bound decode on existing kernels. Across 15 configs (Qwen3/3.5/3.6, Llama-3.2, Gemma-4, sub-1B to 35B) it hits **up to 6.4× prefill over llama.cpp and 3.9× over MLX**, widest on MoE models, with decode gains (≤1.75×) correctly bounded by bandwidth. The cleanest "tensor cores are the prefill lever" story on Apple Silicon, with a public repo. Score: 93 (was 93)

### [Efficient Multi-round LLM Inference over Disaggregated Serving](https://arxiv.org/abs/2602.14516)
AMPD is the first PD-disaggregation framework built for the *interleaved* prefill-decode pattern of agents and iterative RAG: adaptive routing (run incremental prefill locally on the decode worker vs. a remote prefill worker), TTFT-aware prefill reordering, and an ILP deployment planner, all on NVIDIA Dynamo. It lifts SLO attainment **67–340% on average** (up to 967% vs. Dynamo, 3435% vs. vLLM) across Qwen3-32B/Llama-3.1-70B/Mixtral on ToolBench/GAIA/HotpotQA/DuReader. Essential if you serve tool-use or multi-turn agent traffic. Score: 91 (was 92)

### [AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters](https://arxiv.org/abs/2607.19223)
AdaFlash fixes the fatal flaw of diffusion drafters — high domain- and token-level variance — with on-policy distillation (reverse-KL + entry-wise divergence clipping) and an adaptive length head that truncates candidates on the fly. The headline: at concurrency 128, EAGLE-3/DFlash/OSD all fall *below* plain AR decoding (0.76–0.83×), while AdaFlash sustains **1.15× and up to ~66% higher throughput than prior SOTA**, reaching 5.3× at low load. Built on SGLang with an async train/serve pipeline — the right shape for real deployments. Score: 90 (was 90)

### [InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata](https://arxiv.org/abs/2607.18957)
Cold start is 99.6–99.9% of TTFT in serverless serving; InstantInfer models process-tree creation, tensor loading, and model switching as Communicating Finite Automata, then safely overlaps execution and merges fine-grained I/O via a proven-correct refactor of vLLM. Result: **up to 7.2× lower cold-start TTFT, 32.3× faster loading, and 11.8× lower switch stall** across H20/L40 and Qwen3-235B/DeepSeek-R1, saturating ~80% of storage bandwidth. Directly useful for elastic and long-tail model serving. Score: 88 (was 88)

### [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957)
Position-independent KV reuse (CacheBlend/LMCache/EPIC) lets an attacker submit a benign chunk behind a GCG-optimized prefix, so the *cached* KV for that chunk silently encodes an attacker goal — hijacking later victims with **94% success and zero adversarial text in their input**. It survives 10% hit rates, 50% recomputation, and 1024-token gaps, transfers black-box, and defeats RobustKV, CachePrune, and cache compression. If you run cross-user prefix/chunk caching, treat this as a live integrity risk. Score: 86 (was 85)

---

## Surge Watch

The mid-July cohort is carrying the fresh momentum. [KronQ](https://arxiv.org/abs/2607.07964) is the clean breakout — 0 → 32 HF upvotes within days of landing (~July 19); Kronecker-factored Hessian quantization is striking a nerve. Riding alongside it: [Jet-Long](https://arxiv.org/abs/2607.07740) (bifocal-RoPE long-context) at 15 → 23 upvotes in a week, and [Trees from Marginals](https://arxiv.org/abs/2607.06763) jumping 1 → 14 on the speculative-drafting front.

Last week's leader has cooled: [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) has flattened at 79 HF upvotes / 113 GitHub stars — the infinite-context surge has stopped compounding for now.

On the academic side, [FlashAttention-4](https://arxiv.org/abs/2603.05451) is hardening into a staple (influential citations 1 → 4 this month, 27 total), and [Mamba-3](https://arxiv.org/abs/2603.15569) keeps its steady climb (46 → 64 citations since early June, 8 influential).
