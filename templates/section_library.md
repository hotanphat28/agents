## Section & Component Library

> Reference for the LLM when rendering `document.html`.
> Maps use cases → dimensions → tab structure → CSS components.
> Pick sections based on context. No use case requires all sections — choose what has evidence or value.

---

## 5-Dimension Framework

Every document covers a topic through **5 dimensions**. This ensures consistent business + technical coverage regardless of use case. Skip dimensions that have no evidence — but consider all five before deciding what to include.

| Dimension | What it covers | Typical components |
|-----------|---------------|-------------------|
| **Context** | Problem/vision, scope, stakeholders, personas | Hero, `.persona`, `.problem-box`, `.ref-note` |
| **Business** | Impact, journeys, metrics, cost-benefit, process flows, stakeholder mapping | `.journey-table`, `.okr-block`, `.metric-hl`, `.stats-grid`, `.score-table`, `.matrix-2x2` |
| **Technical** | Architecture, data model, integrations, APIs, deployment, configuration | `.card-diagram`, `.ref-table`, `.cap-grid`, `details.collapsible` |
| **Assessment** | Findings, scorecard, risks, dependencies, compliance, quality | `.finding`, `.scorecard`, `.checklist`, `.ref-note` |
| **Action** | Roadmap, decisions, next steps, delivery phases, migration plan | `.timeline`, `.steps-list`, `.story-card`, `.score-table` |

---

## Skill Collaboration Protocol

Documents are produced by **product skill** (content) and **dev skill** (rendering) working together:

1. **Product skill** determines use case type, runs intake, produces structured content across all 5 dimensions, generates PlantUML diagrams, and signals depth level (light / standard / deep).
2. **Dev skill** (Design-Quality UI mode) receives the content and makes rendering decisions: template mode (tabbed or linear), tab labels, component selection per section, and theme application.

**Product owns WHAT.** Dev owns HOW. This library is the bridge between them.

---

## Depth Levels

Each use case can be rendered at different depths. Depth determines mode:

| Depth | Mode | When to use |
|-------|------|-------------|
| **Light** | Linear (no tabs) | Quick summary, pitch, brief, sprint scope. Content fits 1-3 pages. |
| **Standard** | Tabbed | Default for most documents. Multiple domains to cover. |
| **Deep** | Tabbed | Comprehensive analysis with gap/migration/target state. Many diagrams. |

**Linear mode**: Omit `<nav class="tabs">` and `<section class="panel">` wrappers. Cards stack directly inside `<main class="wrap">`.

---

## Use Case → Sections Map

### 1. Analysis

Understand current state, assess quality, identify gaps. Covers: as-is analysis, gap analysis, codebase review, tech debt assessment.

**Depth guidance:**
- Light → Quick audit summary (linear). Skip Business dimension.
- Standard → Full analysis with all dimensions (tabbed).
- Deep → Gap analysis with current vs target state comparison (tabbed).

**Standard tabs:** Context | Business | Technical | Assessment

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Problem Statement / Scope | Hero `{{HEADING}}` + `{{DESCRIPTION}}` | — | Context | ✓ |
| Baseline Metrics | `.stats-grid` / `.metric-hl` | Context | Context | |
| Personas | `.persona` cards | Context | Context | |
| Current Architecture | `.card-diagram` (context diagram SVG) | Technical | Technical | ✓ |
| Component Inventory | `.ref-table` (component, tech, status, owner) | Technical | Technical | ✓ |
| Integration Points | `.ref-table` (system, direction, protocol, status) | Technical | Technical | |
| Data Model | `.card-diagram` (ERD SVG) | Technical | Technical | |
| User Flows (current) | `.journey-table` or `.card-diagram` | Business | Business | |
| Process Map (AS-IS) | `.card-diagram` (BPMN SVG) | Business | Business | |
| Stakeholder Map | `.matrix-2x2` (power × interest) or `.ref-table` | Business | Business | |
| Cost / Effort Baseline | `.stats-grid` or `.ref-table` | Business | Business | |
| Tech Debt Scorecard | `.scorecard` (A–F per dimension) | Assessment | Assessment | ✓ |
| Audit Findings | `.finding` (severity-flagged issues) | Assessment | Assessment | ✓ |
| Pain Points / Gaps | `.pain-grid` with `.critical` / `.warning` | Assessment | Assessment | |
| Compliance Checklist | `.checklist` (pass/fail/warn per control) | Assessment | Assessment | |
| Risks & Dependencies | `.scenario` or `.finding` | Assessment | Assessment | |
| Recommendations | `.steps-list` or `.timeline` | Assessment | Action | ✓ |
| ADRs / Decisions | `details.collapsible` (ADR format) | Assessment | Action | |

