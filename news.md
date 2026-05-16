# Inference Ecosystem — Flash News
**2026-05-16 — 782 papers scanned, 5 featured**

### [ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios](https://arxiv.org/abs/2604.09603)
From Alibaba's Qwen team, ECHO reformulates speculative decoding as a budgeted scheduling problem and is the first dynamic-tree SD framework integrated into SGLang. Sparse confidence gating at calibrated "sweet spots" avoids misjudgment accumulation while an elastic budget scheduler reallocates verification compute across requests. On Qwen3-235B, ECHO delivers up to 5.35x wall-time speedup at BS=1 and 14.4% throughput gains at BS=256 over EAGLE-3 — critically, it is the only SD method that doesn't collapse at high concurrency on industrial-scale MoE models.
Score: 95 (was 97)

### [Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility](https://arxiv.org/abs/2605.14037)
Meta FAIR introduces SP-KV, a learned sparse-write mechanism that trains a lightweight utility predictor jointly with the LLM via next-token prediction — no auxiliary losses needed. At 8.1B scale with 32k context, it retains only ~30% of KV entries beyond a 128-token local window while maintaining -0.2% average benchmark degradation and perfect NIAH retrieval. The decode kernel delivers 2.1-4.6x speedups at batch size 16. Bonus: the learned per-head density patterns serve as an architectural probe, producing hybrid local/global attention layouts that outperform hand-designed interleaving at the same KV budget.
Score: 94 (was 95)

### [KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving](https://arxiv.org/abs/2605.13734)
Accepted at SIGCOMM'26, KVServe treats KV compression as a constraint-driven online decision problem rather than a static algorithm choice. A Bayesian profiling engine cuts offline search from 1000 GPU-hours to 20, producing a 3D Pareto frontier of compression-ratio/accuracy/latency. At runtime, an analytical latency model combined with a lightweight bandit selects the optimal profile under bandwidth and SLO constraints. Integrated into vLLM and tested across 4090 to H100 hardware: up to 9.13x JCT speedup in PD-separated serving and 32.8x TTFT reduction in KV-disaggregated serving.
Score: 94 (was 95)

### [MultiPath Memory Access: Breaking Host-GPU Bandwidth Bottlenecks in LLM Serving](https://arxiv.org/abs/2512.16056)
MMA is the first software-defined multipath system for host-GPU memory copies, recruiting idle peer GPUs as relay nodes via their PCIe links and NVLink. Implemented as a ~3K-line C++ library activated via `LD_PRELOAD` — zero code changes for vLLM and LMCache. On an 8xH20 server, it achieves 245 GB/s peak H2D bandwidth (4.62x over single-PCIe baseline), cuts KV cache fetch TTFT by 1.14-2.38x and model wake-up latency by up to 2.48x. A drop-in win for anyone running KV cache offloading or model switching on multi-GPU nodes.
Score: 93 (was 95)

### [ReasonCache: Accelerating Large Reasoning Model Serving through KV Cache Sharing](https://arxiv.org/abs/2507.21433)
Exploits the observation that 15-40% of LRM reasoning steps are redundant (self-verification, state revisitation, infinite self-loops). A two-stage collaborative filtering algorithm identifies reusable KV cache blocks via lexical similarity then Euclidean distance verification, enabling zero-copy sharing through PagedAttention's reference counting. Across QwQ-32B, DeepSeek-R1-Distill-32B, and Phi-4-reasoning-plus: 40-60% average throughput improvement (peak 89.2%) while retaining 98%+ accuracy — consistently outperforming StreamingLLM, SnapKV, and Quest at comparable compression ratios.
Score: 88 (was 95)

---

## Surge Watch

Nothing noteworthy in signal trends today.
