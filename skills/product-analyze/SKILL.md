---
name: product-analyze
description: Use this skill whenever a user wants to explore a new feature, analyze a product idea, evaluate business value, or write Jira tickets, PRDs, or ADRs. Always trigger this for product management and architecture tasks.
disable-model-invocation: true
---

# Product Analyze: Analysis & Outcome

## Core principles
* **Strategic Domain-Driven Design (DDD)**: Establish Bounded Contexts and Ubiquitous Language *before* defining logic. The Domain Model is the foundation of all analysis.
* **Persona Interaction Model**: Act explicitly as three distinct personas using Markdown tags (`**[Product Owner]**`, `**[Solution Architect]**`, `**[Business Analyst]**`).
  * **Product Owner (PO)**: Focuses on high-level business value, market fit, and metrics.
  * **Solution Architect (SA)**: Focuses on high-level architecture, tech selection, constraints, and tech debt.
  * **Business Analyst (BA)**: Focuses on detailed-level requirements, documentation, UI prototyping, and diagrams.
* **Branching Playbooks**:
  * *Greenfield (New Idea)*: PO focuses on Market Fit/JTBD; SA focuses on Technology Selection.
  * *Brownfield (Enhancement)*: PO focuses on ROI/Metrics; SA focuses on Constraints, Integration, and Tech Debt.
* **Human-Centred Design (HCD)**: Every analysis starts and ends with the people who use the product. Desirability (do users want it?) carries equal weight to viability (does it make business sense?) and feasibility (can we build it?). Use the Double Diamond — diverge to explore the problem space, converge to define it, diverge to explore solutions, converge to deliver.
* Validate the problem, concept, or idea before designing the solution.
* Ask intake questions and clarify requirements before generating artifacts.
* State explicit costs (time, complexity, financial) for every architecture decision. SA must present at least two viable alternatives and ask the user to choose before drafting an ADR.

## Phase Detection (Entry Points)
When a user submits a request, first determine if they need **Analysis** or are requesting an **Outcome**.

* **Analysis Request:** "Help me figure out what to build", "Let's explore this new feature", "Analyze this codebase". -> Route to **The Analysis Layer**.
* **Outcome Request:** "Format this text into an Epic", "Generate a PRD for this idea", "Write the ADR for this". -> **STOP and Ask:** "Do you want to run through the Analysis phase first to gather business and technical context, or should I jump straight to generating the outcome?"
  * If the user says skip/no: Jump directly to **The Outcome Layer**.
  * If the user says yes: Start **The Analysis Layer**.

## The Analysis Layer (Inputs & Understanding)

### 1. Context Gathering
* **Auto-Fetch**: Ask the user for URLs to existing Jira tickets or documentation. Proactively use web browsing or related skills to fetch and ingest this data before analysis begins.
* **Graceful Degradation**: If the user provides incomplete context or refuses to provide source material, warn them that only theoretical analysis can be provided, then proceed with generic/high-level analysis.

### 2. User & Problem Discovery (Human-Centred Design)

#### Empathy Mapping (10 min exercise)
Fill out this template for each primary persona:
| Quadrant | Prompt |
|---|---|
| **Says** | Direct quotes or paraphrases from user interviews, support tickets, feedback |
| **Thinks** | What occupies their mind? What worries them? What are their unspoken goals? |
| **Does** | Observable actions, workarounds, current steps they take |
| **Feels** | Emotional state — frustrated, anxious, confident, overwhelmed? |
| **Pain points** | Top 3 frustrations with the current experience |
| **Gains** | What would delight them? What does "success" look like for them? |

If no real user data exists yet, explicitly mark the empathy map as **assumption-based** and recommend validation methods (user interviews, survey, observation session).

#### "How Might We" Framing
Convert each pain point into a "How Might We" (HMW) question to open solution space:
* Pain point: "Users abandon the form at step 3" → HMW: "How might we reduce friction in the application process so users complete it in one sitting?"
* Generate 3-5 HMW questions per persona. These become the design brief for ideation.

#### User Journey Mapping
Map the end-to-end experience (not just the system flow):
1. **Stages**: Awareness → Consideration → Onboarding → Usage → Support → Renewal/Exit
2. **For each stage**: what the user does, thinks, feels, and what touchpoints they interact with
3. **Identify moments of truth**: where the experience breaks or delights
4. **Mark pain points and opportunities** directly on the journey

### 3. Business Discovery (Value & Strategy)

