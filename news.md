All 8 PDFs read. Based on the full texts, here's my rescored bulletin — note MemDecay dropped well below threshold once the full text revealed its eviction policy actually *loses* to the H2O baseline (the authors' own "instructive loss"), and FlashAccel came down since it's evaluated entirely in simulation on not-yet-shippable hardware.

# Inference Ecosystem — Flash News
**2026-07-14 · 357 papers scanned · top 5**

Quantization, speculative decoding, and offloading own today's batch. The standout is a local-inference system that finally schedules offloading at *tensor* granularity — flanked by a training-free spec decoder and two quant recipes you can ship this week.

## [Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices](https://arxiv.org/abs/2607.10183)
ATSInfer extends llama.cpp (~15K LOC) to offload at *tensor* rather than layer/expert granularity, pairing a knapsack-DP static placement with load-aware dynamic transfer and async CPU-GPU coordination that reacts to thermal throttling. On RTX 3060/4090 it lands up to 1.94× prefill and 3.29× decode over llama.cpp — and beats vLLM (4.35×) and KTransformers (3.15×) on decode — across Qwen3, Llama3.1-70B, and GPT-OSS. If you run models locally, this is the most directly usable systems paper of the batch. Score: 94 (was 95)

## [PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs](https://arxiv.org/abs/2505.18610)
This ICLR'26 paper (Tsinghua, Yu Wang) tackles the KV-cache blowup of reasoning models by progressively shrinking bit-width (16→8→4→2 via an exact integer "right-shift" requant), allocating bits per-block through integer programming, and calibrating with positional interpolation to cover RoPE's low-frequency channels. It beats KIVI by up to 8% on AIME/CMIMC/LiveCodeBench at 2-bit while delivering 2.73–5.18× throughput over FP16, with CUDA kernels released. The go-to KV-quant recipe for long-CoT serving right now. Score: 92 (was 92)

## [Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting](https://arxiv.org/abs/2607.10661)
PTD (COLM'26) is a training-free, model-agnostic self-speculative decoder that grows a draft *tree* inside the target model with stepwise pruning, killing the >80% branch redundancy that caps linear self-drafting. It hits up to 2× speedup (2.30× on GSM-100, 2.08× on MBPP) across Llama-2/3, Qwen-2.5/3, and CodeLlama — beating LADE and Self-Draft with no auxiliary model and code released. Plug-and-play acceleration for off-the-shelf LLMs. Score: 90 (was 92)

## [RDQ: Residual Distribution Quantization for Large Language Models](https://arxiv.org/abs/2607.10137)
RDQ pins sub-4-bit collapse on *residual-stream drift* (total KL drift tracks log-PPL at r=0.999) and fixes it with Cascaded Error Compensation: sequential AWQ-style calibration against the actual drifted activations each layer receives, folded into RMSNorm for exact equivalence. It sets W3/W4 SOTA on LLaMA-3-8B (7.55/5.62), Qwen-2.5-7B, and Mistral-7B — beating LeanQuant/SpinQuant at every cell — at *zero* inference overhead on GGUF/AIMET. Ship-it-today weight quantization. Score: 86 (was 85)

## [Controllably Efficient Language Models](https://arxiv.org/abs/2511.05313)
CAT (NYU) is a meta-sequence mixer that decodes chunks while attending to *compressed* chunks, exposing a single test-time knob — chunk size — that walks the quality–cost frontier with no retraining. One dense-attention CAT matches 10 efficient models (linear/hybrid/sparse) on real-world long-context recall while running 1.4–3.7× faster and 2.2–9.5× more memory-efficient than a dense transformer, all in pure PyTorch with no custom kernels. The rare architecture that turns inference cost into a runtime dial. Score: 86 (was 85)

---

## Surge Watch

The clear new breakout is [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980): GitHub stars doubled 41 → 83 and HF upvotes rose 55 → 67 in just three days (Jul 10→13) — the sharpest code-adoption curve on the board right now, and the first sparse-attention paper to break out since MiniMax.

It's riding a broader long-context/sparse-attention wave: [Jet-Long](https://arxiv.org/abs/2607.07740) (dynamic bifocal RoPE) opened at 15 upvotes and a [Linear Attention Architectures](https://arxiv.org/abs/2607.07953) survey at 11 — both surfaced fresh this week.

Quieter mover: [DSpark](https://arxiv.org/abs/2607.05147) speculative decoding edged 26 → 30 HF upvotes since arriving Jul 10. Last cycle's leaders — MiniMax, KVarN, Prima.cpp — have gone quiet on new signal.
