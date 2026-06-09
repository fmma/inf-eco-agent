I need either `poppler-utils` or `pymupdf` to read the PDFs. Could you approve one of these install commands? Alternatively, if you'd prefer, I can write the bulletin based on the detailed abstracts provided in the paper data.

In the meantime, let me proceed with writing the bulletin using the rich abstract and metadata information available, which contains substantial technical detail.

# Inference Ecosystem — Flash News
**2026-06-09 | 404 papers scanned**

---

### [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/abs/2606.09079)

The headline act this cycle. LSA introduces a Neural Memory Indexer that proactively predicts which KV chunks a query will need, trained via a backbone-free dual-encoder strategy — you never load DeepSeek-V4's full weights during indexer training. The result: physical KV cache compressed to **13.5%** of baseline on average, with **90%+ reduction at 500K context length**, while slightly *improving* accuracy (+0.6% across LongBench-v2, LongMemEval, RULER). This is the "less is more" paradigm done right — if you're serving long-context workloads, this changes your memory planning math entirely.
**Score: 95 (was 95)**

### [APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing](https://arxiv.org/abs/2606.08761)

Finally answers *why* W4A4 works on some GPUs and not others: it's the Tensor-to-CUDA Core throughput ratio (ρ). On high-ρ chips like A100 (ρ=64), group dequantization on CUDA Cores bottlenecks the INT4 Tensor Cores. APEX4 co-designs pure INT4 GEMM kernels with ρ-aware granularity adaptation, ships as a **drop-in vLLM replacement**, and delivers **2.09x end-to-end speedup on A40**, 1.78x on RTX 3090, while recovering A100 to 1.2–1.4x via mixed-granularity mode. Perplexity within 0.63 of FP16 on LLaMA-2-70B. The most deployment-ready W4A4 story yet.
**Score: 95 (was 95)**

### [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382)

Differentiable soft-thresholding for per-head, per-block rank selection in KV cache low-rank projection — no more fixed-rank guesswork. Combines hybrid key/value decomposition with low-rank-aware mixed-precision quantization for up to **20x total KV cache reduction**. Custom Triton kernels deliver **6.9x attention speedup** and **3.1x end-to-end throughput**. Code is open-source. Pairs naturally with systems like FlashMemory for compounding gains.
**Score: 92 (was 95)**

### [Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance](https://arxiv.org/abs/2602.05774)

Reframes draft model training as variational inference over latent draft paths, maximizing marginal acceptance probability rather than token-level likelihood. The EM procedure with Adaptive Rejection Weighting and Confidence-Aware Regularization yields **9.6% speedup over EAGLE-3** across both LLMs and MLLMs. Theoretically grounded and practically meaningful — speculative decoding keeps getting better, and VSD advances the Pareto frontier.
**Score: 90 (was 95)**

### [ART: Attention Run-time Termination for Efficient LLM Decoding](https://arxiv.org/abs/2606.00024)

Elegantly simple idea: monitor the accumulated attention output *during kernel execution* and terminate KV block access once further contributions are negligible. A stability criterion tracks both magnitude and directional changes, with theoretical truncation error bounds. Stacks on top of existing dense or sparse attention — **up to 20% throughput boost** on LongBench/RULER with zero quality loss. This is the kind of "free lunch" optimization that belongs in every long-context serving stack.
**Score: 90 (was 95)**

---

## Surge Watch

[Domino](https://arxiv.org/abs/2605.29707) (decoupling causal modeling from autoregressive drafting in speculative decoding) just had the most explosive debut this cycle — 0 to 140 HF upvotes and 52 GitHub stars in under a week. That's the kind of instant community resonance that signals a real pain point being hit.

The KV cache quantization wave keeps building. [KVarN](https://arxiv.org/abs/2606.03458) (variance-normalized KV quant for reasoning tasks) more than doubled its GitHub stars from 179 to 373 in just 4 days, with HF upvotes climbing from 47 to 57. Another entry in the sub-4-bit KV compression race that OSCAR and OScaR kicked off — this one specifically targeting reasoning workloads where quantization errors compound.

[Attention Sink survey](https://arxiv.org/abs/2604.10098v1) saw a late-breaking GitHub spike from 83 to 113 stars in 4 days (June 5–9) after months of near-flat activity. Renewed practitioner interest in understanding attention sink mechanics as sparse/compressed attention methods proliferate.

[DFlash](https://arxiv.org/abs/2602.06036) continues its steady academic build — citations up from 21 to 28 with influential citations jumping from 8 to 13 over two weeks. Block diffusion speculative decoding is becoming an established subfield, and Domino's arrival confirms the momentum.
