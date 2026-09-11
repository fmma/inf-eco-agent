I've hit a genuine, verified blocker and want to surface it rather than fabricate a bulletin. Here's what I confirmed with read-only checks:

**The 8 PDFs cannot be read in this environment.**

- The **Read tool fails on PDFs** — it renders via `pdftoppm`, and poppler-utils isn't installed (`which pdftotext pdftoppm` → both missing). This is a NixOS host (`/run/current-system/sw/bin` in PATH), so there's no `apt` quick-fix.
- **No Python PDF library** is in the repo venv — `ls .venv/.../site-packages` shows only `arxiv`, `feedparser`, `requests`. So even running Python wouldn't extract text without a `pip install` first.
- **`python3` execution is blocked** by the current permission mode. Every attempt (5×, including with the sandbox override) returned "This command requires approval," while read-only commands (`ls`, `cat`, `which`) run fine.

The PDFs themselves are all present and intact (8 files, 300 KB–1.1 MB each).

**Why this matters beyond this run:** the real `generate_news.py` step invokes Claude with `--allowedTools "Read"`. On any host without poppler-utils, that Read call fails exactly like this — so the PDF-rescore stage is silently broken wherever poppler is missing. Worth checking whether `foadell` has it installed.

I won't write "rescored from full text (was X → Y)" for papers I couldn't actually read — that would be fabrication.

**To unblock, pick one:**

1. **Approve a one-time extraction** (fastest). Approve this and I'll read the text and write the bulletin properly:
   ```
   pip install pypdf && python3 -c "
   from pypdf import PdfReader; import glob,os
   os.makedirs('data/pdftext',exist_ok=True)
   for p in sorted(glob.glob('data/pdfs/*.pdf')):
       t='\n'.join((pg.extract_text() or '') for pg in PdfReader(p).pages)
       open('data/pdftext/'+os.path.basename(p)[:-4]+'.txt','w').write(t)
       print(p, len(t))"
   ```
2. **Install poppler-utils** on this host (fixes the Read tool the way the pipeline expects) — on NixOS, add `poppler_utils` to your environment / `nix-shell -p poppler_utils`.
3. **Fallback:** I write the bulletin from the (unusually detailed) abstracts — they already contain the key numbers — but I'll label it clearly as abstract-based, *not* full-text rescored.

Which do you want? If you just approve option 1, I'll take it from there.

---

## Surge Watch

Diffusion LMs and KV-cache eviction are dominating community attention this cycle — this is not a quiet week.

[Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010) exploded from 8 to 119 HF upvotes in a single day (Sep 8→9) — by far the sharpest spike in the set.

[Random Attention: Rethinking KV Cache Eviction](https://arxiv.org/abs/2609.03430) is the standout debut: ~170 upvotes within days of posting (161→170, Sep 6→9), unusually strong heat for a cache-eviction paper.

[Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737) climbed 10→66 upvotes in three days (Sep 3→6), and [Why Gated DeltaNet Survives 4-Bit Quantization](https://arxiv.org/abs/2609.04098) opened strong at 73 (now 78) — low-bit linear-attention quant is landing.

Slower burn worth watching: [FreeToken](https://arxiv.org/abs/2608.16157) (edge MoE serving) has ridden 26→107 HF upvotes over three weeks, the most sustained traction of any serving paper here.
