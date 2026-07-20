## Section & Component Library

> Reference for rendering `DOCUMENT-TEMPLATE.html`.
> Maps use cases → dimensions → tab structure → CSS components.
> product-analyze skill renders its own HTML output — no dev skill dependency.
> Every outcome ALWAYS includes all 6 dimension tabs. Populate each with evidence; use a brief "No findings" note only when genuinely empty.

---

## 6-Dimension Framework

Every document covers a topic through **6 mandatory dimensions** (tabs). This ensures consistent coverage from problem context through actionable delivery.

| Dimension | Tab Label | What it covers | Typical components |
|-----------|-----------|---------------|-------------------|
| **Context** | Context | Problem/vision, scope, stakeholders, personas, baseline | Hero, `.persona`, `.problem-box`, `.ref-note`, `.stats-grid` |
| **Business** | Business | Impact, journeys, metrics, cost-benefit, process flows, stakeholder mapping | `.journey-table`, `.okr-block`, `.metric-hl`, `.stats-grid`, `.score-table`, `.matrix-2x2` |
| **Functional** | Functional | User flows, functional requirements, use cases, screen inventory, mock-UI/prototypes, acceptance criteria | `.journey-table`, `.story-card`, `.cap-grid`, `.checklist`, `.mock-ui`, `.card-diagram` |
| **Technical** | Technical | Architecture, data model, integrations, APIs, deployment, configuration | `.card-diagram`, `.ref-table`, `.cap-grid`, `details.collapsible` |
| **Assessment** | Assessment | Findings, scorecard, risks, dependencies, compliance, quality | `.finding`, `.scorecard`, `.checklist`, `.ref-note`, `.pain-grid` |
| **Action** | Action | Roadmap, decisions, next steps, delivery phases, migration plan | `.timeline`, `.steps-list`, `.story-card`, `.score-table` |

### Mandatory Tab Order

All outcomes use exactly these 6 tabs in this order:

```html
<nav class="tabs">
  <button class="tab active" data-tab="context">Context <span class="badge">…</span></button>
  <button class="tab" data-tab="business">Business <span class="badge">…</span></button>
  <button class="tab" data-tab="functional">Functional <span class="badge">…</span></button>
  <button class="tab" data-tab="technical">Technical <span class="badge">…</span></button>
  <button class="tab" data-tab="assessment">Assessment <span class="badge">…</span></button>
  <button class="tab" data-tab="action">Action <span class="badge">…</span></button>
</nav>
```

---

## Rendering Rules

product-analyze renders HTML directly using `DOCUMENT-TEMPLATE.html`:

1. Determine use case type (Analysis, Proposal, Plan, Review)
2. Determine depth (Light / Standard / Deep)
3. Load theme from `~/.agents/themes/` or `~/.claude/themes/` → apply via `DESIGN-UI.md`
4. Populate all 6 tabs with appropriate sections per use case
5. Include mock-UI/prototype in **Functional** tab when the topic involves UI or user interactions
6. Save as `YYYYMMDD-<type>-<topic>.html`

**Linear mode** (Light depth only): Omit `<nav class="tabs">` and `<section class="panel">` wrappers. Cards stack directly inside `<main class="wrap">` but still group by all 6 dimensions using `<h2>` headings.

---

## Mock-UI / Prototype Component

Embed interactive HTML prototypes directly in the **Functional** tab. Use for any topic that involves user-facing screens or interactions.

### Pattern

```html
<div class="card">
  <div class="card-header"><span>Mock-UI: [Screen Name]</span></div>
  <div class="card-content">
    <div class="mock-ui" style="border: 1px solid var(--border); border-radius: 8px; overflow: hidden;">
      <!-- Self-contained HTML/CSS prototype -->
      <!-- Use inline styles or scoped <style> to avoid conflicts with document styles -->
      <!-- Keep it functional: buttons, inputs, tabs, modals — styled to match the target design -->
    </div>
  </div>
</div>
```

