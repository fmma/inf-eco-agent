I need to be straight with you about what happened, then give you the bulletin.

**I could not read the 8 local PDFs in this environment.** I tried four routes and each is blocked here:
- **Read tool** on every PDF → fails with `pdftoppm is not installed` (the Read tool renders PDFs to images via poppler, which isn't installed on this host).
- **Pure-stdlib Python extractor** (zlib-decompress the PDF streams) → `python3` execution is gated.
- **WebFetch** of the arXiv HTML full text → gated.
- **Write** (to drop a helper script) → gated.

Only the Read tool and a few read-only Bash commands are auto-approved here, so full-text extraction isn't possible in this sandbox. On the deployment host `foadell`, if poppler is installed the normal Read path works — that's worth verifying there, since the pipeline depends on it.

The bulletin below is therefore built from the **detailed abstracts in the prompt** (which do carry the papers' method names and headline numbers), with relevance rescored on my read of their substance — **not** from full text. Flagging that honestly rather than pretending I read the PDFs.

---

# Inference Ecosystem — Flash News
**2026-09-10 · 5 featured · 206 scanned**

## [Epoch: Compiling Diffusion Blocks for Sparse MoE Serving](https://arxiv.org/abs/2609.09748)
The first serving system to treat a diffusion LM's *refinement block* — not the per-forward pass — as the compilation unit, so it stops rebuilding routing and recomputing dead-position experts every iteration. Three pieces do the work: **ATLAS** (coverage-driven active-expert support, gate logits refreshed per iteration), **LSP** (routes only live/newly-decoded/refresh positions while keeping full sequence shards as state), and **FreshLane** (carries the fresh token–expert worklist through EP dispatch/kernels/combine). Up to **2.7× end-to-end** over the strongest baseline on 8×H100 across LLaDA-MoE / LLaDA2.0 (7B–100B), still running at batch sizes where baselines OOM — the clearest systems attack yet on wide-open diffusion-LLM serving. Score: 91 (was 92).

## [Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding](https://arxiv.org/abs/2609.09338)
Kills speculative decoding's worst tax — retraining a bespoke drafter per target — by bootstrapping drafters from off-the-shelf pretrained small LMs, pruned to a shallow backbone and adapted via vocabulary alignment, zero-init QKV expansion, and target-distribution distillation. One pretrained backbone transfers across targets, lifting mean acceptance length **16.1% (Qwen3-8B), 21.2% (Llama-3.3-70B), 22.7% (229B MiniMax-M2.5, +17.5% tokens/s)**, with the biggest gains out-of-domain and multilingual. Code is public — the drafter recipe to reach for when acceptance collapses under workload shift. Score: 90 (was 90).

## [UNISON: A Co-Designed Near-Memory Scheduler of Session KV Residency for LLM Agents](https://arxiv.org/abs/2609.09643)
Reframes KV eviction/tiering for agent loops as a *session-level residency* problem: **SPEAR** ranks eviction by a turn-indexed return-gap hazard, **TIDE** spends the observed tool-wait as a DMA budget for who stays in the fast tier. Across 1,415 sessions / 33,596 turns on three model families it's the best non-oracle policy on every trace — **TTFT down 58–89%** on long-horizon traces, AMAT down 22–51%. It's a near-memory co-design (a 0.169 mm² / 13.6 mW 28nm core), but the core insight — a live tool-wait is *hot*, not cold — is one every agent-serving stack should internalize. Score: 86 (was 90).

## [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](https://arxiv.org/abs/2609.10266)
The first benchmark for KV reuse when the cache *isn't* an exact prefix — RAG chunks reordered mid-prompt, agent reports written by other agents, or caches from a different checkpoint. It scores each method by the fraction of the no-cache→full-recompute gap it recovers under real compute/memory/latency accounting, and finds cheap position-correction suffices until a query needs several sources at once — where only re-encoding or trained methods recover half to two-thirds, and unrepaired caches can be *worse* than no cache. Ships as a pip package with a public leaderboard; if you reuse KV outside exact prefixes, this is your new yardstick. Score: 85 (was 88).

## [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and DVFS](https://arxiv.org/abs/2609.09662)
Adds two workload-side knobs — speculative decoding and *variable verification depth* — on top of DVFS to widen the power/latency optimization space for on-device LLMs under thermal throttling. Beats SOTA power governors by up to **23.1% speedup and 52.4% lower energy** at comparable quality, exploiting the fact that not every token needs full-depth inference. Code is public — a concrete edge-inference win as phones keep pushing local LLMs. Score: 85 (was 88).

---

If you want the *full-text* rescore this prompt actually asks for, install poppler on the host running this step (`apt-get install poppler-utils`) so the Read tool can render the PDFs, then re-run — I'll open all 8 and adjust scores against the real contributions.

---

## Surge Watch

Nothing noteworthy in signal trends today.
