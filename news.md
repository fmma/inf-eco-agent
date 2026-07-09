All 8 PDFs read. After full-text rescoring, here's the bulletin (top 5 by rescored relevance):

# Inference Ecosystem — Flash News
*2026-07-09 · 701 papers scanned · 5 picks*

The through-line this week: **match hardware to phase, and push work off the critical path.** Cross-vendor cost plays, MoE-aware routing, and two-dimensional KV compression all landed on real silicon.

## [HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators](https://arxiv.org/abs/2606.29986)
HMA-Serve is the first real-silicon demo of *cross-vendor* prefill/decode disaggregation: cheap GDDR Tenstorrent Blackhole chips (~1/10 the per-chip price of an A100) run compute-bound prefill in BFP8, HBM A100s run decode in BF16. It turns the precision/format mismatch into a lever — a layer-wise compute-transfer pipeline hides KV egress, and deferred dequantization ships raw BFP8 bytes to reconstruct lazily on the GPU's *integer ALU* (disjoint from the tensor cores decode saturates). Result: up to 3.2× goodput and **4.8× goodput-per-dollar** over homogeneous A100 disaggregation with no measurable quality loss — the clearest signal yet that the cheapest serving point lies *across* vendors. Score: 95 (was 95)

## [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/abs/2607.00760)
Prior KV compression squeezes either the sequence *or* channel dimension; MosaicKV does both via per-vector element selection and per-segment dynamic strategies, dodging the 82.8% accuracy collapse naive two-D compression causes. The systems half is the win: packed sparse attention runs on idle CUDA cores (memory bandwidth is 90% saturated while CUDA cores sit at ~10%) with CPU-side double-buffering hiding compression management. On H800 it delivers up to 16× attention speedup, 4.8× lower decode latency, 7.3× throughput and 3× memory savings at just 1.76% accuracy loss — pushing the single-request context ceiling to ~1.44M tokens. Score: 92 (was 93)

## [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466)
MoE decode latency is set by the *union* of distinct experts a batch activates, not by load — on Qwen3-30B-A3B, going from 16 to 128 active experts raises MoE-layer latency 4.7× at fixed batch size. ELDR builds a per-request "expert signature" from prefill activations (which predict decode experts at r=0.70–0.92), clusters it with balanced K-means, and routes within a locality band that still respects live load; a block-granular signature cache keeps it coherent under prefix caching. In vLLM on up to 40 GPUs it cuts median TPOT 5.9–13.9% with **outputs identical to standard top-k gating** — a new, lossless routing axis you can bolt on. Score: 91 (was 92)

## [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/abs/2606.30389)
Dynamic sparse attention hides a serialized selection→attention dependency that swells to 71% of decode latency at 512K context. PRR exploits the ~68% temporal overlap in consecutive top-K selections: an EMA predictor (hitting 98% overlap) speculates attention over likely blocks while selection is in flight, then a custom FlashAttention repair kernel folds missed blocks into the partial output via online-softmax — so cost scales with *misses*, not total blocks. Up to 40% lower per-token latency (1.42× over Quest, 1.56× over InfLLM-v2) across 6 LLMs with identical accuracy, kernel released. Score: 90 (was 92)

## [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/abs/2607.00151)
Context engineering (offloading, summarization, sub-agent isolation) invalidates the KV cache and forces re-prefill, spiking agent TTFT. SmoothAgent's insight: these transforms are *segment-decomposable*, so a lookahead runtime asynchronously precomputes the transformed KV caches and swaps them in without blocking, guarded by an SLO-aware scheduler that runs lookahead as best-effort work. Integrated into MiniAgent, LangChain, LlamaIndex, AutoGen and OpenClaw, it cuts transform-point TTFT by up to **11.9×** (summarization) — directly relevant as long-horizon agents become the dominant serving workload. Score: 89 (was 92)

---

## Surge Watch

[DFlash](https://arxiv.org/abs/2602.06036) is the quiet compounding story this cycle: citations 32 → 43 and influential citations 14 → 18 over three weeks, and still ticking up day-to-day. Block-diffusion speculative decoding is graduating from novelty to a cited baseline — the healthiest kind of adoption, with almost no social noise driving it.

[Gated DeltaNet-2](https://arxiv.org/abs/2605.22791) (NVIDIA) just found academic footing after weeks of flatline: 2 → 6 citations with its first 2 influential ones, and GitHub stars 185 → 233. The erase/write decoupling in linear attention is starting to get picked up rather than just admired.

[TokenPilot](https://arxiv.org/abs/2606.17016) keeps accelerating past last cycle's breakout — GitHub stars jumped 36 → 45 in a single day. Cache-efficient agent context management remains the pain point everyone's racing to solve.
