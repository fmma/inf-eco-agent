# Inference Ecosystem — Flash News
**2026-10-08 · 331 papers scanned · 5 featured**

Sparse attention, KV-cache compression, and serving infrastructure dominate this batch — the three levers that matter most as frontier models push toward million-token context.

## [SPIN: Shadow Predictive Indexer for Sparse Attention](https://arxiv.org/abs/2610.09025)
NVIDIA targets the next bottleneck in DeepSeek Sparse Attention: the indexer that must still score the *entire* KV cache every decode step. SPIN predicts important KV blocks from exponential moving averages of prior-iteration scores (vertical + diagonal patterns), stays training-free at 30–40% block sparsity with no quality loss, and adds random exploration to refresh stale blocks. In vLLM on 8× B300 it lifts output throughput up to 14.9% and cuts median ITL up to 13.2% on DeepSeek-V4 — immediately relevant to anyone serving DSA-class models (DeepSeek-V4, GLM-5.2, MiniMax-M3, LongCat-2.0). Score: 91 (was 92)

## [Democratizing MoE inference on commodity GPUs with CoMoE](https://arxiv.org/abs/2610.09424)
A communication-efficient MoE system that turns the host into an active routing hub on consumer GPUs with no NVLink/P2P: host-backed token multicast kills dispatch redundancy, and a fine-grained host-staged combine replaces rigid All-to-All barriers. On RTX 5090 it hits up to 1.46× throughput over SGLang and reaches 85–90% of an A800+DeepEP node at ~23.4% of the hardware cost. Shipped as a drop-in SGLang backend — a compelling cost story for private, local MoE serving. Score: 91 (was 92)

## [Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches](https://arxiv.org/abs/2610.09827)
Resolves the conflict between key quantization (wants flat distributions) and query-channel pruning (wants sharp ones) via paired non-orthogonal Q/K transforms, plus channel-0 BF16 protection and bucket-relative RoPE. At 40% channel sparsity and INT2 it crushes OSCAR on long-context retrieval (Qwen3-4B RULER@64K: 81.5% vs 32.7%), delivers 6.8× KV compression at 128K, and its SGLang kernel reaches up to 3.75× decode throughput over BF16. Combines quantization *and* pruning into one deployable win. Score: 90 (was 90)

## [vLLM-Omni: A Unified Serving Runtime for Omni-Modality Generation](https://arxiv.org/abs/2610.09307)
The vLLM project's answer to heterogeneous multimodal serving: a single orchestrator over multi-stage pipelines (thinker→talker→vocoder, DiT, world-model, robot) with stage replicas, a control/data-split connector, and session control for duplex workloads. Concrete wins include async-chunk slashing Qwen3-Omni TTFT from 3420ms to 508ms at C=32, an MRv2 path halving E2EL, and a fused single-GPU Qwen3-TTS hitting 1.2–2.2× the two-stage throughput. If you're building speech/vision/action serving, this is the infrastructure to watch. Score: 89 (was 90)

## [Self-Indexing Attention for Compression-Compatible Sparse Long-Context Inference](https://arxiv.org/abs/2609.13205)
A training-free scheme that reuses randomized-Hadamard *key signs* as a 1-bit token-level index shared across prefill and decode — no separate indexer metadata, and compatible with external KV compressors like TurboQuant. At 5% attention density it stays near dense on LongBench/RULER while delivering up to 6.1× prefill and 10.3× decode attention-operator speedups. Swapping DeepSeek-V4-Flash's FP8 indexer for packed signs frees memory for +34% decode-pool capacity and +16.2% throughput. Score: 88 (was 90)

---

## Surge Watch

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) is the breakout this cycle — the KV-cache-compression report is compounding on both axes at once: **HF upvotes 191→224 in three days (10-03→10-06)**, one of the highest counts on the board, while citations tore **7→35 in ten days (09-25→10-04)** — the fastest cold-start-to-impact we've tracked.

The speculative-decoding complex that led last cycle is cooling as it matures: [DFlash](https://arxiv.org/abs/2602.06036) cleared **50 influential citations (123 total)** but its daily pace has flattened, and [DSpark](https://arxiv.org/abs/2607.05147) (40→41) and [Domino](https://arxiv.org/abs/2605.29707) (30→31) barely budged this week — the citation energy is rotating toward KV compression.

Steady climbers elsewhere: [Continuum](https://arxiv.org/abs/2511.02230)'s agentic KV-cache-TTL work ran **56→69 citations in ten days**, [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) reached **32 (up from 17 in early September)**, and on HuggingFace [Disaggregated Quantization](https://arxiv.org/abs/2609.26333) roughly doubled its upvotes to **92 (45→92, 09-29→10-06)** — a clean community breakout for the prefill/decode-specialized quant paper.
