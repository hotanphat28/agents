# .agents — Personal AI Skill System

Single-agent, multi-skill architecture. Skills auto-activate from context.

## Structure

```
.agents/
├── skills/
│   ├── product-analyze/      Analysis & Outcome engine (DDD, Architecture, HTML docs)
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   ├── ARCHITECT.md
│   │   ├── OUTCOME-RULES.md
│   │   └── DOCUMENT-TEMPLATE.md
│   ├── product-design/       UI/UX, brand, design systems (Strict Dark Mode & A11y)
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   └── DESIGN-PRINCIPLES.md
│   ├── product-develop/      Implementation (enforces SOLID, DI, Repository patterns)
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   ├── AI-ENGINEERING.md
│   │   ├── OBSERVABILITY.md
│   │   ├── PERFORMANCE.md
│   │   └── DESIGN-PATTERNS.md
│   ├── product-quality/      Testing strategy, automation code, security testing
│   │   ├── SKILL.md
│   │   ├── GLOSSARY.md
│   │   └── TESTING-PATTERNS.md
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
| product-quality | test, coverage, TDD, BDD, test automation, security testing, vulnerabilities |
| mentor-* | "Hey [Name]", coaching, goals, habits, wealth |
| lyric-video-maker | lyric video, music video with synced text |
| podcast-video-maker | podcast video, kinetic typography, audio clip reel |
