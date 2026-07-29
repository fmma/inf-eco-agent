I need to stop and flag a real problem before producing anything, because I could not complete the required first step.

## The PDF-read step is broken in this session

All 8 `Read` calls on the PDFs failed with the same error:

```
pdftoppm is not installed. Install poppler-utils
(e.g. apt-get install poppler-utils) to enable PDF page rendering.
```

The `Read` tool renders PDF pages to images via `pdftoppm` (from **poppler-utils**), which isn't installed here. I tried to work around it by extracting the PDF text layer (pypdf/pymupdf/pdftotext via Bash, or a small helper script via Write), but **Bash and Write are gated in this non-interactive session** — every attempt returned "requires approval" and nothing was granted. So I genuinely cannot read the full texts, and I won't pretend otherwise or invent full-text details.

Root cause / where to fix:
- This working dir is your **local** machine; the automated agent runs on **foadell**. Verify poppler is present where `generate_news.py` actually executes: `apt-get install -y poppler-utils` (or `dpkg -l | grep poppler`). If foadell is missing it too, the nightly PDF-rescore step has been silently degrading.
- Worth adding a preflight check in `scan.sh` (`command -v pdftoppm`) so this fails loudly instead of quietly.

## Fallback bulletin (built from abstracts, **not** full-text rescored)

The abstracts already carry concrete numbers, so this is accurate — but scores are the original abstract-based ones, since I couldn't do the full-text rescore the prompt asks for. Treat the "(abstract-based)" tag as the honest caveat.

# Inference Ecosystem — Flash News
**2026-07-29 · 309 scanned · top 5 (abstract-based, PDFs unreadable this run)**

[AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/abs/2607.25852)
Unified training framework co-specializing two drafters — MTP for high-entropy chat, a block-diffusion backbone (DFly) for code/math — and treats verification as a shared batch-level resource, reallocating compute to high-confidence prefixes and adapting depth online. On Hy3-A21B: ~30% longer accepted length and 1.98–2.40× over autoregressive decoding, 10.5–11.8% above DFlash at concurrency 4–64. Matters because it tackles drafter-vs-workload heterogeneity at the serving layer, not just in a benchmark. Score: 93 (abstract-based)

[Kalypso: Relational LLM Serving](https://arxiv.org/abs/2607.23815)
Makes the serving engine query-plan-aware so KV-cache state pipelines across semantic operators (filter/join/rank/extract) instead of being recomputed, with a memory-aware scheduler balancing upstream parallelism against GPU pressure before eviction. Up to 4.57× faster query completion across diverse workloads. A new serving axis for LLM-as-operator / agentic data pipelines. Score: 92 (abstract-based)

[Beyond Prefill-Decode Disaggregation: Dynamic Operator Scheduling](https://arxiv.org/abs/2607.25498)
DOPS moves past PD disaggregation to operator-granular placement on heterogeneous NPU+PIM silicon: a stage-aware DAG, the "Bifocal" operator-to-device scheduler, and a Weight Layout Arbiter picking hardware-efficient layouts under memory limits. 1.20–2.23× geomean over the PD baseline, +1.28–1.33× from WLA; open-source (TriForm). Score: 92 (abstract-based)

[CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/abs/2607.25291)
Training-free sparse attention that couples a Kernel-Aware Proxy (emits an *ordered* KV-page visit mask) with an Ordered-Skipping Kernel that drops more blocks under a tightened budget using online-softmax stats. 4.93× attention speedup and 2.53× lower TTFT at 128K context with negligible quality loss. Directly targets long-context TTFT, the pain point of binary-mask sparsity. Score: 90 (abstract-based)

[DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/abs/2607.24434)
Makes spec-decode viable when routed experts are streamed from CPU/Flash: one accelerator-resident draft expert per layer (self-distilled), a fixed-footprint shared+top-1+draft drafter, confidence-expansion truncation, and target-expert prefetching. On DeepSeek-V2-Lite and Moonlight-16B-A3B (CPU-GPU and Flash-NPU): 1.45× decode throughput, 84–87% acceptance, 86–88% prefetch hit. Score: 88 (abstract-based)

---

Want me to (a) retry once you've confirmed poppler is installed / approved Bash so I can do the real full-text rescore, or (b) leave this abstract-based version as-is? I'd recommend (a) — the whole point of this step is the full-text adjustment, and three papers are separated by only 1–2 points.

---

## Surge Watch

**Unlimited OCR Works** ([2606.23050](https://arxiv.org/abs/2606.23050)) is the runaway repo of the fortnight — GitHub stars rocketed from 13.6k (Jul 8) to **18.1k** (Jul 24), including +2.7k in the last three tracked days alone, while HF upvotes climbed 51→60. It's OCR/optical-compression-adjacent rather than core serving, but the community pile-on is impossible to ignore.

On the pure-inference side, [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) is the standout organic riser: HF upvotes 55→81 and GitHub stars **41→125 (a 3× jump) since Jul 10** — the strongest efficiency-paper pickup this cycle, and squarely on-topic (infinite-context sparse attention).

Quieter but real: [DFlash](https://arxiv.org/abs/2602.06036) just crossed **53 citations** (up from 42 in early July), the citation leader among the speculative-decoding cohort, and Kimi's [Attention Residuals](https://arxiv.org/abs/2603.15031) is grinding toward 3.5k stars (193 HF upvotes) with star growth quietly re-accelerating to ~18/day.
