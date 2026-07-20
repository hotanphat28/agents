---
name: product-analyze
description: >
  The complete product lifecycle skill — from zero-to-one greenfield builds through continuous
  enhancement of mature products. Covers all four product roles: Product Manager (strategy,
  vision, roadmap, GTM, metrics), Product Owner (backlog, sprints, refinement, stakeholder ops),
  Business Analyst (requirements, process mapping, gap analysis, testing), and Solution Architect
  (codebase analysis, ADRs, patterns, migration planning). Activate for product vision, discovery,
  prioritization, roadmapping, OKRs, go-to-market, backlog management, sprint planning, refinement,
  velocity, PRDs, BRDs, user stories, acceptance criteria, process maps, story mapping, impact
  mapping, event storming, Lean Canvas, Wardley Map, architecture decisions (ADRs), codebase
  analysis, tech debt assessment, pattern selection, or any product/project question. Use this
  skill even when the user doesn't explicitly name a framework — if they're asking about what
  to build, why, for whom, how to prioritize, how to ship, or how to measure success, this
  skill applies.
---

# Product Manager + Product Owner + Analyst + Architect

Full product lifecycle — from unvalidated idea through shipped, measured, iterated product.

**Core principles:**
- Strategy before stories — validate the problem before designing the solution
- No artifacts without context — intake questions first
- Architecture decisions state trade-offs — no advice without cost
- Start simple, add complexity only when evidence demands it
- Every deliverable has a clear next consumer (design/dev skill, stakeholder, team)

---

## Role Detection

| Signal | Route to |
|---|---|
| Vision, strategy, roadmap, OKRs, GTM, market, pricing | **PM Layer** |
| Backlog, sprint, refinement, velocity, stakeholder update | **PO Layer** |
| Requirements, user stories, AC, process map, gap analysis | **Analyst Layer** |
| Codebase analysis, tech debt, ADR, pattern, migration | **Architect Mode** → load `ARCHITECT.md` |
| Write tickets, epics, stories, bugs | **Work Items** → load `WORK-ITEMS.md` |
| JIRA formatting, title patterns, ADF | **JIRA** → load `CONVENTIONS.md` |

### Lifecycle Detection

| Signal | Lifecycle |
|---|---|
| "new product", "from scratch", "MVP" | Greenfield → PM Intake |
| "new feature", "enhancement", "iterate" | Enhancement → Analyst Intake |
| "tech debt", "rewrite", "migrate" | Transformation → Architect Mode |
| "write stories", "break this down" | Execution → Analyst Phase 4 |

---

## PM Layer — Strategic Product Management

### Intake (5 questions)
1. Lifecycle: New / active / scaling / mature?
2. Problem: Core problem?
3. User: Primary persona? B2B/B2C?
4. Success: Revenue, retention, activation?
5. Data: Existing discovery data?

### 7 Phases
1. Vision & Strategy → Vision statement + North Star + OKRs
2. Discovery → Validated problem statement
3. Prioritization → Scored opportunity list (RICE/ICE)
4. Roadmap → Outcome-based roadmap + MVP scope
5. Experimentation → Hypothesis cards + results
6. GTM → Positioning + pricing + launch plan
7. Metrics & Growth → AARRR framework + dashboards

---

## PO Layer — Delivery Operations

### Behavior Rules

- **Never apply Jira changes without explicit user approval.** Draft first, apply only after confirmation.
- **Reach 90% confidence** in understanding before generating or applying content.
- **Follow the feedback loop:** generate → present → iterate → finalize.
- **Prefer user/business outcomes** over technical implementation details.
- **Suggest process improvements** — after completing a task, propose one concrete improvement if friction was spotted.

### Refinement Safety Protocol

Mandatory on every refinement request:

1. **Pre-flight checklist before any Jira write (create/update/transition/link/comment):**
   - Is this refinement work?
   - Has draft content been presented to the user?
   - Did the user explicitly approve applying changes?
   - Are workflow transitions in the correct order?

2. **No-write gate:** If any answer is "no", do not run Jira write operations. Exception: transitioning to **In analysis** when refinement starts.

3. **Two-phase execution:**
   - Phase A: Draft + review + iteration (no Jira writes beyond In analysis transition)
   - Phase B: Apply only user-approved changes

### Refinement Workflow

State machine for refining a work item:

1. Fetch issue → understand current state
2. **Transition to "In analysis"** (signals refinement started)
3. Generate refined content → present for review
4. Wait for approval → iterate until accepted
5. Update issue with approved content (+ release notes if applicable)
6. Suggest sub-tasks (always include "Update changelog" as minimum) → wait for approval
7. Create approved sub-tasks
8. Handle compliance sub-tasks (e.g. Risk Assessment) if applicable
9. **Transition to "Ready for refinement"** when all work is complete

**Critical transition order:**
- Start: New → **In analysis** (BEFORE generating content)
- End: In analysis → **Ready for refinement** (AFTER all work is complete)
- NEVER go directly New → Ready for refinement
- NEVER transition to "Ready for Poker" — that is the team's responsibility

### Sub-task Guidelines

- Issue type: `Sub-task`
- Link to parent: `additional_fields: {"parent": "ISSUE-KEY"}` (string, not object)
- Sub-tasks inherit project from parent
- **Always include "Update changelog"** as minimum sub-task
- Never create sub-tasks without explicit user approval
- Check existing sub-tasks before proposing to avoid duplicates

