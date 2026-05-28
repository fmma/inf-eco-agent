# Inference Ecosystem — Flash News

**2026-05-28** — 502 new papers scanned

---

**xKV: Cross-Layer SVD Knocks KV Cache Down to Size**
[arXiv:2503.18893](https://arxiv.org/abs/2503.18893) · Rescored relevance: 95

ICML 2026. Discovers that KV cache matrices share aligned singular vectors across layers, then exploits this to compress via cross-layer SVD — no training, no calibration. Delivers 8× compression and 4.23× decoding speedup on Llama-3.1/Qwen2.5/DeepSeek-V2 with negligible quality loss. Plug-and-play compression at this ratio is rare; expect this to get adopted fast.

**SiDP: Shared-Weight Data Parallelism for Offline Inference**
[arXiv:2605.28095](https://arxiv.org/abs/2605.28095) · Rescored relevance: 93

Flips the standard DP model: instead of replicating weights per GPU, treats them as a shared NVLink-accessible resource and gives each GPU its own KV cache partition. Result is 1.8× KV capacity and 1.5× throughput over vLLM on H20/H200/B200 clusters. Purpose-built for the offline/batch regime where memory, not latency, is the bottleneck — exactly the economics driving most production workloads today.

**Fast KV Compaction via Attention Matching**
[arXiv:2602.16284](https://arxiv.org/abs/2602.16284) · Rescored relevance: 92

ICML 2026. Formulates KV cache compaction as an attention-matching problem with closed-form solutions, achieving 50× compaction in seconds — orders of magnitude faster than Cartridges and other optimization-based methods. Near-lossless at extreme ratios. Makes on-the-fly KV compaction practical for deployment rather than just a research trick.

**UNIQUE: Universal Sparse Attention Framework**
[arXiv:2605.27740](https://arxiv.org/abs/2605.27740) · Rescored relevance: 90

A page-level top-k sparse attention framework that works across text and speech LLMs without model-specific tuning. 11.4× attention kernel speedup, 5.3× end-to-end decoding speedup over dense vLLM. The key insight is selecting at page granularity rather than individual tokens, which maps cleanly to GPU memory access patterns. Generality across modalities is the standout here.

**HQMQ: Quaternion Quantization for KV Cache**
[arXiv:2605.27646](https://arxiv.org/abs/2605.27646) · Rescored relevance: 88

Calibration-free KV cache quantization using Hurwitz quaternion lattices as a multiplicative codebook. Matches KIVI-4 quality at 16% fewer bits (5.05× compression). Works out-of-the-box across Llama, Qwen, Mistral, Gemma, and Phi — no per-model tuning. Mathematically elegant and practically useful; the calibration-free property removes a real deployment friction point.

---

*Three ICML 2026 acceptances in one batch — KV cache compression is clearly the hottest subfield in inference right now. The common thread: methods that require zero training and drop into existing stacks. The era of "just quantize your weights" is giving way to compressing everything else too.*

---

## Surge Watch

[MinT](https://arxiv.org/abs/2605.13779) landed with a staggering 202 HF upvotes on day one — by far the highest launch in our tracker this cycle. Mind Lab's managed infrastructure for training and serving millions of LLMs clearly struck a nerve; upvotes have since climbed to 217.

[Continuum](https://arxiv.org/abs/2511.02230) is accelerating in academic circles — citations jumped from 20 to 24 with a new influential citation in the 05-27/05-28 window alone, while GitHub stars ticked up from 75 to 80. KV cache TTL for multi-turn agent scheduling is proving timely as agentic workloads scale.

[TEAM](https://arxiv.org/abs/2602.08404) saw a sharp citation spike from 1 to 4 overnight (05-27→05-28) — temporal-spatial expert activation for MoE diffusion LLM acceleration is suddenly getting noticed. [Capacity-Aware Inference](https://arxiv.org/abs/2503.05066) is on a similar trajectory, climbing from 9 to 12 citations with a second influential citation, as MoE straggler mitigation becomes a real production concern.

Fresh launch to watch: [EdgeRazor](https://arxiv.org/abs/2605.04062) debuted at 27 HF upvotes and 44 GitHub stars — mixed-precision quantization-aware distillation for on-device LLMs is drawing immediate practitioner interest.
