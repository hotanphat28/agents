# Outcome Rules

## Document Rendering

### Process
1. Determine use case (Analysis / Proposal / Plan / Review) and depth (Light / Standard / Deep)
2. Assemble the document dynamically using the snippets and base HTML shell provided in `DOCUMENT-TEMPLATE.md`.
3. Use the fallback inline CSS provided in the shell if custom themes are missing or inaccessible.
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow the flexible component guidelines in `DOCUMENT-TEMPLATE.md` to map data to appropriate UI components dynamically.
6. For user-facing screens, do NOT build the prototype here — write a **Prototype Handoff Brief** in the **Functional** tab (per screen: purpose, states, interactions/JS behavior, inputs & validation, data shape, edge cases) and hand off to **builder** to build the interactive throwaway prototype. Also generate Mermaid/PlantUML diagrams for SA architectural decisions.
7. Save as `YYYYMMDD-<type>-<topic>.html`

### Final Review Gate
After the **[Business Analyst]** drafts the outcomes, the **[Product Owner]** and **[Solution Architect]** MUST conduct a rigorous review before finalization:
- **Completeness**: Are all edge cases, rules, and NFRs covered?
- **Conciseness**: Is the document free of bloat and unnecessary complexity?
- **Comprehensiveness**: Does this artifact fully solve the validated problem from the Analysis phase?
- **Trim pass**: Actively cut the lowest-value ~20% (restated context, redundant caveats, over-explained obvious points) before delivering — comprehensive means nothing important is missing, not that everything considered must be shown.
*The documents or tickets cannot be considered final until they pass this gate.*

### Prototype Alignment Gate
When a Prototype Handoff Brief exists, it cannot be handed to **builder** until the **[Business Analyst]** has surfaced every open question, ambiguity, or conflicting requirement about the screens/interactions directly to the user and the user has explicitly confirmed alignment. Never build or hand off on assumptions.

## JIRA & Confluence Work Items

### Jira Refinement Safety Protocol
Preview all proposed tickets in Markdown for user approval before making external API calls. This protocol is enforced natively inside each write-* skill below — do not bypass it by drafting/pushing tickets directly from this skill.

### Delegation
Work item drafting, templates, title patterns, formatting, and attachment rules are owned by dedicated model-invoked skills — do not duplicate their templates here. Invoke the matching skill for the artifact being produced:

| Artifact | Skill |
|---|---|
| Story | `write-story` |
| Bug | `write-bug` |
| Epic | `write-epic` |
| Initiative | `write-initiative` |
| Confluence design doc | `write-design-doc` |

Hand each skill the relevant Analysis Layer output (business value/OKR, requirements, BDD acceptance criteria, diagrams) as intake context; the skill handles drafting, verification, approval gate, and MCP execution itself.
