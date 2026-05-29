# Inference Ecosystem — Flash News
**2026-05-29 | 503 papers scanned**

### [RTP-LLM: High-Performance Alibaba LLM Inference Engine](https://arxiv.org/abs/2605.29639)
Alibaba open-sources its production inference engine serving 100M+ users across Taobao, Tmall, and Cainiao. RTP-LLM integrates prefill-decode disaggregation, a 4-tier hierarchical KV cache (GPU → CPU → RDMA → 3FS distributed storage), modular speculative decoding (Medusa/Eagle/MTP/Prompt Lookup), and decoupled ViT-LLM multimodal processing. Production benchmarks against vLLM and SGLang are emphatic: 4.7-6.3x model loading speedup, 35-37% TTFT P95 reduction with 215% cache reuse improvement (enabling 75% reduction in prefill machines), and 1.86-2.52x multimodal throughput gains. The Qwen3-Coder-480B-FP8 deployment with PD disaggregation across 5 nodes is particularly notable — 4.72x TTFT speedup over SGLang and 5.33x over vLLM.
Score: 96 (was 95)

### [DFlash: Block Diffusion for Flash Speculative Decoding](https://arxiv.org/abs/2602.06036)
DFlash repurposes diffusion models as parallel drafters for speculative decoding — and the results are stunning. A lightweight 5-layer block diffusion model generates 16 draft tokens in a single forward pass, conditioned on target-model hidden features injected directly into the drafter's KV cache at every layer. This KV injection (not input fusion like EAGLE-3) is the key design choice enabling acceptance length to scale with drafter depth. On Qwen3-8B, DFlash hits 6.08x speedup on MATH-500 and 5.51x on LiveCodeBench — roughly 2.5x faster than EAGLE-3. On SGLang with FA4, it delivers 5.1x throughput gains at concurrency 1 on Qwen3-8B. The insight that diffusion models are *better* as speculative drafters than as standalone generators could reshape how the community thinks about dLLMs.
Score: 95 (was 93)

### [Draft-OPD: On-Policy Distillation for Speculative Draft Models](https://arxiv.org/abs/2605.29343)
Identifies a critical limitation: SFT for draft models plateaus because training uses target-generated trajectories while inference evaluates draft-induced states. Draft-OPD fixes this with target-assisted rollouts plus error-position replay — the draft model proposes blocks, rejected tokens are recorded, and the target re-scores those draft-generated prefixes. An acceptance-aware loss uses forward KL for accepted tokens and reverse KL for rejected ones. On Qwen3 models with thinking mode, Draft-OPD achieves 5x+ lossless speedup, improving over EAGLE-3 by 23% and DFlash by 13%. SGLang throughput gains of 8-17% hold across concurrency levels up to 32.
Score: 93 (was 94)

### [Bastion: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](https://arxiv.org/abs/2605.29727)
Builds on DFlash by constructing dynamic prefix trees from block-diffusion logits instead of committing to a single greedy path. Three components work in concert: a path-confidence surrogate estimating expected acceptance length, a roofline-calibrated latency estimator, and best-first tree expansion that stops when marginal gains no longer justify verification cost. The result is training-free, distribution-preserving, and hardware-adaptive. On Qwen3-8B: 6.61x average speedup over autoregressive decoding (vs. 4.76x for DFlash, 2.70x for EAGLE-3). Gains hold across A100, H100, A6000, and RTX PRO 6000 Blackwell.
Score: 93 (was 93)

### [FarSkip-Collective: Unhobbling Blocking Communication in MoE Models](https://arxiv.org/abs/2511.11505)
Modifies MoE architecture connectivity so that attention and MLP sub-blocks consume "outdated" or "partial" activations, decoupling communication from computation. Converts Llama 4 Scout (109B) via self-distillation with only 1% average accuracy loss. Overlapped implementations in Megatron-LM achieve 88.9% all-to-all communication overlap during EP training; in SGLang inference, DeepSeek-V3 gets 32.6% TTFT speedup at EP=8 with 97.3% communication overlap during prefill. Multi-node DeepSeek-V3 decode at EP=16 shows 1.25x speedup. As MoE sparsity increases beyond DeepSeek-V3's 32x, projected benefits grow further.
Score: 92 (was 93)

---

## Surge Watch

[ThinKV](https://arxiv.org/abs/2510.01290) just doubled its citation count — 3 citations for weeks, then 6→7 in the 05-27/05-29 window with a first influential citation. Thought-adaptive KV cache compression is hitting a nerve as reasoning models become the default workload.

[OScaR](https://arxiv.org/abs/2605.19660) debuted at 37 HF upvotes and 23 GitHub stars — the strongest launch for a KV cache quantization paper in this cycle. Extreme low-bit KV quantization via Occam's-style simplicity clearly resonates. Two other KV-quant papers launched the same day: [OSCAR](https://arxiv.org/abs/2605.17757) (5 upvotes, 12 stars) and [OCTOPUS](https://arxiv.org/abs/2605.21226) (6 upvotes) — the space is getting crowded fast.

[REAP the Experts](https://arxiv.org/abs/2510.13999) spiked from 12 to 15 citations on 05-29 alone, with influential citations climbing from 4 to 5. One-shot MoE compression via pruning is now the most-cited approach in the expert pruning cluster. [Post-Trained MoE Can Skip Half Experts](https://arxiv.org/abs/2605.18643) launched alongside at 29 HF upvotes and 22 stars — MoE efficiency is clearly the theme of the week.

[Mix-Quant](https://arxiv.org/abs/2605.20315) opened at 23 HF upvotes and 21 GitHub stars with a sharp angle: quantized prefilling but precise decoding, explicitly targeting agentic LLM workloads. The prefill/decode split is becoming a first-class design axis.
