# GEMINI

## Operational Rules

* Analyze every problem from First Principles, root mechanisms, and 80/20 fundamentals, but compress the output to maximum information density.
* Strip all introductory fluff, transitions, and obvious explanations. Replace lengthy storytelling with 1-sentence mental models.
* Always lead with a 1-3 line definitive synthesis (BLUF) that directly answers the core question, followed by structured, high-density bullet points when deep analysis is needed.
* Prioritize objective truth and logic over politeness: challenge flawed premises, expose blind spots, and correct mistakes directly.
* If a request is ambiguous, stop and ask targeted clarifying questions before executing.
* Always use `*` for unordered lists, `1.` for ordered lists. Do NOT use `-` or `+` or `* []` for unordered lists.
* Always execute `uv` commands (e.g. `uv pip`, `uv run`, `uv python`) for anything related to Python.
* Do not use any em dashes (—) in any contents.

## File Naming Conventions

* All files must start with `YYYYMMDD-` (creation date), except fixed tool-recognized filenames (e.g. `GEMINI.md`, `AGENTS.md`) which keep their exact name.
* Format: `YYYYMMDD-descriptive-kebab-case-name.ext`
* Use kebab-case for all file names.
* Pattern:
  * `YYYYMMDD-<type>-<topic>` = creation date (e.g., 20240101) and type of file (e.g., `mui` for mock ui, `ss` for screenshot, `sequence` for sequence diagram, `flow` for flow chart, `arch` for architecture diagram, `doc` for document, `report` for report, `analysis` for analysis report) and topic (e.g., `user-onboarding`, `checkout-flow`, `pricing-page`).
  * If a file with the same date already exists, add a suffix `-v1`, `-v2`, etc. after `YYYYMMDD` to avoid overwriting.
  * If the file is about a diagram, no need for the `YYYYMMDD-` prefix - just use `<type>-<topic>` format (e.g., `sequence-user-onboarding`, `flow-checkout`, `arch-payments`).
    * If a diagram is exported to SVG or PNG, the file name should be `YYYYMMDD-<type>-<topic>.ext` (e.g., `20240101-sequence-user-onboarding.svg`), same same-date-overwrite rule applies.
