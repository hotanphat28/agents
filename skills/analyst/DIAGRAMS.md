# Diagrams

Disclosed reference for analyst's diagram generation, reached only when an Analysis Layer step or Gap Analysis produces a diagram deliverable.

## Default diagram set
Should have the following diagram types when possible:

* Self decide to have **BPMN Diagrams** for business process flows and decision points or **Flowcharts** for system flows and edge cases
* **Data Flow Diagrams** for data movement across processes, external entities, and data stores (system boundaries/integration points)
* **Sequence Diagrams** for core business flows and edge cases
* **Domain Models** for data structures and relationships
* **Component Diagrams** for system architecture and dependencies — optional, only when architecture complexity warrants a dedicated diagram

This default set applies to every diagram deliverable, including **AS-IS vs TO-BE Architecture Comparisons** (Gap Analysis, Functional & Logic Analysis item 4) for both Greenfield and Brownfield lifecycles — there is no separate tool or workflow for that case.

## Tool fallback chain
1. **Default**: use `/diagram-design` to generate the diagram, then automate exporting it into SVG via `/diagram-design`.
2. **If `/diagram-design` cannot generate the diagram**: fall back to hand-authored SVG embedded in HTML, matching the theme used for the HTML documents.
3. **If hand-authored SVG also cannot represent the diagram**: stop and ask the user how to proceed.

Apply this same three-step chain to AS-IS/TO-BE comparisons — embed the resulting diagram(s) in the **Technical** tab (see `DOCUMENT-TEMPLATE.md` Tab → Component Mapping). There is no separate "Architecture Decisions" tab — only the 6 mandated tabs exist.

## Theming
All diagrams MUST apply and match the theme used for the HTML documents (e.g., matching colors and fonts).
