# Inference Ecosystem Paper Scanner

You are scoring arXiv papers for relevance to LLM inference systems.

## Instructions

1. Read `config.json` for the topic description, keywords, and relevance threshold.
2. The papers JSON has been provided as input (from stdin). Parse it.
3. Score each paper from 1-10 for relevance to the configured topic:
   - **9-10**: Directly about LLM inference systems, serving frameworks, or inference optimization
   - **7-8**: Strongly related (e.g., KV cache, quantization for inference, speculative decoding, batching)
   - **5-6**: Tangentially related (e.g., general model compression, training efficiency that could apply to inference)
   - **1-4**: Not primarily about inference (e.g., pure training, datasets, applications)
4. Write a markdown report to `reports/YYYY-MM-DD.md` (using today's date) containing:
   - A header with the date
   - Summary: total papers scanned, number above threshold
   - A table or list of papers scoring >= the threshold (from config.json), sorted by score descending
   - For each paper: title (linked to arXiv), score, one-line justification, authors (first 3 + "et al." if more), first 200 chars of abstract
5. Update `reports/README.md` — maintain an index of all report files with dates and paper counts. Create the file if it doesn't exist.
6. Git add the new/updated report files, commit with message "scan: YYYY-MM-DD — N relevant papers", and push.

## Output Format for Each Paper

```markdown
### Title of Paper
**Score: 8/10** — One-line justification of why this score.
*Authors: First Author, Second Author, Third Author et al.*
*Published: 2025-01-15*
[arXiv](https://arxiv.org/abs/XXXX.XXXXX) | [PDF](https://arxiv.org/pdf/XXXX.XXXXX)

> First 200 characters of abstract...
```

## Important

- If no papers meet the threshold, still write the report noting "No papers above threshold today."
- Be strict with scoring — only genuinely inference-focused papers should score 7+.
- Do not hallucinate paper details. Use only the data provided in the JSON.
