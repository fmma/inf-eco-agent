# Inference Ecosystem — Flash News
**2026-06-17 | 261 papers scanned**

### [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/abs/2606.17949)

Finally, someone fused model routing with load balancing instead of treating them as separate problems. RouteBalance formulates request scheduling as online assignment over concrete model *instances* — not model names — jointly optimizing quality, latency, and cost on a 3-simplex. On a 13-instance, 28-GPU cluster with four Qwen2.5 sizes (3B–72B), a single deployed stack traces the full quality-cost-throughput frontier by sweeping one weight vector, hitting 2.8s E2E at 30 req/s — 2.6–4.1x ahead of enhanced BEST-Route. A four-arm isolation pins the gain to pricing latency at model-selection time, a decision decoupled routers structurally cannot make. Open source with ~1.5M requests across 442 configurations.
Score: 92 (was 90)

### [LUMEN: Coordinated Failure Recovery for Distributed LLM Serving](https://arxiv.org/abs/2606.17787)

Worker failures in LLM serving clusters degrade TTFT by 4x and TPOT by 1.6x — even for the 97.3% of requests that weren't on the failed worker. LUMEN treats recovery as a load-aware coordination problem across three decision points: KV checkpoint placement, interrupted-request dispatch, and capacity restoration during model reload. The speculation-assisted progressive recovery is clever: it loads a draft model on the recovering worker to provide speculative decoding capacity while the full model reloads in the background. On a real 8-worker SGLang prototype serving Qwen3-14B, LUMEN cuts mean TTFT by 29.6%, TPOT by 7.1%, and recovery time by 64.1% vs stop-and-restart. Scales to 64 workers in simulation.
Score: 90 (was 88)

### [Top-Theta Attention: Sparsifying Transformers by Compensated Thresholding](https://arxiv.org/abs/2502.08363)

An elegantly simple idea: replace top-k attention selection with per-head calibrated thresholds. Static thresholds are calibrated offline from a few hundred samples to retain ~k elements per attention row, then applied as a constant-time elementwise comparison — no row dependency, tiling-friendly, no retraining needed. With softmax denominator compensation (SDC) and V-mean compensation (VMC), Top-Theta achieves 3–10x V-cache reduction on LLaMA2/3 models (7B to 70B) with <1% accuracy degradation on HumanEval, ARC, HellaSwag, and LongBench. The thresholds are resilient to distribution shift (calibrate on ARC-C, deploy on HumanEval), making this a calibrate-once-per-model solution. A prototype kernel on Ascend NPU already shows 1.17x speedup.
Score: 88 (was 88)

### [BACON: Boundary Attention Calibration for Multimodal KV Cache Compression](https://arxiv.org/abs/2606.14782)

KV cache compression in multimodal LLMs has a blind spot: observation-window attention averaging dilutes sparse visual evidence critical for answer grounding. BACON calibrates retention scores using last-query attention as a complementary signal, filtered through intra-layer coherence and inter-layer persistence to suppress noise. Plug-and-play on top of SnapKV, PyramidKV, AdaKV, and SparseMM — tested across Qwen2-VL-7B, LLaVA-NeXT, InternVL3-8B, and Qwen3-VL-30B. At budget 64 on Qwen2-VL with PyramidKV, BACON improves DocVQA by +18.7 points. Zero additional inference latency or memory overhead since it only modifies prefill-stage token scoring.
Score: 85 (was 90)

---

## Surge Watch

[OSCAR](https://arxiv.org/abs/2605.17757) (offline spectral rotation for 2-bit KV cache quantization) had an unreported blockbuster debut — 5→63 HF upvotes and 12→295 GitHub stars between May 22 and Jun 2. For a KV cache quantization paper, that's exceptional practitioner reception. Growth has since plateaued at 295 stars, but this is now the go-to reference in rotation-based KV compression.

[FlashMemory-DeepSeek-V4](https://arxiv.org/abs/2606.09079) (lookahead sparse attention for ultra-long context) debuted Jun 11 and hit 61 HF upvotes / 71 GitHub stars within 5 days — sharp early signal for a DeepSeek V4-specific long-context optimization.

[Draft-OPD](https://arxiv.org/abs/2605.29343) (on-policy distillation for spec-decode drafts) surged 10→34 HF upvotes and 4→36 GitHub stars in two weeks, with its first citation landing Jun 12. The speculative decoding community is clearly hungry for principled draft model training — this fills a gap that retrieval-based and self-speculative methods don't address.

[Gated DeltaNet-2](https://arxiv.org/abs/2605.22791) (decoupled erase/write in linear attention) exploded 3→30 HF upvotes and 19→182 GitHub stars in a single weekend (May 31). Now stable at 185 stars with 2 citations — instant community buy-in for the next iteration of sub-quadratic sequence modeling.