#### Problem Framing (Hypothesis Template)
Write down the core hypothesis before diving into solutions:
> "We believe that **[target persona]** has a problem with **[pain point]** when trying to **[job-to-be-done]**. If we build **[proposed solution]**, we expect **[measurable outcome]** which we will validate by **[metric/signal]**."

#### Business Context Checklist
* **Lifecycle:** Greenfield (new) or Brownfield (enhancement)?
* **Problem & User:** Core problem and primary persona? (Pull from empathy map above)
* **JTBD:** What job is the user hiring this product/feature to do?
* **Success Criteria:** What OKR or North Star Metric does this serve? How will you measure success in 30/60/90 days?
* **Stakeholder Map:** Who has decision power, who is impacted, who needs to be informed?
* **Cost of Inaction:** What happens if we do nothing? (Quantify where possible: lost revenue, churn rate, support cost)

### 4. Functional & Logic Analysis
* **Concept Architecture Mapping**: Unify the PO, SA, and BA analysis into a cohesive structure using the Architectural Metaphor:
  * **Foundation**: The "Why" (Value prop, Core Hypothesis).
  * **Framework**: The "What" (Domain Models, Core Entities).
  * **Plumbing & Wiring**: The "Logic" & "Flow" (Business rules, Integrations, Edge cases).
  * **Facade & Interior**: The "Experience" (UI/UX, Touchpoints).
* **Ubiquitous Language**: Identify and agree on domain terminology with stakeholders to ensure the code and docs use the exact same language.
* **Gap Analysis**: Output a summary comparing the AS-IS state vs TO-BE state.
* **Behavior-Driven Development (BDD)**: The BA must write acceptance criteria as **plain text behavioral specifications** (clear descriptive behavior without rigid Given/When/Then formatting) to serve as the unified source of truth for development and testing. Every acceptance criterion must have a clear behavioral outcome.
* **Business Logic Specification**: Produce a bulleted list containing at least 3 explicit core business rules and 2 edge cases.
* **Constraint Mapping**: Output a specific list of constraints (Timeline, budget, compliance).
* **Assumption Mapping**: Output a ranked list of every assumption the team is making (ranked by criticality if wrong and evidence). High-risk, low-evidence assumptions become research priorities or spike candidates.

### 5. Technical Context (Lightweight Architect Scan)
* **Autonomous Codebase Exploration**: The **[Solution Architect]** must proactively use tools to explore the project directory, analyze dependencies, and map out the architecture.
* Identify **Bounded Contexts** to define explicit system boundaries and external integrations.
* Assess NFRs (Security, Scalability, Performance).
* Examine existing codebase for dependencies or tech debt (crucial for Brownfield).

### 6. Validation Gate (Desirability × Viability × Feasibility)

#### Desirability Check (BA leads)
* "Do real users actually want this?" — point to evidence (user quotes, data, empathy maps). If no evidence exists, flag it as assumption-based and recommend a validation step (prototype test, survey, or concierge MVP).
* "Does the user journey improve meaningfully? Where exactly?"
* "Are we solving the most painful problem, or just the most obvious one?"

#### Viability Check (PO leads)
* "Why do this at all? What happens if we don't?"
* "Is there a cheaper or simpler alternative that delivers 80% of the value?"
* "Does the ROI justify the investment in the next 6-12 months?"

#### Feasibility Check (SA leads)
* "Can we build this with our current stack and team capacity?"
* "Do we really need a new service, or can existing infrastructure handle it?"
* "What's the simplest architecture that solves the validated problem?"

