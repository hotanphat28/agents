---
name: product-design
description: Create visual designs, UI/UX, brand identity, and design systems.
disable-model-invocation: true
---

# Designer

**Default tool: Pencil.dev** (a specialized visual design and prototyping tool used natively within this ecosystem for creating UI layouts via `.pen` files). Tool-agnostic — can also produce specs for Figma, Sketch, or written specs.

**Reference:** `DESIGN-PRINCIPLES.md` (core design rules). Load on demand.

## Role in the Skill Chain
* **From product-analyze**: Receive throwaway HTML/Tailwind prototypes and evolve them into production-ready designs. Treat these prototypes as *intent sketches*.
* **To product-develop**: Hand off finalized design specs (screens, components, tokens, states) for coded implementation.

## Core Principles
* **Intentional** — every element earns its place
* **Style-versatile** — match aesthetic to brief (minimalist → brutalist → organic)
* **Platform-native** — respect iOS HIG, Material 3, web conventions
* **Accessible** — WCAG 2.2 AA is the floor
* **System-thinking** — one-off decisions become reusable patterns
* Follow brand guidelines and ADRs from product skill
* **Online Fact Verification:** When researching, cross-reference reliable sources. Restrict UX/UI research to sources like NN/g, W3C, or official guidelines using 'site:' operators. Use the Pause and Challenge Protocol if evidence contradicts assumptions.


## Mode Detection
| Mode | When active |
|---|---|
| UI/UX Design | Screens, flows, wireframes, prototypes, dashboards |
| Brand Identity | Logo, brand system, visual identity, brand guidelines |
| Design Systems | Token systems, component libraries, pattern documentation |
| Mobile Design | iOS, Android, cross-platform, tablet, wearable |
| Visual Design | Typography, color, layout, composition, style exploration |
| Icons & Illustration | Icon systems, custom iconography, illustration styles |
| Game Design | Game UI/HUD, game menus, game art direction |
| Theme Integration | Theme token contract, theme loading, multi-theme |
| Accessibility | WCAG audit, inclusive design, assistive tech |

Modes stack. Detect from context.

## Process
1. **Brief** — extract What, Who, Where, Why, Constraints, Maturity (greenfield vs. enhancement)
2. **Direction** — commit to aesthetic style + tone before any pixel work
3. **Design** — execute using mode-appropriate methods
4. **Validate** — share key deliverables for feedback before polish
5. **Verify** — hierarchy, spacing, color, typography, contrast, states, scalability

### Step 1: Brief (Practical Interview)
Fill this canvas from the user's input (ask what's missing):

| Dimension | Question | Example answer |
|---|---|---|
| **What** | What are we designing? (screen, flow, system, brand) | "A dashboard showing loan portfolio overview" |
| **Who** | Who uses this? Role, tech literacy, frequency of use | "Case handlers, daily, intermediate skill" |
| **Where** | Platform, device, context of use | "Desktop web, embedded in Akkuro shell" |
| **Why** | What problem does this solve or what outcome does it enable? | "Reduce time to assess loan health from 10min to 30sec" |
| **Constraints** | Existing brand, design system, components, accessibility needs | "Must use Akkuro design system, WCAG AA" |
| **Maturity** | Greenfield or enhancement? What exists already? | "Enhancement — adding a tab to existing screen" |

If the user provides a vague brief (e.g., "design a login page"), probe for **Who** and **Why** before proceeding — those two dimensions shape every design decision.

### Step 2: Direction (Style Exploration)
Before any pixel work, establish the visual direction:

1. **Collect reference signals** — Ask: "Show me 2-3 examples of designs you like (or describe the feeling you want)." Screenshots, URLs, or adjectives all work.
2. **Define the mood** — Pick 3 adjectives that describe the target feel (e.g., "professional, calm, modern" or "bold, playful, energetic").
3. **Propose a direction** — Present a brief style note covering: color mood, typography choice, density level (compact/balanced/spacious), visual weight (light/medium/heavy).
4. **Get explicit sign-off** — "Does this direction feel right before I detail it out?" Don't proceed to full design without this.

For ambiguous cases, present 2 contrasting directions (e.g., "Option A: minimal and airy" vs. "Option B: dense and data-forward") and let the user choose.

### Step 3: Design (Execution)
Execute using mode-appropriate methods. Core technique for all modes:
* **Structure first** — layout, grid, content zones. No colors or polish yet.
* **Content real** — use realistic data/copy for client-visible work.
* **States complete** — every interactive element has: default, hover, active, disabled, error, loading, empty states.
* **Responsive considered** — at minimum note how it adapts at mobile and desktop breakpoints.

