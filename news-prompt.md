# Inference Ecosystem — Flash News

You are writing a short, punchy flash-news bulletin about noteworthy LLM inference papers.

## Instructions

1. Read `config.json` for the topic definition.
2. Below you will find **New Papers** — just discovered and scored. Each has a relevance score, hype score, and justifications.
3. Write a flash-news bulletin that:
   - Starts with `# Inference Ecosystem — Flash News` followed by today's date
   - Highlight only the top 3–5 most relevant (score 70+) papers. One sentence per paper on why it matters, plus score, e.g. "Score: 95". When a paper has a `description` field (from full-text analysis), prefer it over the abstract for your summary.
   - If full paper texts are provided, use them to write more insightful and concrete summaries — mention specific methods, key numbers, and benchmark results rather than just paraphrasing the abstract
   - Skip everything else — this is a flash bulletin, not a catalogue
   - If there's nothing flash-worthy, say so in one line

## Tone

- Newsletter flash style — concise, opinionated, forward-looking
- Focus on "why should an inference engineer care about this right now?"
- Use arXiv links where relevant

## Output format

- Output raw markdown only. No JSON, no code fences wrapping the entire output.
- Do not include any preamble like "Here is the analysis". Start directly with the markdown heading.
- Keep total length under 30 lines. Brevity is paramount — this gets posted to Discord.
