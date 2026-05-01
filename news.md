I have detailed abstracts for all 20 candidate papers. The PDF extraction tools aren't available on this system (no poppler-utils, and python commands need approval), but the abstracts contain sufficient technical detail — method names, speedups, benchmarks — to rescore and write the bulletin. Let me proceed.

# Inference Ecosystem — Flash News
**2026-05-01** | 538 papers scanned

---

### [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157)

Tri Dao is a co-author, and the message is simple: under real paged-memory serving constraints, token-wise INT4 quantization with block-diagonal Hadamard rotation is all you need. They show that fancier methods (vector quantization, Hessian-aware) give marginal gains once you enforce paged KV-cache layouts, fused attention, and regular memory access. Their fused rotation-quantization kernel integrates into paged KV-cache with zero measurable end-to-end overhead — matching plain INT4 throughput across concurrency levels. This is the kind of systems co-design paper that actually changes what gets deployed.
**Score: 95 (was 95)**

### [Scaling Multi-Node MoE Inference Using Expert Activation Patterns](https://arxiv.org/abs/2604.23150)

Georgia Tech + Meta profile Llama 4 Maverick, DeepSeek V3-671B, and Qwen3-230B with 100k+ real expert activation traces and uncover persistent patterns: variable load imbalance, domain-specific expert popularity shifts (code vs. math vs. chat), and strong prefill-decode activation correlation. Their workload-aware micro-batch grouping and expert placement strategy reduces inter-node all-to-all communication by up to 20x, directly cutting MoE decode latency. If you're serving any frontier MoE model across multiple nodes, this is the paper to read.
**Score: 93 (was 95)**

### [Super Apriel: One Checkpoint, Many Speeds](https://arxiv.org/abs/2604.19877)

ServiceNow's SLAM Labs release a 15B supernet where every decoder layer has four trained mixer choices — Full Attention, Sliding Window, Kimi Delta Attention, and Gated DeltaNet. You switch presets between requests at serving time without reloading weights, spanning 2.9x to 10.7x decode throughput at 96% to 77% quality retention. The all-FA preset matches the teacher on all benchmarks. The single-checkpoint design also enables speculative decoding without a separate draft model. Open weights, vLLM serving code, and placement optimizer released.
**Score: 90 (was 88)**

### [FairyFuse: Multiplication-Free LLM Inference on CPUs via Fused Ternary Kernels](https://arxiv.org/abs/2604.20913)

Achieves 32.4 tokens/s on a single Intel Xeon 8558P by fusing ternary weight operations into a single AVX-512 loop — zero floating-point multiplications. Outperforms llama.cpp Q4_K_M by 1.24x with near-lossless quality (WikiText-2 PPL 5.52 vs 5.47 FP16). Roofline analysis confirms the 16x weight compression shifts memory-bound GEMV toward compute on bandwidth-limited CPUs, yielding a 29.6x kernel speedup. Ternary models remain niche, but this proves CPU-only inference has legs.
**Score: 85 (was 95)**

### [Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs](https://arxiv.org/abs/2604.18788)

NPUMoE tackles the three things that make MoE hostile to NPUs: dynamic expert routing, irregular operators, and small-kernel dispatch overhead. It uses offline-calibrated expert capacity/popularity to drive static tiering, grouped expert execution, and load-aware graph residency. On M-series devices across three MoE models and four long-context workloads: 1.3–5.6x latency reduction, 1.8–7.4x energy efficiency gains, and 1.8–5.5x CPU-cycle savings. First serious effort at offloading MoE prefill to Apple's ANE.
**Score: 85 (was 92)**

---

## Surge Watch

Nothing noteworthy in signal trends today.
