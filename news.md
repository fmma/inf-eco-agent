# Inference Ecosystem — Flash News

**2026-03-12** — 133 new papers scanned

---

### LookaheadKV — Learnable Cache Eviction Without Draft Models
[arXiv:2603.10899](https://arxiv.org/abs/2603.10899) — Samsung Research · ICLR 2026

Adds a handful of "lookahead tokens" and a tiny LoRA head to predict which KV entries will matter *before* generation begins, slashing eviction overhead by 14.5× versus draft-model approaches (LAQ, SpecKV) with under 0.5 % extra parameters. Evaluated on LLaMA and Qwen (1 B–8 B) across LongBench, RULER, and MT-Bench with negligible TTFT cost. Code available.
**Rescored relevance: 94**

### AgentServe — CUDA Green Contexts for Single-GPU Agentic Serving
[arXiv:2603.10342](https://arxiv.org/abs/2603.10342)

Partitions streaming multiprocessors via CUDA Green Contexts so a single GPU can run multiple agentic sessions with hard SM isolation, pairing this with a TPOT-driven scheduler that picks batch size per partition. On an RTX 5090 (170 SMs) with Qwen2.5-7B, delivers up to 2.8× TTFT and 2.7× TPOT improvement over SGLang, vLLM, and llama.cpp.
**Rescored relevance: 93**

### S-HPLB — Sparsity-Aware Head Parallelism for Long-Context Attention
[arXiv:2603.10353](https://arxiv.org/abs/2603.10353)

Tackles the load-imbalance problem in sparse attention by adaptively redistributing sparsity budgets across heads (max-min shifting) and then greedily balancing head-to-GPU assignment. Cuts attention latency by 2.88× on 8×A100 for Qwen2.5-72B at 128 K context, built atop MInference.
**Rescored relevance: 90**

### ES-dLLM — Early-Skipping Acceleration for Diffusion Language Models
[arXiv:2603.10088](https://arxiv.org/abs/2603.10088) — Tsinghua IIIS · ICLR 2026

Training-free method that identifies low-importance tokens early in the layer stack and skips their remaining computation, yielding 5.6–16.8× wall-clock speedup on LLaDA-8B and up to 13.5× on Dream-7B (H200). First work to seriously optimize inference for the emerging masked-diffusion LLM paradigm.
**Rescored relevance: 90**

### LLVQ — Leech-Lattice Vector Quantization at 2 Bits
[arXiv:2603.11021](https://arxiv.org/abs/2603.11021) — Qualcomm AI Research

Exploits the 24-dimensional Leech lattice for codebook-free 2-bit post-training quantization, retaining 92 % of Shannon capacity. Beats AQLM, QuIP#, and QTIP across Llama-2/3, Ministral-3, and Qwen-v3 families with a fully parallelizable dequant kernel using fast modulo arithmetic — no lookup tables needed.
**Rescored relevance: 85**

---

*Surge Watch is reported separately.*

---

## Surge Watch

Nothing noteworthy in signal trends today.
