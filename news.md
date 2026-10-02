I hit a hard blocker and want to flag it rather than fake my way past it.

**The PDF rescore step can't run in this environment.** All 8 papers downloaded fine (`data/pdfs/`, timestamped today 05:27), but I cannot read any of them:

- **Read tool** → fails on every PDF: `pdftoppm is not installed. Install poppler-utils`. The Read tool renders PDFs via poppler, which isn't on this host.
- **Python extraction via Bash** (pypdf/pdfminer, or a manual zlib stream parse) → `This command requires approval` (denied).
- **Write a helper script** to `/tmp` → permission not granted.
- **WebFetch** the arXiv HTML full-text as a fallback → permission not granted.

So there is currently **no channel** through which I can read the full text. The only things working are Read-on-text-files and benign read-only Bash (`ls`, `grep`). `grep`/`strings` won't help — arXiv PDFs are FlateDecode-compressed.

I won't emit a bulletin that claims full-text rescoring when I never opened the PDFs — the "Score: X (was Y)" deltas would be fabricated.

**Worth knowing:** if this host is where `scan.sh` runs, step 7 (`generate_news.py`'s PDF rescore) has likely been **silently degrading to abstract-only** since poppler went missing — the pipeline never checks whether the PDFs were actually read, so it still posts a bulletin every day.

**To unblock, pick one:**
1. **Restore PDF reading (best):** install `poppler-utils` so the Read tool works as the pipeline intends. On NixOS add `poppler_utils` to the system/user environment; the equivalent elsewhere is `apt-get install poppler-utils`.
2. **Give the pipeline a text path:** `pip install pypdf` into `.venv` and I (or `generate_news.py`) can extract text without poppler.
3. **Grant me permission** for Bash-python or WebFetch right now, and I'll read the papers and produce the real full-text bulletin this run.
4. **Proceed abstract-only:** I'll write the bulletin from the (unusually detailed) abstracts already in the prompt — genuinely useful, but it's *not* a full-text rescore, so I'd label scores as abstract-based rather than invent deltas.

Which would you like? My recommendation is **#1** (fixes it permanently for the daily scan), with **#3** if you want the real bulletin for this run immediately.

---

## Surge Watch

[DFlash](https://arxiv.org/abs/2602.06036) is the clearest breakout: citations jumped **98→114 in a week (09-26→10-02) with influentials surging 38→45** — a block-diffusion speculative-decoding method now compounding faster than any peer and well past the 100-citation mark.

Speculative decoding is running hot more broadly: [DSpark](https://arxiv.org/abs/2607.05147) leapt **30→38 citations with influentials 9→15**, and [Domino](https://arxiv.org/abs/2605.29707) went **19→28 (influentials doubling 4→8)** over the same 09-26→10-02 window — both sharp, concentrated pickups rather than slow drifts.

[TraceLab](https://arxiv.org/abs/2606.30560) nearly doubled, **13→24 in a week** — the fastest relative climb on the board, as coding-agent serving-workload characterization draws sudden interest. [StreamingVLM](https://arxiv.org/abs/2510.09608) also stepped up **84→93**.

[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) reignited after last week's stall, moving **23→30** — the KV-compression release is accruing citations again rather than cooling as previously flagged.
