I've read all 8 PDFs in full. Based on the complete texts, here's my rescoring and the bulletin. Key adjustments: FFD and GLANCE hold up as top-tier (novel, GPU-real, code/deployed); the ASIC/IMC hardware papers (HBQ, LEAP) and simulator-based DynaNDE drop since they're less directly actionable; SemanticSpec drops because its "semantic acceptance" is lossy; mzCache and AInfer-PD stay strong on real-hardware practicality.

# Inference Ecosystem — Flash News
**2026-09-02 · 388 papers scanned · 5 picks**

### [Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding](https://arxiv.org/abs/2609.00097)
FFD fuses the sparse-attention selector and computer into one Triton kernel, scanning a 2-bit quantized K-cache thumbnail and filtering blocks with a new **top-δ** rule — a relative threshold off a sink/local pseudo-max that buys top-p's adaptivity at top-k's cost. Training-free and plug-and-play, it lands up to 11.6× kernel speedup and 2.37× end-to-end throughput at 256K context, beating Quest/KIVI/Twilight while *matching or exceeding* dense accuracy on RULER (89.4 vs 90.6) and LongBench (26.35 vs 26.22). The long-context decode win of the batch: real 4090+H100 numbers, code released, and a genuinely new selection primitive. Score: 93 (was 92)

### [Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in VLMs](https://arxiv.org/abs/2609.00355)
GLANCE bolts a block-diffusion head onto a frozen Qwen3-VL that reads the target's already-fused vision-language state and drafts a whole block in *one* forward pass — vision costs the drafter nothing — then verifies a wide tree in a single target pass, bitwise-identical to greedy. On grounded tasks (ChartQA/DocVQA) it decodes up to 2.93× faster than autoregression from one draft pass where production EAGLE3-VL needs eight, accepting 2.7× longer blocks. Lossless + one-pass + a clean "grounded is more draftable" entropy law, already running in SGLang — the VLM spec-decoding paper to watch. Score: 91 (was 90)

### [mzCache: On-Device LLM Memory Management under Multitasking](https://arxiv.org/abs/2609.01338)
App-switching pressure evicts on-device weights and KV cache and blows TTFT from 0.8s to 16s; mzCache fixes it with fine-grained shared buffers on unified memory, a hybrid swap splitting KV between in-memory compression and storage, and backward-out/forward-in eviction so the GPU starts prefill while the CPU restores later layers. Built on llama.cpp and shipped as an Android app, it cuts TTFT 2.1–5.5× vs storage-backed partial offload and survives real multitasking where OS paging gets LMK-killed. The most immediately practical paper here for edge/mobile inference. Score: 87 (was 90)

### [DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference](https://arxiv.org/abs/2609.00407)
DynaNDE attacks MoE's data-movement wall on NPU+near-data-processing systems with an analytical latency model capturing hardware heterogeneity and compute/comm overlap, plus a prefix-scan scheduler that places experts per-layer and skips parameter transfers for experts already cached in NPU memory. Gains are strong — 2.6×/2.2× prefill/decode over MoNDE, up to ~30× over NPU-only decode — but results come from a cycle-accurate simulator on NDP hardware, so read it as a direction, not a drop-in. The reuse-aware scheduling formulation is the takeaway as MoE-on-NDP heats up. Score: 84 (was 92)

### [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](https://arxiv.org/abs/2609.00993)
Agentic RL rollouts keep re-issuing prefill while other trajectories decode; AInfer-PD multiplexes P/D on shared devices/KV (no disaggregation) by killing two subtle distributed hazards — a cross-rank collective-ordering *cycle* between P's full-TP AllReduce and D's DP-attention collectives (a rank-aligned "turnstile"), and DeepEP's shared normal/low-latency state (phase-owned buffers/QP ranges). On real H20-3E nodes it trims rollout makespan 7–22% single-node, 18–35% two-node vs multiplexing-off, and 25–33% vs SGLang. Niche but deep — essential if you run large-MoE RL rollout infra. Score: 84 (was 88)

---

## Surge Watch

**[FreeToken](https://arxiv.org/abs/2608.16157)** is the one signal still accelerating: it cleared 100 HF upvotes (99→107) and — the new tell this cycle — its repo detonated from ~7.3K to ~11K GitHub stars in a single week (Aug 26→Sep 2). The code release, not the paper, is now the engine; on-device MoE serving has a genuine breakout.

Meanwhile last cycle's citation darlings are visibly cooling: **[DFlash](https://arxiv.org/abs/2602.06036)** has slowed to 75→78 (influential 26→29) and **[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)** to 12→15 since Aug 27 — still the reference magnets, but well off their July tear. **[dLLM-Cache](https://arxiv.org/abs/2506.06295)** stalled at 163 after its late-Aug pop, and FlashAttention-4 sits flat at 48.

Net: momentum is rotating from citation accrual toward real code adoption — and FreeToken owns that shift.
