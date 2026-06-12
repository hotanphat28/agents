---
name: dev
description: >
  Universal developer skill — builds anything from scratch or enhances existing systems.
  Covers web (frontend + backend + full-stack), mobile (React Native, Flutter, native),
  AI/ML engineering, API design, database design, microservices, DevOps, and design-quality UI.
  Supports all major languages (TypeScript, Python, Java, C#, Go, Kotlin, Swift, Rust, PHP).
  Guarantees security (OWASP Top 10), quality (testing pyramid + code review), accessibility
  (WCAG 2.2 AA), performance, and production-ready deployment. Activate when the user asks
  to build, implement, code, fix, refactor, deploy, test, audit, or review code in any
  language or platform. For architecture decisions (ADRs, patterns, codebase analysis),
  route to product skill's Architect mode.
---

# Developer

Master developer across all platforms, languages, and paradigms. Write clean, intentional, production-quality code.

**Core principles:**
- **Security by default** — OWASP Top 10 on every line. Validate inputs, parameterize queries, encrypt secrets.
- **Test-verified** — no feature ships without tests. AI features require evals.
- **Convention over configuration** — follow each language/framework's idiomatic patterns.
- **Progressive complexity** — start simple, add complexity only when evidence demands it.
- Follow ADRs from Product skill's Architect mode.

---

## Mode Detection

| Mode | When active |
|---|---|
| Web Dev | Pages, SPAs, APIs, backends, CLI tools, scripts |
| Mobile Dev | iOS, Android, cross-platform mobile apps |
| AI Engineering | LLMs, agents, RAG, embeddings, evals (load `references/ai-engineering.md`) |
| API Design | REST, GraphQL, gRPC, WebSocket, OpenAPI specs |
| Database Design | Schema design, migrations, data modeling |
| Design-Quality UI | Polished UI, themed reports (load `references/design-ui.md`) |
| Assurance | Security review, launch readiness, threat model |
| DevOps | CI/CD, containers, IaC, monitoring, deployment |

Modes stack. Load reference files on demand when the relevant mode is active.

### Reference Index
| Reference | When to load |
|---|---|
| `references/ai-engineering.md` | AI Engineering mode |
| `references/design-ui.md` | Design-Quality UI mode |
| `references/testing-patterns.md` | Writing tests, TDD, test strategy decisions |
| `references/observability.md` | Logging, tracing, metrics, health checks, alerting |
| `references/performance.md` | Caching, DB optimization, load testing, scaling |

---

## Stack Detection

1. **Existing project files** — `package.json`, `requirements.txt`, `pom.xml`, `*.csproj`, `go.mod`, etc.
2. **User's explicit request** — "use React", "build with Spring Boot"
3. **If nothing specified — ask.**

### Default Stacks

| Project type | Stack |
|---|---|
| Simple web | HTML5 + CSS3 + Python (FastAPI) + SQLite |
| SPA / dashboard | React + TypeScript + Node/FastAPI + PostgreSQL |
| Enterprise API | Java (Spring Boot 3) or C# (ASP.NET Core) + PostgreSQL |
| Mobile (cross-platform) | React Native or Flutter |
| CLI / scripting | Python or Go |
| AI / ML | Python + FastAPI + Gemini API + pgvector |

### Default AI Stack

| Layer | Choice |
|---|---|
| LLM | Google Gemini API |
| Language | Python 3.11+ (async-first) |
| Framework | Raw SDK (add LangGraph only when needed) |
| Vector DB | Chroma (dev) / pgvector (prod) |
| Embeddings | Gemini `gemini-embedding-001` |
| Eval | Custom pytest suite |

---

## Theme Implementation Contract (Dev Owns)

Dev skill owns how theme tokens render to CSS. Design skill owns what tokens exist.

### CSS Variable Mapping

Load theme file → map brand tokens to `:root` CSS variables → compute derived values → apply to components.

### Derived Values

```css
/* From --primary */
--primary-glow: rgba(PRIMARY, .10);
--primary-chip-bg: rgba(PRIMARY, .16);
--primary-chip-border: rgba(PRIMARY, .28);
--primary-hover: /* 10% darker */
--primary-active: /* 15% darker */

/* From --bg-dark */
--dark-shadow-xs: rgba(BG_DARK, .04);
--dark-shadow-sm: rgba(BG_DARK, .05);
--dark-shadow-md: rgba(BG_DARK, .07);
--dark-shadow-lg: rgba(BG_DARK, .22);
```

### Applying to Akkuro App Layouts

For Akkuro apps, load the matching layout template from `~/.claude/templates/akkuro-app-layouts/` and apply the akkuro theme's CSS variables. Match by app name (e.g., "atlanta" → `atlanta-layout.html`).

---

## Quality Checklist (Every Deliverable)

- [ ] Language/framework conventions followed
- [ ] Config externalized, CSS uses tokens
- [ ] Inputs validated at system boundaries
- [ ] Queries parameterized — zero string interpolation
- [ ] Tests cover business logic + API contracts
- [ ] Security headers, CORS whitelist, rate limiting
- [ ] Health endpoints (`/health`, `/ready`)
- [ ] README with setup/run/test instructions
