# Inference Ecosystem — Flash News

**2026-03-06** — 154 papers scanned · 8 read in full · 5 highlighted

---

### FlashAttention-4: Maximizing Throughput on NVIDIA Blackwell GPUs
*Tri Dao, Jay Shah, Ganesh Bikshandi, Vijay Thakkar, Pradeep Ramani, Harun Bayraktar (Together AI / Colfax / NVIDIA)*

The FlashAttention line reaches Blackwell with a ground-up rewrite in CuTe-DSL (Python), targeting the B200's asymmetric MMA-to-memory ratio. Key moves: a software-emulated exponential that trades 1 ULP accuracy for an extra multiply slot, conditional softmax rescaling that skips ~40 % of rescale work, and a 2-CTA cooperative pipeline for the backward pass. Result: **1 613 TFLOP/s FP16 forward (71 % utilization)**, 1.3× over cuDNN 9.13 and 2.7× over Triton. The Python DSL cuts compile time 20–30× vs. C++ CUTLASS. Open-sourced.

### SlideSparse: Unlocking Sparse Tensor Cores via Sliding-Window Decomposition
*Yuzong Chen et al.*

A new structured-sparsity family — **(2N−2):2N** — that maps to existing 2:4 Sparse Tensor Cores through a provably-optimal sliding-window decomposition (expansion factor γ = 2 − 2/N). At 6:8 sparsity on Qwen2.5-7B (A100, INT8 W8A8), SlideSparse delivers **1.33× end-to-end speedup** with negligible accuracy loss. Tested across A100, H100, B200, RTX 4090/5080, and DGX Spark. Integrated into **vLLM via a single config flag** — the most production-ready sparse-inference path to date.

### VSPrefill: Vertical-Slash Sparse Attention for Long-Context Prefill
*Cheng Luo et al.*

Decomposes attention into vertical (critical-token columns) and slash (local-diagonal) components, then trains a tiny bilayer "VSIndexer" to predict the sparse mask in linear time. Fused TileLang kernels avoid materializing the full attention matrix. On LLaMA-3.1-8B at 128 K context: **4.95× average prefill speedup, 98.35 % accuracy retention** across RULER, LongBench, and InfiniteBench. Scales better than competing sparse-attention methods as sequence length grows.

### WaterSIC: Near-Optimal Post-Training Quantization via Waterfilling
*Jiaqi Chen et al.*

Frames PTQ as a rate-distortion problem and allocates bits per column using the classic waterfilling algorithm. Proves that GPTQ's uniform allocation can be *arbitrarily* far from the information-theoretic limit; WaterSIC closes to within **0.255 bits of the IT bound**. On Llama-3.2-1B and Qwen3-8B across 1–4 bit, it sets new SOTA perplexity at every bitrate — particularly strong at sub-2-bit where other methods collapse.

### Vocabulary Trimming for Faster Speculative Decoding
*Sangjin Cheon et al.*

Constrains the draft model's vocabulary to tokens the target model actually uses in-domain, cutting softmax and sampling cost. A TPE optimizer balances coverage vs. latency: **128 K → 13 K vocab (90 % reduction)** while retaining 93.7 % token coverage. Throughput gains of **6.7 % OOD and 19.6 % in-domain** (NER) on Llama-3.1-8B → 70B. Simple, orthogonal to other spec-decoding improvements.

---

*Other notable papers this batch: **InfoFlow KV** (attention-norm-guided selective KV recomputation for RAG, 3.49× at 32 K on 4× H100); **Helios** (3D-DRAM near-memory accelerator, 3.25× over GPU baselines); **SLO-Aware P/D disaggregation** (M/M/1 queuing model validated on DeepSeek-V3 + H200).*

---

## Surge Watch

**SageBwd** ([2603.02170](http://arxiv.org/abs/2603.02170v1)) woke up — went from zero signals to 11 HF upvotes in a single day. A trainable low-bit attention paper from the Ion Stoica group; if the upvote curve continues tomorrow this one has legs.

**Qwen3-Coder-Next** ([2603.00729](http://arxiv.org/abs/2603.00729v1)) keeps climbing — now at 35 HF upvotes (up from 28 yesterday, 6 two days ago) and GitHub stars crept to ~15.9k. Sustained momentum across three consecutive observations.

**Speculative Speculative Decoding** ([2603.03251](http://arxiv.org/abs/2603.03251v1)) just landed — Tri Dao and Tanishq Kumar. Only 1 HF upvote so far but scored 97 relevance. Too early for signal, but the author pedigree alone warrants a mention. One to track.

DualPath, LK Losses, and the rest: flat. No new movement worth reporting.
