I'm unable to read the PDFs directly — poppler-utils isn't installed and no PDF Python library is available. I'll write the bulletin based on the detailed abstracts and metadata provided, which contain substantial technical detail for all papers.

# Inference Ecosystem — Flash News
**2026-06-10 | 294 papers scanned**

---

### [Achieving Cloud-Grade SLOs for Local MoE Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493)

A CPU-GPU hybrid system that runs **intact FP8 DeepSeek-V3** on consumer hardware — dual-socket CPUs + RTX 5090s — hitting cloud-grade SLOs: 1,800 tok/s prefill (45K prompts in 30s via distributed stream-loading with SmallEP), 21.5 tok/s decode on unquantized FP8, and a novel AVX-512 FP8 GEMV kernel delivering 4–5x lower CPU latency. Prefill-decode disaggregation with zero-copy shared weights sustains concurrency with <15% latency increase. This is the most complete local MoE serving paper we've seen — it doesn't just benchmark, it solves the full SLO stack (TTFT, throughput, concurrency) without distillation or rerouting.
**Score: 95 (was 95)**

### [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/abs/2606.10445)

First demonstrated **real end-to-end decoding speedup from semi-structured sparsity** on B200 GPUs. The Spense format splits weight matrices into a 2:4 sparse region and a dense region — no custom compiler, no activation expansion — just standard sparse and dense GEMM libraries. One-shot post-training pruning on Qwen3-32B and Seed-OSS-36B yields 1.2x end-to-end speedup at FP8 on B200 while preserving accuracy. Co-authored by Samyam Rajbhandari (DeepSpeed). The significance: after years of theoretical sparsity gains, someone finally shows it working end-to-end on the latest hardware with real models.
**Score: 92 (was 92)**

### [Express Language Modeling](https://arxiv.org/abs/2606.10944)

Express converts any non-causal attention approximation into a causal one with matching guarantees, then pairs it with an I/O-aware Triton kernel that **beats FlashAttention 2** on long-context workloads. Applied to four inference bottlenecks simultaneously: long-context prefill, KV cache compression, memory-constrained decoding, and compute-constrained decoding. Achieves O(s) memory with log^(3/2)(n)/s approximation error — a meaningful theoretical advance backed by practical kernel implementations. From Lester Mackey's group at Microsoft Research.
**Score: 90 (was 92)**

### [ReasonAlloc: Hierarchical KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164)

Training-free, plug-and-play KV cache compression for long chain-of-thought reasoning. Discovers a "Reasoning Wave" pattern — layer-wise attention demand that shifts predictably during autoregressive reasoning — and exploits it with offline layer preallocation + online head-wise reallocation. Tested on DeepSeek-R1-Distill models (8B, 14B) and AceReason-14B, outperforming SnapKV and Pyramid-RKV especially at tight budgets (128–512 tokens). The key insight: uniform budgets across layers are wrong for reasoning, and static profiles are wrong for decoding. Negligible overhead.
**Score: 88 (was 92)**

### [K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling](https://arxiv.org/abs/2606.10820)

Distills an AR model into a push-forward mapping that generates k=4 tokens per forward pass by transforming uniform noise into joint future-token samples. Delivers **2.4–3.5x speedup** across batch sizes while reusing the AR teacher backbone and staying compatible with standard serving infrastructure — no draft model, no rejection sampling. Trained via progressive self-forcing distillation. Evaluated on LM1B and OpenWebText with standard causal Transformers. The batch-serving compatibility is the differentiator: speculative decoding helps latency but not throughput under load, while K-Forcing directly reduces forward passes per token in high-load regimes.
**Score: 88 (was 90)**

---

## Surge Watch

[Orthrus](https://arxiv.org/abs/2605.12825) (memory-efficient parallel token generation via dual-view diffusion) quietly became the biggest GitHub story in the diffusion LLM space — from 13 to 412 stars in three weeks (May 16–Jun 8), far outpacing its modest 12 HF upvotes. Practitioners are clearly experimenting with this one.

[Gated DeltaNet-2](https://arxiv.org/abs/2605.22791) (decoupling erase and write in linear attention) went from 19 to 185 GitHub stars and 3 to 30 HF upvotes in about 10 days (May 22–Jun 2). The linear attention design space is heating up fast — this plus Parallax and MDN suggest the community is converging on practical sub-quadratic alternatives.

[Draft-OPD](https://arxiv.org/abs/2605.29343) (on-policy distillation for speculative draft models) had a sharp debut — 0 to 32 HF upvotes and 31 GitHub stars in 5 days (Jun 2–7). Speculative decoding continues to attract new training-side innovations, and this one landed with immediate community interest.

[IndexCache](https://arxiv.org/abs/2603.12201) is building quiet academic momentum — citations jumped from 6 to 10 in 10 days (May 30–Jun 10), with influential citations now at a notable level. Cross-layer index reuse for sparse attention is getting validated as a real technique.
