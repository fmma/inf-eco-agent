I've read all 8 PDFs. Here's my rescored assessment and the bulletin.

# Inference Ecosystem — Flash News
**2026-08-21 · 165 papers scanned · 5 featured**

## [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758)
The standout this week. FlashPrefill V2 turns a sparse-prefill prototype into a real attention backend: a mean-correction term holds RULER accuracy within ~1.1 pts of full attention even below 5% density, while an FA3/4-aligned kernel (PackGQA, warp specialization, pingpong, FP8) plus native paged-KV/continuous-batching drops it straight into SGLang. It hits 47.3× (FP8) and 27.2× (BF16) over FlashAttention-2 at 128K — 30.5× over an FA3/4-aligned *dense* baseline — and cuts end-to-end TTFT up to 4.8× with ~2× serving throughput on H20s. If you serve long context, this is the one to integrate now. Score: 96 (was 95)

## [CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving](https://arxiv.org/abs/2608.19677)
A rare at-scale routing result: Llama-3.3-70B fp8 on 60 H100s sustaining 176 QPS at a 3.5s p99 — 2.3× the best of five baselines — via a periodic prefix-affinity table (top-rate admission + LPT placement) that lifts served KV-hit from 64%→93%. What earns the score is the honesty: two 32B workloads where affinity actually *loses*, and a firm rule to gate any deployment with shadow replay instead of trusting an analytic residency model (which missed hit-rate by 14–45 pts). Score: 89 (was 90)

## [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents](https://arxiv.org/abs/2608.19662)
Agentic tool/skill schemas recur in different orders, so standard prefix caching never fires. ReCache's resource-wise attention builds composition-invariant KV blocks (3.66× TTFT), then contribution-guided layer/head-group pruning + field-aware token pruning cut allocated KV memory 92.4% and speed attention 1.42×, keeping 97.5%/91.8% of dense Inv-F1 in/out-of-distribution. Needs light fine-tuning (Qwen3-4B) and the code is out — timely as agent-serving KV costs balloon. Score: 87 (was 90)

## [RequestRouter: Request-Boundary Routing for Efficient Single-GPU LLM Inference](https://arxiv.org/abs/2605.23057)
A pragmatic reminder that you don't need one universal config. A ~5µs rule-based controller picks one mode per request (GPTQ, INT8, spec-decoding, prefix cache, continuous batching, hybrids) on vLLM/A100, landing 2.10× mean latency speedup and 0.48× energy vs FP16 while retaining 99.6% of accuracy. Best part is the negative result: learned routers (tree/forest) never beat the hand rules once you count their 1000×-higher CPU overhead. Score: 84 (was 90)

## [Learning how to Forget: Fine-tuning for Long-Context Sparse Attention](https://arxiv.org/abs/2608.19920)
AWS's answer to why sparse attention stays a research toy: co-adapt the model to its KV-cache policy. Nested checkpointing + delta-encoded KV buffers let you fine-tune a 4B model with H2O sparse attention on a single 40GB A100, and it beats sequence-parallel-trained models — which, run under eviction, fail to stop and emit garbage. Ships the open-source KeysAndValues library with a FlashInfer SDPA kernel that returns summed attention weights (the missing primitive for H2O-style policies). Score: 82 (was 86)

*Just missed the cut: Daedalus-150M (conv-attention hybrid, 1.76–2.08× faster CPU decode, score 80) and HYDRA (chiplet DSE for hybrid Transformer-Mamba serving, 1.55× throughput, score 74 — strong but hardware-architect territory).*

---

## Surge Watch

Nothing noteworthy in signal trends today.
