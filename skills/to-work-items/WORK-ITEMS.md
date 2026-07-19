# Work Item Templates (Full Reference)

> Templates for all work item types. Use conventions from `CONVENTIONS.md` for formatting.

---

## Epic

```markdown
## Context
Business context, link to parent initiative or OKR.
Why this epic exists — the business driver.

## Description
What this epic delivers and why — value proposition and intended outcome.
No implementation details — that belongs in stories.

## Acceptance criteria
- Verifiable criteria that define "epic complete"
- Should be outcome-based, not task-based

## Out of scope
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]
```

---

## Story

```markdown
## Context
> As a [role], I want [feature], so that [benefit].

## Description
One high-level paragraph — outcome and value focused, no implementation steps.
Focus on WHAT and WHY, not HOW.

## Acceptance criteria
- Verifiable criteria that define "story complete"
- Should be outcome-based, not task-based

## How to test?
- What to test and expected outcomes (not step-by-step scripts)
- Include happy path and key edge cases

## Decisions
- Key decisions with rationale and alternatives considered

## Dependencies (optional)
- External dependencies only (not internal task dependencies)

## Risks/Impacts (optional)
- Potential risks with mitigation strategies

## Notes/Q&A (optional)
- Additional context, links to designs, related tickets
```

---

## Bug

```markdown
## Description
[What is broken — clear, factual, no opinion]

## Steps to reproduce
1. [Navigate to / Open / Start with state]
2. [Specific action with specific inputs]
3. [Next action]

## Actual result
[What actually happens — include error messages, screenshots]

## Expected result
[What should happen according to the acceptance criteria / design]

## Environment
- **Browser/Device**: [e.g., Chrome 125, iOS 18]
- **Environment**: [Dev / Staging / Production]
- **Version/Build**: [e.g., v2.4.1, commit abc123]
- **User role**: [If relevant]
- **Data conditions**: [If relevant]

## Severity & Priority
- **Severity**: Critical / Major / Minor / Cosmetic
- **Priority**: P0 / P1 / P2 / P3

## Frequency
- Always / Intermittent / Rare / Once

## Workaround
[If any workaround exists, describe it]

## Root Cause (if known)
[Technical root cause]

## Related
- [Related tickets, PRs, incidents]
```

### Severity Guide

| Severity | Definition | Example |
|---|---|---|
| **Critical** | System unusable, data loss, security breach | Cannot log in, payments fail, data exposed |
| **Major** | Key feature broken, no workaround | Cannot submit application, report shows wrong data |
| **Minor** | Feature partially broken, workaround exists | Filter doesn't work but search does |
| **Cosmetic** | Visual issue, no functional impact | Misaligned button, typo, wrong color |

---

## Task

```markdown
## Description
[What needs to be done — imperative, clear]

## Context
[Why this task is needed — link to parent story/epic if applicable]

## Acceptance Criteria
- [ ] [Verifiable criterion 1]
- [ ] [Verifiable criterion 2]

## Technical Notes (optional)
[Implementation hints, relevant files, API endpoints]
```

---

## Technical Spike

```markdown
## Question
[The specific question this spike answers — phrased as a question]

## Context
[Why we need to answer this — what decision depends on the result]

## Time Box
[Maximum time allowed — typically 1-3 days]

## Approach
- [Research area 1]
- [Research area 2]
- [Prototype or POC scope]

## Acceptance Criteria
- [ ] Question answered with evidence (not opinion)
- [ ] Trade-offs documented
- [ ] Recommendation made with rationale
- [ ] Findings shared with team

## Expected Output
- Summary document or ADR
- Prototype (if applicable — disposable, not production code)
- Decision recommendation
```

---

## RFC (Request for Comments)

For significant technical or process changes that need team input before deciding.

```markdown
## RFC-[N]: [Descriptive Title]

**Author:** [Name]
**Status:** Draft | Open for Comments | Accepted | Rejected | Withdrawn
**Created:** [Date]
**Comment Deadline:** [Date — typically 1-2 weeks]

### Summary
[1-2 paragraph overview of the proposal]

### Motivation
[Why is this change needed? What problem does it solve?]

### Proposal
[Detailed description of the proposed change]

### Alternatives Considered
| Option | Pros | Cons |
|--------|------|------|
| This proposal | ... | ... |
| Alternative A | ... | ... |
| Alternative B | ... | ... |
| Do nothing | ... | ... |

### Impact
- **Who is affected:** [Teams, systems, users]
- **Migration effort:** [None / Low / Medium / High]
- **Breaking changes:** [Yes/No — if yes, what and how to handle]

### Open Questions
1. [Question 1]
2. [Question 2]

### Timeline
[Proposed implementation timeline if accepted]

### Comments
[Team members add their feedback here]
```

---

## Design Doc

```markdown
## Context & Objectives

### Context
[Business and technical context — why this design doc exists]

### Goals
- [What this design achieves]

### Non-Goals
- [What this design explicitly does NOT address]

## Proposed Design

### Context Diagram
[High-level system context — what interacts with what]
→ Include PlantUML diagram or reference

### Sequence Diagram
[Key flow — request/response between components]
→ Include PlantUML diagram or reference

### Behaviour & Logic
[Business rules, state machines, decision logic]

### Data Schema & API Changes
[New/modified entities, endpoints, contracts]

### Decisions
| Decision | Options | Chosen | Rationale |
|----------|---------|--------|-----------|
| [What] | [A, B, C] | [B] | [Why B] |

## Evaluation & Risks

### Alternatives Considered
[What else was considered and why it was rejected]

### Known Issues & Constraints
[Limitations of this design, accepted trade-offs]

### Future Plan
[What comes next, what's deferred]

## Appendix
- Meeting notes
- Q&A from review sessions
- Reference links
```

---

## Sub-Task

```markdown
## Description
[Specific technical task — part of a parent story]

## Parent
[Link to parent story]

## Acceptance Criteria
- [ ] [Specific, verifiable criterion]

## Notes
[Technical details, file paths, API references]
```

---

## Initiative / Theme

For grouping epics under a strategic theme (used in roadmaps).

```markdown
## Initiative: [Name]

### Strategic Alignment
- OKR: [Which OKR does this support?]
- North Star Impact: [How does this move the North Star metric?]

### Description
[What this initiative is about — 2-3 sentences]

### Epics
| Epic | Status | Target Quarter |
|------|--------|----------------|
| [Epic 1] | Discovery | Q3 |
| [Epic 2] | Ready | Q3 |
| [Epic 3] | Not started | Q4 |

### Success Metrics
| Metric | Baseline | Target |
|--------|----------|--------|
| [Metric] | [Current] | [Goal] |

### Risks
- [Key risks at the initiative level]
```
