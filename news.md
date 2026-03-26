Now I have all the information I need from the PDFs. Let me write the bulletin based on my rescored assessments.

# Inference Ecosystem — Flash News
**2026-03-26 — 136 papers scanned**

### [AVO: Agentic Variation Operators for Autonomous Evolutionary Search](https://arxiv.org/abs/2603.24517v1)

NVIDIA lets an autonomous coding agent loose on attention kernels for 7 days on Blackwell B200 GPUs — and it beats both cuDNN (by up to 3.5%) and FlashAttention-4 (by up to 10.5%) on causal MHA, peaking at 1668 TFLOPS in BF16. The discovered optimizations — branchless accumulator rescaling (+8.1%), correction/MMA pipeline overlap, register rebalancing across warp groups — reflect genuine hardware-level reasoning across synchronization, scheduling, and register allocation. The GQA adaptation took only 30 minutes of additional agent effort, yielding up to 9.3% over FA4. This is the strongest evidence yet that agentic search can surpass months of expert kernel engineering.
Score: 95 (was 78)

### [Self-Distillation for Multi-Token Prediction](https://arxiv.org/abs/2603.23911v1)

Tencent's MTP-D adds gradient-detached, TopN-logits-selected self-distillation from the main head to MTP heads during pretraining, boosting acceptance rates by 7.5% (4 heads) and translating to 22.9% inference speedup with no main-head accuracy loss. The looped extension strategy scales MTP heads from 4 to 16 via cheap continued pretraining (70B tokens), reaching up to 3.05x speedup over single-head MTP. Directly applicable to DeepSeek-V3-style cascaded MTP architectures now shipping in production LLMs like MiMo, GLM, and Qwen3.
Score: 88 (was 82)

### [AttentionPack: Attention-aware Inference Optimizations for Large Vision-Language Models](https://arxiv.org/abs/2603.23914v1)

AttentionPack exploits the low-rank structure of visual token KV caches via multi-head SVD compression, achieving up to 8x memory reduction on VideoLLaVA and 5x on LLaVA with negligible quality loss. The attention-aware partial decompression trick cuts decompression FLOPs by 67% by using lower ranks for low-attention tokens. Combines cleanly with eviction, 4-bit quantization, and a fused FlashAttention-style kernel that halves decode latency. Particularly relevant as VLMs push to longer video contexts and higher-resolution multi-image inputs.
Score: 85 (was 88)

### [The Diminishing Returns of Early-Exit Decoding in Modern LLMs](https://arxiv.org/abs/2603.23701v1)

A systematic study introducing the Early-exit Adaptability Score (EAS) metric, benchmarked across Llama2→4, Qwen2→3, GPT-OSS, and Mamba families. The verdict: modern LLMs are getting worse for early-exit, not better. Newer models show reduced layer redundancy thanks to improved pretraining recipes, with similarity to the final layer emerging only in the last few layers. Dense transformers still offer more early-exit potential than MoE or SSMs, and models >20B parameters fare best. Important calibration for anyone investing in early-exit inference optimizations — the easy wins are disappearing.
Score: 80 (was 82)

### [LLM Inference at the Edge: Mobile, NPU, and GPU Trade-offs Under Sustained Load](https://arxiv.org/abs/2603.23640v1)

Benchmarks Qwen 2.5 1.5B (4-bit) across RPi5+Hailo-10H NPU, Galaxy S24 Ultra, iPhone 16 Pro, and RTX 4050 over 20 sustained iterations. The headline: thermal throttling, not peak compute, is the binding constraint on mobile. The iPhone 16 Pro loses 44% throughput within 2 iterations; the S24 Ultra's GPU gets frequency-floored by the OS at iteration 6. Meanwhile, the Hailo-10H NPU sustains 6.9 tok/s at 1.87W with 0.04% throughput variance and 271 mJ/token — matching RTX 4050 energy proportionality at 19x lower throughput. Essential reading for anyone planning always-on edge agent deployments.
Score: 82 (was 88)

---

## Surge Watch



[SpecEyes](https://arxiv.org/abs/2603.23483v1) is the fresh mover this cycle — 19 → 47 HF upvotes and 6 → 36 GitHub stars in a single day. A speculative perception/planning approach for agentic multimodal LLMs; worth watching whether this sustains or was a one-day spike.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) keeps grinding: 161 HF upvotes (+3) and 2,722 GitHub stars (+49 since last report). Growth has clearly tapered but the absolute numbers are remarkable — this is the defining inference paper of March 2026.

[Mamba-3](https://arxiv.org/abs/2603.15569v1) is quietly picking up academic traction — citations jumped from 4 to 6 in the last two days, including its first influential citation. HF engagement is minimal (6 upvotes) but the citation velocity suggests researchers are building on it.

Everything else in the tracker is flat or showing only marginal movement. The inference-fleet-sim / FleetOpt / semantic router cluster continues accumulating cross-citations but no organic community pickup.
