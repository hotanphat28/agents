# AI Analysis Guardrails

When analyzing a product or feature that involves AI, LLMs, or Machine Learning, apply these specific checks during the Validation Gate.

## 1. Viability Check (Product Owner)
* **The "Dumb" Alternative:** Is there a cheaper, deterministic heuristic (regex, simple if-statements, traditional search) that delivers 80% of the value without the cost and latency of an LLM?
* **Unit Economics:** Estimate the token cost per transaction. Does the business value generated per transaction exceed the LLM API costs? 
* **Latency vs. Accuracy:** Define the SLA. Are users willing to wait 5-10 seconds for a highly accurate response, or do they need a sub-second response that might require a smaller, less capable model?

## 2. Desirability Check (Business Analyst)
* **Trust & Transparency:** How does the UI communicate uncertainty? (e.g., "AI-generated response", citations, confidence scores).
* **The Fallback Path:** What is the UX when the AI hallucinates, times out, or returns a safety violation? The user must never be dead-ended.
* **Human-in-the-Loop:** For high-stakes decisions, does the user have the ability to review, edit, or override the AI's output before it takes effect?

## 3. Feasibility Check (Solution Architect)
* **Model Selection:** Open source (Llama, Mistral) vs. Commercial API (GPT-4, Claude 3.5, Gemini). Consider data privacy constraints.
* **Data Privacy & Compliance:** Are we sending PII or sensitive corporate data to external APIs? Does the provider guarantee zero data retention/training?
* **Context Limits:** Will the required data fit within the model's context window, or is a RAG (Retrieval-Augmented Generation) architecture required?
* **Non-Determinism:** How will the system handle the fact that identical inputs may produce different outputs? (e.g., temperature=0, structured JSON schemas).

## Architecture Decisions (ADR)
Any AI feature MUST produce an ADR that explicitly selects the model, justifies the cost, defines the privacy boundary, and outlines the evaluation strategy.
