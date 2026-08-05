# Outcome Rules

## Document Rendering

### Process
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Assemble the document dynamically using the snippets and base HTML shell provided in `DOCUMENT-TEMPLATE.md`.
3. Use the fallback inline CSS provided in the shell if custom themes are missing or inaccessible.
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow the flexible component guidelines in `DOCUMENT-TEMPLATE.md` to map data to appropriate UI components dynamically.
6. Include high-fidelity, interactive throwaway prototypes in the **Functional** tab using **HTML/CSS/Tailwind** when the topic involves user-facing screens. Also generate Mermaid/PlantUML diagrams for SA architectural decisions.
7. Save as `YYYYMMDD-<type>-<topic>.html`

### Final Review Gate
After the **[Business Analyst]** drafts the outcomes, the **[Product Owner]** and **[Solution Architect]** MUST conduct a rigorous review before finalization:
- **Completeness**: Are all edge cases, rules, and NFRs covered?
- **Conciseness**: Is the document free of bloat and unnecessary complexity?
- **Comprehensiveness**: Does this artifact fully solve the validated problem from the Analysis phase?
*The documents or tickets cannot be considered final until they pass this gate.*

## JIRA Conventions

### Jira Refinement Safety Protocol
Preview all proposed tickets in Markdown for user approval before making external API calls.

### Title Patterns
* Epic: `[Capability noun phrase]`
* Story: `[Action verb] [what] [context]`
* Bug: `[Component] - [Symptom]`
* Task: `[Imperative action]`
* Sub-task: `[Verb] [specific action]` (Always include "Update changelog")

*Rules:* Max 80 chars. Omit ticket IDs. Start with capital letter. Omit trailing periods.

### Text Formatting
Use only Atlassian Document Format (ADF) rendered via Markdown.
* Use standard markdown for bold, italic, code blocks, lists.
* Semantic Styling: Use **bold** for entities/components, ***bold+italic*** for APIs/topics, `code` for fields/variables.
* Links: Use full browse URLs (e.g., `[PROJ-123](https://[instance].atlassian.net/browse/PROJ-123)`).

## Work Item Templates

### Epic Template
```markdown
## Context
Business context, link to parent initiative or OKR.

## Description
Describe only value proposition and outcomes.

## Acceptance criteria
* Verifiable criteria that define "epic complete". Outcome-based.

## Out of scope
* Explicitly excluded items.
```

### Story Template
```markdown
## Context
> As a [role], I want [feature], so that [benefit].

Why this story is needed, what problem it solves, and how it fits into the larger epic or initiative. Include any relevant background information, con`straints, or dependencies.

## Description
Describe only value proposition and outcomes in one paragraph.

## Acceptance criteria
* Verifiable criteria that define "story complete". Outcome-based.

### Functional specifications (optional, add if the story needs logic or rules)
* Functional design, logic, and rules that must be followed to meet the acceptance criteria.

### Technical specifications (optional, add if the story is too technical)
* Technical design, architecture, and implementation details that must be followed to meet the acceptance criteria.

### Non-functional requirements (optional, add if needed)
* Performance, security, reliability, maintainability, usability, etc.

## Out of scope
* Explicitly excluded items.

## How to test?
* What to test and expected outcomes (happy path and edge cases)

## Assumptions (optional, add if needed)
* Assumptions made during analysis and design.

## Decisions (optional, add if needed)
* Key decisions with rationale

## Dependencies (optional, add if needed)
* External dependencies and potential risks

## Risks / Impacts (optional, add if needed)
* Potential risks and impacts on other systems or teams

## Notes / Q&A (optional, add if needed)
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

## Domain model (Bounded Contexts, Aggregates) / Component diagram(s)

## Technical changes
|Components|Changes|JIRA Tickets|
|---|---|---|
|	|	|	|

## Known risks and mitigations

```