### Mock-UI Rules
- Self-contained (no external dependencies beyond icon CDN already loaded)
- Scoped styles (use `.mock-ui` prefix or inline styles to avoid leaking)
- Interactive where useful (tabs, dropdowns, hover states via inline JS)
- Realistic data (use plausible sample data, not "lorem ipsum")
- Annotated (add `.ref-note` below the mock explaining key interactions)

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
- Light → Quick audit summary (linear). Minimal Functional/Business content.
- Standard → Full analysis with all 6 dimensions (tabbed).
- Deep → Gap analysis with current vs target state comparison (tabbed).

**Tabs:** Context | Business | Functional | Technical | Assessment | Action

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Problem Statement / Scope | Hero `{{HEADING}}` + `{{DESCRIPTION}}` | — | Context | ✓ |
| Baseline Metrics | `.stats-grid` / `.metric-hl` | Context | Context | |
| Personas | `.persona` cards | Context | Context | |
| User Flows (current) | `.journey-table` or `.card-diagram` | Business | Business | |
| Process Map (AS-IS) | `.card-diagram` (BPMN SVG) | Business | Business | |
| Stakeholder Map | `.matrix-2x2` (power × interest) or `.ref-table` | Business | Business | |
| Cost / Effort Baseline | `.stats-grid` or `.ref-table` | Business | Business | |
| Current User Journeys | `.journey-table` | Functional | Functional | |
| Screen Inventory (current) | `.ref-table` (screen, route, purpose, status) | Functional | Functional | |
| Functional Gaps | `.pain-grid` or `.checklist` | Functional | Functional | ✓ |
| Mock-UI (target state) | `.mock-ui` embedded prototype | Functional | Functional | |
| Current Architecture | `.card-diagram` (context diagram SVG) | Technical | Technical | ✓ |
| Component Inventory | `.ref-table` (component, tech, status, owner) | Technical | Technical | ✓ |
| Integration Points | `.ref-table` (system, direction, protocol, status) | Technical | Technical | |
| Data Model | `.card-diagram` (ERD SVG) | Technical | Technical | |
| Tech Debt Scorecard | `.scorecard` (A–F per dimension) | Assessment | Assessment | ✓ |
| Audit Findings | `.finding` (severity-flagged issues) | Assessment | Assessment | ✓ |
| Pain Points / Gaps | `.pain-grid` with `.critical` / `.warning` | Assessment | Assessment | |
| Compliance Checklist | `.checklist` (pass/fail/warn per control) | Assessment | Assessment | |
| Risks & Dependencies | `.scenario` or `.finding` | Assessment | Assessment | |
| Recommendations | `.steps-list` or `.timeline` | Action | Action | ✓ |
| ADRs / Decisions | `details.collapsible` (ADR format) | Action | Action | |
| Delivery Phases | `.timeline` | Action | Action | |

**Deep mode additions (gap analysis):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Target State Vision | `.problem-box` or Hero watermark "TO-BE" | Context | Context |
| Gap Summary | `.pain-grid` or `.ref-table` (current vs target) | Assessment | Assessment |
| Target Architecture | `.card-diagram` (target context diagram) | Technical | Technical |
| Target Mock-UI | `.mock-ui` prototype of desired state | Functional | Functional |
| Value-Effort Matrix | `.matrix-2x2` | Assessment | Assessment |
| Bridging Actions | `.timeline` (phased migration) | Action | Action |

---

### 2. Proposal

Propose something new — from problem validation to full PRD. Covers: discovery, feature proposal, concept pitch, to-be proposal, PRD, design brief.

**Depth guidance:**
- Light → Concept pitch or discovery one-pager (linear). Focus on Context + Action.
- Standard → Feature proposal or PRD (tabbed).
- Deep → Full to-be proposal with target architecture and ADRs (tabbed).

