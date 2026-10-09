I can't complete the bulletin as specified, and I don't want to fake it. Here's the blocker:

**The Read tool can't open any of the 8 PDFs** — poppler-utils isn't installed in this environment. The error, verbatim:

> pdftoppm is not installed. Install poppler-utils (e.g. `brew install poppler` or `apt-get install poppler-utils`) to enable PDF page rendering.

My fallback attempts to extract the text another way (pdftotext / a Python PDF lib via Bash) are being blocked by permission prompts — consistent with the news step's `--allowedTools "Read"` restriction, which doesn't permit Bash.

So I have the **abstracts only**, not the full text the rescore is meant to be based on. I won't write "Score: 95 (was 88)" style rescores as if I'd read the papers when I haven't.

**Fastest fix** (makes Read work — matches the error message):
```
sudo apt-get install -y poppler-utils
```
Then re-run the news step.

**Alternatives:**
- Approve a one-off Bash command and I'll pull the text with a Python PDF library (pip-installing one if needed) and proceed properly.
- Tell me to write the bulletin **now from the abstracts only** — I'll label it as abstract-based and drop the "(was X)" full-text rescores. The abstracts here are detailed (method names, speedups, benchmarks), so it'd still be a solid bulletin, just not a full-text rescore.

One thing worth flagging for the pipeline itself: since `generate_news.py` runs with `--allowedTools "Read"`, **poppler-utils is effectively a hard dependency of the news step** — if it's ever missing on `foadell`, this step fails exactly like this with no Bash fallback. Might be worth asserting its presence early in `scan.sh`.

Which option do you want?

---

## Surge Watch

[Mamba-3](https://arxiv.org/abs/2603.15569) is the quiet breakout this cycle — pure citation compounding, not community buzz: it tore **80→104 citations in two weeks (09-24→10-09)**, influential cites jumping **11→18**, all on ~7 flat HF upvotes. Its kernel-side sibling [FlashAttention-4](https://arxiv.org/abs/2603.05451) ran the same play, **58→77 citations over the identical window (influential 8→11)** on 2 upvotes — the foundational-architecture papers are accruing academic pull faster than anything with a HuggingFace page.

On the community axis, the KV-cache-compression lane that was absorbing *citation* energy last cycle is now pulling *upvotes*. [Periodic Weak Spots](https://arxiv.org/abs/2609.36322) (chunked-KV phase sensitivity) surfaced at **113 HF upvotes**, [STEPQuant](https://arxiv.org/abs/2609.38169)'s delta-rule recurrent-state quant landed **100 upvotes + 94 GitHub stars** in one reading (10-09), and [Prefill-Free Cross-Family KV Cache Transfer](https://arxiv.org/abs/2609.32259) leapt **3→96 upvotes (10-03→10-09)** — a clean breakout for cross-model KV reuse.

Last cycle's leader [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) still tops the board (224 upvotes, 35 cites) but has logged no fresh signal since 10-06 — the momentum has rotated to the names above.
