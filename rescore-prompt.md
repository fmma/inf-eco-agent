# Inference Ecosystem — Full-Text Rescore

You are rescoring a single arXiv paper for relevance to LLM inference systems, now with access to the full text.

## Instructions

1. Read `config.json` for the topic description and keywords.
2. Below you will find the paper's metadata (title, authors, abstract) and its full text.
3. Rescore the paper from 0–100 for **relevance** using the same rubric:
   - **90-100**: Directly about LLM inference systems, serving frameworks, or inference optimization
   - **70-89**: Strongly related (e.g., KV cache, quantization for inference, speculative decoding, batching)
   - **50-69**: Tangentially related (e.g., general model compression, training efficiency that could apply to inference)
   - **0-49**: Not primarily about inference (e.g., pure training, datasets, applications)
4. Rescore the paper from 0–100 for predicted **hype** (how much attention it will get):
   - **80-100**: Major lab, famous authors, addresses hot topic, likely to get implementations
   - **60-79**: Known research group, novel approach to trending problem, practical and likely adopted
   - **40-59**: Solid work from less prominent group, incremental improvement on hot topic
   - **0-39**: Niche venue/authors, narrow applicability, unlikely to generate broad attention
5. Write a **description**: 2–3 sentences summarizing what the paper proposes, how it works, and key results. Be concrete — mention method names, speedups, benchmarks.
6. The score may go up or down compared to the abstract-only score. Use the full text to be more precise.
7. Output **only** a JSON object to stdout. No markdown, no explanation.

## Output Format

Print exactly this JSON structure and nothing else:

```json
{"id": "http://arxiv.org/abs/XXXX.XXXXXv1", "score": 85, "justification": "One-line reason for score.", "description": "2-3 sentence summary of the paper's contribution.", "hype": 70, "hype_justification": "One-line reason for hype score."}
```

## Important

- Be strict — only genuinely inference-focused papers should score 70+.
- Do not hallucinate details. Use only the text provided.
- Output ONLY the JSON object. No other text.
