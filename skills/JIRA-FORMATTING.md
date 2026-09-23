# JIRA Formatting & Attachments

Shared reference for `write-story`, `write-bug`, `write-epic`, and `write-initiative` — single source of truth for Jira markup and attachment handling. Do not restate this content inside those skills; point here instead.

## Formatting
Atlassian Document Format via Markdown only: **bold** for entities/components, ***bold+italic*** for APIs/topics, `code` for fields/variables and ```code blocks``` for code snippets. Use standard success, warning, and info panels when highlighting important information. Where the template has an Acceptance criteria section, write it as plain bullets (`*`), never checkboxes. Full browse URLs for links.

## Rich media & attachments
Local file paths (e.g. `![alt](/local/path.png)`) do not work in JIRA — Atlassian servers can't reach your filesystem. Upload the image/diagram/screenshot to the ticket via the MCP attachment tool first, then embed it using JIRA's attachment syntax (e.g. `!filename.png!`), never the local path.
