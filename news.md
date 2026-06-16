# Inference Ecosystem — Flash News
**2026-06-16 | 409 papers scanned, 5 selected**

### [Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing](https://arxiv.org/abs/2606.16264)
Neither disaggregated nor non-disaggregated LLM serving alone nails both TTFT and TPOT SLOs — disaggregated systems suffer from prefill queuing while non-disaggregated ones get wrecked by prefill-decode interference. Tropical introduces SLO-aware multiplexing that piggybacks short prefills onto decode workers during their TPOT slack windows, achieving Pareto-optimal TTFT/TPOT attainment. Evaluated on real Mooncake traces with InternLM-20B across 8xA100s, it serves 2.09x more requests at 90% SLO attainment versus both vLLM and DistServe. A clean systems idea with immediate practical value for anyone running disaggregated serving.
**Score: 92 (was 95)**

### [SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing](https://arxiv.org/abs/2606.16135)
Multi-turn conversations accumulate massive KV caches that must be reloaded from CPU/SSD over slow PCIe, dominating TTFT. SwiftCache exploits idle GPU memory on co-located low-demand models to store prefix KV caches, transferring them over NVLink (400 GB/s) instead of PCIe (32 GB/s). A layer stream cache keeps only the active layer's KV locally, expanding max context length up to 3.98x. On real ShareGPT/L-Eval workloads with Qwen3 and LWM models on H20 GPUs, it cuts P99 TTFT by up to 69% versus vLLM and SGLang with under 10% interference to co-located models. The elastic cache with O(1) block-major resizing is a particularly elegant contribution.
**Score: 93 (was 95)**

### [CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering](https://arxiv.org/abs/2506.11418)
Published in TMLR, CentroidKV merges KV cache entries within similarity-based clusters using a novel Chunked Soft Matching algorithm — an adaptation of bipartite soft matching from vision transformers to KV cache compression. The alternating partition strategy within chunks is proved optimal, and complexity drops from O(n²d) for naive pairwise to O(ncd) where c is chunk size. Achieves 75% KV cache memory reduction while maintaining accuracy on RULER and LongBench, with 1.92x decode speedup and 4x serving throughput in vLLM integration. The theoretical grounding and clean experimental story make this a reference point for the KV cache compression space.
**Score: 90 (was 95)**

### [Approaching Shannon Bound with Lossless LLM Weight Compression](https://arxiv.org/abs/2606.15789)
A systematic entropy analysis across models from 1.5B to 405B reveals that LLM weights store 2-10x more bits than their information content requires — even INT4 weights have massive redundancy due to heavy-tailed distributions. The paper introduces tile-level ANS decompression fused directly into the GEMM pipeline, decoding compressed weight tiles into shared memory exactly when tensor cores need them, achieving bitrates within 0.01-0.1 bits of Shannon's limit. Integrated into SGLang, Mixtral-176B goes from batch 20 to batch 95 (4.8x), yielding 1.6x throughput. Outperforms NeuZip by 11x and DFloat11 by 7x. This is strictly lossless — zero accuracy loss — making it complementary to any quantization scheme.
**Score: 90 (was 93)**

### [Service-Induced Congestion in Memory-Constrained LLM Serving](https://arxiv.org/abs/2606.15555)
A rigorous dynamical-systems analysis of a failure mode unique to LLM serving: KV caches grow during service, so memory pressure is *created* by the serving process itself. The paper proves that under standard continuous batching, the eviction-free equilibrium is unstable — the system converges to a worst-case limit cycle with up to 50% throughput loss. For heterogeneous workloads, stability depends on whether decode lengths are coprime (a striking number-theoretic result). Validated in Vidur and on real GPUs with SGLang. Rate-limited admission and request mixing are proposed as countermeasures. A foundational theoretical contribution that every inference engineer managing memory-constrained deployments should understand.
**Score: 88 (was 95)**

---

## Surge Watch

[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) is this cycle's standout debut — HF upvotes surged 83→131 and GitHub stars nearly doubled from 184→293 in just 3 days (Jun 13–16). A production sparse attention paper from MiniMax gaining this kind of traction this fast signals serious practitioner interest.

[DFlash](https://arxiv.org/abs/2602.06036) (block diffusion for speculative decoding) quietly crossed the 5K GitHub stars milestone, climbing 4750→5117 over two weeks with citations also ticking up 21→32. Sustained, broad-based growth rather than a spike — this one has legs.

[KVarN](https://arxiv.org/abs/2606.03458) has plateaued at ~400 stars (up just 7 since Jun 13) and HF upvotes frozen at 60. The breakout reported last time is definitively over. [Domino](https://arxiv.org/abs/2605.29707) tells the same story: 145 HF upvotes and 64 stars, modest single-digit gains from the explosive debut numbers. The speculative decoding training wave has crested.

Worth watching: [VIA-SD](https://arxiv.org/abs/2606.12243) (intra-model routing for speculative decoding verification) jumped 0→32 HF upvotes in 4 days — early but sharp signal for a fresh spec-decode verification approach.
