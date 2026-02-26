# Inference Ecosystem — Flash News
**2026-02-26**

**DualPath** smashes the KV-cache I/O wall in agentic LLM serving. By opening a second storage→decode loading path over RDMA and balancing with a global scheduler, it squeezes up to 1.87× offline throughput and 1.96× online throughput out of disaggregated inference clusters — a direct answer to the storage NIC bottleneck everyone running multi-turn workloads hits.
[arXiv](https://arxiv.org/abs/2602.21548v1) · Score: 95 | Hype: 75

**Multi-Layer Scheduling for MoE LLM Serving** tackles vLLM head-on with a three-tier scheduler (request / engine / expert) tailored for Mixture-of-Experts. SJF + load-aware dispatching + expert hotspot balancing yields up to 17.8% TTFT and 13.3% TPOT reductions across 100+ experiments.
[arXiv](https://arxiv.org/abs/2602.21626v1) · Score: 92 | Hype: 60

**DySCO** from Princeton NLP dynamically rescales attention weights at decode time using retrieval heads — training-free, works on any off-the-shelf model. Up to 25% relative gains on 128K-context reasoning benchmarks with modest extra compute. Long-context inference just got cheaper.
[arXiv](https://arxiv.org/abs/2602.22175v1) · Score: 78 | Hype: 72

**Confidence-Driven Multi-Scale Model Selection** routes queries between small and large LLMs based on confidence estimates, cutting GPT-4o token usage ~60% while matching top-model accuracy on MMLU. Simple idea, big savings for API-heavy deployments.
[arXiv](https://arxiv.org/abs/2602.22090v1) · Score: 75 | Hype: 50

**Sparsity Induction** pushes post-training pruning further by promoting sparsity at both distribution and feature levels *before* cutting weights — scaling transforms + spectral norm loss, zero inference overhead. Better pruning performance across architectures.
[arXiv](https://arxiv.org/abs/2602.21652v1) · Score: 72 | Hype: 50

Also worth watching: **Interleaved Head Attention** (Dhillon, Zaheer) adds cross-head mixing to MHA with O(H²P) params, boosting multi-key retrieval 10-20% and reasoning benchmarks ~3-6%. A fundamental attention architecture tweak. [arXiv](https://arxiv.org/abs/2602.21371v1) · Score: 72 | Hype: 60