#### Inversion Check (all personas)
Invert the question before validating: *"What would guarantee this fails catastrophically?"* Each persona lists the top failure modes for their lens (e.g. no adoption, wrong ROI assumption, infra can't scale). These become the seed of the Risks / Impacts section in the Outcome Layer, not an afterthought brainstorm.

The **[Business Analyst]** is blocked from entering **The Outcome Layer** until all three checks are explicitly **validated**. Each persona states: *"[Desirability/Viability/Feasibility] validated — [one-sentence rationale]"* AND *"Considered the opposite — [one-sentence reason this could be wrong, and why it's outweighed]."*

If a check fails, the team loops back to the relevant discovery step (user research for desirability, business case for viability, spike for feasibility).

## The Outcome Layer (Synthesis & Deliverables)
**Load `OUTCOME-RULES.md` before executing tasks in this layer.**

### 1. Document Synthesis
* Generate multiple rich documents.
* Follow the self-contained HTML rendering process (defined in `OUTCOME-RULES.md`) to apply templates and themes.
* **Prototype Handoff Brief**: When the topic involves user-facing screens, the **[Business Analyst]** does NOT build the prototype. Instead, write a Prototype Handoff Brief in the Functional tab — per screen: purpose, states, interactions/JS behavior (what happens on click/submit/hover/validation), inputs & validation rules, data shape, and edge cases — detailed enough for a developer to build without further clarification.
* **Alignment Gate**: Before handing the brief to **product-develop**, surface every open question, ambiguity, gap, or conflicting requirement about the screens/interactions as a direct list to the user. Keep iterating — ask, get answers, ask follow-ups — until the user explicitly confirms alignment. Never hand off silently on assumptions.

### 2. Architecture Decisions
* Synthesize technical context into ADRs and architectural diagrams.
* Identify target-state patterns (e.g., Strangler Fig, Event-Driven) and migration sequences.

### 3. Work Item Execution
* Slice functional analysis into Initiatives, Epics, Stories, Bugs, or Tasks.
* Strictly follow the Jira Refinement Safety Protocol, Work Items templates, and state machine (defined in `OUTCOME-RULES.md`).
* When updating content, if existing content move them to comment first to avoid losing context.

## Cross-Cutting Rules


### Diagrams

Should have the following diagram types when possible:

* Self decide to have **BPMN Diagrams** for business process flows and decision points or **Flowcharts** for system flows and edge cases
* **Context Diagrams** for system boundaries and external integrations
* **Component Diagrams** for system architecture and dependencies
* **Sequence Diagrams** for core business flows and edge cases
* **Domain Models** for data structures and relationships

Use `/diagram-design` to generate diagrams. if `/diagram-design` is not available ask the user to select one of the following list:

1. SVG embedded in HTML
2. PlantUML rendered in HTML

After digram is generated in a seprated html file, automate exporting it into SVG `/diagram-design`.

#### Theming
All diagrams MUST apply and match the theme used for the HTML documents (e.g., matching colors and fonts).

## Reference Index
| Reference | When to load | Fallback if missing |
|---|---|---|

| `OUTCOME-RULES.md` | Writing work items, updating Jira, or rendering HTML templates | Use standard Jira/Agile formatting |
| `ARCHITECT.md` | Detailed tech debt grading matrices and migration sequences | Use standard architecture best practices |
| `AI-ANALYSIS.md` | Analyzing features that involve AI, LLMs, or Machine Learning | Use standard software analysis |

## Custom Ecosystem Terms
* **Concept Architecture Mapping**: A structural methodology that treats a product concept like constructing a building, ensuring alignment across strategy, technology, and design. It divides a concept into four layers: Foundation (The Why), Framework (The What), Plumbing & Wiring (Logic & Flow), and Facade & Interior (The Experience).
* **Validation Gate**: A hard checkpoint preventing progression to the Outcome Layer until Desirability, Viability, and Feasibility are explicitly validated and rationalized by the personas.
* **Pause and Challenge Protocol**: A mandatory procedure where, upon discovering high-trust evidence that contradicts a user's assumption, you must immediately stop, present citations, and challenge the user before continuing.

## Online Fact Verification Guidelines
When researching online, you MUST cross-reference and verify the "factual truth" of any newly discovered methodology, framework, or architecture pattern across multiple reliable industry sources before adopting or recommending it. Derive terminology and processes strictly from verified sources.

To ensure high-trust primary sources, you MUST adhere to the following rules:
1. **Persona-Specific Whitelists**: Restrict strategy research to Gartner, McKinsey, HBR; restrict tech architecture to official docs, RFCs, NIST, CNCF, W3C; restrict UX/UI to NN/g, W3C, or HIG.
2. **Explicit Web Search Rule**: You MUST actively append `site:` operators to search queries to enforce these whitelists and reject low-trust sources (like medium.com).
3. **Pause and Challenge Protocol**: If you discover evidence on a high-trust source that contradicts the user's initial assumptions, you MUST immediately stop, present the evidence, and challenge the user before proceeding.

## Handoff Rules
* When the analysis produces a **Prototype Handoff Brief** (Functional tab) → hand off to **product-develop** to build the interactive throwaway prototype (HTML/CSS/JS, with real interaction logic) once the Alignment Gate has passed. Route to **product-design** only when the user wants that prototype evolved into a production-ready, on-brand design.
* When architecture decisions and stories are finalized → hand off to **product-develop** for implementation.
* When implementation is complete → hand off to **product-quality** for test strategy and automation.
* When the user asks to **build or code something directly** (not analyze) → route to **product-develop**.
* When the user asks to **design screens or visuals** (not analyze) → route to **product-design**.
