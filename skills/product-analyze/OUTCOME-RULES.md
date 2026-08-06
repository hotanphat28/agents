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
* Initiative: `[Capability noun phrase]`
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

### Initiative Template
```markdown
## Context
Strategic theme or OKR this initiative rolls up to, and why it matters now.

## Business value
The problem or opportunity, and the expected business outcome.

## Scope & requirements
High-level capabilities or epics this initiative covers.

## Acceptance criteria
* Verifiable criteria that define "initiative complete". Outcome-based.

## Out of scope
* Explicitly excluded items.

## Success metrics
* Measurable indicators (e.g. North Star Metric, OKR key results) used to judge success.

## Timeline
Target start/end or milestone dates, and key dependencies.
```

### Epic Template
```markdown
## Context
Why this epic is needed, what problem it solves, and how it fits into the larger initiative. Include any relevant background information, constraints, or dependencies.

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

Why this story is needed, what problem it solves, and how it fits into the larger epic. Include any relevant background information, constraints, or dependencies.

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
* What to test and expected outcomes (happy path and edge cases). Should be clear, measurable, and testable. Should be step-by-step instructions for QA or developers to verify the story is complete and meets the acceptance criteria.

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
Log of decisions made during design, with links to supporting discussions or tickets. Accordion-style collapsible sections are preferred for each decision, with a summary line and a "Details" section for the rationale, alternatives considered, and any supporting diagrams or links.

## Meeting notes
List of all meettings, workshops, or design reviews that contributed to the design doc. Include date, attendees, and a link to the meeting notes or recording. Accordion-style collapsible sections are preferred for each meeting, with a summary line and a "Details" section for the notes or recording link.

## Q&A
List of Q&A sessions or discussions that contributed to the design doc. Include date, attendees, and a link to the Q&A notes or recording. Accordion-style collapsible sections are preferred for each Q&A, with a summary line and a "Details" section for the notes or recording link.

## Context and scope
Why and what this design doc is needed, what problem it solves, and how it fits into the larger initiative. Include any relevant background information, constraints, or dependencies.

### In scope (Acceptance criteria)
* Explicitly included items, with rationale for why they are in scope. Include acceptance criteria that are clear, measurable, and testable.

### Out of scope
* Explicitly excluded items, with rationale for why they are out of scope.

## Customer journey

### Happy flow
Step by step description of the happy flow, including any relevant screenshots, mockups, or diagrams. Include expected behavior and any known workarounds.

### Edge cases
Step by step description of the edge case, including any relevant screenshots, mockups, or diagrams. Include expected behavior and any known workarounds.

## Workflow diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## System context diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Sequence diagram(s)
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Domain model (Bounded Contexts, Aggregates) / Component diagram(s)
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Technical changes
| Components | Changes | JIRA Tickets |
|---|---|---|
|  |  |  |

## Known risks and mitigations
List of known risks and mitigations, with rationale for why they are risks and how they will be mitigated. Include any relevant screenshots, mockups, or diagrams. Accordion-style collapsible sections are preferred for each risk, with a summary line and a "Details" section for the mitigation plan and any supporting diagrams or links.
```
