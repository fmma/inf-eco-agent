# Inference Ecosystem — Flash News
**2026-04-10 | 530 papers scanned**

### [Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC](https://arxiv.org/abs/2604.07609)

Blink eliminates the host CPU from the steady-state inference path entirely, replacing it with a persistent GPU scheduler kernel and a BlueField-3 SmartNIC for request handling via RDMA. Benchmarked against vLLM, TensorRT-LLM, and SGLang on Llama-3 8B, Phi-4 15B, Qwen-3 32B, and Qwen-3 30B-A3B (MoE), it cuts P99 TTFT by up to 8.47x, P99 TPOT by 3.40x, and energy per token by 48.6% — even in isolation. Under CPU interference from colocated workloads, baselines collapse by 1-2 orders of magnitude while Blink is completely unaffected. The MoE results are especially striking: 3.45x TTFT and 1.85x TPOT advantage over TRT-LLM. This is the most architecturally ambitious inference paper in a while — it redefines what "the serving stack" means.
Score: 97 (was 97)

### [Valve: Production Online-Offline Inference Colocation with Jointly-Bounded Preemption Latency and Rate](https://arxiv.org/abs/2604.07874)

Tencent's Valve colocates latency-critical online serving with offline inference on the same GPU using sub-millisecond channel-controlled compute preemption (at most once per request) and rate-limited sub-layer KV cache reclamation. Deployed on 8,054 GPUs in production, it boosts cluster utilization by 34.6% — equivalent to saving 2,170 GPUs — while keeping online TTFT increase below 5% and TPOT increase below 2%. The practical deployability is key: one line of driver modification and 20 lines of framework patch across vLLM, SGLang, and TRT-LLM. For any team running inference at scale with idle GPU cycles, this is the colocation approach that actually ships.
Score: 95 (was 95)

### [Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving](https://arxiv.org/abs/2604.08075)

A deceptively simple fleet-level optimization: split your vLLM fleet into a short-context pool (8K, 128 concurrent sequences) and a long-context pool (64K, 16 sequences), then route requests by estimated total token budget using a self-calibrating bytes-per-token EMA — no tokenizer needed. On Azure and LMSYS traces serving Llama-3-70B, this cuts GPU-hours by 31-42% and preemption rates by 5.4x. A Qwen3-235B-A22B case study on MI300X projects $15.4M/yr savings at 10K req/s. The closed-form cost model `savings = alpha * (1 - 1/rho)` lets you estimate gains from your traffic CDF before changing anything.
Score: 88 (was 95)

### [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426)

Yandex researchers expose a blind spot in KV cache offloading: existing methods like ShadowKV are evaluated on easy needle-in-haystack tasks but fail badly on context-intensive workloads requiring bulk information extraction. Their new Text2JSON benchmark (extracting structured JSON from documents) shows significant degradation on both Llama 3 and Qwen 3. The culprit: SVD-based key compression and coarse chunk-based landmark selection. Replacing SVD with quantization (FP8/HIGGS) and using quantized per-token landmarks instead of chunk averages recovers most of the gap. A practical warning for anyone deploying KV offloading on real workloads.
Score: 82 (was 95)

### [Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference](https://arxiv.org/abs/2604.07394)

Flux Attention adds a lightweight Layer Router (trained via Gumbel-Softmax in 12 hours on 8xA800) that dynamically assigns each transformer layer to full or sparse attention based on input context. Unlike head-level dynamic sparsity which creates GPU synchronization bottlenecks, layer-level routing keeps memory access contiguous, delivering real wall-clock gains: 2.8x prefill and 2.0x decode speedup at 256K context on Qwen3 and Llama-3.1. The router learns task-aware allocation — retrieval-intensive tasks get more full-attention layers, summarization tasks get more sparse. The backbone stays frozen throughout training.
Score: 82 (was 95)

---

## Surge Watch

[TriAttention](https://arxiv.org/abs/2604.04921v1) shows no sign of slowing down: 93 HF upvotes and 383 GitHub stars on its fourth data point, up from 82/284 yesterday. That's another +99 stars overnight — the same clip as the day before. KV cache compression via trig transforms is clearly hitting a nerve with the long-context crowd.

[MegaTrain](https://arxiv.org/abs/2604.05091v1) gets its third reading and the verdict is real momentum, not just launch-day curiosity: 38 HF upvotes (+12) and 190 GitHub stars (+91), nearly doubling again. The "100B on one GPU" pitch is converting browsers into stargazers at a sustained rate.

[MARS](https://arxiv.org/abs/2604.07023v1) is the new entry to watch — a multi-token generation method that jumped from 12 to 25 HF upvotes and 2 to 12 GitHub stars overnight. Only two data points, but the velocity pattern echoes MegaTrain's early trajectory.

Everything else is steady-state or flat. [Attention Residuals](https://arxiv.org/abs/2603.15031v1) added just 12 stars (3,054 total) — the cool-down continues. [TAPS](https://arxiv.org/abs/2603.27027v1) remains frozen at 141/4.
