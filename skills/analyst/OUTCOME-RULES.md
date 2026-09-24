# Outcome Rules

## Document Rendering

### Process
1. Determine use case (Analysis / Proposal / Plan / Review) and depth:
   * **Light** — quick note or single-screen ask. Linear, no tabs (per `DOCUMENT-TEMPLATE.md` General Guidance). Only the Generic Card / Reference Table components that directly answer the ask.
   * **Standard** (default) — full 6-tab structure. Exactly the rows in `DOCUMENT-TEMPLATE.md`'s Tab → Component Mapping that have content from the Analysis Layer; skip a row entirely if that analysis step wasn't run, don't invent placeholder content for it.
   * **Deep** — full 6-tab structure plus every optional/conditional component that applies (ADRs, Prototype Handoff Briefs, AS-IS/TO-BE `delta.html`, Concept Architecture Card) even when only partially filled, so reviewers see the full shape of the analysis.
2. Assemble the document dynamically using the snippets and base HTML shell provided in `DOCUMENT-TEMPLATE.md`.
3. Use the fallback inline CSS provided in the shell if custom themes are missing or inaccessible.
4. Populate **6 mandatory tabs**: Context | Business | Functional | Technical | Assessment | Action
5. Follow the fixed Tab → Component Mapping in `DOCUMENT-TEMPLATE.md` to place each piece of data in its assigned tab and order — do not improvise placement.
6. For user-facing screens, do NOT build the prototype here — write a **Prototype Handoff Brief** in the **Functional** tab (per screen: purpose, states, interactions/JS behavior, inputs & validation, data shape, edge cases) and hand off to **builder** to build the interactive throwaway prototype. Also generate Mermaid/PlantUML diagrams for SA architectural decisions.
7. Save as `YYYYMMDD-<type>-<topic>.html`

### Final Review Gate
After the **[Business Analyst]** drafts the outcomes, the **[Product Owner]** and **[Solution Architect]** MUST conduct a rigorous review before finalization:
* **Completeness**: Are all edge cases, rules, and NFRs covered?
* **Conciseness & trim pass**: apply the global `Response depth` rule (`ai-operating-system.instructions.md` / `GEMINI.md`: comprehensive but concise, cut the lowest-value ~20%), not restated here.
* **Comprehensiveness**: Does this artifact fully solve the validated problem from the Analysis phase?
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
