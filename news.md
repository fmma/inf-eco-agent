# Inference Ecosystem — Flash News
**2026-02-25**

Huge batch today — the arXiv firehose delivered several papers directly targeting inference system bottlenecks.

**KV cache is the new battleground.** [CHESS](https://arxiv.org/abs/2602.20732) proposes a context-aware hierarchical KV cache pruning system that matches full-KV quality using only **1% of the cache** and delivers up to **4.56x throughput** — algorithm-system co-design at its best. Score: 95 | Hype: 65

**Speculative decoding gets smarter.** [KnapSpec](https://arxiv.org/abs/2602.20217) reformulates draft model selection as a knapsack problem, adaptively skipping attention vs MLP layers based on real-time hardware latency. Training-free, plug-and-play, up to **1.47x wall-clock speedup** on Qwen3 and Llama3. Score: 95 | Hype: 70

**FPGAs enter the long-context arena.** [FAST-Prefill](https://arxiv.org/abs/2602.20515) is the first FPGA accelerator targeting long-context prefill with dynamic sparse attention — **2.5x TTFT speedup** and **4.5x energy efficiency** over A5000 GPU on sequences up to 128K tokens. Score: 94 | Hype: 55

**Edge inference goes ROM.** [TOM](https://arxiv.org/abs/2602.20662) co-designs ternary quantization with read-only memory to hit **3,306 TPS** on BitNet-2B using ~500 MB weights and ~1.2 GB VRAM — the memory wall meets the ROM wall. Score: 93 | Hype: 55

**MoE serving gets resilient.** [ReviveMoE](https://arxiv.org/abs/2602.21140) from Huawei Cloud enables fast failure recovery in large-scale MoE deployments without restarting serving instances, supporting both collocated and disaggregated architectures. Already deployed in production MaaS. Score: 90 | Hype: 60

Also notable: [ISO-Bench](https://arxiv.org/abs/2602.19594) drops a benchmark of 54 real vLLM/SGLang optimization tasks from merged PRs — no agent dominates, and surprisingly they identify bottlenecks correctly but fail to produce working patches. The [R&Q framework](https://arxiv.org/abs/2602.19938) tackles MoE expert load imbalance at inference time via replicate-and-quantize, cutting imbalance 1.4x within the original memory budget.