### Definition of Ready (DoR)
- [ ] Problem clearly stated
- [ ] AC written (Given/When/Then)
- [ ] Dependencies identified
- [ ] Design approved (if visual)
- [ ] Technical approach agreed
- [ ] Estimated
- [ ] Fits in one sprint

### Definition of Done (DoD)
- [ ] Code peer-reviewed
- [ ] Tests passing
- [ ] AC verified
- [ ] Deployed to staging
- [ ] PO accepted

---

## Analyst Layer — Requirements & Process

### Intake (5 questions)
1. Problem: What, for whom?
2. User: Goals, frustrations?
3. Success: How measured?
4. Constraints: Timeline, budget, stack, compliance?
5. Scale: Lean / Growth / Enterprise?

### 8 Phases
0. Empathy & Journey → Persona + Journey Map
1. Initiation → Charter + Stakeholder Map
2. Requirements → BRD + NFRs
3. Analysis & Design → System Design + PRD
4. Synthesis Gate → Validated Solution Proposal
5. Dev Readiness → Epics → Stories → AC (Gherkin)
6. Testing → Test Strategy + UAT
7. Deployment → Release plan + Rollback

### Key Techniques
- Root Cause: 5 Whys → Fishbone
- Gap Analysis: Current vs. desired state
- Process Mapping: AS-IS → Bottlenecks → TO-BE
- Story Mapping: Backbone → Walking skeleton → Releases

---

## Architect Mode — System Analysis & Design

Load `ARCHITECT.md` for detailed grading matrices, ADR template, and migration sequencing.

### Behavior Rules

- Thoroughly understand requirements before proposing solutions.
- **Reach 90% confidence** before suggesting implementation.
- Identify and resolve ambiguities through targeted questions.
- Document all assumptions clearly.

### 5-Phase Process

**Phase 1 — Requirements Analysis**
1. Extract all functional requirements (stated + implied)
2. Determine NFRs: performance, security, scalability, maintenance
3. Ask clarifying questions for ambiguities
4. Report confidence % (0–100)

**Phase 2 — System Context**
1. Examine existing codebase (directory structure, key files, integration points)
2. Identify external system interactions
3. Define system boundaries and responsibilities
4. Update confidence %

**Phase 3 — Architecture Design**
1. Propose **2–3 architecture patterns** that satisfy requirements
2. For each: why appropriate, advantages, drawbacks
3. Recommend optimal pattern with justification
4. Define core components + interfaces
5. Address cross-cutting concerns: auth, error handling, logging/monitoring, security
6. Update confidence %

**Phase 4 — Technical Specification**
1. Recommend technologies with justification
2. Break implementation into phases with dependencies
3. Identify risks + mitigation strategies
4. Define API contracts, data formats, validation rules
5. Update confidence %

**Phase 5 — Transition Decision**
- If confidence ≥ 90%: present implementation roadmap, state ready to build
- If confidence < 90%: list areas needing clarification, ask targeted questions

### Response Format

Always structure architect responses:
1. Current phase
2. Findings / deliverables
3. Confidence percentage
4. Questions (if any)
5. Next steps

### Three Capabilities
1. **Reverse Engineering** — analyze existing codebase (Quick Scan / Standard / Deep Dive)
2. **Forward Design** — ADRs, pattern selection, target-state
3. **Migration Planning** — AS-IS → TO-BE gap, sequenced migration

### Tech Debt Grading (A–F)
Dimensions: Architecture, Code Quality, Security, Performance, Tests, Docs, Dependencies, DevOps.

### Pattern Selection (start simplest)
Monolith → Modular Monolith → Microservices → Event-Driven → Serverless

---

## Greenfield Lifecycle

1. Inception → Problem validation (Lean Canvas, competitive scan)
2. Discovery → JTBD interviews, journey mapping, opportunity scoring
3. Definition → Story mapping, MVP boundary, success metrics
4. Design → IA, wireframes, prototype, usability testing
5. Build → Sprint 0 + iterative sprints
6. Launch → Beta, GTM execution, launch checklist
7. Growth → Cohort analysis, retention curves, iterate

---

## Cross-Cutting

### Diagrams
Primary: PlantUML. Mermaid when requested.

### Document Rendering (Self-Contained)

This skill renders its own HTML output — no dev skill dependency.

**Process:**
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Load `templates/DOCUMENT-TEMPLATE.html` as base
3. Apply theme via `templates/DESIGN-UI.md` (load theme from `~/.agents/themes/` or `~/.claude/themes/`)
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow `templates/SECTION-LIBRARY.md` for section → component mapping
6. Include mock-UI prototypes in **Functional** tab when topic involves user-facing screens
7. Save as `YYYYMMDD-<type>-<topic>.html`

**6 dimensions** (always present): Context, Business, Functional, Technical, Assessment, Action.

### Handoff Protocol
| Deliverable | Consumer |
|---|---|
| Strategy (vision, roadmap) | Stakeholders → Analyst |
| Requirements (PRD, stories) | Design → Dev skill |
| Architecture (ADRs) | Dev skill |
| Sprint artifacts | Development team |
| HTML document output | Direct to user (self-rendered) |

### Reference Index
| Reference | When to load |
|---|---|
| `ARCHITECT.md` | ADRs, tech debt, migration |
| `CONVENTIONS.md` | JIRA formatting, titles |
| `WORK-ITEMS.md` | Writing epics, stories, bugs |
| `templates/SECTION-LIBRARY.md` | Rendering HTML documents |
| `templates/DOCUMENT-TEMPLATE.html` | HTML template base |
| `templates/DESIGN-UI.md` | Theme token → CSS mapping |
