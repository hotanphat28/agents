---
name: product-analyze
description: The complete product lifecycle skill — structured around two core phases: Analysis and Outcome. Use this skill for discovery, ideation, business values, functionalities, technical requirements, and synthesizing these into documentation, templates, and JIRA tickets. Applies to both greenfield builds and brownfield enhancements.
---

# Product Analyze: Analysis & Outcome
Full product lifecycle — from unvalidated idea through shipped, measured, iterated product.

## Core principles
* **Persona Interaction Model**: Act explicitly as three distinct personas using Markdown tags (`**[Product Owner]**`, `**[Solution Architect]**`, `**[Business Analyst]**`).
  * **Product Owner (PO)**: Focuses on high-level business value, market fit, and metrics.
  * **Solution Architect (SA)**: Focuses on high-level architecture, tech selection, constraints, and tech debt.
  * **Business Analyst (BA)**: Focuses on detailed-level requirements, documentation, UI prototyping, and diagrams.
* **Branching Playbooks**:
  * *Greenfield (New Idea)*: PO focuses on Market Fit/JTBD; SA focuses on Technology Selection.
  * *Brownfield (Enhancement)*: PO focuses on ROI/Metrics; SA focuses on Constraints, Integration, and Tech Debt.
* Strategy before stories: Validate the problem/concept/idea before designing the solution
* No artifacts without context: Intake questions and clarify requirements first
* Architecture decisions state trade-offs: No advice without cost. SA must present at least two viable alternatives with explicit costs (time, complexity, financial) and ask the user to choose before drafting an ADR.
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
* **Auto-Fetch**: Ask the user for URLs to existing Jira tickets or documentation. Proactively use web browsing or related skills to fetch and ingest this data before analysis begins.
* **Graceful Degradation**: If the user provides incomplete context or refuses to provide source material, warn them that only theoretical analysis can be provided, then proceed with generic/high-level analysis.

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
* **Autonomous Codebase Exploration**: The **[Solution Architect]** must proactively use tools to explore the project directory, analyze dependencies, and map out the architecture.
* Define system boundaries and external integrations.
* Assess NFRs (Security, Scalability, Performance).
* Examine existing codebase for dependencies or tech debt (crucial for Brownfield).

### 5. Devil's Advocate Phase (Validation Gate)
Before any documentation or tickets can be drafted, the idea MUST survive rigorous pushback:
* **PO Devil's Advocate**: The **[Product Owner]** must actively challenge the core value proposition. (e.g., "Why do this at all?", "What happens if we do nothing?", "Is there a cheaper alternative?").
* **SA Technical Pushback**: The **[Solution Architect]** must actively challenge the technical necessity. (e.g., "Do we really need a new microservice?", "Can we achieve this with existing infrastructure?", "Why not just use a simple cron job?").
* **Explicit BA Gate**: The **[Business Analyst]** is COMPLETELY BLOCKED from entering **The Outcome Layer** (no templates, no tickets, no prototypes) until both the PO and SA explicitly state to the user: *"Devil's Advocate phase complete. Value and necessity validated."*

Once the "Analysis Checklist" (Problem defined, AS-IS/TO-BE mapped, Tech boundaries identified, and Devil's Advocate survived) is completely checked off by the PO and SA, hand off to the **[Business Analyst]** for the **Outcome Layer**.

## The Outcome Layer (Synthesis & Deliverables)
This layer transforms the Mental Model into tangible artifacts. The **[Business Analyst]** takes over here. **Load `OUTCOME-RULES.md` before executing tasks in this layer.**

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

To ensure high-trust primary sources, you MUST adhere to the following rules during online research:
1. **Persona-Specific Whitelists**:
   - **Product Owner (PO)**: Restrict strategy and business research to sources like Gartner, McKinsey, Harvard Business Review, or official financial reports.
   - **Solution Architect (SA)**: Restrict technical architecture and constraint research to official documentation (e.g., `docs.aws.amazon.com`, `developer.apple.com`), RFCs, NIST, CNCF, or W3C.
   - **Business Analyst (BA)**: Restrict UX/UI and documentation standard research to sources like Nielsen Norman Group, W3C, or official Material Design/Human Interface Guidelines.
2. **Explicit Web Search Rule**: You MUST actively append `site:` operators to your search queries to enforce these whitelists and actively reject low-trust sources (like medium.com or unverified blog posts).
3. **Pause and Challenge Protocol**: If you discover evidence on a high-trust primary source that directly contradicts the user's initial assumptions or requirements, you MUST immediately stop, present the evidence (with citations), and challenge the user's assumption before proceeding.

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
