# AI Engineering

Personal defaults and patterns for LLM integration, RAG, agents, and evals.

---

## Default AI Stack

| Layer | Technology |
|---|---|
| LLM Provider | Google Gemini API (primary), Anthropic Claude (secondary) |
| Language | Python 3.11+ (async-first) |
| Agent Framework | None (raw SDK) — add LangGraph/CrewAI only when complexity warrants |
| Vector DB | Chroma (dev) / pgvector (prod) / Pinecone (managed) |
| Embeddings | Gemini `gemini-embedding-001` |
| Eval | Custom pytest suite |

---

## Prompt Management

- Store prompts as files in `ai/prompts/`, not inline strings
- Version with semantic versioning (system-v1.0.md, system-v1.1.md)
- Pin prompt version per environment (dev = latest, prod = exact)
- Log prompt version with every LLM call
- Temperature: 0 for deterministic, 0.3-0.7 creative, 1.0+ brainstorming

---

## RAG Defaults

| Setting | Value |
|---|---|
| Chunk size | 512-1024 tokens |
| Overlap | 10-20% |
| Top-k retrieval | 3-5 chunks |
| Similarity threshold | 0.7-0.8 cosine |
| Search strategy | Hybrid (vector + BM25) |
| Reranking | Cross-encoder when precision matters |

Always attach source metadata (file, page, section, date) to chunks. Always cite sources in responses.

---

## Agent Design Rules

- Tool names: `verb_noun` format (`search_documents`, `create_ticket`)
- Tool descriptions: explain WHEN to use, not just what it does
- Max iterations: 5-10 loops to prevent runaway agents
- Log every tool call (input, output, latency)
- High-stakes actions require human confirmation

---

## Eval Protocol (Non-Negotiable)

Every AI feature ships with an eval. No exceptions.

1. **Golden dataset**: 20-50 test cases (happy path + edge cases + adversarial)
2. **Run on every change**: prompt edits, model upgrades, pipeline changes
3. **Track metrics over time**: accuracy trends in dashboard
4. **Regression alerts**: notify when accuracy drops below threshold

### Scoring Methods

| Method | When |
|---|---|
| Exact match | Structured output, classification |
| Contains / regex | Key info extraction |
| Semantic similarity | Open-ended generation |
| LLM-as-judge | Quality, helpfulness, safety |

---

## Cost Management

- Track cost per request (tokens × price)
- Set budget alerts + hard ceilings per day/month
- Cache identical requests (hash input → cache response)
- Use smaller models for simple tasks, route complex to capable models
- Compress context: summarize history, prune irrelevant chunks

---

## Safety Guardrails

- Input filtering: block prompt injection at user boundary
- Output filtering: sanitize before display (strip HTML, validate format)
- Token budget + rate limiting per user/session
- Timeout: 30-120s max per agent run
- Don't send PII to external LLM APIs unless necessary and consented
