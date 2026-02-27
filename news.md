Here's the flash news bulletin I've drafted:

---

# Inference Ecosystem — Flash News

**2026-02-27**

Big day for LLM serving infrastructure — five papers pushing real production bottlenecks.

**FLYING SERVING** dynamically switches between data and tensor parallelism *while the engine is running*, no restarts needed. Zero-copy weight views, KV cache preservation across layouts, and a deadlock-free scheduler yield up to 4.79x improvement under high load. Built on vLLM. [arXiv](https://arxiv.org/abs/2602.22593) — Score: 95 | Hype: 70

**S2O** breaks the sparsity ceiling for long-context attention by factorizing FlashAttention execution and loading non-contiguous tokens via an online permutation policy inspired by virtual memory. Early stopping on importance-sorted blocks delivers 7.51x attention speedup and 3.81x end-to-end on Llama-3.1-8B at 128K context. [arXiv](https://arxiv.org/abs/2602.22575) — Score: 93 | Hype: 65

**STATIC** from Google/YouTube flattens prefix trees into CSR sparse matrices for constrained decoding on TPUs/GPUs — 948x faster than CPU trie, 0.25% of inference time overhead. First production-scale deployment of strictly constrained generative retrieval, now open-sourced. [arXiv](https://arxiv.org/abs/2602.22647) — Score: 88 | Hype: 75

**InnerQ** regroups KV cache quantization along the inner dimension so dequantization aligns with the vector-matrix multiply, enabling scale factor reuse across GPU compute units. Up to 22% speedup over prior KV quantization and 88% over FP16, with no accuracy loss on Llama. [arXiv](https://arxiv.org/abs/2602.22200) — Score: 92 | Hype: 60

**SideQuest** (Meta) uses the reasoning model itself to compress its own KV cache as a parallel side-task — 65% peak token reduction on agentic workloads with minimal accuracy loss, outperforming all heuristic baselines. Trained with just 215 samples. [arXiv](https://arxiv.org/abs/2602.22603) — Score: 92 | Hype: 60

Also notable: **ReMix** introduces continuous mixing states for diffusion LLM decoding (2-8x speedup, training-free) and **LLMServingSim 2.0** provides a unified simulator for heterogeneous/disaggregated serving stacks with <1% error vs real deployments.

---

It looks like write permission was denied. Would you like me to try writing it again, or would you prefer to copy the content above?
