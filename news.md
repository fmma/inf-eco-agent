# Inference Ecosystem — Flash News

**2026-03-02**

## Top Papers

**[LK Losses](https://arxiv.org/abs/2602.23881v1)** — Nebius drops a deceptively simple idea: stop training speculative decoding drafters with KL divergence and directly optimize acceptance rate instead. Their LK losses exploit the fact that at suboptimal convergence (where every real drafter lives), minimizing KL ≠ maximizing acceptance. Drop-in replacement, zero overhead, 8–10% gains in average acceptance length across EAGLE-3, MEDUSA, MLP speculators, and DeepSeek MTP on targets up to 685B. Larger gains at temperature=1 and for capacity-constrained drafters. Score: 95 | Hype: 75

**[GPU Efficiency for LLM Adapter Serving](https://arxiv.org/abs/2602.24044v1)** — BSC/IBM build a Digital Twin of vLLM's continuous batching + KV-cache dynamics for LoRA serving, achieving <5% throughput error at 90x speedup over real benchmarking. A greedy placement algorithm on top finds the minimum GPU count to serve a workload without starvation — the "Maxpack" sweet spot where one more adapter tips you into queue explosion. Tested on H100s with Llama-3.1-8B and Qwen-2.5-7B. Score: 92 | Hype: 55

**[KEEP](https://arxiv.org/abs/2602.23592v1)** — KV-cache management for embodied planning agents, where memory updates constantly invalidate cached states. Groups memory by update frequency (static vs dynamic), uses attention-based importance propagation to selectively recompute cross-segment interactions, and balances KV loading across transformer layers to eliminate pipeline bubbles. 2.68x TTFT speedup over text-based memory on ALFRED; 1.90x over CacheBlend. Built on vLLM. Score: 88 | Hype: 52

**[DiCo](https://arxiv.org/abs/2602.23792v1)** — Training-free parallel decoding for diffusion LLMs (LLaDA, Dream). Identifies clusters of conditionally independent masked tokens via seed expansion, decodes them in parallel, and finishes stragglers with compound decoding using logit margins. 3.4–7.9x speedup on GSM8K/MBPP/HumanEval while often *improving* accuracy over vanilla sequential decoding. Score: 82 | Hype: 62

**[CUDA Agent](https://arxiv.org/abs/2602.24286v1)** — RL-trained agent that generates optimized CUDA kernels, hitting 100% faster-than-torch.compile rate on KernelBench L1/L2 and 92% on L3 — outperforming Claude Opus 4.5 and Gemini 3 Pro by ~40% on the hardest split. If this generalizes, hand-tuned kernel work just got a lot less necessary. Score: 65 | Hype: 80

## Hype Surges

No hype surges this cycle.
