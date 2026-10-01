# Diagrams

Disclosed reference for analyst's diagram generation, reached only when an Analysis Layer step or Gap Analysis produces a diagram deliverable.

## Default diagram set
Should have the following diagram types when possible:

* Self decide to have **BPMN Diagrams** for business process flows and decision points or **Flowcharts** for system flows and edge cases
* **Data Flow Diagrams** for data movement across processes, external entities, and data stores (system boundaries/integration points)
* **Sequence Diagrams** for core business flows and edge cases
* **Domain Models** for data structures and relationships
* **Component Diagrams** for system architecture and dependencies — optional, only when architecture complexity warrants a dedicated diagram

Default tool: use `/diagram-design` to generate diagrams. If `/diagram-design` is not available, ask the user to select one of the following list:

1. SVG embedded in HTML
2. PlantUML rendered in HTML

After a diagram is generated in a separate html file, automate exporting it into SVG via `/diagram-design`.

This default covers BPMN/Flowchart, **all Sequence diagrams**, and Domain Model diagrams — even though `archify` also has a Sequence type, do not use it for this skill's Sequence diagrams; it is reserved solely for the AS-IS/TO-BE case below.

## AS-IS vs TO-BE Architecture Comparison (Gap Analysis)

When the Gap Analysis step (Functional & Logic Analysis, item 4) covers **Data Flow** or **Component** diagrams **and** the lifecycle is Brownfield (a real codebase exists to trace), use `archify` instead of `/diagram-design` so the comparison is evidence-backed and diffable:

1. Trace the current codebase to produce an evidence-backed AS-IS architecture JSON (nodes cite `SRC n` file/line at the current commit).
2. Author the TO-BE architecture JSON by hand from the analysis (no code evidence required — it does not exist yet), reusing the same component ids as the AS-IS snapshot where the component still exists — archify's `compare` requires at least one shared component id to prove both snapshots describe the same system.
3. Use archify's `compare` command for the `architecture` type to render the Before / Delta / After comparison (`compare` isn't documented in archify's own `SKILL.md` — locate the installed archify skill first, then check its `bin/archify.mjs` usage banner for exact syntax).
4. Embed or link the resulting HTML in the **Technical** tab (see `DOCUMENT-TEMPLATE.md` Tab → Component Mapping) instead of two separate static diagrams. There is no separate "Architecture Decisions" tab — only the 6 mandated tabs exist.

For **Greenfield** concepts (no existing codebase to trace) there is no AS-IS state, so stay on `/diagram-design` for the Data Flow/Component diagram of the proposed TO-BE only.

## Theming
All diagrams MUST apply and match the theme used for the HTML documents (e.g., matching colors and fonts).
