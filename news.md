I can't read the PDFs directly (no poppler-utils installed and no PDF Python libraries available). I'll write the bulletin using the detailed abstracts provided, which contain specific methods, benchmarks, and results.

# Inference Ecosystem — Flash News
**2026-04-27 · 603 papers scanned**

### [Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation](https://arxiv.org/abs/2604.22312)

NVIDIA ships GVR, an exact Top-K algorithm for sparse-attention decoding that exploits temporal correlation between consecutive decode steps. Integrated directly into TensorRT-LLM's DeepSeek Sparse Attention stack on Blackwell, it achieves 1.88x average speedup over the production radix-select kernel (up to 2.42x per layer) while preserving bit-exact outputs. End-to-end TPOT improves 7.52% at 100K context, with gains scaling at longer sequences. If you're serving DeepSeek-V3.2 on Blackwell, this is already in the stack. Score: 96 (was 95)

### [FASER: Fine-Grained Phase Management for Speculative Decoding in Dynamic LLM Serving](https://arxiv.org/abs/2604.20503)

FASER tackles the rigidity of current speculative decoding systems by introducing per-request speculative length tuning within continuous batches, early pruning of rejected tokens inside verification, and spatial multiplexing to overlap draft and verify phases. Prototyped in vLLM, it delivers up to 53% throughput gain and 1.92x latency reduction over state-of-the-art. This is the most practical spec-decode improvement we've seen — it works with existing draft models and adapts to volatile online traffic patterns. Score: 94 (was 95)

### [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157)

Co-authored by Tri Dao, this paper asks what KV-cache quantization actually survives production serving constraints — paged memory layouts, fused attention, regular memory access. The answer: token-wise INT4 with block-diagonal Hadamard rotation. Their fused rotation-quantization kernel integrates into paged KV-cache with zero measurable end-to-end overhead, matching plain INT4 throughput. More complex methods (vector quantization, Hessian-aware) add marginal gains once you account for serving compatibility. A systems co-design reality check the field needed. Score: 92 (was 95)

### [FairyFuse: Multiplication-Free LLM Inference on CPUs via Fused Ternary Kernels](https://arxiv.org/abs/2604.20913)

FairyFuse eliminates all floating-point multiplications from ternary LLM inference by fusing eight sub-GEMVs into a single AVX-512 loop of masked additions and subtractions. The result: 32.4 tok/s on a single Xeon 8558P, outperforming llama.cpp Q4_K_M by 1.24x with near-lossless quality (WikiText-2 PPL 5.52 vs 5.47 FP16). Roofline analysis shows 16x weight compression shifts memory-bound GEMV toward compute on bandwidth-limited CPUs — a 29.6x kernel speedup. If you're deploying on CPU-only infrastructure, this is the new baseline to beat. Score: 85 (was 95)

### [MCAP: Deployment-Time Layer Profiling for Memory-Constrained LLM Inference](https://arxiv.org/abs/2604.21026)

MCAP uses Monte Carlo activation profiling at load time to estimate per-layer importance, then drives dynamic precision dispatch (W4A8 vs W4A16) and residency tiering (GPU/RAM/SSD) from a single weight set. The NVE runtime achieves 1.5–1.8x decode throughput over llama.cpp Q4_0 on T4 and enables models to run in memory regimes previously infeasible without modifying weights. Interesting approach to making one checkpoint serve many hardware targets. Score: 78 (was 93)

---

## Surge Watch

[Act While Thinking](https://arxiv.org/abs/2603.18897) is the sleeper signal this week. After a full month of absolute zero engagement, it suddenly picked up 3 citations (2 influential) in the last 6 days. Influential citations on a pattern-aware speculative tool execution paper suggest it's being referenced by substantial follow-up work — worth watching whether this becomes a trend or a one-off cluster.

[Accelerating Speculative Decoding with Block Diffusion Draft Trees](https://arxiv.org/abs/2604.12989) continues its quiet dev-community climb: 246→294 GitHub stars (+48 in 6 days), now nearly matching TriAttention's early trajectory. Still only 6 HF upvotes — this is purely implementation-driven interest.

Previous hot signals are cooling as expected. [Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619) went from +69 stars in two days to just +16 over the past six — the surge we flagged is over, settling at 247. [FlashAttention-4](https://arxiv.org/abs/2603.05451) flatlined at 9 citations after its academic acceleration.
