I've read all 8 PDFs. Here's the bulletin, with relevance rescored from the full texts.

# Inference Ecosystem — Flash News
2026-09-29 · 900 papers scanned · top 5 picks

### [Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs](https://arxiv.org/abs/2609.33477)
The first prefix cache that gives hybrid (full + linear attention) LLMs the same page-level reuse as vanilla transformers, *without* materializing recurrent-state checkpoints — it stores sparse hidden-state "anchors" and rebuilds the linear state by replaying a short suffix, leaning on the recurrence's own decay to forget old inputs. In SGLang it retains 91.4–100% of full-prefill quality on LongBench/RULER at 0.36–0.51× the storage of SGLang's 8192-token checkpoint cache, cuts median TTFT 15–70% on branching workloads, and sustains 2.3–4.3× throughput once the working set exceeds HBM. Scores high because hybrid models (Qwen3.5/3.6, Kimi Linear, Nemotron-H) are everywhere now and their prefix caching is a live open problem — this is real algorithm-system co-design in a production engine. Score: 92 (was 95)

### [PQ-HSA: Reusing Product-Quantized Scores for Hybrid Sparse-Approximate Attention](https://arxiv.org/abs/2609.33746)
Clean insight: the IVF-PQ scores you compute to *rank* keys for sparse selection can double as *logits* for the unselected "background," aggregated per inverted list with list value means under one softmax — no second scoring pass. At 128K/1–2% budget it beats Quest and SnapKV on Llama-3.1-8B and Qwen3-30B-A3B (the background term alone lifts macro accuracy 0.71→0.83 on 8B) and stays near full attention; inside vLLM on one H20 the decode attention call runs 1.6× faster than FlashAttention-3, growing to 2.7× at 512K. A rigorous mechanism study plus a released vLLM plugin that runs on two engine versions unchanged make it immediately usable for long-context serving. Score: 90 (was 95)

### [Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving](https://arxiv.org/abs/2609.33536)
ElasticKV decouples *execution-readiness* from target KV fidelity: a compact BASE state (the high-order 8 bits of the 16-bit target) is directly executable and later refined back exactly, and a pair-structured layout turns two half-blocks into one reclaimable GPU block. On vLLM under high concurrency it delivers 3.8–4.0× lower mean and 9.1× lower P90 TTFT while eliminating preemptions (e.g. 4989→0 on Qwen3-8B), validated on both A100 and AMD MI355X. The framing — fidelity as a runtime-managed execution property that kills the preemption-driven TTFT knee — is genuinely novel and cross-vendor. Score: 89 (was 95)

### [EfficientAgent: What Makes KV Cache Offloading Work for Concurrent Agents?](https://arxiv.org/abs/2609.33762)
Explains why KV offloading is inconsistent for agents: a cached prefix survives only if the host tier holds the whole pool's *reuse working set* ((A−1)·N̄·β_rank), which a stack-distance model sizes and predicts before deployment. On SWE-bench Verified coding agents (Qwen3-Coder-30B-A3B, 8×H20), a tier sized to the ~11.4 GiB working set cuts recomputed prompt tokens 93% and end-to-end time 39%; payoff hinges on compute-per-host-byte (pays on RTX 3090/H20, loses on H800). Turns offloading from folklore into a predictable design decision right as agentic/RL-rollout serving explodes, with replay tooling and code released. Score: 88 (was 95)

### [SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving](https://arxiv.org/abs/2609.34117)
Since MoE prefill is compute-bound (pruning buys little) but decode is expert-weight-bound, SlimWise runs full-model prefill and hands its KV cache straight to a pruned decoder — no conversion, because pruning preserves KV format — then recovers residual accuracy with a distillation stage that updates just 0.42–2.12% of params. Implemented in vLLM for both PD-disaggregated and PD-colocated (phase-aware router masking) serving, it hits up to 1.81× decode throughput at 50% pruning (2.39× at 75%) on Qwen3.6-35B-A3B with minimal accuracy loss. Bonus finding worth heeding: benchmark accuracy hides large pruning-induced swings in reasoning length. Score: 87 (was 95)

---

## Surge Watch

[Flash-dLLM](https://arxiv.org/abs/2609.26796) is the cycle's standout accelerant: it nearly tripled on HuggingFace — **13→36 upvotes and 8→17 GitHub stars in five days (09-24→09-29)** — even as last cycle's discrete-diffusion breakout, [Unlocking Lossless Speedups](https://arxiv.org/abs/2609.04010), flattens at ~113. The diffusion-inference torch is passing.

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) refuses to plateau: its cold open compounded from **174→188 HF upvotes (09-24→09-29)**, still the clear leader of the recent debut board rather than fading like most launch-day spikes.

Quantization is quietly pulling fresh eyes: [Disaggregated Quantization](https://arxiv.org/abs/2609.26333) (Alistarh et al.) opened at **45 HF upvotes** from a standing start, and [HyQuant](https://arxiv.org/abs/2608.27875) surged **~0→29** after weeks flat — first real traction for both.
