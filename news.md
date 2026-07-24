All eight PDFs read. After full-text rescoring, five clear the 70 bar; GaugeQuant (thin eval — PPL-only, two models, needs training), AdaDSF (≤1.5B, requires alignment training), and the multimodal-edge survey (no new results) dropped below threshold. Here's the bulletin:

# Inference Ecosystem — Flash News
**2026-07-24 · 187 papers scanned · 5 make the cut**

Long-context speculative decoding headlines a strong batch, plus a MoE pruning win, a spec-decoding side-channel, and hard truths about KV eviction.

### [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535)
The standout. Built-in MTP/NEXTN draft heads run *full* attention over the entire KV cache every draft step, so at 1M context the "free" draft dominates — native drafts even go net-negative (0.80× vs dense on Qwen-122B code QA). The fix is a training-free StreamingLLM window+sink on the **draft attention only**, leaving verification intact: lossless by construction, +28–44% per-decode-step savings across Qwen GDN-MoE 35B/122B and Nemotron Mamba2-hybrid 120B in SGLang, 1.22–1.58× at best depth, plus reclaiming 7.7–11% of total KV. Ports to H100/fp8, reproduction package shipped — a genuine drop-in for anyone serving long-context spec decoding. Score: 93 (was 92)

### [PreMoE: Proactive Inference for Efficient Mixture-of-Experts](https://arxiv.org/abs/2505.17639)
Training-free MoE pruning via Predicted Expert Utility — router logits refined by confidence filtering and a max(s, σ(s)) transform. On DeepSeek-R1, 50% sparsity **halves deployment NPUs and lifts throughput 23%** near-losslessly, scaling 30B→718B; it lands within 0.8 normalized points of REAP at 12% vs 75% profiling overhead. COLM 2026, code released, real infra savings — squarely actionable for MoE serving. Score: 87 (was 88)

### [Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing](https://arxiv.org/abs/2607.20723)
Per-token API timing alone leaks your stack. The attack confirms **Gemini Flash 2.5 runs speculative decoding with a ~128K draft window**, and an analytical GPU timing model recovers Llama layer count, hidden dim, and head count (top-5 within ±1: 83–98%). Disclosed to Google — a wake-up that your spec-decoding and architecture choices are observable through streaming latency. Score: 80 (was 82)

### [Error Certificates for KV-Cache Eviction via Randomized Design](https://arxiv.org/abs/2607.21475)
Proves deterministic eviction (H2O/SnapKV) *cannot* estimate its own induced error — "silent failure." Randomizing the tail (Poisson + a one-scalar Hájek logit offset) yields a per-step certificate at 0.97 coverage. Refreshingly honest pre-registration: question-aware eviction is nearly free at 25–50% and plain output log-prob beats the certificate at predicting failure — its real value is **attribution** (cache-induced vs inherent, AUC 0.73–0.75) and recomputation scheduling in streaming/agent-memory. Reframes when KV monitoring is worth it. Score: 76 (was 84)

### [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot TTS on GPUs](https://arxiv.org/abs/2607.21042)
NVIDIA takes IndexTTS-2 production with TensorRT/TensorRT-LLM: **5.0× on the autoregressive GPT, 3.6× end-to-end** (RTF 0.84→0.24), plus streaming (~600ms TTFA) and batching at minimal WER/SIM/UTMOS cost. The reusable recipe for adapting TensorRT-LLM to AR speech — prompt-tuned conditioning, merged embed tables, custom position IDs, per-step hidden-state outputs — is the transferable win. Score: 75 (was 76)

---

## Surge Watch

The loudest signal this cycle is [Unlimited OCR Works](https://arxiv.org/abs/2606.23050): GitHub stars rocketed from 15.3k (July 21) to 18.1k (July 24) — **+2.7k in three days** — while HF upvotes climbed 55 → 60 and it picked up a 4th citation. After a slow build through early July (13.6k stars), it's suddenly compounding hard; the fastest-accelerating repo in the set.

On the speculative-decoding front, [DSpark](https://arxiv.org/abs/2607.05147) (confidence-scheduled semi-autoregressive drafting) keeps grinding upward: 26 → 37 HF upvotes and 2 → 4 citations over two weeks — quiet but genuinely sustained since landing mid-July.

Meanwhile last week's mid-July breakouts have all stalled: [KronQ](https://arxiv.org/abs/2607.07964) flat at 32 upvotes since July 20, [Jet-Long](https://arxiv.org/abs/2607.07740) stuck at 23, and [Trees from Marginals](https://arxiv.org/abs/2607.06763) frozen at 14. The quant/long-context/drafting cohort's initial surge has run its course — the momentum has rotated elsewhere.
