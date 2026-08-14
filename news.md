I've read all eight PDFs. Rescoring against the full texts (not just abstracts), I weighted deployability, novelty, and immediacy for inference engineers. KARAT drops from its abstract score (excellent work, but custom silicon in a simulator), while NOVA-KV rises (complete theory→kernel with a striking hybrid-MoE result). EdgeXpert (edge ASIC, narrow audience, ~80) and HeteroPanacea (conditional simulator findings, ~85) fell just below the top 5. Here's the bulletin:

# Inference Ecosystem — Flash News
**2026-08-14 · 5 picks from 826 papers scanned**

KV-cache compression and speculative decoding dominate this batch — plus a look at where sparse-attention serving hardware is heading.

## [Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms](https://arxiv.org/abs/2608.04074)
NOVA-KV reframes 2-bit KV quantization as transform coding against *attention-product* error and proves the optimal key transform is **non-orthogonal** — unlike every QuaRot/OSCAR-style rotation — then pairs it with volume-equalized vector quantization for a fixed-width, paged-cache-friendly SGLang kernel. At 2 bits it tracks BF16 on RULER-NIAH where scalar methods collapse, most starkly on hybrid-attention MoE: on GPT-OSS-20B, QuaRot/OSCAR fall to 0.0 while NOVA-KV holds 54–90%. Rigorous theory all the way to a shipping kernel, plus the hybrid-MoE robustness that matters for current model designs, make it the standout. Score: 93 (was 92)

## [AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding](https://arxiv.org/abs/2608.02989)
Tree verification on an MoE target activates the *union* of experts across all draft nodes — most later discarded — so AcceptMoE builds a per-block eligible expert set weighted by offline commitment probability, self-sizes it via effective rank (no budget to tune), and prunes by cache residency under offloading. In SGLang it reaches 1.29× throughput with experts resident and **2.06× under offloading** with 73.6–77.1% less host-to-device traffic, at just −0.27pp accuracy. Directly deployable, and it fixes a real, subtle cost hiding inside MoE + speculative decoding. Score: 90 (was 92)

## [When RL Meets Adaptive Speculative Training: A Unified Training-Serving System](https://arxiv.org/abs/2602.06932)
Aurora (Together.ai; Tri Dao, Percy Liang, Ce Zhang) closes the speculator train/serve loop, framing online drafter learning as asynchronous RL and hot-swapping updated speculators into a live SGLang server without interruption. The payoff is **day-0 deployment**: an untrained speculator adapts on live traffic to a 1.5× speedup on MiniMax-M2.1 229B and Qwen3-Coder-Next 80B, plus 1.25× over a static drafter under traffic shift. Gains shrink at large batch sizes, but killing the offline-pretrain bottleneck for freshly released frontier models is a genuine operational win. Score: 89 (was 92)

## [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555)
As frontier models (GLM-5.2, DeepSeek-V3.2, MiniMax-M3) adopt retrieval-based sparse attention, the decode bottleneck shifts from bandwidth to *capacity* — so KARAT relocates the KV cache and index keys onto general-purpose processing-near-memory (LPDDR + SM-like cores sized to the indexer's operational intensity), freeing GPU HBM for larger MoE batches. With OFMS/CMR scheduling to hide pipeline bubbles, the simulated system delivers 2.09–6.13× throughput/TDP over GPU-only and 1.36–3.21× on training-free sparse attention. Custom silicon rather than something to deploy today, but the sharpest map yet of where sparse-attention serving hardware is heading. Score: 88 (was 95)

## [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](https://arxiv.org/abs/2608.03893)
NVIDIA finds cross-model KV cache has enough *linear* structure that a gradient-free per-head ridge map (RoPE-stripped, top-k source layers, 500 calibration sequences) can convert one model's cache into another's — skipping prefill entirely when you swap models for cost-quality cascading or routing. Four of six matched-KV pairs retain 73–98% accuracy at 2.7–25× lower latency than re-prefill; the two that fail linearly recover +37pp HellaSwag with an MLP. Matched-KV/within-family limits and mapper storage temper it, but a closed-form cross-model prefill-reuse lever is a genuinely new, practical idea for multi-model serving. Score: 87 (was 92)

---

## Surge Watch

Quiet board overall, but two papers broke their own patterns this week.

[Unlimited OCR Works](https://arxiv.org/abs/2606.23050) is the standout: the HF plateau I flagged as topped-out finally cracked — upvotes **75 → 80** after weeks pinned at 75 — while stars kept ripping **21,883 → 23,675 (Aug 4 → Aug 14)**, ~180/day. It's back to a dual-signal climb, not the star-only story it looked like last week.

On the citation side, [REAP the Experts](https://arxiv.org/abs/2510.13999) is the fastest mover — **25 → 30 citations and 9 → 11 influential in 10 days** (21 → 30 since Jul 8). One-shot MoE pruning is compounding, and the rising *influential* count says it's landing, not just getting name-checked. Honorable mention: [The Geometry of LLM Quantization](https://arxiv.org/abs/2507.18553) (GPTQ as Babai's algorithm) at **15 → 19** in two weeks — theory framing picking up.

Cooling: [DSpark](https://arxiv.org/abs/2607.05147), last week's lead, managed just **+2 HF upvotes (41 → 43)** in 10 days, down from +4/week. The steady dual-signal climb is flattening.
