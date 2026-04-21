# Inference Ecosystem — Flash News
**2026-04-21 | 573 papers scanned**

### [Neural Garbage Collection: Learning to Forget while Learning to Reason](https://arxiv.org/abs/2604.18002v1)

Stanford's Li, Hamid, Fox, and Goodman introduce a paradigm shift: instead of hand-designed KV cache eviction heuristics, let the model *learn* what to forget via reinforcement learning. NGC treats cache eviction as a discrete action (sampled via Gumbel-top-k) alongside token generation, optimized end-to-end from task reward alone — no proxy objectives, no teacher models. On Countdown it more than doubles the next-best baseline (49.6% vs 21.2% at 2.4x cache reduction); on AIME 2025 it hits 21.4% pass@32 at 4.6x compression where SnapKV manages 10.7%. The "budget-aware interoception" trick — conditioning the prompt on eviction rate — enables generalization to unseen cache budgets. This is the paper to watch if you believe efficiency should be a learned capability, not an engineered one.
Score: 95 (was 93)

### [Open-TQ-Metal: Fused Compressed-Domain Attention for Long-Context LLM Inference on Apple Silicon](https://arxiv.org/abs/2604.16957v1)

A solo developer just made Llama 3.1 70B at 128K context run on a single 64 GB Mac — something every existing framework (mlx-lm, llama.cpp, Ollama) cannot do. The trick: a custom Metal compute shader that reads packed int4 KV cache directly, dequantizes in GPU registers via bitwise ops, and computes attention with online softmax in a single pass — zero intermediate matrices. The fused `sdpa_int4` kernel achieves 48x attention speedup at 128K context over dequantize-then-attend. Across 330 experiments, the paper also reveals that the attention scale factor (not model size) determines whether angular quantization like PolarQuant works: Gemma 4's `attn_scale=1.0` amplifies directional error 25-100x vs Llama's standard 1/sqrt(d), and QJL's 0.85 per-layer correlation collapses to ~0 after 80 layers at 70B scale.
Score: 93 (was 95)

### [HieraSparse: Hierarchical Semi-Structured Sparse KV Attention](https://arxiv.org/abs/2604.16864v1)

First system to leverage GPU sparse tensor cores (NVIDIA Ampere/Hopper `mma.sp` instructions) for KV cache attention acceleration in both prefill and decode. The Trans-Both kernel design transposes both GEMMs to make K and V^T the sparse operands, enabling theoretical 2x speedup on both phases. At 50% sparsity, HieraSparse achieves 4.57x attention speedup over MUSTAFAR's unstructured approach and 1.2x better compression ratio at the same sparsity level. The `movmatrix`-based in-register re-layout between GEMMs avoids shared-memory overhead. End-to-end on Llama-3.1-8B at 128K context: 1.41x TTFT reduction and 1.54x TPOT reduction. Code released at GitHub.
Score: 90 (was 95)

### [Neural Garbage Collection (NGC)](https://arxiv.org/abs/2604.18002v1) already covered above.

### [River-LLM: Large Language Model Seamless Exit Based on KV Share](https://arxiv.org/abs/2604.18396v1)

Early exit in decoder-only LLMs has a dirty secret: the KV Cache Absence problem means skipped layers leave holes for subsequent tokens, and existing fixes (recompute, masking, state propagation) eat your speedup. River-LLM solves this with a "KV-Shared Exit River" — lightweight W4A16-quantized copies of backbone layers that share the same KV cache address space. When a token exits early, it traverses the quantized exit layers that naturally fill in the missing KV entries at 2.4x throughput. The exit decision uses state transition similarity (input-output cosine similarity) which correlates with cumulative quantization error. Training-free, 1.71-2.16x wall-clock speedup across Llama 3.2 1B / 3.1 8B / Phi4-mini / Ministral3 8B on GSM8K, MATH, and HumanEval, with memory footprint approaching full quantization.
Score: 88 (was 92)

### [HybridGen: Efficient LLM Generative Inference via CPU-GPU Hybrid Computing](https://arxiv.org/abs/2604.18529v1)

For long-context inference where KV caches overflow GPU memory, HybridGen parallelizes attention across CPU and GPU — each processor computes on KV tokens in its local memory. The key enabler: decoupling attention logit computation (Q*K^T is independent across tokens) from softmax/value aggregation, plus exploiting consecutive-layer input similarity (cosine sim >0.9 after layer 1) to let the CPU proactively compute next-layer logits while the GPU finishes the current layer. A feedback scheduler dynamically adjusts how many tokens the CPU processes based on runtime latency. With CXL-expanded memory and semantic-aware KV mapping (keys in fast DRAM, values in CXL), HybridGen outperforms FlexGen, InfiniGen, and four other baselines by 1.41-3.2x across OPT/Llama/Qwen on three GPU platforms.
Score: 88 (was 95)

---

## Surge Watch

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619) — the overnight spike we flagged yesterday wasn't a one-off. Stars surged again from 193 to 231 (+38 in 24h) after being flat at 162 for over a week. That's +69 stars in two days — something (likely a major integration or implementation push) is actively driving GitHub traffic. HF engagement remains flat at 80, so this is purely dev-community driven.

[FlashAttention-4](https://arxiv.org/abs/2603.05451) is accelerating in the academic graph: 5→9 citations in the past week, with 2 new in the last 3 days. It's becoming a standard reference in the attention optimization literature. Still just 1 HF upvote and zero GitHub stars after 7 weeks — the researcher/practitioner gap is widening, not closing.

Everything else is steady-state. TriAttention's initial explosion has fully cooled (+1 HF, +8 stars since yesterday). Nemotron 3 Super is still climbing (now 36 HF) but decelerating.
