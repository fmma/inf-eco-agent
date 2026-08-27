I've read all seven PDFs in full. Rescoring on full text: **Prefix Sliding** rises (training-free 3× with public code and a genuinely constant per-token cost — the standout), **TOPAS** eases slightly (headline gains are synthetic; real MetaGPT gains are 9.8–22%), **AsymSpec** drops (full text reveals it's a *lossy* greedy steering scheme, not lossless SD), the **Quantization survey** rises (the FP4 flip + which-transform guide are directly actionable), **APT** drops (an ASIC co-design in simulation), and **Goodput** (55) and **Text-to-SQL** (62) fall below threshold. Five papers clear 70.

# Inference Ecosystem — Flash News
**2026-08-27 · 5 picks from 148 papers scanned**

Long-horizon reasoning and the FP4 hardware transition dominate today's batch — and the standout is a training-free trick that finally makes 100k-token reasoning affordable.

## [Prefix Sliding for efficient test-time scaling](https://arxiv.org/abs/2608.26070)
Muennighoff et al. (Stanford/UW/Prime Intellect) keep only the prompt prefix plus a sliding window of the last few thousand reasoning tokens, capping KV memory at a **constant cost per token** no matter how long the model thinks. Training-free, it runs Qwen3 **3× faster** while matching full attention — an 8192-token window even *beats* it on AIME25 (35.8 vs 34.2) — and RL training then scales traces past 100k tokens. One knob (window size), a custom Hopper FlashAttention kernel, and public code: the drop-in most reasoning-serving stacks should test this week. Score: 92 (was 90)

## [TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving](https://arxiv.org/abs/2608.25523)
The first SGLang scheduler to *jointly* decide which agent prefixes stay resident and which requests to admit under a shared KV budget, scoring post-decision states by remaining-path reduction vs. near-term reuse. On synthetic DAGs it cuts mean/p99 JCT up to 39.8%/49.4%; on real MetaGPT workflows a more modest but real 9.8–22% mean-JCT drop, at just 1.9ms/decision (0.31% overhead). If you serve agentic pipelines, prefix residency is a scheduling lever you're probably leaving on the table. Score: 89 (was 92)

## [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://arxiv.org/abs/2608.26004)
Breaks the drafter=verifier context assumption: a lightweight drafter reads the *full* prompt and steers a compressed-context verifier via contrastive δ-fusion plus a parameter-free JSD acceptance gate, recovering ~90% of full-context accuracy at **0.2–0.3× compute and 1.3–1.7× throughput** (and extending cross-modally, VL drafter → text verifier). The catch the abstract buries: it's a *lossy* greedy steering scheme, not lossless SD, and needs verifier logits — but a compelling operating point exactly when input compression is unavoidable. Score: 88 (was 92)

## [Transforms for LLM Quantization: The Great Inversion and Format Co-Design](https://arxiv.org/abs/2608.25188)
A 200-work survey that finally organizes the 4-bit transform zoo under one principle — the "Great Inversion": shared-scale kernels reward energy *flattening* (Hadamard/rotation), the exact opposite of classical transform coding's concentration (KLT). It maps the **integer→FP4 flip** (rotation is near-essential on INT4, neutral-to-harmful on NVFP4, block-confined on MXFP4) and distills a which-transform-when guide by deployment regime. The definitive reference as Blackwell/MI355X push everyone onto MXFP4/NVFP4. Score: 88 (was 85)

## [APT: Accelerating Diffusion Transformers via Attention Probability-Guided Pruning and Quantization](https://arxiv.org/abs/2608.25380)
A HW/SW co-designed accelerator for high-res DiTs (PixArt-α, SD3, FLUX) that uses attention probabilities as a unified prune/6-bit/12-bit signal, plus a Timestep-Aware FlashAttention that predicts this step's attention map from the last one — hitting up to 8.16×/3.01× speedup over A100/EXION. It's a 14nm ASIC in simulation, so no direct software payoff, but that temporal-reuse trick for FlashAttention is worth stealing for GPU kernels. Score: 72 (was 80)

---

## Surge Watch

The HuggingFace board went quiet this cycle — [FreeToken](https://arxiv.org/abs/2608.16157) and [LLMRouter](https://arxiv.org/abs/2608.06867) both settled with no fresh movement — so the real story moved to the citation ledger.

[dLLM-Cache](https://arxiv.org/abs/2506.06295) is the new quiet compounder: **156 → 160 citations in two days**, capping a steady month-long climb (154 on Aug 4 → 160 now). Diffusion-LLM caching is turning into load-bearing infrastructure, not a curiosity.

Correction to last week's call: [DFlash](https://arxiv.org/abs/2602.06036) is **not** flat. Its repo added ~340 GitHub stars since mid-August (**5,626 → 5,968**) while citations kept ticking up (**67 → 74**, influential 24 → 26) — quietly one of the most durable performers on the board. Its pairing, [DSpark](https://arxiv.org/abs/2607.05147), genuinely has stalled (citations 16 → 18, upvotes stuck at 45).

Otherwise it's still: [FlashAttention-4](https://arxiv.org/abs/2603.05451) added a single citation (46 → 47) since last report, and no new HuggingFace launch cleared the bar this week.
