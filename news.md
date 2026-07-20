I've read all 8 PDFs in full. Below is the rescored flash-news bulletin. Notable rescores after full-text review: the GPU-collectives paper jumped (80→91 — real vLLM ITL gains across 5 production models, NCCL-native), the vLLM-config study eased down (90→82 — rigorous but a measurement study, no new method), and the MLIR compiler (87→~60) and AdaLook (82→~68) fell below the 70 threshold and are cut — the MLIR paper in particular reports zero speedup/benchmark numbers.

# Inference Ecosystem — Flash News
**2026-07-20 · 104 papers scanned · top 5 featured**

Unusually deployment-ready week: speculative decoding gets a smarter vocabulary, MoE serving learns to page its own weights, and NVIDIA drags AllReduce to the hardware speed-of-light.

## [Speculative Decoding with a Speculative Vocabulary](https://arxiv.org/abs/2602.13836)
SpecVocab ditches the fixed 32K reduced vocabulary that EAGLE-3/FR-Spec/VocabTrim rely on and instead *speculates* a per-step top-2K subset via a low-rank ranking module, backed by a fused kernel that cuts logit computation 3–5×. Across Qwen3 and OLMo 2 it beats EAGLE-3 on both acceptance length and real SGLang throughput (+8.1% on OLMo 2 7B, +4.3% on Qwen3 8B) using under 2% of vocab logits — and shows EAGLE-3's reduced-vocab *training* needlessly hurts drafts. A clean win on the year's hottest inference primitive. Score: 92 (was 95)

## [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184)
The sharpest idea yet for the MoE weight-vs-KV-cache squeeze: treat Any-Precision expert bit-planes as pageable weights (à la PagedAttention) and re-quantize experts at runtime as KV pressure grows, guided by offline Hessian sensitivity + live routing stats + prompt residuals. On Qwen1.5-MoE, Mixtral-8×7B and Gemma-4-26B it holds FP16-equivalent accuracy with up to 72% memory savings and 1.94× throughput, or +39.3% quality at matched memory for ≤4.1% throughput loss — shipped as a fused mixed-precision MoE kernel on vLLM. Score: 92 (was 94)

## [Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives](https://arxiv.org/abs/2607.16100)
NVIDIA+ETH target the small-AllReduce latency sitting on every tensor-parallel decode step, killing global memory barriers via LL/sentinel sync, double buffering, and a novel two-shot LL128-atomic kernel — landing within 7% of the speed-of-light bound (2.37µs vs 11µs for NCCL ring on 4×GB200). Wired into vLLM it trims inter-token latency 7–13% (4 GPU) and 9–11% (8 GPU) across Llama-3.1-70B, DeepSeek-V3 and Qwen3-235B, worth >$11 per 1M tokens on DeepSeek-V3. Barrier-free and NCCL-native, so it's usable now. Score: 91 (was 80)

## [Attention to Detail: Evaluating Energy, Performance, and Accuracy Trade-offs Across vLLM Configurations](https://arxiv.org/abs/2607.09172)
A 9,000-run, 5-model factorial sweep of three vLLM knobs with genuinely actionable rules: FlashInfer minimizes energy while FlashAttention-3 minimizes latency (they decouple), prefix caching mostly helps TTFT, and chunked prefill is a no-op under the default 8,192-token budget. The eyebrow-raiser — attention backend and prefix caching measurably shift *accuracy* via FP non-associativity, meaning unreported inference configs quietly break benchmark reproducibility. Score: 82 (was 90)

## [Cache-Aware Prompt Compression: A Two-Tier Cost Model for LLM API Caching](https://arxiv.org/abs/2607.15516)
A rigorous teardown of Sonnet's prompt cache exposes a two-tier architecture with a sharp ~3,500-token threshold (ρ≈0.83 below it), debunking the literature's ρ=1.0 assumption. CAPC pairs *query-agnostic* compression with explicit cache_control and a tier-preserving ratio bound, coming out cheapest in 16/16 LongBench configs and in production (51.7% off a 94k-token tool schema; τ-bench reward equal to vanilla while query-aware compression runs +40.1% — its cache-busting cost made concrete). Score: 80 (was 80)

---

## Surge Watch

Nothing noteworthy in signal trends today.
