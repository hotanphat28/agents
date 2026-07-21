---
name: product-analyze
description: >
  The complete product lifecycle skill — structured around two core phases: Analysis and Outcome.
  Use this skill for discovery, ideation, business values, functionalities, technical requirements,
  and synthesizing these into documentation, templates, and JIRA tickets. Applies to both
  greenfield builds and brownfield enhancements.
---

# Product Analyze: Analysis & Outcome
Full product lifecycle — from unvalidated idea through shipped, measured, iterated product.

## Core principles
* Strategy before stories — validate the problem before designing the solution
* No artifacts without context — intake questions first
* Architecture decisions state trade-offs — no advice without cost
* Start simple, add complexity only when evidence demands it
* Every deliverable has a clear next consumer (design/dev skill, stakeholder, team)

## Phase Detection (Entry Points)
When a user submits a request, first determine if they need **Analysis** or are requesting an **Outcome**.

* **Analysis Request:** "Help me figure out what to build", "Let's explore this new feature", "Analyze this codebase". -> Route to **The Analysis Layer**.
* **Outcome Request:** "Format this text into an Epic", "Generate a PRD for this idea", "Write the ADR for this". -> **STOP and Ask:** "Do you want to run through the Analysis phase first to gather business and technical context, or should I jump straight to generating the outcome?"
  * If the user says skip/no: Jump directly to **The Outcome Layer**.
  * If the user says yes: Start **The Analysis Layer**.

## The Analysis Layer (Inputs & Understanding)
This layer builds a comprehensive "Mental Model" across multiple dimensions before any deliverables are written.

### 1. Context Gathering
Always explicitly ask the user to provide the source of documentation, source code directory, or existing context. Scan and analyze this provided source first.

### 2. Business Discovery (Ideation & Value)
Ask only what cannot be deduced from context gathering:
* **Lifecycle:** Greenfield (new) or Brownfield (enhancement)?
* **Problem & User:** Core problem and primary persona?
* **Strategy & Success:** OKRs, North Star Metric, GTM strategy, Revenue/Retention?

### 3. Functional & Logic Analysis
* Map the AS-IS state vs TO-BE state (Gap Analysis).
* Define core business rules, journey maps, and edge cases.
* Identify constraints (Timeline, budget, compliance).

### 4. Technical Context (Lightweight Architect Scan)
* Define system boundaries and external integrations.
* Assess NFRs (Security, Scalability, Performance).
* Examine existing codebase for dependencies or tech debt (crucial for Brownfield).

Once the mental model is 90% confident, transition to the **Outcome Layer**.

## The Outcome Layer (Synthesis & Deliverables)
This layer transforms the Mental Model into tangible artifacts. **Load `OUTCOME-RULES.md` before executing tasks in this layer.**

### 1. Document Synthesis
* Generate multiple rich documents.
* Follow the self-contained HTML rendering process (defined in `OUTCOME-RULES.md`) to apply templates and themes.

### 2. Architecture Decisions
* Synthesize technical context into ADRs and architectural diagrams.
* Identify target-state patterns (e.g., Strangler Fig, Event-Driven) and migration sequences.

### 3. Work Item Execution
* Slice functional analysis into Epics, Stories, Bugs, or Tasks.
* Strictly follow the Jira Refinement Safety Protocol and state machine (defined in `OUTCOME-RULES.md`).

## Cross-Cutting Rules

### Online Fact Verification Guidelines
When researching online, you MUST cross-reference and verify the "factual truth" of any newly discovered methodology, framework, or architecture pattern across multiple reliable industry sources before adopting or recommending it. Never invent terminology or processes. If a concept cannot be factually verified across multiple sources, fall back to the definitions in `GLOSSARY.md` or standard practices.

### Diagrams

Should have the following diagram types when possible:

* **Context Diagrams** for system boundaries and external integrations
* **Sequence Diagrams** for core business flows and edge cases
* **Component Diagrams** for system architecture and dependencies
* **Domain Models** for data structures and relationships

#### Hierarchy (in order of preference)
1. SVG embedded within HTML
2. Draw.io (if MCP server is available)
3. Mermaid
4. PlantUML

#### Theming
All diagrams MUST apply and match the theme used for the HTML documents (e.g., matching colors and fonts).

## Reference Index
| Reference | When to load | Fallback if missing |
|---|---|---|
| `GLOSSARY.md` | Resolving ambiguous product, agile, or architecture terminology | Use standard industry definitions |
| `OUTCOME-RULES.md` | Writing work items, updating Jira, or rendering HTML templates | Use standard Jira/Agile formatting |
| `ARCHITECT.md` | Detailed tech debt grading matrices and migration sequences | Use standard architecture best practices |
