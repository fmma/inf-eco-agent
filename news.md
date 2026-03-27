I'm unable to read the PDFs directly (poppler-utils not installed). I'll write the bulletin based on the detailed abstracts provided, which contain substantial technical detail.

# Inference Ecosystem — Flash News
**2026-03-27 | 150 papers scanned**

---

### [SliderQuant: Accurate Post-Training Quantization for LLMs](https://arxiv.org/abs/2603.25284)

Finally, a PTQ framework that stops treating all layers the same. SliderQuant introduces inter-layer and intra-layer sliding quantization windows that assign different strategies to shallow, intermediate, and deep layers — because the first and last layers are dramatically more sensitive to quantization than the middle. Evaluated across Llama 1/2/3, Qwen2.5, DeepSeek-R1 distilled models, and large MoE architectures for both weight-only and weight-activation quantization, it beats rotation-based PTQ methods (QuaRot, SpinQuant) across the board on generation, reasoning, math, and code benchmarks. If you're deploying quantized MoE or DeepSeek-R1 variants, this is the new baseline to compare against.
**Score: 88 (was 90)**

### [S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation](https://arxiv.org/abs/2603.25702)

Block-diffusion LLMs like LLaDA2.1 are gaining traction as alternatives to autoregressive generation, but their few-step decoding regimes are brittle. S2D2 exploits the insight that a block-diffusion model with block size 1 *is* autoregressive — so the same pretrained model serves as both drafter and verifier, no extra training needed. Lightweight routing policies decide when verification is worth the cost, yielding up to 4.7x speedup over AR decoding on SDAR and 4.4x on LLaDA2.1-Mini with equal or better accuracy. As diffusion LLMs mature, this kind of training-free acceleration will be essential for practical deployment.
**Score: 86 (was 88)**

### [GlowQ: Group-Shared Low-Rank Approximation for Quantized LLMs](https://arxiv.org/abs/2603.25385)

Low-rank error correction for quantized models isn't new, but existing methods (LQER, QERA, ASER) insert correction modules into every decoder block, hurting latency. GlowQ caches a single shared right factor per input-sharing group and selectively restores only where accuracy benefits most. The selective variant GlowQ-S cuts time-to-first-byte by 23.4% and boosts throughput by 37.4% over baselines (BitsAndBytes, AWQ, GPTQ) while staying within 0.2pp accuracy. A practical drop-in for anyone running 4-bit serving who wants to claw back the latency penalty of error correction.
**Score: 80 (was 82)**

### [Large Language Model as Token Compressor and Decompressor](https://arxiv.org/abs/2603.25340)

Turns an off-the-shelf LLM into a content-adaptive token compressor via LoRA adapter heads that translate long text into variable-length discrete "Z-tokens" — semantically dense regions get more tokens, predictable regions get aggressively compressed. Achieves up to 18x token reduction on Wikipedia and CNN/DailyMail while preserving reconstruction fidelity. Supports prompt compression and direct autoregressive generation in Z-token space, which could be a practical pathway for token-efficient long-context inference at serving time.
**Score: 73 (was 75)**

### [PackForcing: Short Video Training Suffices for Long Video Sampling](https://arxiv.org/abs/2603.25730)

Not a pure LLM paper, but the KV-cache management ideas transfer. PackForcing introduces a three-partition cache — sink tokens (full-res anchors), mid tokens (32x compressed via 3D conv + VAE re-encoding), and recent tokens (full-res) — with dynamic top-k selection and continuous Temporal RoPE adjustment. Generates 2-minute 832x480 video on a single H200 with a bounded 4GB KV cache and 24x temporal extrapolation from 5s training clips. The hierarchical cache compression with dynamic eviction is worth watching for anyone designing long-context KV management strategies.
**Score: 70 (was 72)**

---

## Surge Watch



[SpecEyes](https://arxiv.org/abs/2603.23483v1) continues to climb — 47 → 53 HF upvotes and 36 → 43 GitHub stars since yesterday. Sustained two-day growth confirms this wasn't a one-day spike. The speculative perception approach for agentic VLMs is finding a real audience.

[Mamba-3](https://arxiv.org/abs/2603.15569v1) citation velocity is accelerating: 4 → 7 citations in three days, now with an influential citation. HF engagement remains low (6 upvotes) but researchers are clearly building on this — the academic signal is stronger than the community signal, which is typical for architecture papers that matter.

[Attention Residuals](https://arxiv.org/abs/2603.15031v1) added another 45 GitHub stars (2,722 → 2,767) but HF upvotes flatlined at 161. The growth engine is shifting from discovery to adoption. Still March 2026's inference paper of record.

[FlashAttention-4](https://arxiv.org/abs/2603.05451v1) quietly picked up its second citation and first influential citation. Slow burn for a paper with "FlashAttention" in the name — the lack of a public implementation is likely the bottleneck.