**Deep mode additions (gap analysis):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Target State Vision | `.problem-box` or Hero watermark "TO-BE" | Context | Context |
| Gap Summary | `.pain-grid` or `.ref-table` (current vs target) | Assessment | Assessment |
| Target Architecture | `.card-diagram` (target context diagram) | Technical | Technical |
| Value-Effort Matrix | `.matrix-2x2` | Assessment | Business |
| Bridging Actions | `.timeline` (phased migration) | Assessment | Action |

---

### 2. Proposal

Propose something new — from problem validation to full PRD. Covers: discovery, feature proposal, concept pitch, to-be proposal, PRD, design brief.

**Depth guidance:**
- Light → Concept pitch or discovery one-pager (linear). Focus on Context + Action.
- Standard → Feature proposal or PRD (tabbed).
- Deep → Full to-be proposal with target architecture and ADRs (tabbed).

**Standard tabs:** Vision | Users | Solution | Delivery

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Problem Statement | Hero `{{HEADING}}` + `.problem-box` | — | Context | ✓ |
| OKRs / Objectives | `.okr-block` | Vision | Business | |
| Success Metrics | `.metric-hl` (North Star) + `.stats-grid` | Vision | Business | ✓ |
| Business Case | `.ref-note` (info callout) or `.callout-box` | Vision | Business | |
| Competitive Landscape | `.ref-table` or `.matrix-2x2` | Vision | Business | |
| Personas | `.persona` cards | Users | Context | ✓ |
| User Journeys | `.journey-table` | Users | Business | |
| Pain Points | `.pain-grid` with `.critical` / `.warning` | Users | Context | |
| Real-World Scenarios | `.scenario` with `.red` / `.amber` / `.blue` | Users | Context | |
| Target Architecture | `.card-diagram` (SVG) | Solution | Technical | |
| Feature Capabilities | `.cap-grid` / `.cap-card` | Solution | Technical | ✓ |
| API Changes | `.ref-table` (endpoint, method, purpose) | Solution | Technical | |
| Data Model | `.card-diagram` or `.ref-table` | Solution | Technical | |
| ADRs / Decisions | `details.collapsible` (ADR format) | Solution | Technical | |
| Scope (in/out) | `.checklist` (pass = in, fail = out) | Solution | Context | |
| Prioritization | `.score-table` (RICE/ICE) | Delivery | Business | |
| Value-Effort Matrix | `.matrix-2x2` | Delivery | Business | |
| Risks & Dependencies | `.finding` or `.scenario` | Delivery | Assessment | ✓ |
| Key Assumptions | `.ref-table` with `.tag` severity | Delivery | Assessment | |
| Release Strategy | `.timeline` (phased plan) | Delivery | Action | ✓ |
| Constraints | `.ref-note` (warning callout) | Delivery | Assessment | |
| Next Steps | `.steps-list` | Delivery | Action | |

**Deep mode additions (to-be proposal):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Gap Summary | `.pain-grid` or `.ref-table` (current vs target) | Vision | Assessment |
| Migration Phases | `.timeline` (phased plan) | Delivery | Action |
| Strangler Pattern / Boundary | `.card-diagram` | Solution | Technical |
| Success Metrics (target) | `.stats-grid` + `.metric-hl` | Vision | Business |

---

### 3. Plan

