All 8 PDFs read. After rescoring on full text, here is the bulletin:

# Inference Ecosystem — Flash News
**2026-11-13 · 5 papers**

Agentic KV tiering, batched early-exit, and intra-GPU parallelism lead today's drop.

### [Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI](https://arxiv.org/abs/2606.00866)
MORI (Stoica group) ranks agent programs by "idleness" — their recent fraction of time spent in tool calls — and uses that one relative metric to place KV caches across HBM, DRAM, and a drop tier, with admission control at both tiers plus proactive promotion. On real Claude Code and Codex traces (Qwen2.5-7B, gpt-oss-120b, Qwen3-235B), it delivers 64% higher throughput and 72% lower p90 TTFT than the best offloading baseline, and keeps 24% more throughput even at a 1:4 GPU:CPU split. With agentic loops now the dominant serving pattern, this is the KV-tiering policy to copy. Score: 92 (was 90)

### [Batched Early-Exit LLM Inference Done Right with DREX](https://arxiv.org/abs/2512.15705)
DREX introduces cross-iteration batching: continuing tokens wait at the exit layer and one deep pass every k steps amortizes the deep-weight read across many tokens, with a "speculative holding" variant that keeps held tokens decoding from the exit layer's own guess. Built on vLLM with a calibrated cost-model controller, it hits 2.22–2.24× decode speedup on Llama-2-70B and 1.58–1.91× on real LayerSkip CNN/DM within 1.4 ROUGE-2 points — 9–63% ahead of EAGLE — and never forces an exit, so it adds no quality loss of its own. Score: 90 (was 92)

### [SubGPU Pipelining: Intra-GPU Fine-Grained Spatial Parallelism for LLM Inference](https://arxiv.org/abs/2611.14904)
NVIDIA cuts a decode layer's operator graph into contiguous segments bound to disjoint SM pools via CUDA Green Contexts and streams microbatches through them, overlapping the memory- and compute-bound kernels that temporal execution serializes. Simulation of GPT-OSS 120B on 32×B200 shows up to 2.2× higher per-user throughput at matched per-GPU throughput; a real two-stage Blackwell prototype raises mean DRAM utilization from 71.8% to 83.6% and cuts iteration time 10.33% with zero kernel changes. A credible glimpse of the next axis of serving parallelism. Score: 90 (was 93)

### [Read Once, Answer Many: Parallel Prompting for Shared-Context LLM Inference](https://arxiv.org/abs/2611.15130)
For workloads asking many questions about one long document (doc QA, labeling, LLM-as-judge), Parallel Prompting decodes P questions as P independent streams of a single request, reading the shared KV once per step instead of once per question via an in-kernel stream-id mask. In ~80 lines on SGLang (CUDA-graph compatible), it is 3.7× faster than stock SGLang+FlashInfer on an A100 and wins all 144 paired runs; gains shrink to 1.3–1.9× on GQA models and with long answers. Dead-simple to adopt for offline shared-context batches. Score: 87 (was 92)

### [Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading](https://arxiv.org/abs/2611.15842)
Measuring real CPU→GPU copies for OLMoE-1B-7B, this paper shows the eviction rule, not the router, is the lever that matters: evicting the expert whose next use lies farthest in the future (Belady) copies 2.1× fewer experts than LRU at zero quality loss, within 3.5% of optimal. Sixteen tokens of lookahead recover 96% of the gain, while learned temporally-extended routing and GRPO router fine-tuning fail to beat plain LRU. A clean, immediately actionable result for anyone running MoE offloading. Score: 86 (was 90)

---

## Surge Watch

**[The Other Half of the Memory Wall](https://arxiv.org/abs/2609.18063) just crossed 10k GitHub stars** — 9,170 → 10,434 (Nov 9 → Nov 13), still ~300 stars/day on top of the tripling I flagged last week. The SSD-MoE-serving repo remains the one signal with real staying power — stars don't backfill, and this one hasn't flinched. But HF upvotes have gone flat (29 → 30): the pull is now entirely on the code side, not the paper side.

Otherwise it's quiet. The eye-catching citation jumps topping the gain list (DFlash, DSpark, Domino, etc.) are the same Semantic Scholar backfill from yesterday's note — synchronized across unrelated topics, not momentum. And HF upvotes remain depressed across the board from the early-November bookkeeping reset, with no fresh breakout stepping in to replace REAP or Continuum.
