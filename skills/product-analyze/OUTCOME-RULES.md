# Outcome Rules (Full Reference)

This document contains all rules for synthesizing Analysis into concrete Deliverables (Documents, Architecture Decisions, and Jira Work Items).

---

## 1. Document Rendering (Self-Contained)

This skill renders its own HTML output — no dev skill dependency.

**Process:**
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Load `templates/DOCUMENT-TEMPLATE.html` as base
3. Apply theme via `templates/DESIGN-UI.md` (load theme from `~/.agents/themes/` or `~/.claude/themes/`)
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow `templates/SECTION-LIBRARY.md` for section → component mapping
6. Include mock-UI prototypes in **Functional** tab when topic involves user-facing screens
7. Save as `YYYYMMDD-<type>-<topic>.html`

---

## 2. JIRA Refinement Safety Protocol

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

### Refinement Workflow State Machine

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

---

## 3. JIRA Conventions

### Title Patterns
- Epic: `[Capability noun phrase]`
- Story: `[Action verb] [what] [context]`
- Bug: `[Component] - [Symptom]`
- Task: `[Imperative action]`
- Spike: `Spike: [Question to answer]`
- Sub-task: `[Verb] [specific action]` (Always include "Update changelog")

*Rules:* Max 80 chars. No ticket IDs. Start with capital letter. No trailing period.

### Text Formatting & ADF
JIRA Cloud uses Atlassian Document Format (ADF) rendered via Markdown. Wiki markup is NOT supported.
- Use standard markdown for bold, italic, code blocks, lists.
- Semantic Styling: Use **bold** for entities/components, ***bold+italic*** for APIs/topics, `code` for fields/variables.
- Links: Use full browse URLs (e.g., `[PROJ-123](https://[instance].atlassian.net/browse/PROJ-123)`).

### Estimation (Fibonacci & T-Shirt)
- **1-3 pts** (XS/S): Minor changes, <= 1 day.
- **5-8 pts** (M/L): Medium to Large, 2-5 days.
- **13+ pts** (XL): Too large, must be split.

---

## 4. Work Item Templates

### Epic Template
```markdown
## Context
Business context, link to parent initiative or OKR.

## Description
What this epic delivers and why (value proposition). No implementation details.

## Acceptance criteria
Verifiable criteria that define "epic complete". Outcome-based.

## Out of scope
Explicitly excluded items.
```

### Story Template
```markdown
## Context
> As a [role], I want [feature], so that [benefit].

## Description
One high-level paragraph — outcome and value focused. What and Why, not How.

## Acceptance criteria
- Verifiable criteria (Given/When/Then)

## How to test?
- What to test and expected outcomes (happy path and edge cases)

## Decisions
- Key decisions with rationale

## Dependencies & Risks (optional)
- External dependencies and potential risks
```

### Bug Template
```markdown
## Description
[Factual description of what is broken]

## Steps to reproduce
1. [Step 1]
2. [Step 2]

## Actual result vs Expected result
[What happens] vs [What should happen]

## Environment & Severity
- Browser/OS/Version
- Severity (Critical/Major/Minor/Cosmetic)
```

### Spike / RFC / Design Doc
- **Spike**: Define Question, Context, Time Box (1-3 days), Approach, and Expected Output.
- **RFC**: Define Motivation, Proposal, Alternatives, Impact, and Open Questions.
- **Design Doc**: Define Goals/Non-Goals, Proposed Design (Context/Sequence diagrams), Data Schema, and Known Risks.
