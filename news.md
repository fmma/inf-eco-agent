# Inference Ecosystem — Flash News
**2026-08-28 · 337 papers scanned · 5 picks**

## [Pushing the Envelope of LLM Inference with Ultra-Low-Bit Quantized Models](https://arxiv.org/abs/2508.06753)
Intel ships close-to-roofline 2-bit GEMM microkernels for AVX2 CPUs and Intel Xe2 GPUs, using a VNNI4-interleaved weight layout and fused quantize/dequantize on GPU. Integrated into PyTorch-TPP (CPU) and vLLM (GPU): up to 7× over BF16 and 2.2× over bitnet.cpp on CPU, 6.7× on Xe2, and a production ternary 27B model runs at ~48 tok/s on a client GPU. The lesson is that the *runtime kernels*, not just the quantized weights, are what actually unlock ultra-low-bit — and these land in frameworks you already run. Score: 93 (was 95)

## [Scorpio: Serving Right Requests at the Right Time for Heterogeneous SLOs](https://arxiv.org/abs/2505.23022)
An SLO-aware scheduling layer on vLLM that treats heterogeneous TTFT/TPOT targets as a resource: a TTFT Guard (least-deadline-first + reject-the-unattainable) plus a TPOT Guard (credit-based batching + virtual-batch-size admission control). Up to 14.4× goodput and +46.5% SLO adherence under high load vs vLLM/Mooncake/S3, at <1% scheduling overhead. Drop-in scheduling that converts loose-SLO slack into headroom for tight-SLO requests — immediately useful for multi-tenant serving. Score: 91 (was 95)

## [FLINT: Efficiently Leveraging High Bandwidth Flash for Capacity-Scalable LLM Inference](https://arxiv.org/abs/2608.25062)
Onur Mutlu's group attacks the memory-capacity wall with a workload-driven high-bandwidth-flash substrate: a hardware burst-buffer controller (no SRAM staging buffer or compiler prefetch hints), off-path "phantom-plane" refresh, and a compact read-only FTL. In simulation across DeepSeek-V3/V4, Kimi-K2 and Llama, it delivers 2.2× decode throughput over HBM-only and hits a 50ms TPOT SLO with 3.1× fewer GPU packages. Not deployable today, but the clearest blueprint yet for serving trillion-param models from a single accelerator once HBF arrives. Score: 90 (was 97)

## [Launch-Bound and Substitutable: Why Three Inference Optimizations Fail in MoE Models](https://arxiv.org/abs/2608.26612)
A rigorous myth-buster on OLMoE, DeepSeek-V2-Lite and Qwen3-30B. Fused Triton kernels hit 5.6–9× in isolation but 0.999× end-to-end — the model is launch-bound (~1000 kernel launches/forward pass, not arithmetic); INT4's quality loss is 97.3% weight error and only 2.7% routing drift (experts are substitutable, proven by causal route-replay); and removing all torch.compile graph breaks makes the model 3× slower. Redirects MoE optimization to the real lever — batching the expert dispatch — and warns off two popular dead ends. Score: 88 (was 88)

## [RADAR: Accelerate LLM Inference With RL-Based Dynamic Draft Trees](https://arxiv.org/abs/2512.14069)
Speculative decoding with an offline-RL LSTM that decides per-step whether to keep calling the draft model, so tree depth adapts to context instead of a fixed 8 calls. Layered on EAGLE-3 it reaches 3.17–4.82× over autoregressive decoding (3–12.9% over EAGLE-3) while cutting draft-model calls 18.7%, lossless, with code released. A lightweight add-on to the EAGLE-3 stack many teams already deploy. Score: 86 (was 92)

---

## Surge Watch

The HuggingFace board finally has a breakout, and it's a correction to last cycle's own call.

**Reversal of last cycle's "settled, no fresh movement" verdict on [FreeToken](https://arxiv.org/abs/2608.16157) — it just went vertical.** HF upvotes climbed **61 → 99 in eight days** (Aug 20 → 28), now at the doorstep of 100, while its GitHub repo rocketed from **67 stars on Aug 20 to 8,823 on Aug 28 — +1,519 in the last two days alone**. Bandwidth-adaptive edge-MoE serving is abruptly the hottest repo on the board.

On the citation ledger, [MEMENTO](https://arxiv.org/abs/2604.09852) is the new quiet climber: **7 → 12 citations in eight days** (influential 1 → 3, Aug 18 → 26) after a month stuck at 6–7 — self-managed context is gaining academic traction even with HF upvotes flat at 1.

Last cycle's movers have cooled: [DFlash](https://arxiv.org/abs/2602.06036) (74 cites / 5,968 stars) and [dLLM-Cache](https://arxiv.org/abs/2506.06295) (160 cites) are both flat since the last report, and no other HuggingFace launch cleared the bar this cycle.