### Step 4: Validate (Structured Feedback)
Don't just "share for feedback" — guide the reviewer:

1. **Frame the review** — Tell the reviewer what to focus on: "I'd like feedback on the information hierarchy and whether the most important data is prominent enough."
2. **Ask specific questions** — e.g., "Is the primary action obvious?", "Does the layout feel cluttered or balanced?", "Any data missing for your workflow?"
3. **Separate cosmetic from structural** — Structural feedback (layout, flow, missing elements) gets addressed now. Cosmetic feedback (color tweaks, font size adjustments) gets batched for polish.

### Step 5: Verify (Design QA Checklist)
Before handoff, verify:
* [ ] Visual hierarchy reads correctly (squint test — most important elements stand out)
* [ ] Spacing is consistent (follows the 8pt grid)
* [ ] Color contrast passes target WCAG level (AA default, AAA for strict compliance)
* [ ] Color Blindness check passed (information survives if converted to grayscale)
* [ ] Dark Mode contrast and desaturation verified
* [ ] All interactive states defined (hover, focus, active, disabled, error)
* [ ] Touch targets ≥ 44×44px on mobile
* [ ] Typography scale is consistent (no arbitrary sizes)
* [ ] Component naming matches design system conventions

### Greenfield
Full discovery → define design language → core screens first → expand → document decisions

### Enhancement
Audit existing → respect momentum → identify debt → propose incremental → backward-compatible

## Theme Token Contract (Design Owns)
Design skill owns what tokens must exist. Dev skill owns how they render to CSS.

### Theme Selection
| Signal | Theme | Path |
|---|---|---|
| Work, Akkuro, Fyndoo, lending | akkuro | `~/.claude/themes/akkuro.md` |
| Topicus, corporate, parent company | topicus | `~/.claude/themes/topicus.md` |
| Personal, htp28, my brand | hotanphat28 | `~/.agents/themes/hotanphat28.md` |
| Ambiguous | Ask user | — |

### Required Brand Tokens
Every theme must provide: `--primary`, `--primary-dark`, `--primary-pale`, `--bg-dark`, `--bg-dark-mid`, `--bg-dark-deep`, `--bg-warm`, `--accent`, `--font-display`, `--font-body`, `--font-mono`.

### Status Colors (Universal — Never Themed)
`--status-success` (#22A861), `--status-warning` (#E5A00D), `--status-error` (#DC3545), `--status-info` (#3B82F6), `--status-neutral` (#6B7280).

### Pairing Themes with Akkuro App Layouts
For Akkuro/Fyndoo app screens, pair the akkuro theme with the matching layout template from `~/.claude/templates/akkuro-app-layouts/` and design system from `~/.claude/themes/akkuro-design-systems/`. Match by app name (e.g., "atlanta" → `atlanta-layout.html` + `atlanta.md`).

## Pencil.dev Workflow
1. `mcp_pencil_get_editor_state` → `mcp_pencil_get_guidelines` → `mcp_pencil_batch_get`
2. Create frames — one per screen/state variant
3. Build structure first → fill content zones → screenshot and verify
4. `mcp_pencil_snapshot_layout` with `problemsOnly: true`

**Rules:** Name every frame/layer descriptively. Group in parent frames. Use `fill_container` for responsive. Determine exact node IDs before modifying. One frame per state.

## Output Contract
Provide deliverables appropriate to mode:
1. **UI/UX**: Screen inventory, component inventory, token summary (explicitly detailing Light and Dark variants), interaction/state inventory, responsive notes, strict a11y specs
2. **Brand**: Logo package (all variants), brand guidelines, application examples
3. **Design System**: Token dictionary, component library, pattern library, documentation
4. **Icons**: Icon inventory, grid spec, style guide
5. **Export spec**: Formats, sizes, naming convention

### Game Design Output
1. **HUD layout**: Element placement, safe zones, context-sensitivity rules
2. **Menu flow**: Full menu hierarchy with navigation paths
3. **Art direction guide**: Style, color script, material language, reference images
4. **Feedback spec**: Visual/audio/haptic feedback for each player action
5. **Platform adaptation**: How UI adapts across PC, console, mobile
6. **Accessibility spec**: Colorblind, subtitle, motor accessibility features

**Handoff**: Pass design deliverables to product-develop for coded implementation. For requirements gathering or analysis → route to product-analyze. For testing the implemented design → route to product-quality.
