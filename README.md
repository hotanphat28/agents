# .agents — Personal AI Skill System

Single-agent, multi-skill architecture. Skills are user-invoked for precise control and focus.

## Structure

```
.agents/
├── skills/
│   ├── ADF.md                Shared Atlassian Document Format reference (write-story/bug/epic/initiative/design-doc)
│   ├── analyst/              Analysis & Outcome engine (Concept Architecture, Story Mapping, OKRs, DDD, Clean Architecture, HTML docs)
│   │   ├── SKILL.md
│   │   ├── AI-ANALYSIS.md
│   │   ├── ARCHITECT.md
│   │   ├── DISCOVERY-METHODS.md
│   │   ├── OUTCOME-RULES.md
│   │   └── DOCUMENT-TEMPLATE.md
│   ├── designer/              UI/UX, brand, design systems (Strict Dark Mode & A11y)
│   │   ├── SKILL.md
│   │   └── DESIGN-PRINCIPLES.md
│   ├── builder/               Implementation (enforces SOLID, DI, Repository patterns)
│   │   ├── SKILL.md
│   │   ├── AI-ENGINEERING.md
│   │   ├── OBSERVABILITY.md
│   │   ├── PERFORMANCE.md
│   │   └── DESIGN-PATTERNS.md
│   ├── inspector/             Testing strategy, automation code, security testing
│   │   ├── SKILL.md
│   │   └── TESTING-PATTERNS.md
│   ├── naval/                 Naval Ravikant persona
│   │   ├── SKILL.md
│   │   └── NAVAL-FRAMEWORKS.MD
│   ├── tony/                  Tony Robbins persona + goals template
│   │   ├── SKILL.md
│   │   ├── TONY-FRAMEWORKS.MD
│   │   └── GOALS-TEMPLATE.HTML
│   ├── maker-karaoke-video/   HyperFrames karaoke videos
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── generate_karaoke.py
│   ├── maker-lyric-video/     HyperFrames lyric videos
│   │   ├── SKILL.md
│   │   └── examples/
│   │       ├── generate_lyric.py
│   │       ├── generate_thumbnail.py
│   │       └── transcribe.py
│   ├── maker-podcast-video/   HyperFrames kinetic typography
│   │   ├── SKILL.md
│   │   └── examples/
│   │       ├── captions.js
│   │       └── index.html
│   ├── numerologist/          Pythagorean & Quynh Huong numerology readings
│   │   ├── SKILL.md
│   │   ├── PYTHAGOREAN-RULES.md
│   │   ├── QUYNH_HUONG_NUMEROLOGY.XLSX
│   │   ├── QUYNH_HUONG_NUMEROLOGY_1.JPG
│   │   └── QUYNH_HUONG_NUMEROLOGY_2.JPG
├── design-system/
│   └── hotanphat28/          Personal brand design system (single source of truth for brand tokens)
│       └── DESIGN.md
```

## Skill Invocation

| Skill | Suggested Use Cases |
|---|---|
| analyst | analysis, concept architecture, story mapping, OKRs, roadmap, PRD, stories, ADR, report, proposal, plan, security review, code-shape sketches |
| designer | wireframe, prototype, UI, brand, design system, theme |
| builder | build, implement, code, fix, refactor, deploy, TDD, unit test |
| inspector | test, coverage, BDD, test automation, security testing, vulnerabilities |
| naval / tony | "Hey [Name]", coaching, goals, habits, wealth |
| maker-lyric-video | lyric video, music video with synced text |
| maker-karaoke-video | karaoke video, sing-along video with timed lyrics highlighting |
| maker-podcast-video | podcast video, kinetic typography, audio clip reel |
| numerologist | numerology, life path, birth chart, destiny number, compatibility, Sifu |
