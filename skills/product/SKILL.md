---
name: product
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
| Codebase analysis, tech debt, ADR, pattern, migration | **Architect Mode** → load `references/architect.md` |
| Write tickets, epics, stories, bugs | **Work Items** → load `references/work-items.md` |
| JIRA formatting, title patterns, ADF | **JIRA** → load `references/jira-conventions.md` |

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

Load `references/architect.md` for full details (tech debt grading, ADR template, migration planning).

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

### Document Rendering
Product skill owns content (5 dimensions: Context, Business, Technical, Assessment, Action). Dev skill renders via `document.html`. See `~/.agents/templates/section_library.md`.

### Handoff Protocol
| Deliverable | Consumer |
|---|---|
| Strategy (vision, roadmap) | Stakeholders → Analyst |
| Requirements (PRD, stories) | Design → Dev skill |
| Architecture (ADRs) | Dev skill |
| Sprint artifacts | Development team |

### Reference Index
| Reference | When to load |
|---|---|
| `references/architect.md` | ADRs, tech debt, migration |
| `references/jira-conventions.md` | JIRA formatting, titles |
| `references/work-items.md` | Writing epics, stories, bugs |
