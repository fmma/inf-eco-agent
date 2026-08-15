I've read all eight PDFs in full. Here's my rescored assessment: **HiSparse** and **Janus** are the two standouts (production-grade systems work, both real 4.7× gains on SGLang), **OasisKV** has a genuinely novel training-free predictor, **Autonomy-of-Heads** is elegant and zero-cost to deploy, and **GraceKV** reframes KV compression well. I'm dropping **Astrolabe** (older models, marginal capacity gains — narrower than the abstract implied), **RotaryQuant** (Apple-Silicon-only, only helps under memory pressure), and **PFM** (simulated NPU-PIM hardware, not deployable) below the top tier.

# Inference Ecosystem — Flash News
**2026-08-15 · 769 papers scanned · top 5 of the batch**

### [HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management](https://arxiv.org/abs/2608.07009)
Top-k sparse attention slashed compute but never the HBM bill — HiSparse fixes that by keeping full KV in host memory and bounding each request's decode footprint to a small fixed GPU cache, resolving every layer's selections in one fused CUDA kernel inside the decode graph. It's exact (outputs unchanged), indexer-agnostic across DSA/NSA/Quest, and — crucially — already merged into upstream SGLang. Up to 4.7× peak long-context throughput on H200/B200/GH200 at comparable TPOT, with a no-IO oracle proving the resolution logic itself is free. The rare paper that actually ships. Score: 96 (was 95)

### [Janus: Disaggregating Attention and Experts for Scalable MoE Inference](https://arxiv.org/abs/2512.13525)
Janus splits attention and MoE layers onto separate GPU pools so each scales independently, then balances *distinct activated-expert counts* (not tokens) via a synchronization-free GPU-kernel scheduler and adaptive two-phase communication. On DeepSeek-V2 and Qwen3-235B it hits up to 4.7× per-GPU throughput over monolithic SGLang and 2.2× over MegaScale-Infer while meeting TPOT SLOs, plus 39% GPU savings on a 24h production trace. The most complete MoE-serving systems paper this batch. Score: 94 (was 96)

### [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097)
The clever bit: OasisKV reuses speculative-decoding draft tokens (EAGLE-3 MTP) as a training-free, one-step-ahead predictor of which KV blocks the next step will attend to — 98.7% top-K agreement — then prefetches them off the critical path over PCIe/network. Built on vLLM with a fully async pipeline and capped eviction, it delivers 1.69× on reasoning and up to 2.1× multi-GPU long-context within 0.7 pts of full attention, and 2.1–2.3× under PD disaggregation with 6.5–9.7× less admission KV. Score: 93 (was 95)

### [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849)
"Heads know what they know": AoH classifies retrieval vs streaming heads purely from the effective-rank of the frozen Wₖᵀ·W_q kernel — no calibration prompts, no runtime scores, no learned gates, computed once before any input. At 50% sparsity it keeps 96.5% of full-attention quality while cutting prefill/decode latency up to 41%/66% and halving KV memory at 256K, GQA- and FlashAttention-compatible. Zero-cost deployment makes this an easy drop-in prior for existing sparse-attention stacks. Score: 89 (was 90)

### [Every Cache Entry Earns Its Place: Global Allocation for KV Cache Compression](https://arxiv.org/abs/2608.07001)
GraceKV reframes KV compression as one global budget auction: prototype trees let coverage (Add) and resolution (Split) operations compete across layers, heads, and slots instead of following fixed per-layer quotas. Training-free and GPU-resident, it ranks first in 24/32 LongBench+RULER settings and stays robust to 128× compression where token-eviction rivals collapse — at the cost of a ~2s one-time build after prefill. A principled answer to the eviction-vs-merging split. Score: 87 (was 90)

---

## Surge Watch

Quiet board overall, but the speculative-decoding corner is compounding on citations this week.

[DFlash](https://arxiv.org/abs/2602.06036) is the standout: citations sat frozen at **54 (Jul 30 → Aug 4)**, then jumped to **67 by Aug 15** (+13, influential 22 → 24), and HF upvotes finally broke their weeks-long plateau — **90 → 94** — with stars still grinding up (5,554 → 5,626). Back to a genuine dual-signal climb.

Plot twist on [DSpark](https://arxiv.org/abs/2607.05147): last week I flagged it cooling, and HF upvotes did stall (**41 → 43**). But the citation side roared — **8 → 14 citations and 2 → 4 influential in 11 days**. Its reception just migrated from HuggingFace to the literature.

Honorable mention: [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) is quietly dual-climbing — **6 → 9 citations and 392 → 408 stars** over ~10 days, upvotes 153 → 156. Meanwhile last week's citation lead [REAP the Experts](https://arxiv.org/abs/2510.13999) stalled dead at **30 citations / 11 influential**, no movement since the Aug 14 print.
