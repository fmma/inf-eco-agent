I've read all eight PDFs. Here is my rescored flash-news bulletin.

# Inference Ecosystem — Flash News
**2026-10-07 · 5 papers · 487 scanned**

### [Adaptive KV Cache Reuse for Fast Long-Context LLM Serving](https://arxiv.org/abs/2605.24022)
CacheTune does an offline FFT of each independently-encoded KV chunk to pick the ~15% of tokens whose recomputation restores the missing cross-chunk attention, reusing the rest — and the same indices tell the system which KV *not* to load from the cache tier. Result: 3.72–4.86× TTFT speedup and 3.93–6.21× throughput over full recompute at ~95% quality, beating CacheBlend/EPIC/ProphetKV, and still 2.34–2.36× when caches sit on SSD/HDD. RAG and multi-doc prefill is now the dominant serving cost and plain prefix caching does nothing for non-prefix chunks, so this is directly useful today. Score: 91 (was 92).

### [DLoop: Looped Speculative Decoding](https://arxiv.org/abs/2610.07659)
A confidence gate lets the draft model run several drafting stages before a single verification, with loop-aware training keeping it reliable on its own hidden states. It drops onto EAGLE-3, DFlash, Domino, DSpark and MTP modules with no extra parameters, improving wall-clock speedup 5–41% while staying lossless and composing on top of tree verification. The key win: it raises speedup for *parallel* draft models, where adaptive draft-length methods don't help. Score: 89 (was 92).

### [Nucleus Speculative Decoding](https://arxiv.org/abs/2610.07822)
NSD relaxes verification — accept a draft token if it passes the standard rule *or* lands in the target's top-p nucleus — reusing probabilities already computed during the pass. Up to 5.16× over autoregressive and 3.15× over standard SD, with ~48% fewer verification calls and a clean bound (the extra acceptance equals the draft's excess mass inside the nucleus). A drop-in, drafting-agnostic verifier change with theory and released code, though it trades exactness for throughput. Score: 89 (was 92).

### [ECO: Energy-Oriented Configuration Optimization for Attention–FFN Disaggregated LLM Serving](https://arxiv.org/abs/2610.08373)
A calibrated stage-and-pipeline energy prior plus cost-aware constrained Bayesian optimization searches GPU allocation, parallelism, frequency and power caps under just 16 measured trials. On A6000/A100 with Qwen and DeepSeek it cuts serving energy 40.5% and lifts output-token rate 20.7% versus default while meeting SLOs, landing 25–33% below generic BO and genetic search. Real NVML-measured energy wins and a reusable recipe make this matter for anyone running AFD deployments. Score: 88 (was 93).

### [LatentIndex: Cross-Layer Sharing with Layer-Specific Selection for Sparse Attention](https://arxiv.org/abs/2610.04635)
It brings MLA's latent-sharing to sparse-attention indexers: each layer group caches one shared latent from its anchor, and layer-specific decoders absorbed into queries let every layer still select its own tokens. On DeepSeek-V3.2/GLM-5 it cuts indexer-cache storage 61.1% and beats IndexCache recall by up to 3.28pp, while the hierarchical-selection variant delivers 2.30–2.72× decode indexer speedups over DSA. With DSA-style sparse attention now the long-context frontier, reclaiming cross-layer redundancy without forcing layers onto one token set is the right lever. Score: 86 (was 90).

---

## Surge Watch

[DFlash](https://arxiv.org/abs/2602.06036) is the scholarly breakout this cycle — the block-diffusion speculative-decoding paper is compounding faster than anything on the board, **citations 98→121 (09-25→10-07), influentials 38→49**. Its speculative-decoding cousins are surfing the same wave: [Domino](https://arxiv.org/abs/2605.29707) ran **19→30** and [DSpark](https://arxiv.org/abs/2607.05147) **30→40 (influentials 9→17)** over the same window — speculative decoding is where the citation energy is right now.

On HuggingFace, a fresh attention-architecture cluster from the Jingze Shi group cold-started hot on 10-03: [MassAlloc Attention](https://arxiv.org/abs/2609.32712) debuted at **74 upvotes + 766 GitHub stars**, sibling [CoWindow Attention](https://arxiv.org/abs/2609.32704) at **66** — sharpest launch since DeepSeek-V4.1-Flash, though worth watching whether it holds past day one.

[TraceLab](https://arxiv.org/abs/2606.30560)'s coding-agent workload trace nearly doubled citations **13→25 (09-26→10-07)**, the fastest-moving serving-characterization paper.

Among last cycle's heavyweights the attention race has split: [Mamba-3](https://arxiv.org/abs/2603.15569) cleared **100 citations (99→102, influentials 18)** while [FlashAttention-4](https://arxiv.org/abs/2603.05451) stalled at **75→76** — momentum has rotated to the SSM side.
