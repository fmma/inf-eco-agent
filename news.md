# Inference Ecosystem — Flash News
**2026-04-14 | 592 papers scanned**

### [Tessera: Unlocking Heterogeneous GPUs through Kernel-Granularity Disaggregation](https://arxiv.org/abs/2604.10180v1)
Tessera is the first system to disaggregate LLM inference at the GPU *kernel* level across heterogeneous clusters. By extracting inter-kernel dependencies from PTX and scheduling compute-bound kernels to high-FLOPS GPUs while routing memory-bound ones to high-bandwidth cards, it achieves up to 2.3x serving throughput and 1.6x cost efficiency over prefill-decode or attention-FFN disaggregation. Evaluated across five GPU types (A100 through B200) and four model families including Mamba and diffusion models — unlike prior methods that only work on standard Transformers. The killer result: an A100+L40s pair under Tessera *beats* two homogeneous A100s at lower cost.
Score: 96 (was 95)

### [Transactional Attention: Semantic Sponsorship for KV-Cache Retention](https://arxiv.org/abs/2604.11288v1)
Identifies a fundamental blind spot in all existing KV-cache eviction methods: "dormant tokens" like API keys and credentials that receive near-zero attention but are critical for agentic function-calling. At K=16 tokens (0.4% of context), six baselines (H2O, TOVA, SnapKV, StreamingLLM, PyramidKV, DynamicKV) score 0% on credential retrieval — Transactional Attention hits 100% via structural anchor patterns that "sponsor" adjacent value tokens. TA-Fast drops all attention terms for FlashAttention compatibility with 52% less memory. Orthogonal to any existing compression method at <1% latency overhead. Directly relevant as LLMs move to multi-turn tool-calling workflows where state must survive aggressive cache compression.
Score: 92 (was 95)

### [IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs](https://arxiv.org/abs/2604.10539v1)
Published at ICLR 2026. Instead of storing KV-cache pages by token order, IceCache clusters semantically similar tokens into the same pages via a hierarchical DCI-tree, then retrieves the top-k most relevant pages per attention head during decoding. With just a 256-token budget, it retains 99% of full-KV accuracy on LongBench across Llama-3.1-8B, Mistral-7B, Qwen3-32B, and LongChat-7B. Even at 64 tokens it beats PQCache at 256. The pipelining scheme that overlaps CPU-side DCI indexing with GPU computation keeps overhead practical. Scales to 300k tokens on RULER with minimal latency degradation.
Score: 91 (was 92)

### [SpecMoE: Efficient MoE Inference via Self-Assisted Speculative Decoding](https://arxiv.org/abs/2604.10152v1)
Tackles the PCIe bandwidth wall in CPU-offloaded MoE serving by turning the target model into its own draft model: pin the hottest N experts per block on GPU, speculate without any CPU-GPU transfers, then verify all draft tokens in one coalesced batch. No retraining, no separate draft model, no extra memory. On NLLB-MoE (128 experts/block) with an H100, SpecMoE delivers 4.30x throughput at batch-256 and cuts CPU-to-GPU transfer by 76.7%. Also works on low-hotness models like Mixtral-8x7B (2.17x) and Llama-4-Scout (1.42x). The affinity-based expert selection mechanism handles routing mismatches at <200KB overhead.
Score: 90 (was 93)

### [WaveTune: Wave-aware Bilinear Modeling for Efficient GPU Kernel Auto-tuning](https://arxiv.org/abs/2604.10187v1)
Discovers that GPU kernel latency follows a *wave-conditioned piecewise bilinear* pattern — step-like at small grids, linear at large — and exploits this physical structure for microsecond-level runtime config selection. A sparse profiling phase builds per-config bilinear models indexed by wave count; at runtime, a dual-table lookup picks the optimal tile/warp/pipeline config in 5-6 microseconds (vs. milliseconds for XGBoost cost models or seconds for brute-force). Delivers up to 1.83x kernel speedup on FlashAttention and 1.33x end-to-end TTFT reduction on Qwen3-30B-A3B, tested across A100, H20, B200, MI308X, and MI355X. Production-ready overhead profile.
Score: 88 (was 93)

---

## Surge Watch

[MegaTrain](https://arxiv.org/abs/2604.05091v1) crossed 400 GitHub stars — 313 → 404 in two days. Growth rate is moderating (+91 vs. last report's +123 burst) but it's still the fastest-cloning repo in this batch. HF upvotes inching up to 43, confirming the practitioner-over-researcher split.

[MARS](https://arxiv.org/abs/2604.07023v1) correction: called it stalled last time at 29/15, but it's now 34 HF upvotes and 18 stars — a quiet but real uptick. Multi-token generation for autoregressive models is finding a slower-burn audience than the initial spike suggested.

[DMax](https://arxiv.org/abs/2604.08302v1) is decelerating: 38 → 45 HF upvotes and 75 → 92 stars in two days, versus +21/+70 in its debut window. Healthy adoption for a diffusion LLM decoding paper, but not a runaway.

[Mamba-3](https://arxiv.org/abs/2603.15569v1) is the quiet academic mover — citations jumped from 10 to 13 (latest reading) with 1 influential, while HF upvotes sit at just 6. Researchers are citing it; practitioners aren't starring it.

TriAttention, Attention Residuals, and TAPS have all flatlined — still big numbers, but the growth stories are over.