Detail execution — from sprint brief to full migration plan. Covers: implementation plan, data migration plan, API/integration spec, sprint goal brief, implementation handoff.

**Depth guidance:**
- Light → Sprint brief or implementation handoff (linear). Focus on Context + Action.
- Standard → Implementation plan (tabbed).
- Deep → Full migration plan with rollback strategy and detailed specs (tabbed).

**Standard tabs:** Overview | Architecture | Implementation | Delivery

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Scope & Objectives | Hero + `.problem-box` or `.ref-note` (info) | — | Context | ✓ |
| Personas | `.persona` cards | Overview | Context | |
| Success Metrics | `.stats-grid` or `.metric-hl` | Overview | Business | |
| Cost-Benefit Summary | `.ref-table` or `.callout-box` | Overview | Business | |
| Architecture Diagram | `.card-diagram` (SVG) | Architecture | Technical | ✓ |
| Component Map | `.ref-table` (component, status, description) | Architecture | Technical | ✓ |
| API Changes / Endpoints | `.ref-table` (endpoint, method, purpose, auth) | Architecture | Technical | |
| Data Model Changes | `.card-diagram` or `.ref-table` | Architecture | Technical | |
| Sequence Diagrams | `.card-diagram` per flow | Architecture | Technical | |
| ADRs / Decisions | `details.collapsible` (ADR format) | Architecture | Technical | |
| Screen Inventory | `.ref-table` (screen, route, purpose, priority) | Implementation | Technical | |
| User Stories | `.story-card` (with Gherkin AC) | Implementation | Action | |
| Acceptance Criteria | `.ref-table` or `.checklist` | Implementation | Action | |
| Test Strategy | `.ref-table` or `.checklist` | Implementation | Assessment | |
| Delivery Phases | `.timeline` | Delivery | Action | ✓ |
| Dependencies | `.ref-note` (warning callout) or `.scenario` | Delivery | Assessment | ✓ |
| Constraints & Risks | `.finding` (severity-flagged) | Delivery | Assessment | |
| Rollback Strategy | `.callout-box` or `.ref-note` | Delivery | Assessment | |
| Next Steps | `.steps-list` | Delivery | Action | |

**Deep mode additions (migration / integration spec):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Source → Target Mapping | `.ref-table` (source field, target field, transform) | Implementation | Technical |
| Data Validation Rules | `.checklist` or `.ref-table` | Implementation | Assessment |
| Error Handling Strategy | `.ref-table` (error, response, retry) | Architecture | Technical |
| Auth / Security Model | `.ref-table` or `.cap-grid` | Architecture | Technical |
| Performance Targets | `.stats-grid` or `.metric-hl` | Overview | Business |
| Reconciliation / Verification | `.checklist` (pass/fail per check) | Delivery | Assessment |

---

### 4. Review

Audit and verify — security, launch readiness, compliance. Covers: security review, launch readiness checklist, performance audit.

**Depth guidance:**
- Standard is the default — reviews should always be thorough.
- Light is discouraged (audits need completeness).

**Standard tabs:** Summary | Checklist | Findings | Remediation

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Review Scope | Hero + `.ref-note` (info) | — | Context | ✓ |
| Risk Assessment | `.score-table` (impact × likelihood) | Summary | Assessment | ✓ |
| Scorecard | `.scorecard` (A–F: security, perf, reliability) | Summary | Assessment | ✓ |
| Key Metrics | `.stats-grid` | Summary | Business | |
| Compliance Checklist | `.checklist` (pass/fail/warn per control) | Checklist | Assessment | ✓ |
| OWASP / Standard Mapping | `.ref-table` (control, status, evidence) | Checklist | Technical | |
| Findings by Severity | `.finding` (grouped by severity) | Findings | Assessment | ✓ |
| Code-Level Issues | `.finding` with `code` snippets | Findings | Technical | |
| Dependency Audit | `.ref-table` (package, version, CVE, status) | Findings | Technical | |
| Remediation Plan | `.timeline` (phased fixes) | Remediation | Action | ✓ |
| Quick Wins | `.steps-list` | Remediation | Action | |
| Long-Term Improvements | `.callout-box` or `.ref-note` | Remediation | Action | |

