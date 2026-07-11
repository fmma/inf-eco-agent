All 8 PDFs read. Writing the bulletin now.

# Inference Ecosystem — Flash News
**2026-07-11 · 683 papers scanned · top 5 picks**

Quantization, disaggregation, and parallel decoding dominate this batch. The through-line: everyone is attacking the KV cache and the memory-bound decode wall from a different angle.

### [Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying AR, Diffusion, and Self-Speculation Decoding](https://arxiv.org/abs/2607.05722)
NVIDIA trains one set of weights that decodes in three modes — AR, diffusion, or self-speculation where diffusion drafts and AR verifies. It beats Eagle3/MTP on acceptance length (5.46/6.82 native/LoRA vs 2.75/4.24), giving the 8B model 6× tokens/forward over Qwen3-8B and 4× throughput on SPEED-Bench with SGLang on GB200 (2.4× over Eagle3 at batch 1). It's a drop-in AR replacement that outperforms today's speculative-decoding default, with the full 3B/8B/14B base/instruct/VLM family already on HF and a SOL analysis showing 76.5% more headroom. Score: 93 (was 90)

### [Lynx: Progressive Speculative Quantization for Accelerating KV Transfer in Long-Context Inference](https://arxiv.org/abs/2607.01831)
Lynx reframes KV-cache transfer in disaggregated serving as speculative decoding at the *network* boundary: it splits the quantized cache into a high-priority 4-bit "Anchor" (MSB) stream and a "Residual" (LSB) stream, starts decoding speculatively the instant the Anchor lands, then losslessly verifies against full precision when the Residual arrives. Using hierarchical log-quantization with outlier-aware chunking, it hits INT4-level TTFT at BF16 accuracy — beating INT8 TTFT by up to 1.43× and CacheGen accuracy by 5.1%, with gains growing at long context and low bandwidth. A genuinely novel way to hide transfer latency behind useful work. Score: 93 (was 92)

### [FPTQuant: Function-Preserving Transforms for LLM Quantization](https://arxiv.org/abs/2506.04985)
Qualcomm adds three cheap, mergeable transforms (pre-RoPE Q/K rotation, per-head value transform, pseudodynamic per-token residual scaler) that shape activations for quantization with no custom kernels and near-zero inference overhead. Crucially it targets *static* INT4 — what real accelerators actually support, unlike the dynamic quant most papers assume — hitting up to 3.9× prefill speedup over FP16 and running 15–29% faster than FlatQuant at comparable accuracy. On par or better than QuaRot/SpinQuant across Llama-2/3, Ministral, and Qwen. Score: 90 (was 92)

### [SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565)
First scheduling study on real agentic-serving traces (Alibaba BAILIAN), where KV reuse exceeds 80% vs 54–62% in chat. The insight: cache-aware routers pin whole sessions onto a few hot instances, so balancing only each session's *first* request restores load balance without losing local reuse — via a stateless turn-number hint inferred from the request itself. On vLLM+LMCache it lifts cluster TPS 10–16% (colocation) and prefill TPS 2–34% (disaggregation) with lower TTFT/TPOT. Score: 90 (was 92)

### [Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving](https://arxiv.org/abs/2607.02043)
Microsoft shows prefill *compute* is only 2–23% of P95 TTFT in a 2P2D cluster — the rest is queuing and inter-node KV transfer. Kairos proactively deflects prefill onto idle decode nodes as chunked-prefill steps, using a sub-1ms analytical model (MAPE <10%) to pick the largest chunk schedule that keeps in-flight decodes within TBT SLO, and eliminates KV transfer entirely for deflected requests. On vLLM+DeepSeek-V2-Lite it cuts P95 TTFT up to 81% and raises SLO attainment up to 79% under bursty load. Score: 88 (was 90)

---

## Surge Watch

[DFlash](https://arxiv.org/abs/2602.06036) is the cycle's academic runaway: citations nearly doubled 21 → 45 and influential cites leapt 8 → 20 since late May, with stars now past 5,400. Block-diffusion speculative decoding is landing in follow-up work, not just demos — and [Block Diffusion Draft Trees](https://arxiv.org/abs/2604.12989) is compounding right alongside it (7 → 10 citations this week and its first 2 influential cites, on just 8 HF upvotes). Diffusion-based drafting is turning into a genuine research thread.

New face worth watching: [FlashMemory-DeepSeek-V4](https://arxiv.org/abs/2606.09079), the DeepSeek-V4-branded lookahead sparse-attention paper, has climbed to 65 HF upvotes and 88 stars since its mid-June debut.

Meanwhile last cycle's star magnets have cooled: [KVarN](https://arxiv.org/abs/2606.03458) (67 upvotes / 434 stars), [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) (150 / 372), and [Domino](https://arxiv.org/abs/2605.29707) (152 upvotes, 114 stars) have all plateaued at last week's levels — social buzz settling into steady maturity.
