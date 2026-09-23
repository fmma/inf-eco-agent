I've read all 8 PDFs in full. Here's my rescore and bulletin — the top 5 by full-text relevance are Weave, DeepSeek-V4.1-Flash, SSD-LLaMA, ASPIRE, and OpWeave. The Pareto Atlas (single model/workload, simulated sparse attention) and JustFit (single-author, niche MLX, weak baseline) rescored below them; Token Latency Fairness is strong conceptually but self-describes as an ongoing project with limited eval.

# Inference Ecosystem — Flash News
**2026-09-23 · 898 papers scanned · top 5 featured**

MoE serving and KV-cache compression own this batch — the through-line is squeezing more usable context and throughput from fixed silicon, from H100 clusters down to consumer laptops.

## [Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel](https://arxiv.org/abs/2609.21483)
Weave decides the communication/computation SM split *per layer and per GPU* from runtime routing results via a cost model living inside a persistent megakernel, then adds chunk-pipelining and "bubble stealing" so idle comm SMs grab GEMM tiles. On 4×H100 across six MoE models it lands 2.89× geomean MoE-layer and 1.33× end-to-end speedup over DeepEP/Comet/TD, reaching 91% SM-active at 47% overlap where baselines sit below 15% — for 0.54μs of overhead (<0.021% of layer time). This is the current state of the art for expert-parallel overlap. Score: 95 (was 96).

## [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)
This 552B MoE fuses a Causal Encoder-Decoder (8B activated at prefill, 16B at decode), cross-layer KV reuse in CSA2, and FP4 main KV to shrink the global cache to 890 bytes/token (~1/4 of V4-Flash), while SWA Bounded Replay cuts persistent KV to ~1/8. Decode FLOPs stay near-flat from 4K→1M context and Reuse-mode layers run in just 15 prefill / 11 decode kernels. Open checkpoints, agentic parity with Opus-5/GPT-5.6 (DeepSWE 74.2, Terminal-Bench 2.1 90.6), plus a full deployment playbook (EPD disaggregation, FlashMLA/DeepGEMM) make it required reading. Score: 95 (was 95).

## [SSD-LLaMA: SSD-Native Inference for Trillion-Parameter MoE](https://arxiv.org/abs/2609.18110)
SSD-LLaMA turns NVMe into executable model memory via an expert-pack layout (one aligned O_DIRECT read per expert), a three-tier SSD/RAM/VRAM cache, CUDA rANS decompression, and expert-level CPU-GPU balancing — hitting 77.7% of peak SSD bandwidth vs 43% for baselines. It runs the 1T Kimi-K2.7-Code at 1+ tok/s and the 2.8T Kimi-K3 at 0.465 tok/s decode on a single RTX 5090 with 32GB RAM, improving decode 2.10–15.58× over llama.cpp/KTransformers. Built in llama.cpp, it makes frontier-scale local MoE genuinely usable. Score: 93 (was 95).

## [ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context](https://arxiv.org/abs/2609.17943)
ASPIRE breaks synchronized draft-verify: a unified mixed forward lets some requests draft (sparse attention) while others verify (full attention) in one pass, an online scheduler picks per-request draft length from acceptance-rate + batch-aware cost, and a single refresh layer keeps sparse context fresh (closing a 16pp acceptance gap at draft length 10). Across Qwen3 and DS-LLaMA it delivers 1.70–4.58× decode throughput over autoregressive and ~27% over MagicDec/Vegas — losslessly. COLM 2026, code released. Score: 92 (was 95).

## [OpWeave: Flexible Operator Disaggregation for Heterogeneous LLM Serving](https://arxiv.org/abs/2609.14237)
OpWeave (CMU) generalizes attention-FFN disaggregation to arbitrary operator partitions, pairing an analytical cost model that bounds the gains with a regularity-aware planner over a vLLM runtime. It cuts serving cost up to 1.78× on homogeneous H100 and 1.89× on H100+A100, using 20.7 vs 124 pipeline stages and 22.8× less inter-node transfer — decisive for hybrid-attention models (Gemma-3, Qwen3-Next) where fixed two-way splits stall. Score: 91 (was 95).

---

## Surge Watch

Speculative-decoding-over-diffusion stays the hottest citation line in the set. [DFlash](https://arxiv.org/abs/2602.06036) keeps compounding — 93→95 citations with influential jumping 33→35, and its long-frozen HF upvotes finally unstuck (95→99). It's now corroborated by [DSpark](https://arxiv.org/abs/2607.05147) (confidence-scheduled semi-autoregressive speculative decoding), which ran 22→30 citations in ~2 weeks (9 influential) — the fastest young accretor in the set.

On the systems side, [FlashAttention-4](https://arxiv.org/abs/2603.05451) is accreting steadily: 50→57 citations in ~2 weeks, 8 influential — healthy pace for a marquee kernel paper.

Serving/workload papers crossed 50 in tandem: [ServeGen](https://arxiv.org/abs/2505.09999) (46→52) and [Continuum](https://arxiv.org/abs/2511.02230) (48→52, KV-cache TTL for agents) — production-serving citations quietly ticking up.

Community upvotes stayed flat again — a citations-driven cycle with no fresh HF surge to report.
