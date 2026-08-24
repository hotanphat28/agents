# Outcome Rules

## Document Rendering

### Process
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Assemble the document dynamically using the snippets and base HTML shell provided in `DOCUMENT-TEMPLATE.md`.
3. Use the fallback inline CSS provided in the shell if custom themes are missing or inaccessible.
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow the flexible component guidelines in `DOCUMENT-TEMPLATE.md` to map data to appropriate UI components dynamically.
6. For user-facing screens, do NOT build the prototype here — write a **Prototype Handoff Brief** in the **Functional** tab (per screen: purpose, states, interactions/JS behavior, inputs & validation, data shape, edge cases) and hand off to **product-develop** to build the interactive throwaway prototype. Also generate Mermaid/PlantUML diagrams for SA architectural decisions.
7. Save as `YYYYMMDD-<type>-<topic>.html`

### Final Review Gate
After the **[Business Analyst]** drafts the outcomes, the **[Product Owner]** and **[Solution Architect]** MUST conduct a rigorous review before finalization:
- **Completeness**: Are all edge cases, rules, and NFRs covered?
- **Conciseness**: Is the document free of bloat and unnecessary complexity?
- **Comprehensiveness**: Does this artifact fully solve the validated problem from the Analysis phase?
*The documents or tickets cannot be considered final until they pass this gate.*

### Prototype Alignment Gate
When a Prototype Handoff Brief exists, it cannot be handed to **product-develop** until the **[Business Analyst]** has surfaced every open question, ambiguity, or conflicting requirement about the screens/interactions directly to the user and the user has explicitly confirmed alignment. Never build or hand off on assumptions.

## JIRA Conventions

### Jira Refinement Safety Protocol
Preview all proposed tickets in Markdown for user approval before making external API calls.

### Title Patterns
* Initiative: `[Capability noun phrase]`
* Epic: `[Capability noun phrase]`
* Story: `[Action verb] [what] [context]`
* Bug: `[Component] - [Symptom]`

*Rules:* Limit titles to 80 characters. Keep titles free of ticket IDs and trailing periods. Begin titles with a capital letter.

### Text Formatting
Use only Atlassian Document Format (ADF) rendered via Markdown.
* Use standard markdown for bold, italic, code blocks, lists, blockquotes, tables.
* Semantic Styling: Use **bold** for entities/components, **_bold+italic_** for APIs/topics, `code` for fields/variables, and ```code blocks``` for code snippets.
* Links: Use full browse URLs (e.g., `[PROJ-123](https://[instance].atlassian.net/browse/PROJ-123)`).

## Work Item Templates

### Initiative Template
```markdown
## Context
Strategic theme or OKR this initiative rolls up to, and why it matters now in one or two paragraphs.

## Business value
The problem or opportunity, and the expected business outcome in list one-liner format.

## Scope & requirements
High-level capabilities or epics this initiative covers in list one-liner format.

## Acceptance criteria
Verifiable criteria that define "initiative complete". Outcome-based. In list one-liner format.

## Out of scope
Explicitly excluded items. In list one-liner format.

## Success metrics
Measurable indicators (e.g. North Star Metric, OKR key results) used to judge success in list one-liner format.

## Timeline
Target start/end or milestone dates, and key dependencies.
```

### Epic Template
```markdown
## Context
Why this epic is needed, what problem it solves, and how it fits into the larger initiative. Include any relevant background information, constraints, or dependencies. One or two paragraphs.

## Description
Describe only value proposition and outcomes.

## Acceptance criteria
Verifiable criteria that define "epic complete". Outcome-based. In list one-liner format.

## Out of scope
Explicitly excluded items. In list one-liner format.
```

