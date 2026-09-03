I've read all 8 PDFs in full. Here is the bulletin.

# Inference Ecosystem — Flash News
**2026-09-03 · 252 papers scanned · 5 picks**

Long-context sparse attention and speculative decoding dominate today's batch, plus a forward look at where the interconnect bottleneck is heading.

## [Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737)
Declarative Attention (DA) lets an off-the-shelf model declare where to attend via `<global>`/`<focus>`/`<local>` tags in its chain-of-thought; the engine parses them like tool calls and skips most of the KV-cache read, making token selection O(1) instead of the O(N)-per-step scan that proxy-score methods pay. Zero-shot on Gemma-4-31B and Qwen-3.6-27B it cuts decode attended tokens 52%/31% for just 1.27/2.75pp accuracy loss, with a real vLLM integration projecting 0.71×/0.77× decode wall-time. A genuinely new, legible axis of sparse attention that improves with scale — the most conceptually fresh work here. Score: 91 (was 90)

## [CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling](https://arxiv.org/abs/2609.01925)
CRISP swaps FlexPrefill's JSD head-routing for C_struct, a constant-time structural-mass proxy, and formalizes the post-softmax "mass cliff" to prove cumulative-coverage thresholds ingest O(n) background noise at long context — fixed by a calibration-free sink-aware threshold (α=1.0). It Pareto-dominates FlexPrefill: up to 5.30× attention speedup at 512k tokens, matches or beats dense attention on retrieval, and recovers +28.0pp on Qwen passkey. The strongest, most rigorously-motivated long-context prefill optimization in the batch. Score: 91 (was 90)

## [WhiFlash: Token-Level Cross-Paradigm Speculative Decoding](https://arxiv.org/abs/2606.07710)
WhiFlash is the first SD method to route token-by-token between an autoregressive drafter (EAGLE-3) and a diffusion parallel drafter (DFlash), motivated by the finding that the winning paradigm flips wildly within a single sequence. Lazy Catch-up and KV-only Prefill hold switch cost below 7% of per-round latency, delivering up to 69.6% throughput over EAGLE-3 and 37.3% over DFlash — and beating the prompt-level routing oracle that bounds HedgeSpec-style methods. Score: 88 (was 88)

## [Scaling Inference Prefill with High-Radix Photonic Interconnects](https://arxiv.org/abs/2609.01821)
A Lightmatter / HotI-2026 modeling study of when 3D-integrated photonics (4× scale-up bandwidth, radix to 1152 GPUs) pay off for MoE prefill: 2.1–2.9× at 1K–8K tokens, 4.3–5.8× at 128K on rack-limited GPUs, up to 8.5× for long-context configs crossing the scale-up-pod boundary. Refreshingly honest that it's analytical (XLA cost model, no deployed optics) and prefill-centric — its own DES shows decode saturation can swallow the TTFT win unless you co-size the decode pool. Essential context on the coming interconnect wall. Score: 86 (was 90)

## [HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Models](https://arxiv.org/abs/2609.02029)
HeadWiseKV assigns each residual global-attention KV head a static multilevel history window (via prefix-conditioned SeqCalib calibration) and materializes it as real per-head physical residency — not a logical mask over a full cache — so it actually lowers the prefill memory peak. Training-free, it holds near-Full-KV RULER/LoCoMo across four hybrid models (Qwen3.6, Gemma4) while cutting peak VRAM 8.59% at 112K and stretching verified context 114K→161K (1.41×). Score: 85 (was 90)

---

## Surge Watch

Nothing noteworthy in signal trends today.
