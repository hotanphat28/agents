# .agents — Personal AI Skill System

Single-agent, multi-skill architecture. Skills auto-activate from context.

## Structure

```
.agents/
├── skills/
│   ├── product-analyze/      Analysis & Outcome engine (self-renders HTML docs)
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   ├── ARCHITECT.md
│   │   ├── OUTCOME-RULES.md
│   │   └── templates/
│   │       ├── DOCUMENT-TEMPLATE.html
│   │       ├── SECTION-LIBRARY.md
│   │       └── DESIGN-UI.md
│   ├── product-design/       UI/UX, brand, design systems
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   └── DESIGN-PRINCIPLES.md
│   ├── product-develop/      Implementation (all languages/platforms)
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   ├── AI-ENGINEERING.md
│   │   ├── OBSERVABILITY.md
│   │   └── PERFORMANCE.md
│   ├── product-quality/      Testing strategy + automation code
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   └── TESTING-PATTERNS.md
│   ├── mentor-feynman/       Richard Feynman persona
│   ├── mentor-james/         James Clear persona
│   ├── mentor-naval/         Naval Ravikant persona
│   ├── mentor-tony/          Tony Robbins persona + goals template
│   ├── lyric-video-maker/    HyperFrames lyric videos
│   └── podcast-video-maker/  HyperFrames kinetic typography
└── themes/
    └── hotanphat28/          Personal brand theme
```

## Skill Routing

| Skill | Activates on |
|---|---|
| product-analyze | analysis, roadmap, PRD, stories, ADR, report, proposal, plan, security review |
| product-design | wireframe, prototype, UI, brand, design system, theme |
| product-develop | build, implement, code, fix, refactor, deploy |
| product-quality | test, coverage, TDD, BDD, test automation |
| mentor-* | "Hey [Name]", coaching, goals, habits, wealth |
| lyric-video-maker | lyric video, music video with synced text |
| podcast-video-maker | podcast video, kinetic typography, audio clip reel |

## Flows

1. **Full Feature** — analyze → design → develop → quality
2. **Document** — analyze (self-renders 6-tab HTML)
3. **UI Redesign** — design → develop
4. **Architecture** — analyze (Outcome layer) → develop
5. **Security Review** — analyze (Review use case)
6. **Goals** — mentor → develop (render goals.html)
7. **Tickets** — analyze (Outcome layer)
8. **Mentoring** — mentor-*
9. **App Prototyping** — design + develop
10. **API Schema** — retrieve-lending-schema
11. **Testing** — quality
