I can't access the PDFs due to sandbox restrictions, but the abstracts provide strong detail. Here's the bulletin based on the available information:

# Inference Ecosystem — Flash News
**2026-03-04 — 132 papers scanned**

**Speculative Speculative Decoding (Saguaro)** — Tri Dao and team introduce SSD, which parallelizes the draft-verify loop in speculative decoding by pre-emptively preparing speculations for likely verification outcomes. Saguaro eliminates drafting overhead entirely when predictions hit, delivering **2x over optimized spec-decode baselines and 5x over autoregressive** on open-source engines. This is the most important spec-decode advance since Medusa. [arXiv](https://arxiv.org/abs/2603.03251v1) — Score: 97

**Practical FP4 Training at 671B Scale** — A recipe for MXFP4 efficiency on Hopper GPUs *without* native FP4 tensor core support, using direct FP8-to-FP4 quantization and scaling-aware format conversion. On a 671B MoE (DeepSeek-scale), they get **14.8% memory reduction and 12.5% throughput gain** (1157→1302 tok/GPU/s) over FP8 baselines. Makes sub-8-bit training practical today. [arXiv](https://arxiv.org/abs/2603.02731v1) — Score: 92

**Ouroboros: Wafer-Scale SRAM CIM for LLM Inference** — A wafer-scale compute-in-memory architecture that keeps everything in SRAM, no off-chip data movement. Token-grained pipelining replaces sequence-level batching to handle variable lengths. Results: **4.1x throughput, 4.2x energy efficiency** on average, peaking at 9.1x/17x for 13B models. [arXiv](https://arxiv.org/abs/2603.02737v1) — Score: 92

**SUN: Cross-Model Decode Sharing** — Samsung decomposes decoder-only transformers into prefill and decode modules, fine-tunes only prefill, and shares a frozen decode module across multiple LLMs. Enables cross-model batching in disaggregated serving — **2x throughput per GPU** with TPOT within 5%. QSUN adds 4-bit decoding for another 45% speedup. [arXiv](https://arxiv.org/abs/2603.02599v1) — Score: 88

**Cross-Family Speculative Prefill** — Meta shows that attention-based token importance transfers across model families (Qwen→LLaMA→DeepSeek), enabling training-free prompt compression even without an in-family draft model. Retains 90–100% accuracy while cutting TTFT substantially. Key primitive for agentic pipelines with heterogeneous model stacks. [arXiv](https://arxiv.org/abs/2603.02631v1) — Score: 85
