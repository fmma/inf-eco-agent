I've read all 8 PDFs in full. Here's the flash-news bulletin based on my full-text rescoring:

# Inference Ecosystem — Flash News
2026-08-18 · 286 papers scanned · top 5

### [FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://arxiv.org/abs/2608.16157)
The week's standout. FreeToken co-designs the whole local-serving stack around a closed-form q\* policy that splits each decode step's expert cache-misses between PCIe cache-fills and in-place CPU execution, sized from two bandwidths profiled on the actual machine — all kept inside a static CUDA graph. It serves a 35B model at 39.3 tok/s on an 8GB RTX 4060 laptop (beating Codex's 33 tok/s median), a 284B DeepSeek-V4-Flash on a gaming desktop, and 753B GLM-5.2 on one RTX PRO 6000 at 2× llama.cpp — 1.5–2.3× decode over KTransformers/Ollama with worst-case TTFT under 44s where every baseline blows past 150s. If you serve agents locally, read this today. Score: 94 (was 92)

### [GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems](https://arxiv.org/abs/2608.15584)
Production engines page the whole KV cache at one granularity; GraniKV splits it — a contiguous HOT pool for the shared prefix (which finally makes a fat-GEMM HydraGen-style backend usable in a real engine) and a token-level COLD pool for suffixes, with a per-step dispatcher picking dense vs. cascade attention by effective batch size. On SGLang it hits 2.16×/1.98×/1.57× output throughput at 16K shared prefixes across Llama-3.1-8B/Qwen-2.5-14B/32B, and crucially sustains 1.95× under heterogeneous multi-prefix load where batch-global cascade collapses to parity. Directly targets the Claude-Code/RAG shared-prefix pattern that now dominates production. Score: 90 (was 90)

### [FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference](https://arxiv.org/abs/2608.15602)
Binary-quant papers usually dequantize back to FP16 and forfeit the speedup; FluxBin actually cashes it in via a multiplication-free LUT kernel (scale-fusion + Virtual Columnar Mapping to densify salient columns). Its training-free PTQ — decoupled row/column binary bases plus Hessian-guided hybrid precision — lands ~2.6 effective bits at accuracy on par with fine-tuned QuIP#, for 5.92× speedup, 10.19× energy savings, and 70B on a single A100. The decode-only gain (6.3×) even holds at large batch, since LUT reduction is batch-independent. Score: 91 (was 90)

### [FlashQuant: Sparse-Dense Fusion for Outlier-Aware LLM Inference](https://arxiv.org/abs/2608.15531)
Outlier-aware W4A16 splits into a dense low-bit GEMM and a sparse high-precision SpMM that existing stacks run as two kernels, re-reading activations from HBM twice. FlashQuant fuses them into one kernel with shared sparse-dense tiling, a Tile-COO outlier format, and pipelined scheduling — 2.74–4.18× over cuBLAS BF16 and up to 1.53× over the strongest unfused Marlin+Sputnik baseline across RTX 3090/4090/5090, cutting outlier memory traffic ~45%. A clean, portable win for anyone running outlier-preserving quantized decode. Score: 88 (was 90)

### [Global Simulation-Guided Dynamic Operator Scheduling for Multi-Tenant Serving](https://arxiv.org/abs/2608.15762)
Container-granularity scheduling strands second-scale idle GPU slices; SliceScheduler drops to operator (layer) granularity, exposing a cluster-wide Global Mapping Graph and a fast what-if simulator (~177 ops/ms, ~10⁴× faster than SimAI) to slot low-priority work into those gaps without OOM or SLA breaches. Production-trace replay shows 1.10–2.29× token throughput and ~9% better SLO attainment at effectively zero runtime overhead (0.0% vs. direct execution). Practical for MaaS operators squeezing utilization out of co-located tenants. Score: 86 (was 92)

---

## Surge Watch

Nothing noteworthy in signal trends today.
