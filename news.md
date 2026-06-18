I'll proceed with the detailed abstracts to write the bulletin. The abstracts contain specific methods, speedups, and benchmarks sufficient for rescoring and news generation.

# Inference Ecosystem — Flash News
**2026-06-18 | 223 papers scanned**

---

### [JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394)

JetFlow solves the causality-efficiency dilemma in speculative decoding by training a causal parallel draft head over fused hidden states from the frozen target model — giving you one-forward drafting efficiency with branch-wise causal conditioning. On H100 GPUs with Qwen3 models, it hits **9.64x speedup on MATH-500** and **4.58x on conversational workloads**, consistently beating both bidirectional-head and tree-based SD baselines. Ships with vLLM integration for realistic serving loads, code and models open. This is the new bar for speculative decoding.
**Score: 94 (was 95)**

### [Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://arxiv.org/abs/2606.18431)

Throws out decode-length prediction entirely and replaces it with distribution-aware priority boosting driven by lightweight statistical signals. The result: **P99 TTLT drops 35–50%** versus SRPT *even with perfect length knowledge*, and TTFT improves 34–47% across reasoning-heavy and chat workloads. The co-optimized cache-aware preemption handles memory-coupled decode dynamics that prediction-based schedulers ignore. If you're chasing tail latency in production, this paper just made predict-then-schedule look obsolete.
**Score: 95 (was 95)**

### [ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/abs/2606.18741)

Currently, changing TP/PP topology means restarting the service — minutes of downtime, KV cache lost, recomputation overhead. ReMP decouples parallelism topology from runtime state and migrates KV cache across both TP and PP dimensions. Topology switches complete in **1–7 seconds on 7B–70B models** (up to 100x faster than restart). Under dynamic workloads it significantly beats fixed-configuration baselines on TTFT, TPOT, and throughput. Essential for anyone operating multi-tenant GPU clusters with shifting traffic patterns.
**Score: 91 (was 93)**

### [ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/abs/2606.18600)

Makes heterogeneous spot GPU clusters viable for LLM serving by combining a roofline-model performance estimator with DP-based placement optimization across mixed GPU types. Fault tolerance via output-preserving request migration with concurrent initialization through a shared tensor store. On AWS with L4/A10G/L40S serving Llama-3.1-70B and Qwen3-32B: **1.42x throughput over baselines** and **~31% cost savings** versus on-demand. If you're spending real money on GPU inference, this is the heterogeneous spot playbook.
**Score: 88 (was 92)**

### [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2606.18967)

Applies self-speculative decoding to RL rollout generation — the latency bottleneck in RLHF-style post-training. Uses a quantized drafter induced from the target model (no separate pretraining), plus a system-aware toggle that activates speculation only in memory-bound regimes where it actually helps. Cuts **rollout latency by 19.6%** and **end-to-end training latency by 12.7%** while preserving final model quality. Niche but timely as RL post-training scales up.
**Score: 80 (was 85)**

---

## Surge Watch

[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) had the hottest debut this cycle — 83→131 HF upvotes and 184→293 GitHub stars in just 3 days (Jun 13–16). Production-ready sparse attention from a major lab is clearly in demand.

[KVarN](https://arxiv.org/abs/2606.03458) (variance-normalized KV cache quantization) surged from 179→399 GitHub stars in 11 days (Jun 5–16). The "mitigates error accumulation in reasoning tasks" angle is resonating — practitioners want KV quantization that doesn't break chain-of-thought.

[Domino](https://arxiv.org/abs/2605.29707) (decoupling causal modeling from autoregressive drafting) went viral: 2→145 HF upvotes between Jun 2 and Jun 7, now at 145 upvotes / 64 GitHub stars. A clean architectural insight for speculative decoding that clearly struck a nerve.

[DFlash](https://arxiv.org/abs/2602.06036) (block diffusion flash speculative decoding) crossed 5K GitHub stars — up from 4,750 on May 31 to 5,117 by Jun 16, with citations climbing 21→32 (14 influential). This is becoming the de facto infrastructure layer for diffusion LLM acceleration.
