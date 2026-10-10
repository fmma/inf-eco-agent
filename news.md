The project's only dependency is `requests` — there's no Python PDF library, and the intended PDF-reading path is Claude's `Read` tool, which here can't work because `poppler-utils` (the `pdftoppm` binary it renders with) isn't installed on this host. My fallbacks (extracting text with `pypdf`/`fitz`/`pdfminer`) are all blocked by this run's permission sandbox, which only auto-allows `Read` and safe read-only shell.

So I genuinely can't read the five PDFs here, and I won't pretend I did. Here's where that leaves us and how to fix it.

## What's broken
`generate_news.py` → `claude --allowedTools "Read"` → `Read` on a `.pdf` → `pdftoppm` → **not installed**. On the production host this binary presumably exists; on this host it doesn't, so the full-text step can't run. If this *is* the production host (foadell), that's the real bug breaking the nightly news step.

## Fastest fixes (pick one)
1. **Make `Read` work as designed** (best — fixes the actual pipeline, not just this session):
   `sudo apt-get install -y poppler-utils`
   Then re-run and `Read` will render the PDFs.
2. **One-off text extraction** — approve a single Bash command and I'll pull the text and write the bulletin properly this run:
   `pip install --quiet pymupdf` (then I extract + rescore from full text), or if you'd rather not add a dep, `sudo apt-get install -y poppler-utils` also gives you `pdftotext`.

If you approve either, I'll do the full-text rescore and produce the bulletin exactly as specified.

## Or proceed now from abstracts
The abstracts I was given are unusually detailed and carry the headline numbers (galahad-kv's 2.8–4.3× load vs. recompute / 8.8–12.3× less GPU energy / 82–98% deep-recall; GUI-KV's −38.9% decode FLOPs with +4.1% step accuracy; Speedbump-P/D dropping speculative decoding below autoregressive; Omni-Diffusion-Distill's 18.2×/21.2× speedups at GenEval 0.828). I can write a solid, concrete bulletin from those **right now** — clearly labeled as abstract-based, with scores marked provisional rather than full-text rescores.

Want me to (a) wait for you to approve the fix and do it properly, or (b) give you the abstract-based bulletin immediately? I'd recommend **(1) install poppler-utils** since it also unbreaks the scheduled runs.

---

## Surge Watch

**Looped models are this cycle's community surge.** A cluster of looped-transformer papers broke out on HuggingFace in a single day (10-09): [ALoDLM](https://arxiv.org/abs/2610.04198) landed at **74 upvotes** from a standing start, [Decoding Looped Transformers Better for (Almost) Free](https://arxiv.org/abs/2610.02185) hit **46**, and [Towards Looped Models Done Right, Part II](https://arxiv.org/abs/2610.06833) climbed **20→30 (10-07→10-09)**. A theme that was invisible last cycle is suddenly the one pulling upvotes.

[Context Language Models](https://arxiv.org/abs/2609.37725) is the other clean breakout — **46 HF upvotes and 625 GitHub stars** on its first reading (10-09), the heaviest repo traction of any new arrival this cycle.

On the citation axis, last cycle's diffusion-speculative-decoding story keeps compounding: [DFlash](https://arxiv.org/abs/2602.06036) ran **114→127 citations (10-02→10-10)** with influential cites **45→53** — still accruing academic pull faster than its community signal (flat ~100 HF upvotes), echoing the foundational-architecture pattern from Mamba-3/FlashAttention-4.
