I've read all 8 PDFs in full. Here is the rescored flash-news bulletin.

# Inference Ecosystem — Flash News
**2026-08-20 · 164 papers scanned · top 5 featured**

### [Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets](https://arxiv.org/abs/2608.19147)
Turns idle office Intel AI PCs into a serving cluster: models are split by layer into pre-compiled INT4 OpenVINO shards, glued together by three composable tricks — a `beam_idx` Gather injection that unlocks the GPU plugin's IndirectKVCache fusion (recovering ~15% to reach monolithic parity), mask-based KV rewind that makes speculative decoding pay off on stateful OpenVINO without the ~48ms physical-trim cost, and cross-stream micro-batching. A two-node Llama 3.1 8B pipeline serves two users at 43.97 tok/s (1.79× single-node monolithic), stays interactive at ~4× naïve under 100ms/hop WAN, and scales to a 70B model no single node can hold — all bit-exact, with code and repro scripts. Score: 90 (was 90)

### [S2-MoE: Efficient Self-Speculative Decoding for MoE on Edge Devices](https://arxiv.org/abs/2608.15018)
Makes speculative decoding and MoE cooperate — normally a bad pairing because rejected drafts trigger disjoint expert activations — via routing-aware adaptive expansion, reuse-aware expert gating, and a context-aligned KV cache shared between draft and target. Training-free and built into llama.cpp, it reaches up to 5.3× (2.0× avg) over autoregressive decoding on Jetson Orin and consistently beats EAGLE-3 and Cascade across DeepSeek, OLMoE, Qwen3, and GPT-OSS under tight memory budgets. Its verification-cost model tracks measured latency at R²=0.94–0.99 and quality stays within ~1% PPL. Score: 90 (was 90)

### [FlashAttention for Scalable Vector Architectures](https://arxiv.org/abs/2608.18656)
FlashAttention-V rewrites the ggml/llama.cpp attention kernel for long-vector CPUs (RISC-V RVV, Arm SVE) using inter-head packing to exploit vector lengths beyond the head dimension, where existing kernels stall at VL≤D. Simulated prefill speedups hit 22–42× over *scalar* FlashAttention (12–14× confirmed on real Banana Pi BPI-F3 silicon), though gains over the existing *vectorized* FP16 kernel are a more modest 1.2–2× and end-to-end wins are small. The sharp practitioner takeaway: Q8_0's interleaved weight-scale layout structurally blocks long-vector scaling, burning 60% of cycles on packing/reduction. Score: 87 (was 92)

### [Cacheable by Design? Training MoE Routers for Locality Against the Edge Memory-Bandwidth Wall](https://arxiv.org/abs/2608.18261)
A rigorous measurement study of the MoE bandwidth wall: Qwen3-235B on an 8GB GPU decodes at 0.44 tok/s (matching bytes/token ÷ SSD bandwidth), naïve batching collapses at batch 32 from paging thrash, and the released `llama-moe-trace` tool measures 2.0× adjacent-token expert reuse — an LRU cache of just 13.4% of experts serves 66% of requests. The headline is an honest pre-registered negative result (training routers for locality fails a strict ≤1% perplexity gate at 137M scale), but the actionable win is that training-free cache-aware rerouting *stacks* with trained locality to cut ~80% of misses at ≤3.4% PPL. Score: 83 (was 88)

### [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference](https://arxiv.org/abs/2608.18578)
A deployment warning aggregate benchmarks miss: INT4/NF4 disproportionately degrades retrieval of repeatedly-overwritten values (Qwen 81.0%→68.3% at high interference), an effect specific to semantically similar distractors that *reverses sign* on numeric controls — ruling out generic noise. It's mechanistically a rise in same-key intrusions (21.5%→24.6%), localized to the quantized backbone rather than `lm_head`, and even INT8 carries a smaller-but-real penalty in 2 of 3 models. If you serve 4-bit models over long, updatable, semantically dense state (assistants tracking evolving user preferences), this is a genuine hidden cost. Score: 77 (was 72)

---

## Surge Watch

[FreeToken](https://arxiv.org/abs/2608.16157) is the new breakout — HF upvotes **more than doubled overnight, 26 → 61 (08-19 → 08-20)**, with a GitHub repo surfacing at 67 stars on day one. Edge-native MoE serving clearly hit a nerve; watch this one.

Last week's rocket [LLMRouter](https://arxiv.org/abs/2608.06867) has cooled: upvotes flatlined at **106** (08-19 → 08-20) while stars only crept to 2,390. The cold-start surge has plateaued.

Smaller early spike to track: [Dynamic Multi-Byte Prediction](https://arxiv.org/abs/2608.15454) jumped **2 → 13 HF upvotes in a day**.

On the academic side, block-diffusion speculative decoding keeps compounding — [DFlash](https://arxiv.org/abs/2602.06036) crossed **70 citations (67 → 70, influential 24 → 25)** and [DSpark](https://arxiv.org/abs/2607.05147) ticked **14 → 16** since 08-18. Newcomer [MEMENTO](https://arxiv.org/abs/2604.09852) also popped **7 → 10 citations** this week — context-management for agents finding an audience.
