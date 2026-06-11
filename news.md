# Inference Ecosystem — Flash News

**2026-06-11 | 286 papers scanned, 5 featured**

### [MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs](https://arxiv.org/abs/2512.22219)

The Mirage team at CMU introduces the first compiler that automatically fuses an entire multi-GPU LLM inference pass into a single persistent mega-kernel. MPK's SM-level task graph (tGraph) representation breaks through kernel-per-operator barriers to enable cross-operator software pipelining, fine-grained compute-communication overlap, and decentralized in-kernel scheduling — all impossible with CUDA Graphs or conventional kernel fusion. Evaluated across A100, H100, and B200 on five models including Qwen3-8B and Qwen3-30B-A3B, MPK delivers 1.0–1.7x lower latency over SGLang and vLLM with just a few lines of `torch.compile(backend=MPK)`. On Qwen3-8B/A100, per-token decode drops from 14.5ms to 12.5ms — approaching the 10ms hardware floor. OSDI-grade work with artifact evaluation and open source.
Score: 96 (was 95)

### [FOCUS: DLLMs Know How to Tame Their Compute Bound](https://arxiv.org/abs/2601.23278)

ICML 2026 paper that diagnoses why diffusion LLMs (DLLMs) hit a throughput wall at scale: block-wise parallel decoding computes the full block every step, but only ~10% of tokens actually decode. FOCUS discovers that the attention-score delta between layers 0 and 1 strongly predicts which tokens will decode, then evicts non-decodable tokens after two layers — cutting processed tokens by 65-80% with no training. Against LMDeploy on SDAR-8B and LLaDA2.0 across ShareGPT/WildChat/MATH, FOCUS achieves up to 3.52x throughput at block size 64 while preserving or improving generation quality. A key unlock for making diffusion LLM serving production-viable.
Score: 92 (was 90)

### [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/abs/2606.12243)

Reformulates speculative decoding as multi-tier verification using a KL-geometry framework. Instead of binary accept/reject, VIA-SD routes "middle-zone" tokens through a slim-verifier — a dynamically routed submodel derived from the full verifier via layer skipping (DIMR). The slim-verifier shares embeddings and LM head with the full model, preserving distributional consistency at ~4% memory overhead. Across Gemma2, LLaMA2, and Qwen families on QA/reasoning/code/translation tasks, VIA-SD cuts rejection rates by 0.10–0.22 and delivers 10–20% speedup over cascade-SD baselines. Plugs directly into EAGLE-3 and PEARL without retraining.
Score: 88 (was 92)

### [Teaching Diffusion to Speculate Left-to-Right](https://arxiv.org/abs/2606.11552)

Addresses a fundamental mismatch in diffusion-based speculative decoding: block-diffusion drafters train bidirectionally, but verifiers accept tokens left-to-right, so ~47% of correct draft tokens get discarded due to upstream rejections. Three composable training-time fixes — position-wise loss decay, first-error focal loss targeting the chain-breaking position, and a differentiable chain reward — raise accepted draft length by 21–76% across Llama-3-8B, Qwen3-4B/8B on HumanEval/AIME/GSM8K. Combined with DDTree verification, the fully stacked config hits 294.7 tok/s (132.5% over baseline). Compatible with SpecDiff-2 streak distillation, adding +74% on top.
Score: 85 (was 92)

### [Beyond Per-Token Pricing: Concurrency-Aware LLM Cost Estimation](https://arxiv.org/abs/2606.11690)

Every public LLM cost calculator assumes fixed GPU utilization — this paper measures the error. On identical H100 hardware, effective cost spans $0.21 to $15.25 per million output tokens as offered request rate varies from 1 to 200 rps, a 17.5–36.3x underutilization penalty that no calculator exposes. The Ceff(H,M,Q,λ,L) framework, validated with 42 vLLM benchmarks across Llama-8B/Qwen3-30B-A3B/Mixtral-8x7B on H100 and A100, shows FP8 benefits MoE architectures 2.2–2.4x more than dense models, and that active parameter count — not total size — drives saturation economics. The open-source `vllm-cost-meter` scrapes live Prometheus metrics and reports real $/M-tokens.
Score: 82 (was 88)

---

## Surge Watch

[KVarN](https://arxiv.org/abs/2606.03458) (variance-normalized KV cache quantization for reasoning tasks) exploded onto the scene — 179 to 373 GitHub stars in just 4 days (Jun 5–9) with 57 HF upvotes. The reasoning-aware quantization angle is clearly resonating with practitioners.

[Domino](https://arxiv.org/abs/2605.29707) (decoupling causal modeling from autoregressive drafting in speculative decoding) went from 2 to 140 HF upvotes in 5 days (Jun 2–7). One of the sharpest community receptions we've tracked for a spec-decode paper.

[OSCAR](https://arxiv.org/abs/2605.17757) (spectral covariance-aware rotation for 2-bit KV quantization) rocketed from 12 to 295 GitHub stars and 5 to 63 HF upvotes in 10 days (May 22–Jun 2). The extreme KV compression space is getting crowded but this one broke through decisively.

[Attention Sink in Transformers](https://arxiv.org/abs/2604.10098) (survey on utilization, interpretation, and mitigation) saw renewed practitioner attention — GitHub stars jumped from 83 to 127 in 6 days (Jun 5–11) after being flat for a month. Surveys don't usually get this kind of delayed traction.

[DFlash](https://arxiv.org/abs/2602.06036) continues building academic credibility — influential citations doubled from 8 to 13 in 10 days (May 31–Jun 11), with total citations hitting 29. Block diffusion speculative decoding is becoming a validated research direction.
