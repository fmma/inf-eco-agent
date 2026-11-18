I've now hit three independent walls, so let me be straight about the situation before giving you something useful.

**I could not open the 8 PDFs in this environment.** The Read tool renders PDFs as images via `pdftoppm`, and `poppler-utils` isn't installed on this host. My two fallbacks were both blocked by permission approvals that can't be granted in a non-interactive session: extracting text with `python3` (gated — `ls`/`cat` are allowed, but code execution isn't), and pulling the arXiv HTML full text via WebFetch (gated — "permission not granted"). The PDFs themselves are present and intact in `data/pdfs/`; the problem is purely that nothing here can decode them.

Note this is a local-host gap, **not** a production problem: the scheduled scan runs on `foadell` with `poppler-utils` installed and `--allowedTools "Read"`, so the real pipeline's Read step works. To make full-text rescoring work *here*, either `sudo apt-get install poppler-utils`, or allow `Bash(python3:*)` / WebFetch for this session.

Because the abstracts you passed are unusually detailed (full method names, baselines, and numbers), here's a **best-effort bulletin built from those abstracts**. The relevance scores are my judgment from the abstracts — not the full-text rescore this step is supposed to do — so treat them as provisional, and I did **not** fabricate any full-text-only detail.

---

# Inference Ecosystem — Flash News
**2026-11-18 · 508 papers scanned · top 5** — *abstract-based; PDFs were not readable in this run*

### [Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models](https://arxiv.org/abs/2611.23228)
Training-free sliding-window inference for hybrid (attention + Gated DeltaNet) VLMs. Spool caches each frame's affine state transformation and composes them associatively, so expired frames are removed from every recurrent layer's state *exactly* — no replaying the window through the backbone — backed by a custom data structure and GPU kernels. Across 5 open hybrid VLMs and 4 video-reasoning benchmarks it posts the lowest p95 TTFT in all 20 combos: **6.6× geomean** over the faster of two recent vLLM baselines, while adding 2.3pp accuracy. Streaming video/robotics agents on recurrent-hybrid backbones are the frontier, and sliding-window eviction over recurrent state was the blocker. Score: 95.

### [Storing the Gemma 4 K=V Cache Once](https://arxiv.org/abs/2611.23035)
A model-specific KV trick with **zero kernel changes**: in Gemma 4 31B's global-attention layers the value is the normalized key projection and the key is the value times a fixed weight, so one 640-value row can stand in for the full 1024-value key *and* value — exact in real arithmetic, read by a stock paged-attention kernel through two overlapping strided views. A vLLM prototype is bit-identical (2/432 answers differ, within run-to-run noise) and cuts steady decode KV memory **1.34–1.40×** at 32K–64K; on an A100 prefill/decode pair with NIXL it runs 1.38×/1.24× more decode tokens per step (16K/8K prompts) and lifts eager decode throughput 1.30×/1.11×. Caveats: the runtime prototype makes an eager step 4–9% slower and doesn't yet stack with an 8-bit KV cache. Anyone serving Gemma 4 is leaving the report's advertised 37.5% global-KV saving on the table — this reclaims it. Score: 92.

### [XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools](https://arxiv.org/abs/2611.22280)
Sparse-attention KV offloading for emerging scale-up memory pools (e.g. X-Mem). The insight: even with a big pool, decode stays HBM-bound because hot KV buffers and the resident indexer-key (K-index) cache occupy HBM, and the two have distinct access patterns — so XM-Sparse offloads both and matches each to a tailored I/O path (TMA-based retrieval fused with attention in a tile-level pipeline for dynamic KV; SM-efficient GPU-initiated DMA prefetch for the predictable K-index). Built on SGLang, on DeepSeek-V3.2 and GLM-5.3 it delivers up to **4.98×/4.52×** higher decode throughput than PCIe-based ECHO/HiSparse and up to 1.34× over a naive integration, across 16K–1M contexts. This is precisely where long-context serving is heading: sparse attention plus CXL-class memory expansion. Score: 92.

### [Lost in a Few Heads: Diagnosing and Repairing Block Selection in Sparse Attention](https://arxiv.org/abs/2611.21917)
A sharp diagnosis of why block-sparse attention loses long-context retrieval at a fixed budget — not budget exhaustion, but a handful of "blind heads" that under-rank the needle because a mean-pooled key summary dilutes its decisive token. A teacher-forced calibration probe finds them, and restoring full attention (or a 4-bit scorer at the same budget) in *only* those heads fixes it with no training: MiniCPM4.1-8B at 64K goes **54.1→97.5%** multi-key retrieval; on Qwen3-8B with SeerAttention-R gates, fixing 18 of 288 KV heads goes 29.8→97.7%. In production engines, full attention in those few heads still keeps 84–89% of the TTFT sparse attention saves at 32K–128K — and the pattern holds across InfLLM-V2, NSA, DashAttention, SeerAttention-R and MoBA. A cheap, training-free accuracy patch for the sparse attention everyone is shipping. Score: 91.

### [JigSLO: Solving the Resource Puzzle for Efficient Multi-LLM Serving](https://arxiv.org/abs/2509.06261)
Contention-aware multi-LLM serving for GPU spatial sharing — the first to model memory-*bandwidth* contention between co-located instances, via a time-shared access model (contended/uncontended periods → a time-weighted latency estimate) that predicts per-instance latency under any co-location from standalone profiles alone. It schedules prefill and decode as separate instances, jointly selects tensor parallelism, compute share and batch, and pools/transfers KV prefill→decode. Across chat, code, and long-context summarization it beats SOTA by **2.3× in SLO attainment and 1.2× in throughput**, matching the best attainment with half the GPUs on long-context. Bandwidth contention is the usually-unmodeled gap that makes spatial sharing underperform. Score: 90.

---

Want me to proceed differently? If you install `poppler-utils` (or grant `python3`/WebFetch) and re-run, I'll do the real full-text read and rescore across all 8 PDFs — including MiSTiQ, HyCoInfer, and the EPD-disaggregation energy paper, which I left out of the top 5 above on abstract strength alone.

---

## Surge Watch

**DeepSeek's KV-compression flagship is the citation story this cycle.** [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) has climbed 55→191→225 citations since mid-October and is *still* moving — 216→225 in just the last two days — with influential citations up to 11. The field is absorbing it fast, and it sits dead-on the KV-cache theme everyone's building around.

**FlashAttention-4 cleared the 100 line.** [FlashAttention-4](https://arxiv.org/abs/2603.05451) jumped 77→111 citations with influential citations doubling (11→22) — the kernel layer compounding right alongside the KV tricks stacked on top of it.

**SSD-served MoE is a GitHub sleeper hit.** [The Other Half of the Memory Wall](https://arxiv.org/abs/2609.18063) has ridden ~3.1K→11.7K stars since mid-October and is still climbing, while HF upvotes stay modest at 31 — real adoption outrunning the paper's buzz.
