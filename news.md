All 7 PDFs read. After reviewing the full texts, I'm rescoring based on actual contribution and deployability for inference engineers (notably: GBV's practical speedups evaporate for modern models at temp 1.0 per its own appendix, and the parallelism paper mostly confirms known trade-offs — both drop out of the top 5).

# Inference Ecosystem — Flash News
**2026-10-06 · 538 papers scanned · top 5 picks**

This week leans hard into long-context KV and speculative decoding — the standout being a drop-in vLLM sparse-decode path that finally stays inside the CUDA graph.

## [MOIRA: Mass-Oriented Indexing with Ragged Attention for Long-Context Decoding](https://arxiv.org/abs/2610.04313)
Training-free sparse decode for vLLM: a coverage rule keeps the fewest KV pages reaching attention-mass fraction γ *per head and per layer*, and a new "self-planning attention" kernel balances the ragged page lists on-GPU so the entire decode step stays captured in the CUDA graph — exactly where FlashInfer's host-side plan breaks. On an H200 at 128k RULER, γ=0.99 matches dense accuracy reading only 27-33% of pages and cuts TPOT 2.2-2.5× vs dense FA3; serving throughput rises 45-51% under load. The rare sparse-attention result that is both accurate and genuinely shippable today. Score: 93 (was 92)

## [MOLT: A Fine-Grained GPU Memory Sharing System for LLM Serving with Opportunistic Fine-Tuning](https://arxiv.org/abs/2610.05748)
Turns the idle memory autoscalers leave behind into PEFT throughput: "continuous memory handover" lets inference reclaim memory from a *running* tuning step one saved activation at a time (recomputed in the backward pass) rather than discarding the whole step, staying safe under CPU-GPU async and tensor parallelism. Across 24B-70B on H100/B200 it holds inference SLO attainment ≥99.7% while completing 1.9-3.3× the tuning work of discard-based SIRIUS. Niche unless you colocate fine-tuning, but a clean fix for real GPU waste. Score: 86 (was 92)

## [SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models](https://arxiv.org/abs/2610.04875)
Multi-branch speculative decoding for diffusion LLMs pays a dense per-forward cost; SpecFold notices draft branches inherit most tokens from their parents (>72% of hidden states barely move), so a token-level residual gate reuses parent attention/FFN and Triton kernels pack only the divergent positions. Up to 1.64× over Spiffy and 1.99× over vanilla across Fast-dLLM-v2 and Nemotron-Labs-Diffusion, accuracy intact. Textbook algorithm-system co-design and a smart bet as DLLM serving matures. Score: 85 (was 90)

## [OVAL: Output-Aware Local Page Bases for KV Cache Retrieval](https://arxiv.org/abs/2610.06686)
Argues key-only page summaries optimize the wrong objective — what matters is how retrieval error propagates through the *values* into the attention output — and builds a page basis mixing key energy with key-value coupling via a single knob η. Training-free, identical decode-time scoring cost to key-only spectral, +3.7-3.9 avg@k on MATH500/AIME24/GPQA and best LongBench v2 on two of three models, at ~10% decode overhead with code released. A principled refinement in the crowded KV-retrieval space. Score: 84 (was 92)

## [From Overloaded to Guaranteed: High-Throughput Multi-SLO Enforcement for LoRA-Assisted On-Premise LLM Deployment](https://arxiv.org/abs/2610.04956)
HALO tackles multi-LoRA serving on constrained on-prem boxes with two levers: spatially multiplexing GPU SMs so base and LoRA layers run concurrently (hiding LoRA overhead), and a "request-level slack" metric that lets relaxed-SLO requests yield decode slots to urgent ones — breaking blind batching. Result: P99 TTFT down 2.1-5.0× and throughput up 19.5-29.5% over SLoRA/VTC/QoServe on Llama3-8B, Yi1.5-34B, and Qwen2.5. The SM-partitioning trick is reusable well beyond LoRA. Score: 83 (was 90)

---

## Surge Watch

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) is the breakout this cycle — the KV-cache-compression tech report rocketed to **224 HF upvotes (191→224 in three days, up from 174 two weeks ago)** while citations compounded **7→35 (09-25→10-04)**. Fastest-moving release on the board right now.

GitHub momentum has rotated to edge-MoE serving: [Serving 35B MoEs from SSD](https://arxiv.org/abs/2609.18063) blew past 3K stars, **2,363→3,085 (10-03→10-06)** — roughly 700 in three days, with HF upvotes ticking 19→22.

On the scholarly side, two heavyweight systems papers are compounding hard: [FlashAttention-4](https://arxiv.org/abs/2603.05451) added citations **58→75 (09-24→10-06, influentials 8→11)** and [Mamba-3](https://arxiv.org/abs/2603.15569) ran **81→99 (influentials 11→17)** over the same window — both now outpacing the quantization names.

Meanwhile [Disaggregated Quantization](https://arxiv.org/abs/2609.26333)'s upvote surge has flattened (**91→92**), marking last cycle's jump as a launch-day pop rather than durable traction.
