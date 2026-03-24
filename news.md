# Inference Ecosystem — Flash News
**2026-03-24 — 213 papers scanned**

## [CALVO: Improve Serving Efficiency for LLM Inferences with Intense Network Demands](https://arxiv.org/abs/2603.21257v1)

As distributed KV cache pools become standard, CALVO identifies a bottleneck hiding in plain sight: KV cache *loading* time now dominates TTFT for long-context requests with high cache hit ratios, yet existing engines (vLLM, SGLang) treat it as subordinate to GPU compute. CALVO decouples loading across L3/L2/L1 stages into autonomous dispatcher-executor pairs running asynchronously, and incorporates loading delay into a binary linear cost model for scheduling (SJF for latency, LSTF for SLO attainment). Built atop vLLM + LMCache with 3.3K lines of code, it achieves up to 61.67% higher SLO attainment and 81.3% lower average TTFT on LooGLE/ICL/Code benchmarks. This matters now because agentic workloads are pushing cache reuse ratios above 88%, exactly the regime where network cost eclipses compute.
Score: 92 (was 95)

## [Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs](https://arxiv.org/abs/2603.22206v1)

Multi-agent workflows run multi-stage LLM calls where each stage's output becomes the next stage's context, but existing serving systems assume homogeneous model replicas. Chimera builds a middleware layer atop vLLM that co-designs routing, queue management, and load balancing across heterogeneous model pools (Qwen 1.5B-14B, Llama3B, Ministral8B). It combines a ModernBERT-based semantic router for per-model confidence, a QRF-based length predictor for workflow-level STJF scheduling, and an activity monitor tracking in-flight predicted token volumes. On APPS and MATH benchmarks, Chimera achieves 1.2-3.4x latency reduction over vLLM with 8-16 percentage point score improvements, at under 2.2% scheduling overhead. The latency slack parameter gives operators a clean knob between speed and quality.
Score: 88 (was 88)

## [Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels](https://arxiv.org/abs/2603.22276v1)

DoRA's row-wise norm of W+sBA forces every major framework (PEFT, torchtune, Unsloth, SWIFT, LLaMA-Factory, Axolotl) to materialize a dense [d_out, d_in] product, consuming ~512 MB per module at d=8192, r=384. This paper decomposes the squared norm into base, cross, and Gram terms computable through O(d_out*r + r^2) intermediates, then fuses the four-kernel DoRA composition into a single Triton pass with a numerically stable form that avoids catastrophic cancellation near g=1. Across six 8-32B VLMs on RTX 6000 PRO, H200, and B200, inference is 1.5-2.0x faster than HF PEFT with up to 7 GB lower peak VRAM. The 32B models that OOM on RTX 6000 PRO during training now run inference on it. Immediately useful for anyone deploying DoRA adapters at scale.
Score: 85 (was 78)

## [The Workload-Router-Pool Architecture for LLM Inference Optimization](https://arxiv.org/abs/2603.21354v1)

The vLLM Semantic Router project distills a year of work (21 papers) into the Workload-Router-Pool (WRP) framework, a 3x3 interaction matrix covering what the fleet serves (chat vs. agent, warm vs. cold, prefill-heavy vs. decode-heavy), how requests are dispatched (static rules, bandit adaptation, RL cascading), and where inference runs (heterogeneous GPU, disaggregated P/D, KV-cache topology). More roadmap than system, but the paper codifies important findings: routing topology is a stronger energy lever than GPU generation (1/W law), agents generate 3-10x more LLM calls than chat, and co-designing router compression with pool boundaries yields 3-6% lower cost than retrofitting. Twenty-one concrete research directions are proposed, tiered by maturity.
Score: 82 (was 95)

## [LLM Router: Prefill is All You Need](https://arxiv.org/abs/2603.20895v1)

From NVIDIA. Instead of routing on fragile semantic embeddings, this paper uses internal prefill activations via Encoder-Target Decoupling: a "foreign" open-source encoder (e.g., Qwen3.5-122B) predicts the correctness of closed-source targets (e.g., Claude, GPT) using hidden states from Fisher-Separability-optimal layers. The SharedTrunkNet architecture captures 45.58% of the oracle-best accuracy gap while achieving 74.31% cost savings. Evaluated across frontier, small, and mixed model pools (Claude Opus 4.6, GPT-5.2, Qwen, Nemotron) on MMLU-Pro, HLE, and LiveCodeBench. The key insight that activation geometry carries stronger routing signal than any semantic backbone is worth internalizing.
Score: 78 (was 80)

---

## Surge Watch

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) from the Kimi team is the runaway hit this week. HF upvotes nearly tripled from 53 to 151 and GitHub stars surged from 1,067 to 2,615 in seven days, picking up an influential citation along the way. Community reception suggests this architectural tweak is getting serious attention from practitioners.

[Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619v1) doubled on both fronts since appearing on Mar 17: 41 → 76 HF upvotes and 70 → 140 GitHub stars. Steady, sustained growth rather than a spike, which tends to signal genuine utility over novelty.

[GradMem](https://arxiv.org/abs/2603.13875v1) went from zero signals on Mar 17 to 33 HF upvotes and 25 GitHub stars by Mar 24. First meaningful traction for a test-time gradient descent approach to context memory, worth watching whether it sustains.
