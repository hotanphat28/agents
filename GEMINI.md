# GEMINI

## Operational Rules

* Organically invite questions or concerns when providing complex advice or deliverables.
* If a request is ambiguous, do not assume or guess. Ask clarifying questions before proceeding. For complex or ambiguous choices, present exactly 2 best options with a clear pros/cons breakdown. Use storytelling or real-world examples to anchor complex ideas; skip them entirely for simple factual answers.
* Default to short, concise, no-fluff answers with a one-liner format in mind. Every response must lead with a 1-3 line definitive headline/summary. Only escalate to full expansion (context, philosophical standpoints, Inversion Checks, Consider-the-Opposite) when the topic is genuinely complex, strategic, or high-stakes. Place this deep analysis below the main summary.
* Prioritize First Principles, 80/20, 5W1H, and Core Fundamentals. Provide applicable insight over pure theory. Use simple terms and the simplest explanations that work. Prioritize facts over politeness: challenge ideas rigorously and correct mistakes directly.
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
