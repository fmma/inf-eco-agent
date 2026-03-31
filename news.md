PDF reading is blocked by the sandbox environment. I'll proceed with the detailed abstracts to write the bulletin — they contain specific methods, benchmarks, and speedups.

# Inference Ecosystem — Flash News
**2026-03-31 | 333 papers scanned**

---

### [ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation](https://arxiv.org/abs/2603.27138)

GPU memory remains the binding constraint for long-context decode batches, and ScoutAttention tackles it with a clever twist on KV cache offloading: the CPU starts computing attention for layer N+1 while the GPU is still on layer N, hiding most of the CPU latency behind GPU work. A block-wise sparse attention scheme keeps CPU load manageable, and an asynchronous periodic recall mechanism preserves accuracy within 2.4% of the full-cache baseline. Net result: **2.1x speedup** over prior offloading methods. If you're serving 100K+ context on commodity boxes with big DRAM, this is the paper to read. Score: 92 (was 95)

### [TAPS: Task-Aware Proposal Distributions for Speculative Sampling](https://arxiv.org/abs/2603.27027)

Speculative decoding drafters are almost always trained on generic data — TAPS asks what happens when you match drafter training data to your actual workload. Using HASS and EAGLE-2 backbones, they show MathInstruct-trained drafters dominate on reasoning while ShareGPT-trained ones win on chat, with mixed data improving robustness. The real contribution: a **confidence-based routing** scheme that selects the best specialized drafter at inference time, and a merged-tree verification strategy that yields the highest acceptance lengths overall. Practical takeaway for anyone running speculative decoding in production: your drafter training mix matters as much as its architecture. Score: 90 (was 95)

### [RSR-core: A High-Performance Engine for Low-Bit Matrix-Vector Multiplication](https://arxiv.org/abs/2603.27462)

Production-ready engine for binary/ternary weight MVM with optimized CPU and CUDA kernels implementing the Redundant Segment Reduction algorithm. Achieves **62x speedup on CPU** and **1.9x speedup on CUDA** for token generation with popular ternary LLMs. Ships with HuggingFace integration for preprocessing and inference — pip install and go. As 1-bit and 1.58-bit models mature, this is the kind of kernel infrastructure that makes them actually deployable. [Code on GitHub](https://github.com/UIC-InDeXLab/RSR-core). Score: 88 (was 92)

### [SCIN: Switch-Centric In-Network Architecture for LLM Inference](https://arxiv.org/abs/2603.28239)

Rethinks NVLink SHARP's accelerator-centric All-Reduce by moving the reduction initiator into the switch itself. This eliminates redundant data movement (GPU→switch→GPU round-trip) and enables in-network quantization to 8-bit, nearly doubling effective bandwidth. On a multi-FPGA prototype: **8.7x All-Reduce speedup** for small messages, **1.74x faster TTFT** and 1.34x faster TPOT on LLaMA-2. Still at the FPGA-prototype stage, but the architectural insight — that the switch should own the reduction, not the GPU — points where multi-GPU interconnects are heading. Score: 85 (was 95)

### [KVSculpt: KV Cache Compression as Distillation](https://arxiv.org/abs/2603.27819)

Instead of evicting or merging existing KV pairs, KVSculpt optimizes a smaller set of unconstrained KV pairs in continuous embedding space via L-BFGS (keys) and closed-form least squares (values) to preserve attention behavior. An adaptive budget allocation scheme redistributes compression ratios across layers and heads based on difficulty — and the non-uniformity is extreme: per-layer MSE varies by up to **100x**, per-head by up to **467x**. Achieves 3.5–4.1x KL divergence reduction over select-and-fit baselines on Qwen2.5-1.5B. A fundamentally different take on KV compression that treats it as a distillation problem. Score: 82 (was 92)

---

## Surge Watch

[PackForcing](https://arxiv.org/abs/2603.25730v1) is the breakout of the week: zero signals on Mar 28, then 40 HF upvotes and 101 GitHub stars by Mar 31. Efficient long-video inference via short-video training clearly struck a chord — fastest cold-start we've tracked this month.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) HF upvotes reactivated after a week flat at 162: now 169 (+7 in 3 days), with GitHub stars pushing to 2,843 (+48). Adoption curve hasn't flattened — this project has legs.

[SpecEyes](https://arxiv.org/abs/2603.23483v1) surge is over: +1 HF upvote and +5 stars over 3 days, down from the 19 → 57 run. Settled into steady state around 58 upvotes / 48 stars.