---

## Component Quick Reference

| Component | What it renders | Best for |
|-----------|----------------|----------|
| `.ref-table` | Data table with mono headers | Inventories, mappings, comparisons, any structured data |
| `.ref-note` | Coloured callout (warning/info/success/error) | Constraints, notes, important context |
| `.finding` | Severity-flagged item (icon + title + desc) | Audit findings, code quality issues, risks |
| `.stats-grid` + `.stat-box` | Grid of KPI boxes | Baseline metrics, coverage stats, summary numbers |
| `.cap-grid` + `.cap-card` | Feature/capability cards with icon | Feature lists, capability inventories |
| `.scorecard` | A–F graded cards | Tech debt scoring, maturity assessment |
| `.timeline` | Phased roadmap with dot markers | Delivery phases, migration plan, remediation plan |
| `.persona` | User card with avatar + details | Stakeholders, user personas |
| `.checklist` | Pass/fail/warn items | Compliance, readiness, scope in/out |
| `.journey-table` | Journey map table with emotions | Customer journeys, user flows |
| `.okr-block` | Objective + Key Results | Strategic goals, success framing |
| `.metric-hl` | Large highlighted metric | North Star metric, key target |
| `.score-table` | Scoring table with bars | RICE/ICE prioritization, risk scoring |
| `.story-card` | User story with Gherkin AC | Dev-ready stories, acceptance criteria |
| `.matrix-2x2` | 2×2 quadrant grid | Value-effort, power-interest, priority matrix |
| `details.collapsible` | Expandable section | ADRs, long code blocks, detailed notes |
| `.problem-box` | Left-bordered highlight box | Problem statements, vision statements, scope |
| `.pain-grid` + `.pain-card` | 2×2 card grid with severity borders | Pain points, gaps, feature comparison |
| `.scenario` | Icon + title + description row | Risks, opportunities, real-world situations |
| `.steps-list` | Numbered action items | Next steps, action plans, quick wins |
| `.callout-box` | Amber callout box | Assets, references, warnings, auxiliary notes |
| `.card-diagram` | SVG image container | Architecture, ERD, sequence, process diagrams |
| `.grid-2` / `.grid-3` | 2 or 3 column grid layout | Side-by-side comparisons, multi-column content |
| `.tag` + variant | Inline status badge | Status indicators in tables (`.tag-success`, `.tag-error`, `.tag-warning`, `.tag-info`, `.tag-neutral`, `.tag-primary`) |

### Security / Launch Review

**Suggested tabs:** Summary | Checklist | Findings | Remediation

| Section | Component | Tab |
|---------|-----------|-----|
| Review Scope | Hero + `.ref-note` | — |
| Compliance Checklist | `.checklist` (pass/fail/warn per control) | Checklist |
| Findings by Severity | `.finding` (grouped by severity) | Findings |
| Risk Assessment | `.score-table` (impact × likelihood) | Summary |
| Remediation Plan | `.timeline` (phased fixes) | Remediation |
| Scorecard | `.scorecard` (security, perf, reliability grades) | Summary |

---

### Design Brief (handoff to design skill)

**Suggested tabs:** Context | Constraints | Screens | Assets

| Section | Component | Tab |
|---------|-----------|-----|
| Objective | Hero (what we're designing and why) | — |
| Target Users | `.persona` cards | Context |
| User Flows | `.journey-table` or `.ref-table` | Context |
| Brand / Theme | `.ref-note` (which theme to apply) | Constraints |
| Accessibility Requirements | `.checklist` | Constraints |
| Screen Inventory | `.ref-table` (screen, purpose, priority) | Screens |
| Interaction Requirements | `.cap-grid` per screen | Screens |
| Reference Assets | `.ref-note` (links, screenshots, competitors) | Assets |
| Technical Constraints | `.ref-note` (warning — responsive, perf) | Constraints |