### Story Template
```markdown
## Context
> As a [role], I want [feature], so that [benefit].

Why this story is needed, what problem it solves, and how it fits into the larger epic. Include any relevant background information, constraints, or dependencies. One or two paragraphs.

## Description
Describe only value proposition and outcomes in one paragraph.

## Acceptance criteria
Verifiable criteria that define "story complete". Outcome-based. In list one-liner format.

### Functional specifications (optional, add if the story needs logic or rules)
* Functional design, logic, and rules that must be followed to meet the acceptance criteria.

### Technical specifications (optional, add if the story is too technical)
* Technical design, architecture, and implementation details that must be followed to meet the acceptance criteria.

### Non-functional requirements (optional, add if needed)
* Performance, security, reliability, maintainability, usability, etc.

## Out of scope
Explicitly excluded items. In list one-liner format.

## How to test?
What to test and expected outcomes (happy path and edge cases). Should be clear, measurable, and testable. Should be step-by-step instructions for QA or developers to verify the story is complete and meets the acceptance criteria.

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

Apply INVEST principles when drafting a Story:
* **Independent**: Ensure the story can be developed and delivered without waiting on other stories.
* **Negotiable**: Frame requirements as goals to be solved rather than strict contracts.
* **Valuable**: Explicitly state the value delivered to the end user or customer.
* **Estimable**: Provide enough clarity for the team to estimate size and complexity.
* **Small**: Keep the scope small enough to complete in a single iteration.
* **Testable**: Write acceptance criteria that can be explicitly verified through tests or demonstrations.

Best practices for writing a Story:
* Keep it short, simple and focused on a single outcome.
* Focus on user value and business impact, not technical implementation.
* One story should not cover multiple features or requirements.
* Always include acceptance criteria that are clear, measurable and testable.
* Collaborate with stakeholders to ensure the story meets their needs and expectations.
* If it is a technical story, include context and rationale for the technical decision.

Always create the following sub-tasks to a Story (ensure checking for existing to avoid duplication)
* Create test cases
* Execute test cases
* Create or update UnitTests
* Review
* Merge
* Demo

### Bug Template
```markdown
## Description
Factual description of what is broken

## Steps to reproduce
1. Step 1
2. Step 2

## Actual result
What happens

## Expected result
What should happen

## Environment & Severity
* Browser/OS/Version
* Severity (Critical/Major/Minor/Cosmetic)
```

### Design Doc Template
```markdown
## Decisions log
| Date | Who joined? | Decision(s) | JIRA ticket(s) |
|---|---|---|---|
|	|   |   |   |

## Meeting notes
List of meeting notes which can expand or collapse. Include date, attendees, and a link to the notes or recording. Accordion-style collapsible sections are preferred for each meeting, with a summary line and a "Details" section for the notes or recording link.

YYYY-MM-DD: [Meeting title] - [Attendees]

## Q&A
List of Q&A sessions or discussions that contributed to the design doc. Include date, attendees, and a link to the Q&A notes or recording. Accordion-style collapsible sections are preferred for each Q&A, with a summary line and a "Details" section for the notes or recording link.

## Context and scope
Why and what this design doc is needed, what problem it solves, and how it fits into the larger initiative. Include any relevant background information, constraints, or dependencies.

### In scope (Acceptance criteria)
Explicitly included items, with rationale for why they are in scope. Include acceptance criteria that are clear, measurable, and testable. In list one-liner format.

### Out of scope
Explicitly excluded items, with rationale for why they are out of scope. In list one-liner format.

## Customer journey

### Happy flow
Step by step description of the happy flow, including any relevant screenshots, mockups, or diagrams. Include expected behavior and any known workarounds.

### Edge cases
Step by step description of the edge case, including any relevant screenshots, mockups, or diagrams. Include expected behavior and any known workarounds.

## Workflow / Flowchart / BPMN diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## System context diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Sequence diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Component diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Domain model diagram
User can decide what diagram format to use (Draw.io, Mermaid, etc.) and whether to embed or attach the diagram. Match the page's diagram style to any theme the team already uses for the product.

## Technical changes
| Components | Changes | JIRA Tickets |
|---|---|---|
|   |   |   |

## Known risks and mitigations
List of known risks and mitigations, with rationale for why they are risks and how they will be mitigated. Include any relevant screenshots, mockups, or diagrams. Accordion-style collapsible sections are preferred for each risk, with a summary line and a "Details" section for the mitigation plan and any supporting diagrams or links.
```
