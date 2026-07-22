# Outcome Rules
This document contains all rules for synthesizing Analysis into concrete Deliverables (Documents, Architecture Decisions, and Jira Work Items).

## Document Rendering
This skill renders its own HTML output — no dev skill dependency.

### Process
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Load `templates/DOCUMENT-TEMPLATE.html` as base
3. Apply theme via `templates/DESIGN-UI.md` (load theme from `~/.agents/themes/` or `~/.claude/themes/`)
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow `templates/SECTION-LIBRARY.md` for section → component mapping
6. Include mock-UI prototypes in **Functional** tab when topic involves user-facing screens
7. Save as `YYYYMMDD-<type>-<topic>.html`

## JIRA Conventions

### Title Patterns
* Epic: `[Capability noun phrase]`
* Story: `[Action verb] [what] [context]`
* Bug: `[Component] - [Symptom]`
* Task: `[Imperative action]`
* Sub-task: `[Verb] [specific action]` (Always include "Update changelog")

*Rules:* Max 80 chars. No ticket IDs. Start with capital letter. No trailing period.

### Text Formatting
JIRA Cloud uses Atlassian Document Format (ADF) rendered via Markdown. Wiki markup is NOT supported.
* Use standard markdown for bold, italic, code blocks, lists.
* Semantic Styling: Use **bold** for entities/components, ***bold+italic*** for APIs/topics, `code` for fields/variables.
* Links: Use full browse URLs (e.g., `[PROJ-123](https://[instance].atlassian.net/browse/PROJ-123)`).

## Work Item Templates

### Epic Template
```markdown
## Context
Business context, link to parent initiative or OKR.

## Description
What this epic delivers and why (value proposition). No implementation details.

## Acceptance criteria
* Verifiable criteria that define "epic complete". Outcome-based.

## Out of scope
* Explicitly excluded items.
```

### Story Template
```markdown
## Context
> As a [role], I want [feature], so that [benefit].

## Description
One high-level paragraph — outcome and value focused. What and Why, not How.

## Acceptance criteria
* Verifiable criteria that define "story complete". Outcome-based.

### Business rules
* Business rules and constraints that apply to this story.

### Non-functional requirements
* Performance, security, reliability, maintainability, usability, etc.

## How to test?
* What to test and expected outcomes (happy path and edge cases)

## Assumptions (optional)
* Assumptions made during analysis and design.

## Decisions (optional)
* Key decisions with rationale

## Dependencies (optional)
* External dependencies and potential risks

## Risks / Impacts (optional)
* Potential risks and impacts on other systems or teams

## Notes / Q&A (optional)
* Additional notes and questions & answers.
```

Consider checking content of a Story based on INVEST principles:
* **Independent**: Can be developed and delivered independently of other stories.
* **Negotiable**: Not a contract; can be changed or rewritten.
* **Valuable**: Delivers value to the end user or customer.
* **Estimable**: Can be estimated for size and complexity.
* **Small**: Small enough to be completed in a single iteration.
* **Testable**: Acceptance criteria can be verified through tests or demonstrations.

Best practices for writing a Story:
* Keep it short, simple and focused on a single outcome.
* Focus on user value and business impact, not technical implementation.
* One story should not cover multiple features or requirements.
* Always include acceptance criteria that are clear, measurable and testable.
* Collaborate with stakeholders to ensure the story meets their needs and expectations.
* If it is a technical story, include context and rationale for the technical decision.

### Bug Template
```markdown
## Description
Factual description of what is broken

## Steps to reproduce
1. Step 1
2. Step 2

## Actual result vs Expected result
[What happens] vs [What should happen]

## Environment & Severity
* Browser/OS/Version
* Severity (Critical/Major/Minor/Cosmetic)
```

### Design Doc Template
```markdown
## Decisions log

## Meeting notes

## Notes / Q&A

## Context and scope

### In scope - Acceptance criteria

### Out of scope

## Customer journey

### Happy flow

### Edge cases

## Workflow

## System content diagram

## Sequence diagram(s)

## Domain model / Component diagram(s)

## Technical changes
|Components|Changes|JIRA Tickets|
|---|---|---|
|	|	|	|

## Known risks and mitigations

```