**Tabs:** Context | Business | Functional | Technical | Assessment | Action

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Problem Statement | Hero `{{HEADING}}` + `.problem-box` | — | Context | ✓ |
| Personas | `.persona` cards | Context | Context | ✓ |
| Pain Points | `.pain-grid` with `.critical` / `.warning` | Context | Context | |
| Scope (in/out) | `.checklist` (pass = in, fail = out) | Context | Context | |
| OKRs / Objectives | `.okr-block` | Business | Business | |
| Success Metrics | `.metric-hl` (North Star) + `.stats-grid` | Business | Business | ✓ |
| Business Case | `.ref-note` (info callout) or `.callout-box` | Business | Business | |
| Competitive Landscape | `.ref-table` or `.matrix-2x2` | Business | Business | |
| User Journeys | `.journey-table` | Business | Business | |
| User Flows (proposed) | `.journey-table` or `.card-diagram` | Functional | Functional | ✓ |
| Feature Capabilities | `.cap-grid` / `.cap-card` | Functional | Functional | ✓ |
| Screen Inventory | `.ref-table` (screen, route, purpose, priority) | Functional | Functional | |
| Mock-UI / Prototype | `.mock-ui` embedded prototype | Functional | Functional | |
| Acceptance Criteria | `.story-card` or `.checklist` | Functional | Functional | |
| Real-World Scenarios | `.scenario` with `.red` / `.amber` / `.blue` | Functional | Functional | |
| Target Architecture | `.card-diagram` (SVG) | Technical | Technical | |
| API Changes | `.ref-table` (endpoint, method, purpose) | Technical | Technical | |
| Data Model | `.card-diagram` or `.ref-table` | Technical | Technical | |
| ADRs / Decisions | `details.collapsible` (ADR format) | Technical | Technical | |
| Risks & Dependencies | `.finding` or `.scenario` | Assessment | Assessment | ✓ |
| Key Assumptions | `.ref-table` with `.tag` severity | Assessment | Assessment | |
| Constraints | `.ref-note` (warning callout) | Assessment | Assessment | |
| Prioritization | `.score-table` (RICE/ICE) | Assessment | Assessment | |
| Value-Effort Matrix | `.matrix-2x2` | Assessment | Assessment | |
| Release Strategy | `.timeline` (phased plan) | Action | Action | ✓ |
| Next Steps | `.steps-list` | Action | Action | |

**Deep mode additions (to-be proposal):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Gap Summary | `.pain-grid` or `.ref-table` (current vs target) | Assessment | Assessment |
| Migration Phases | `.timeline` (phased plan) | Action | Action |
| Strangler Pattern / Boundary | `.card-diagram` | Technical | Technical |
| Success Metrics (target) | `.stats-grid` + `.metric-hl` | Business | Business |
| Full Mock-UI Suite | Multiple `.mock-ui` per screen | Functional | Functional |

---

### 3. Plan

Detail execution — from sprint brief to full migration plan. Covers: implementation plan, data migration plan, API/integration spec, sprint goal brief, implementation handoff.

**Depth guidance:**
- Light → Sprint brief or implementation handoff (linear). Focus on Context + Action.
- Standard → Implementation plan (tabbed).
- Deep → Full migration plan with rollback strategy and detailed specs (tabbed).

