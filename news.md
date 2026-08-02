I now understand the situation completely. Confirmed by both the filesystem check and the code logic in `generate_news.py`:

- `find_top_papers` (line 65-73) only downloads PDFs for papers scoring ≥70 that were scored today. The single paper today scored **2**, so `top_papers` is empty and **no PDFs were downloaded**.
- `build_prompt` (line 124) only emits the "Full-Text PDFs" section `if pdf_paths` — which is why there are no PDF file paths in my prompt. There is nothing to Read.
- The lone paper is a biostatistics causal-inference method (doubly robust EIF estimators on VitalDB ICU data) that matched only on the word "inference" — genuinely off-topic for LLM inference systems, and far below the minimum relevance of 70.

No paper qualifies for the bulletin. Rather than fabricate relevance for an off-topic paper, I'll output an honest "nothing cleared the bar" bulletin in the required format.

# Inference Ecosystem — Flash News
**2026-08-02 · 0 papers make the cut** (1 scanned)

Quiet day on the wire. Only one new arXiv paper surfaced in scanning, and it doesn't belong to us: *Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories*. It's a biostatistics method — cross-fitted doubly robust estimators with EIF-targeted validation over irregular clinical time series (lab values, physiologic signals), demoed on VitalDB ICU-disposition data. Pure statistical *inference*, zero overlap with model serving, decoding, KV cache, or systems. Full-text rescore: **2 (was 2)**.

Nothing for inference engineers to action today — no PDFs met the relevance threshold, so none were pulled for deep review. Back tomorrow.

---

## Surge Watch

New leader of the slow-burn pack: [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) is the board's cleanest organic climb — GitHub stars **tripled 41 → 129** and HF upvotes rose **55 → 82 across Jul 10–30**, a steady week-over-week grind rather than a launch-day spike. The most convincing sustained signal now that Unlimited OCR has gone quiet on fresh readings.

Spec-decoding to watch: [DSpark](https://arxiv.org/abs/2607.05147) keeps building — HF upvotes **26 → 39 since Jul 10** and citations **2 → 7 (2 now influential) in ~3 weeks**, unusually fast academic pickup for a July paper.

Debut-and-freeze: [Full Attention Strikes Back](https://arxiv.org/abs/2605.16928) landed hot at **99 HF upvotes on Jul 23** and hasn't budged in the 8 days since — a strong launch stalled exactly one vote short of the 100 line.
