Here's the generated bulletin. It seems I need write permission to save it to `news.md`. The output should be:

# Inference Ecosystem — Flash News

**2026-03-05 — 139 papers scanned**

### Qualcomm Cracks the Quantization Error Code with CAT

Qualcomm AI Research decomposes 4-bit quantization error into *concentration* (outlier spread) and *alignment* (weight-activation direction match) via SQNR analysis — and shows that popular Hadamard/rotation transforms only fix concentration while completely ignoring alignment. Their new Concentration-Alignment Transform (CAT) uses a small calibration set to jointly optimize both, yielding W4A4 SQNR that rivals W6A6 on Qwen v3 8B. On Llama 2 7B, Llama 3 8B, Ministral 8B, and Qwen 3 8B, CAT matches or beats FlatQuant and SpinQuant at 4-bit — without any training. This is the clearest theoretical framework yet for understanding *why* transforms help quantization, and it's immediately actionable. [arXiv:2603.04359](https://arxiv.org/abs/2603.04359) — Score: 90 (was 82)

### Bielik-Q2-Sharp: The $285 Guide to Extreme 2-bit Quantization

A single independent researcher systematically compares six SOTA 2-bit PTQ methods (QuIP#, SpinQuant+GPTQ, ButterflyQuant, QTIP, VPTQ, AQLM) on an 11B Polish LLM. The standout finding: a **MC-generation dissociation** where rotation-based methods (SpinQuant, ButterflyQuant) preserve log-likelihood but produce catastrophic autoregressive generation — loops and garbage text. QTIP achieves the best per-bit efficiency (79.4% MC acc at ~2.4 bpw, 3.27 GB), while QuIP# E8P12 matches the IQ2_XXS baseline within statistical noise. All models, Hessians, and evaluation logs are public. Essential reading if you're pushing models below 3 bits. [arXiv:2603.04162](https://arxiv.org/abs/2603.04162) — Score: 80 (was 78)

### Speculative Decoding Meets Ascend NPU — With Caveats

First end-to-end Medusa-style speculative decoding on Huawei Ascend NPU for OpenPangu-7B. The key engineering contribution: a fully static tree verification scheme with zero-copy path retrieval that sidesteps the NPU's static-graph execution constraint. Achieves 1.35x speedup for short sequences (L=128), but gains erode past 512 tokens as KV-cache memory bandwidth dominates — the NPU is more memory-sensitive than GPU here. Honest analysis of the memory wall on NPU hardware, useful for anyone targeting Ascend deployments. [arXiv:2603.03383](https://arxiv.org/abs/2603.03383) — Score: 78 (was 90)

### HyperParallel: Huawei's Supernode-Aware Framework for Trillion-Scale Models

Huawei/HKUST propose treating supernode clusters (384+ Ascend NPUs with unified memory) as a single logical computer inside MindSpore. Three components: HyperOffload (hierarchical HBM/DRAM memory management, 70% longer supported sequence lengths), HyperMPMD (fine-grained MPMD parallelism boosting MoE communication masking from 60% to 90%), and HyperShard (declarative parallel strategy specification). Mostly a vision paper with selected benchmarks, but signals where large-scale inference infrastructure is heading on non-NVIDIA hardware. [arXiv:2603.03731](https://arxiv.org/abs/2603.03731) — Score: 72 (was 75)

### Online Routing for Multi-Layer Hierarchical Inference

Formalizes the problem of routing inference tasks across edge-to-cloud hierarchies where feedback only arrives at the terminal oracle layer. Their VR-Ly-EXP4 algorithm integrates Lyapunov optimization with a variance-reduced bandit estimator to handle the depth-amplified feedback sparsity. On 80K jobs across 114 task types with 23 models, VR-Ly-EXP4 consistently achieves the lowest error rate and highest hit rate across 3-to-5-layer hierarchies. Directly relevant as inference moves toward tiered edge/cloud architectures. [arXiv:2603.04247](https://arxiv.org/abs/2603.04247) — Score: 72 (was 72)

---

## Surge Watch



**Qwen3-Coder-Next** ([2603.00729](http://arxiv.org/abs/2603.00729v1)) is picking up steam — HF upvotes jumped from 6 to 28 overnight, and GitHub stars ticked up to ~15.9k. Not an inference paper per se, but the agentic coding angle means inference efficiency matters downstream. Worth watching if the upvote curve holds.

**DualPath** ([2602.21548](http://arxiv.org/abs/2602.21548v1)) continues to hold steady at 37 HF upvotes — solid baseline traction for a storage-bandwidth paper, but growth has slowed to a trickle (+4 over 3 days). No surge here, just a paper that found its audience early.

Everything else is flat. LK Losses, ISO-Bench, Vectorized Trie, and DynaMoE show zero or negligible movement — the community hasn't picked these up yet despite high relevance scores on paper.
