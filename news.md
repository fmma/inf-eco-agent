# Inference Ecosystem — Flash News

**2026-03-11** — 154 new papers scanned

---

### [The qs Inequality: Why Mixture-of-Experts Models Pay Twice at Inference](https://arxiv.org/abs/2603.08960)

AMD Research formalizes the "double penalty" of MoE inference: expert routing fragments microbatches (killing weight reuse), while resident expert pools consume HBM headroom needed for KV cache. Their *qs inequality* (quality-equivalence × sparsity) shows quality-matched dense models achieve **4.5× throughput advantage** over DeepSeek-V3 at 128k context on MI300X. The paper recommends training with MoE, then distilling to dense for deployment — a sharp reframing of the MoE inference cost story.
**Rescored relevance: 95**

### [ConFu: Speculative Decoding with Contemplate Tokens and Future Prediction](https://arxiv.org/abs/2603.08899)

UCLA and Qualcomm extend EAGLE-style speculative decoding by giving draft models "contemplate tokens" — learned soft prompts that let the drafter anticipate the target model's future generation direction. A dynamic MoE mechanism selects contemplate strategies per token, and anchor token sampling replicates future prediction during training. Achieves **8–11% speedup over EAGLE-3** on Llama-3 3B/8B (H100, SpecBench) with no target model changes.
**Rescored relevance: 90**

### [Demand Paging for LLM Context Windows](https://arxiv.org/abs/2603.09023)

Pichay treats the LLM context window as L1 cache and applies OS-style demand paging — eviction policies, fault-driven pinning, and cooperative memory management via "phantom tools." Deployed on **857 production Claude Code sessions** (4.45B tokens), it measures 21.8% structural waste in long contexts and achieves up to 93% context reduction with a 0.025% fault rate across 1.4M evictions. A 4-level memory hierarchy (L1–L4) gives a concrete systems framework for context management at scale.
**Rescored relevance: 88**

### [JigsawServe: Joint Optimization for Compound Inference Systems](https://arxiv.org/abs/2603.08797)

UIUC's JigsawServe co-optimizes latency, accuracy, and GPU resources for multi-model task graphs (e.g., social media pipelines, AR assistants). A MILP formulation over MIG+MPS spatial GPU partitioning delivers **11.3× max serviceable demand** versus closest prior work, with 43.3% GPU utilization at <0.6% SLO violations. First principled serving framework for compound AI systems where multiple models share hardware.
**Rescored relevance: 85**

### [Compiler-First Mamba-2: Portable SSM Inference via XLA](https://arxiv.org/abs/2603.09555)

Imperial College London implements Mamba-2 entirely in XLA standard primitives — no custom CUDA kernels — achieving O(1) autoregressive state caching as a JAX PyTree. On TPU v6e: ~140 TFLOPS prefill (15% MFU), 64% HBU on decode, matching the PyTorch/CUDA reference token-for-token. Opens SSM deployment on CPU, GPU, and TPU from a single codebase (open-sourced as mamba2-jax).
**Rescored relevance: 82**

---

## Surge Watch

Nothing noteworthy in signal trends today.
