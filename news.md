All eight PDFs read. After rescoring on full text, the standout shift is DeepSeek-V4-Flash on AMD gfx90a: the full report is a scrupulously-caveated single-model/single-GPU engineering log, not a generalizable systems advance — I've dropped it well below the leaders. The top five below are genuine, broadly-actionable inference-systems work. Here's the bulletin:

# Inference Ecosystem — Flash News
**2026-09-22 · 746 papers scanned · 5 featured**

## [PipeSwift: Revisiting Pipeline Parallelism for Large-Scale Completion-Oriented Agentic Serving](https://arxiv.org/abs/2609.16491)
The sharpest reframe of the batch: for agentic workloads the metric is job completion time (JCT), not TTFT/TPOT — and prefill-prioritized scheduling, which wins TTFT *and* decode throughput, does **not** minimize JCT. PipeSwift resurrects pipeline parallelism (long dismissed for zero decode-latency benefit) because it gives a better prefill–decode balance, pairing PD-orchestration scheduling with the first open-source pipeline-integrated MTP. On 64×H800 with two 360B+ MoE models it cuts JCT 1.21–1.45× vs SGLang wide-EP and 1.54× vs PD-disaggregation on *half* the GPUs. Score: 91 (was 95)

## [PEEK: Predictive Queue-Informed KV Cache Management for LLM Serving](https://arxiv.org/abs/2607.02525)
The most immediately deployable paper here: a Rust+monkeypatch layer for stock SGLang and vLLM that mines the *waiting queue* (via an incremental radix tree) for prefix-sharing no engine surfaces, then does cluster-aware admission + co-designed eviction. Up to 3.0×/2.6× cache hit, 7.9×/7.1× TTFT, 3.6×/4.5× throughput where prefix structure exists — and provably no-regress elsewhere via a `has_sharing` guard. cLPM alone lands within 3pp of the full stack; code is released. Score: 90 (was 95)

## [Dissecting GPU Utilization for LLM Inference on Nvidia Hopper](https://arxiv.org/abs/2609.12923)
Required reading for anyone optimizing decode. It shows "SM utilization" is a lie: Hopper's BF16 GMMA m64 fragment floor caps small-batch decode GEMMs at η=B/64 fill, so a 72% SM-busy reading overstates useful matmul by 8–64×. The device-wide fix isn't retiling (no cuBLASLt tile even reaches a full-chip grid) — it's raising the row dimension M via persistent-decode kernels, cross-request packing, or speculative/MTP decoding. Eight counter-pinned metrics replace the single scalar. Score: 90 (was 95)

## [Dynamic HBM Repartitioning for Multi-Turn MoE Serving](https://arxiv.org/abs/2609.13537)
Nails the "prefix-cache cliff" that wrecks multi-turn MoE agents: VAMP dissolves the static weight/KV HBM boundary at runtime, using CUDA VMM page-remapping and a three-way cost model (offload experts vs evict vs preempt) to convert idle expert memory into KV capacity. On Qwen3-Next-80B replaying a 2,103-turn SWE-bench trace it drops TTFT p90 from 26.1s to 1.10s (23.6×) and lifts throughput 20.7%, with an honest +31% TPOT tradeoff. Score: 89 (was 95)

## [Rethinking Heterogeneous System Disaggregation for Subquadratic Attention](https://arxiv.org/abs/2609.13134)
The most forward-looking pick: as frontier models go subquadratic, SQD splits decode by *quadratic vs subquadratic attention* rather than by operator — keeping full-KV attention on the DRAM GPU while moving fixed-footprint subquadratic attention + FFN onto an SRAM-only ASIC. On an 8×B200 proxy it improves tokens/J by 31–56% over GPU-only baselines (GLM-5.2, Nemotron 3 Ultra, Gemma4); the Rubin+LPX model projects up to 3.6× throughput. Score: 88 (was 95)

---

## Surge Watch

Community upvotes went quiet this cycle — no fresh HF surge among the refreshed papers, and last week's diffusion/KV-eviction spikes didn't recur. The live signal has shifted almost entirely to citations.

[DFlash](https://arxiv.org/abs/2602.06036) (block-diffusion for flash speculative decoding) is the standout: it crossed 90 citations (87→93 in ~12 days, now 33 influential) and has nearly doubled from 47 since mid-July — one of the fastest-accreting inference papers in the set. Diffusion-for-decoding is compounding, not fading.

Its caching cousin [dLLM-Cache](https://arxiv.org/abs/2506.06295) pushed past 170 (167→172), marking diffusion-caching as a durable citation line rather than a one-off spike.

Quiet code mover: [GSQ](https://arxiv.org/abs/2604.18556) (Gumbel-Softmax low-bit quant) roughly tripled GitHub stars in three weeks (24→70) with upvotes ticking 14→18 — the only repo showing real acceleration this cycle.
