I hit a genuine environment blocker on the required step — reading the PDFs — and I don't want to fake a full-text rescore I couldn't actually do. Here's the concrete situation:

- **The Read tool can't render these PDFs.** It shells out to `pdftoppm` (poppler-utils) to rasterize pages, and that binary isn't installed on this host. All 7 PDF reads failed with `pdftoppm is not installed. Install poppler-utils`.
- **The Python fallback is blocked too.** I tried to extract the embedded text layer with `pymupdf`/`pypdf` instead, but Bash and Write both come back as "requires approval," which isn't being granted in this run. So the only tool actually available to me — Read — is the one that can't parse PDFs here.

This isn't a "tool unavailable" cop-out; it's a specific missing system dependency, and the full-text rescore the prompt asks for is impossible until it's resolved.

Three ways forward:

1. **Install poppler (the real fix).** `sudo apt-get install -y poppler-utils` — then Read works as designed and I can rescore from full text. Worth confirming this is present in **foadell**'s `configuration.nix` too, otherwise the scheduled 05:00 scan is silently degrading every day it hits PDFs.
2. **Approve one Bash call.** I'll extract the text with a Python PDF lib and do the proper full-text rescore + bulletin. Just approve the command.
3. **Proceed from abstracts now.** I write the bulletin from the (fairly detailed) abstracts + metadata immediately — but I'd label the scores honestly as abstract-based, *not* full-text rescores, since I can't claim to have read papers I couldn't open.

Which do you want? If you're just after the Discord post, say the word and I'll do **#3** right away. If you want it done as designed, **#1** is the durable fix — and I'd check the poppler dependency on foadell so this doesn't quietly break the automated runs.

---

## Surge Watch

[LLMRouter](https://arxiv.org/abs/2608.06867) is the clear breakout. It surfaced on 08-16 already at **97 HF upvotes / 2,355 GitHub stars** and kept climbing to **106 upvotes / 2,377 stars** by 08-19 — one of the fastest cold-starts we've tracked, blowing past the 100-upvote line in days. A unified router infra release clearly hit a nerve.

On the academic side, [FlashAttention-4](https://arxiv.org/abs/2603.05451) keeps compounding: **33 → 42 citations (influential 4 → 6) in the two weeks to 08-16** — a rare sustained citation ramp for a kernel paper, signaling it's fast becoming a default reference.

Diffusion-style speculative decoding is quietly accruing cites too: [DFlash](https://arxiv.org/abs/2602.06036) jumped **54 → 67 citations (Aug 4 → 15)** and [DSpark](https://arxiv.org/abs/2607.05147) doubled **8 → 14** over the same window — the block-diffusion drafter idea is gaining real traction.
