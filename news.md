I need to be straight with you about what happened: **I could not read any of the 8 PDFs, so I cannot do the full-text rescore this step is designed for.**

**Why:** Claude Code's Read tool renders PDFs via `pdftoppm`, and poppler isn't installed on this host:
```
pdftoppm is not installed. Install poppler-utils ...
```
Every fallback is unavailable in this session too — I verified each:
- No `pdftotext` / `strings` binary on this box (it's a Nix system: `/run/current-system/sw/bin`).
- The PDFs are FlateDecode-compressed (125 streams in one I checked), so `grep`/`cat` yield only compressed bytes.
- The project `.venv` has no PDF library (only arxiv/requests/feedparser), and `pip install`, `python3 -c`, `Write`, and `WebFetch` all returned "requires approval" — this session only auto-allows read-only shell.

So I have the papers' **abstracts and metadata**, but not their full text. This matters because the whole point of this step — reading PDFs to adjust scores off the actual contribution — can't run. I won't fabricate "was X → Y" deltas or imply I read the papers.

**The fix:** install poppler-utils on the host that runs the scan (on `foadell`, add `poppler_utils` to the system packages, or `apt-get install poppler-utils` on a Debian box). Then Read will work and this step produces a genuine full-text bulletin. Worth confirming poppler is actually present on `foadell` — if it isn't, every production run is silently degrading to abstract-only quality.

---

Below is a **fallback bulletin built from the abstracts + hype signals only** (not full text). Every number is quoted from the papers' own abstracts; scores are the original abstract-based scores, not full-text rescores.

# Inference Ecosystem — Flash News
**2026-07-10 — 5 picks from 765 papers scanned** *(abstract-based; full-text rescore unavailable — poppler missing on host)*

[DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147)
Pairs a parallel drafting backbone with a lightweight sequential module to add intra-block dependencies (fixing suffix/acceptance decay), then uses confidence-scheduled verification that tailors verify length per request from prefix-survival probability and engine throughput. Deployed in the **DeepSeek-V4** serving system under live traffic, it beats the production MTP-1 baseline by **60–85% per-user speed at matched throughput** and unlocks new interactivity tiers. Production deployment + Pareto-frontier shift makes this the most consequential entry here. Score: 92 (abstract-based).

[Prima.cpp: Fast 30-70B LLM Inference on Heterogeneous and Low-Resource Home Clusters](https://arxiv.org/abs/2504.08791)
Runs 30–70B models across mixed consumer CPUs/GPUs with pipelined-ring parallelism (overlapping disk I/O with compute/comms) and Halda, a heterogeneity-aware scheduler. Hits **674 ms/token TPOT for 70B at <6% memory pressure**, 26 tok/s for 32B with speculative decoding, and **5–17× lower TPOT than llama.cpp/exo/dllama** while staying OOM-free. Open code and 141 HF upvotes — the clearest "run big models at home" story right now. Score: 95 (abstract-based).

[Sangam: Efficiently Serving Diffusion LLMs with the AR Stack](https://arxiv.org/abs/2607.04206)
Brings AR serving mechanics to cached diffusion LLMs via a deficit token-budget scheduler (admits in-flight decodes first, whole prefills only when budget allows) for amortized stall-free scheduling, plus hybrid serving that overflows prefills onto decode workers. Cuts mean latency **9–20% (colocated, decode-heavy LLaDA-8B)** and **8–20% (hybrid, prefill-heavy Dream-7B)**. From Aditya Akella's group with open code — the reference point as dLLM serving heats up. Score: 92 (abstract-based).

[RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://arxiv.org/abs/2606.31519)
Uses randomized rotated binary quantization with binary-INT4 arithmetic to estimate attention weights, giving an **unbiased proxy score with a proven error bound** that drives adaptive Top-p retrieval (dynamic budget) instead of static Top-k. Ships a hardware-aware system with async pipelining and lazy updates to hide overhead, accelerating inference and cutting memory I/O with quality preserved. Error-bounded sparse attention + released code is a strong practical package. Score: 93 (abstract-based).

[SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)
Organizes context into entropy-guided semantic spans across a GPU-CPU hierarchy without discarding tokens: a GPU summary vector routes, a CPU low-rank SVD basis reconstructs on demand, and a trained zoom-in expands query-relevant spans — base LLM frozen, **<0.05% trainable params**. Delivers **+5.9% over the strongest semantic-compression baseline and −53.3% GPU memory vs full KV at 128K**. No-information-loss compression that stays reversible is the differentiator. Score: 92 (abstract-based).

---

Want me to (a) stop here so you can install poppler and re-run for the real full-text version, or (b) treat this abstract-based bulletin as good enough for today? I did **not** write anything to `news.md` — per the prompt, generation output isn't saved by me, and I'd rather you decide given the caveat.

---

## Surge Watch

[KVarN](https://arxiv.org/abs/2606.03458) is the cycle's biggest star magnet: GitHub stars rocketed 179 → 434 and HF upvotes 47 → 67 since early June, though the curve is flattening now as it matures. Variance-normalized KV-cache quantization that survives reasoning tasks clearly struck a nerve.

[Domino](https://arxiv.org/abs/2605.29707) is still climbing — stars surged 64 → 114 since mid-June, HF upvotes reached 152, and it logged its first citations (3, one influential) on 07-10. Decoupling causal modeling from autoregressive drafting is moving past social buzz into cited work.

[MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) crossed 150 HF upvotes (up from 83) with stars doubling 184 → 372 since mid-June — big-lab sparse attention getting genuine community pickup rather than a launch-day spike.

Quietly, [Mamba-3](https://arxiv.org/abs/2603.15569) keeps stacking citations with near-zero social noise: 50 → 62 total and 5 → 8 influential in three weeks — the same healthy, low-hype adoption curve.
