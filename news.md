I've read all eight PDFs in full. Here is the rescored bulletin.

# Inference Ecosystem — Flash News
**2026-09-25 · 5 picks from 465 papers scanned**

Long-context KV cache and speculative decoding own this batch. The theme: stop treating the KV cache as one flat pool — tier it, sparsify it, or skip drafting it entirely.

### [SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816)
SPLASH virtualizes the KV cache across HBM and High-Bandwidth Flash, then co-designs sparse attention around flash's page granularity and 1,024-plane parallelism — scoring one mean-key centroid per page (just 3.1% storage overhead), striping pages for plane-balanced retrieval, and hiding the centroid scan under HBM-window attention. Across five models at 128K–1M tokens it lands 3.5×–11.4× per-GPU decode throughput at a 100ms TPOT SLO within 4% of dense accuracy, fitting a 12.9TB cache into 5 GPUs' worth of HBF versus 68 of HBM. Simulation-only (HBF isn't shipping yet), but the clearest blueprint for where long-context serving memory is heading. Score: 92 (was 95)

### [When Fancy Eviction Fails: Rethinking Cache Replacement for LLM Prefix Reuse](https://arxiv.org/abs/2609.28870)
A production-trace study (two orgs, 14 eviction algorithms, HBM + pool regimes) with a blunt result: nothing beats LRU because prefix reuse is paced by active sessions, so recency is unusually predictive — and frequency policies (LFU, W-TinyLFU) actively collapse. The wins live on new axes: quick demotion for one-hit prompts, plus compute-aware "partial-node" eviction that weights victims by recompute FLOPs (deeper blocks cost more), cutting TTFT 19.9% and lifting prefill throughput 18.8% on vLLM/Qwen3-Coder-30B. Rigorous, immediately actionable, and the traces + simulator are being released. Score: 91 (was 90)

### [Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference](https://arxiv.org/abs/2602.08329)
PrHS selects KV entries *before* attention scoring — dodging the posterior bias of Quest/H2O/HShare — with an information certificate bounding error by dropped attention mass. Its three composable selectors (clustered-index sharing across similar queries, a depth-adaptive sliding window, early-token freezing) plus fused CUDA kernels skip >90% of head-layer retrievals, cut attention FLOPs ~15%, and hit a 9.9× attention-operator speedup and 3.3× end-to-end throughput on A100, staying robust past 128K where prior sparse methods degrade. Score: 90 (was 93)

### [TIDE: Temporal Incremental Draft Engine for Self-Improving LLM Inference](https://arxiv.org/abs/2602.05145)
TIDE attacks why providers ship speculative decoding disabled by default — draft/target drift under shifting workloads — by adapting the EAGLE-3 drafter online, reusing target hidden states already computed during inference as free training signal and gating speculation/training on measured acceptance length. It recovers throughput on misaligned non-English traffic where a static draft *drops* to 0.70–0.86×, reaches up to 1.66× at batch 1, and its H100-serving/MI250-training split cuts draft training time 3.02× and storage 24×. Built on SGLang/vLLM — a genuinely deployable answer to spec-decode-in-production. Score: 90 (was 93)

### [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://arxiv.org/abs/2609.24197)
Block-diffusion drafters project target hidden states into a separate drafter-side KV cache that grows O(N) per request; H-Spec kills it with a hybrid Mamba-attention drafter — Mamba modules seeded from last-token target hidden states, attention modules reusing target KVs in place — keeping block-parallel drafting at zero extra cache. Mean accepted length improves 5.0–13.3% and batch-1 ITL 5.3–12.6% over the best baseline, and under vLLM concurrent serving it Pareto-dominates on throughput at the lowest KV utilization, with the margin widening as concurrency rises. Score: 89 (was 92)

---

## Surge Watch

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) (KV cache compression) is the marquee debut: it cold-opened at **174 HF upvotes** on 09-24 — the single biggest first-day splash in the set — and already logged 7 citations by 09-25. DeepSeek's name still moves the crowd on contact.

Attention efficiency is where the fresh energy pooled, both 09-24 debuts: [Grouped Value Attention](https://arxiv.org/abs/2609.13285) (on-demand key reconstruction) opened at **81 upvotes**, and [SAS](https://arxiv.org/abs/2609.13141) (end-to-end attention sparsification) at **65 upvotes + 60 GitHub stars**. The community is clearly hungry for cheaper KV/attention right now.

On the citation side, [DFlash](https://arxiv.org/abs/2602.06036) quietly re-accelerated after last cycle's cooldown call — **93→98 citations and 33→38 influential cites in three days** (09-22→09-25), plus HF 95→99. It's the rare paper still compounding.

Meanwhile [Random Attention](https://arxiv.org/abs/2609.03430) (187) and Kimi's [Attention Residuals](https://arxiv.org/abs/2603.15031) (197 HF) have flattened — the torch has passed to this week's newcomers.