**Tabs:** Context | Business | Functional | Technical | Assessment | Action

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Scope & Objectives | Hero + `.problem-box` or `.ref-note` (info) | — | Context | ✓ |
| Personas | `.persona` cards | Context | Context | |
| Success Metrics | `.stats-grid` or `.metric-hl` | Business | Business | |
| Cost-Benefit Summary | `.ref-table` or `.callout-box` | Business | Business | |
| User Stories | `.story-card` (with Gherkin AC) | Functional | Functional | |
| Acceptance Criteria | `.ref-table` or `.checklist` | Functional | Functional | |
| Screen Inventory | `.ref-table` (screen, route, purpose, priority) | Functional | Functional | |
| Mock-UI / Wireframes | `.mock-ui` embedded prototype | Functional | Functional | |
| Architecture Diagram | `.card-diagram` (SVG) | Technical | Technical | ✓ |
| Component Map | `.ref-table` (component, status, description) | Technical | Technical | ✓ |
| API Changes / Endpoints | `.ref-table` (endpoint, method, purpose, auth) | Technical | Technical | |
| Data Model Changes | `.card-diagram` or `.ref-table` | Technical | Technical | |
| Sequence Diagrams | `.card-diagram` per flow | Technical | Technical | |
| ADRs / Decisions | `details.collapsible` (ADR format) | Technical | Technical | |
| Test Strategy | `.ref-table` or `.checklist` | Assessment | Assessment | |
| Dependencies | `.ref-note` (warning callout) or `.scenario` | Assessment | Assessment | ✓ |
| Constraints & Risks | `.finding` (severity-flagged) | Assessment | Assessment | |
| Rollback Strategy | `.callout-box` or `.ref-note` | Assessment | Assessment | |
| Delivery Phases | `.timeline` | Action | Action | ✓ |
| Next Steps | `.steps-list` | Action | Action | |

**Deep mode additions (migration / integration spec):**

| Section | Component | Tab | Dimension |
|---------|-----------|-----|-----------|
| Source → Target Mapping | `.ref-table` (source field, target field, transform) | Technical | Technical |
| Data Validation Rules | `.checklist` or `.ref-table` | Assessment | Assessment |
| Error Handling Strategy | `.ref-table` (error, response, retry) | Technical | Technical |
| Auth / Security Model | `.ref-table` or `.cap-grid` | Technical | Technical |
| Performance Targets | `.stats-grid` or `.metric-hl` | Business | Business |
| Reconciliation / Verification | `.checklist` (pass/fail per check) | Assessment | Assessment |

---

### 4. Review

Audit and verify — security, launch readiness, compliance. Covers: security review, launch readiness checklist, performance audit.

**Depth guidance:**
- Standard is the default — reviews should always be thorough.
- Light is discouraged (audits need completeness).

**Tabs:** Context | Business | Functional | Technical | Assessment | Action

| Section | Component | Tab | Dimension | Required |
|---------|-----------|-----|-----------|----------|
| Review Scope | Hero + `.ref-note` (info) | — | Context | ✓ |
| Key Metrics | `.stats-grid` | Business | Business | |
| User Impact | `.scenario` or `.pain-grid` | Functional | Functional | |
| Affected User Flows | `.journey-table` or `.checklist` | Functional | Functional | |
| OWASP / Standard Mapping | `.ref-table` (control, status, evidence) | Technical | Technical | |
| Code-Level Issues | `.finding` with `code` snippets | Technical | Technical | |
| Dependency Audit | `.ref-table` (package, version, CVE, status) | Technical | Technical | |
| Risk Assessment | `.score-table` (impact × likelihood) | Assessment | Assessment | ✓ |
| Scorecard | `.scorecard` (A–F: security, perf, reliability) | Assessment | Assessment | ✓ |
| Compliance Checklist | `.checklist` (pass/fail/warn per control) | Assessment | Assessment | ✓ |
| Findings by Severity | `.finding` (grouped by severity) | Assessment | Assessment | ✓ |
| Remediation Plan | `.timeline` (phased fixes) | Action | Action | ✓ |
| Quick Wins | `.steps-list` | Action | Action | |
| Long-Term Improvements | `.callout-box` or `.ref-note` | Action | Action | |

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
| `.mock-ui` | Embedded HTML prototype container | Interactive wireframes, screen mockups, UI prototypes |

### Design Brief (handoff to design skill)

When the outcome is a design brief for the design skill, still use the 6-tab structure but focus content on Context (objective, users, brand) and Functional (screens, interactions, mock-UI).
