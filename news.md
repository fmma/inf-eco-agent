I'm unable to read the PDFs directly — `poppler-utils` isn't installed and my file write/script permissions are being denied. I'll rescore and write the bulletin based on the detailed abstracts provided, which contain substantial technical detail.

**Rescored relevance** (abstract-based adjustment):

| Paper | Original | Rescored | Notes |
|-------|----------|----------|-------|
| YOCO/CLSA (2606.06467) | 93 | 96 | 7.6x decode + 17.1x throughput at 128K — most impactful single result |
| Vortex (2606.06453) | 92 | 94 | Programmable sparse attention + AI-agent-driven search, B200 results |
| Tangram (2606.06302) | 95 | 94 | Clean system design, 2.6x throughput, open-source |
| RedKnot (2606.06256) | 95 | 88 | Ambitious scope but abstract is heavy on vision, light on benchmarks |
| SlidingServe (2606.05933) | 95 | 90 | Solid SLO-aware scheduling, 30% capacity gain |
| QCFuse (2606.05875) | 92 | 90 | Practical RAG prefill speedup in SGLang |
| Prefill-Decode Control (2602.02987) | 95 | 82 | Theoretical framework — strong but less immediately deployable |
| AdaPLD (2606.05742) | 90 | 85 | Good spec-dec results but incremental over prior retrieval-based methods |

Top 5 selected: CLSA, Vortex, Tangram, SlidingServe, QCFuse.

# Inference Ecosystem — Flash News
**2026-06-05 — 361 papers scanned**

## [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467)

Microsoft Research (Furu Wei's group) extends the YOCO KV-sharing architecture with cross-layer sparse attention (CLSA): a single indexer computes token-level top-k selection once and reuses the routing index across all cross-decoder layers, amortizing the cost that usually kills token-sparse methods. The result is **7.6x decoding speedup and 17.1x overall throughput improvement at 128K context** — the kind of numbers that make you rethink your long-context serving stack. This is the most complete architectural answer yet for jointly solving prefill, KV storage, and decode bottlenecks in long-context models.
**Score: 96 (was 93)**

## [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453)

Beidi Chen's group ships a system that splits sparse attention into a Python-embedded frontend language (for rapid algorithm prototyping) and an efficient backend integrated into production serving stacks. The killer feature: AI agents use Vortex to *automatically search* for sparse attention algorithms, with the best found variant hitting **3.46x throughput over full attention** while preserving accuracy. Tested on MLA-based GLM-4.7-Flash (4.7x throughput) and the 229B MiniMax-M2.7 on B200 GPUs. This turns sparse attention from a research exercise into a deployable, searchable design space.
**Score: 94 (was 92)**

## [Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302)

Makes non-uniform KV compression actually work in production serving. Three techniques — deterministic per-head budget allocation (eliminating dynamic scheduling overhead), head-group paging (maximizing memory reclamation), and ahead-of-time load balancing — solve the fragmentation and scheduling nightmares that previously made heterogeneous KV cache impractical. Delivers **2.6x throughput improvement** over baselines with no accuracy loss. Code is open-source at [github.com/aiha-lab/TANGRAM](https://github.com/aiha-lab/TANGRAM).
**Score: 94 (was 95)**

## [Beyond Greedy Chunking: SLO-Aware Sliding-Window Scheduling for LLM Inference](https://arxiv.org/abs/2606.05933)

SlidingServe introduces a sliding-window scheduler that looks ahead to the next iteration when deciding chunk sizes, paired with a lightweight batch latency predictor and dynamic-programming-based request selection under SLO pressure. The combination yields **30% higher service capacity** and **16–53% fewer SLO violations** under heavy load compared to existing chunked-prefill schedulers. Practical for anyone running SLO-bound serving where greedy chunking leaves throughput on the table.
**Score: 90 (was 95)**

## [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875)

Tackles the RAG prefill bottleneck in SGLang with a compressed-view selector: chunk-anchor query probing conditions user-query states on compact per-chunk anchors, while critical-layer profiling identifies which tokens to recompute — all without stalling the layer-wise cache-fusion pipeline. Achieves **1.7x prefill speedup** over full prefill and 1.5x over ProphetKV across four LLMs and six datasets, matching full-prefill quality. If you're serving RAG workloads, this is the KV-reuse approach to watch.
**Score: 90 (was 92)**

---

## Surge Watch

[DFlash](https://arxiv.org/abs/2602.06036) (Block Diffusion for Flash Speculative Decoding) is this cycle's breakout — 27 citations with 13 influential (48% influential ratio) as of 06-05, up from 21/8 just five days earlier. When nearly half your citers consider you a key reference, you're becoming foundational infrastructure for diffusion LLM decoding. 4,750+ GitHub stars confirm production-level interest.

[dMoE](https://arxiv.org/abs/2605.30876) (dLLMs with Learnable Block Experts) is catching fire fresh off the press — 21→36 HF upvotes in 3 days with a new paper that fuses MoE routing into diffusion LLMs. The dLLM design space is clearly still in its rapid expansion phase.

[Act While Thinking](https://arxiv.org/abs/2603.18897) quietly climbed to 8 citations (from 0 in early April), all on speculative tool execution for LLM agents. The agentic inference stack — not just serving, but tool-call acceleration — is becoming its own citation cluster.

[Hyperloop Transformers](https://arxiv.org/abs/2604.21254) went from 0 to 6 citations (2 influential) in six weeks, a fast ramp for a novel recurrent-in-depth architecture. Weight sharing for inference efficiency is drawing early adopters.

Previous cycle's standouts have entered plateau: Continuum, Mamba-3, and TokenCake all held flat on their last readings (29, 46, and 9 citations respectively). The initial surge is over — now it's about who integrates.
