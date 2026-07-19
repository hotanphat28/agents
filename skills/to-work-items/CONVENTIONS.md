# JIRA Conventions (Full Reference)

## Title Patterns

| Type | Pattern | Example |
|------|---------|---------|
| Epic | `[Capability noun phrase]` | `Collateral Valuation Automation` |
| Story | `[Action verb] [what] [context]` | `Add validation for loan amount on disbursement form` |
| Bug | `[Component] - [Symptom]` | `Loan Calculator - Interest rate shows NaN for zero principal` |
| Task | `[Imperative action]` | `Upgrade Spring Boot to 3.4` |
| Spike | `Spike: [Question to answer]` | `Spike: Evaluate BRE options for eligibility rules` |
| Sub-task | `[Verb] [specific action]` | `Implement DTI calculation endpoint` |

### Title Rules

- Maximum 80 characters
- No ticket IDs in title (JIRA already shows them)
- No vague words: "improve", "update", "fix things", "various"
- Start with capital letter
- No trailing period
- No prefix tags like `[BE]` or `[FE]` — use labels or components instead

---

## Text Formatting

### Semantic Styling

| Category | Style | Example |
|----------|-------|---------|
| Client, Product, System, Component, Entity | **bold** | **Atlanta**, **Collateral** |
| Kafka topic, API, Process, Page, Feature, Method | ***bold+italic*** | ***loan-application-submitted***, ***POST /api/loans*** |
| Field, Button, Variable, Parameter, Key/Value | `code` | `loanAmount`, `Submit`, `status=ACTIVE` |
| File path, class name, SQL | `code` | `LoanService.cs`, `SELECT * FROM loans` |
| Quote from requirement or stakeholder | > blockquote | > "Must support concurrent editing" |

---

## JIRA Markdown Formatting (ADF)

JIRA Cloud uses Markdown syntax rendered to Atlassian Document Format (ADF). Wiki markup is NOT supported.

### Supported Syntax

| Element | Syntax |
|---------|--------|
| Headings | `#` / `##` / `###` |
| Bold | `**text**` |
| Italic | `*text*` |
| Strikethrough | `~~text~~` |
| Unordered list | `*` or `-` |
| Ordered list | `1.` |
| Code inline | `` `code` `` |
| Code block | ```` ```language ```` |
| Link | `[text](url)` |
| Table header | `\|\|col\|\|` |
| Table cell | `\|val\|` |
| Mention | `@username` |
| Emoji | `:emoji_name:` |

### Broken (DO NOT USE)

| Syntax | Problem | Use instead |
|--------|---------|-------------|
| `h1. Heading` | Wiki markup — not rendered | `# Heading` |
| `_text_` | Underscore italic — broken | `*text*` |
| `{{term}}` | Monospace — not rendered | `` `term` `` |
| `{code}...{code}` | Code block — broken | ```` ```lang ```` |
| `[text\|url]` | Wiki link — broken | `[text](url)` |
| `{panel}` | Panels — not supported | Use headings + content |
| `{noformat}` | No format block — broken | ```` ``` ```` |

---

## JIRA Links

Always use browse URLs (not API URLs):

```
[PROJ-123](https://[instance].atlassian.net/browse/PROJ-123)
```

For multiple tickets:
```
Related: [PROJ-123](https://...), [PROJ-456](https://...)
```

---

## Labels & Components

### Label Conventions

| Purpose | Label pattern | Example |
|---------|--------------|---------|
| Feature area | `area:feature-name` | `area:collateral`, `area:onboarding` |
| Type refinement | `type:tech-debt`, `type:spike` | `type:tech-debt` |
| Priority flag | `priority:critical` | `priority:critical` |
| Team | `team:team-name` | `team:alpha` |

### Component Usage

Use JIRA components (not labels) for:
- Application modules (e.g., `loan-service`, `portal-ui`)
- Shared services (e.g., `auth`, `notifications`)
- Infrastructure (e.g., `ci-cd`, `monitoring`)

---

## JQL Patterns

### Common Queries

```jql
# My open work
assignee = currentUser() AND status != Done ORDER BY priority DESC

# Sprint backlog
sprint in openSprints() AND type in (Story, Bug, Task) ORDER BY rank ASC

# Ready for refinement
status = "To Do" AND "Story Points" is EMPTY AND type = Story

# Stale items (>90 days without update)
updated <= -90d AND status not in (Done, Closed) AND type in (Story, Bug)

# Bugs by severity
type = Bug AND status != Done ORDER BY priority ASC, created DESC

# Epic progress
type = Story AND "Epic Link" = PROJ-100 ORDER BY status ASC

# Items without acceptance criteria
type = Story AND description !~ "Given" AND status = "To Do"
```

### API Optimization

| Goal | Technique |
|---|---|
| Exclude sub-tasks | `type in (Story, Bug, Task, Epic)` |
| Fetch minimal fields | `fields=summary,description,issuetype,status` |
| Limit results | `maxResults=50` |
| Recent only | `updated >= -30d` |

**Token impact:**
- Full fields (all) = ~50K tokens per 20 issues
- Minimal fields = ~5K tokens per 20 issues
- Always use minimal fields unless specific fields are needed

---

## Sprint Naming Convention

```
[Team] Sprint [N] — [Date range]
```
Example: `Alpha Sprint 42 — 2025-06-02 to 2025-06-13`

---

## Workflow Transitions

Standard workflow states and when to transition:

| From | To | Trigger |
|---|---|---|
| Backlog | To Do | Refined and prioritized for upcoming sprint |
| To Do | In Progress | Developer starts working |
| In Progress | In Review | PR created, ready for code review |
| In Review | In QA | Code review approved, merged to dev branch |
| In QA | Done | QA verified, PO accepted |
| Any | Blocked | External blocker identified |
| Blocked | Previous state | Blocker resolved |

---

## Estimation Conventions

### Story Points (Fibonacci)

| Points | Meaning | Reference |
|--------|---------|-----------|
| 1 | Trivial — config change, copy update | 15 min - 1 hour |
| 2 | Simple — single component, clear path | Half day |
| 3 | Small — straightforward, minor integration | 1 day |
| 5 | Medium — multiple components, some uncertainty | 2-3 days |
| 8 | Large — cross-cutting, integration needed | 1 week |
| 13 | Very large — significant complexity | Should be split |
| 21+ | Epic-sized | Must be split |

### T-Shirt to Points Mapping

| T-Shirt | Points | Rough effort |
|---------|--------|-------------|
| XS | 1 | <0.5 day |
| S | 2-3 | 0.5-1 day |
| M | 5 | 2-3 days |
| L | 8 | ~1 week |
| XL | 13+ | Split required |
