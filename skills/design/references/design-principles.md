# Design Principles & Theory

Core foundations, fundamentals, and best practices that every design decision should be grounded in.

---

## 1. Visual Hierarchy

### The Hierarchy Stack (strongest → weakest)
1. **Size & scale** — largest elements read first
2. **Color & contrast** — high-contrast elements demand attention
3. **Position** — top-left (LTR) or center dominates
4. **Typography weight** — bold before regular
5. **Whitespace** — isolated elements feel more important
6. **Depth** — elevated elements (shadows) appear closer/more urgent

### Typography Hierarchy

| Level | Use | Sizing Rule |
|---|---|---|
| Display | Hero headlines, landing pages | 48–72px (3–4.5rem) |
| H1 | Page title | 32–40px (2–2.5rem) |
| H2 | Section headers | 24–28px (1.5–1.75rem) |
| H3 | Subsection headers | 20–22px (1.25–1.375rem) |
| H4 | Card titles, group labels | 16–18px (1–1.125rem) |
| Body | Primary content | 16px (1rem) — the anchor |
| Small | Captions, metadata, hints | 12–14px (0.75–0.875rem) |

**Scale ratios:**
- Minor third (1.2) — compact UIs, data-heavy dashboards
- Major third (1.25) — balanced, most apps
- Perfect fourth (1.333) — editorial, marketing pages
- Golden ratio (1.618) — dramatic, hero-heavy pages

**Line height:** Body 1.5–1.6, headings 1.1–1.3. Tighter for large text, looser for small.

**Measure (line length):** 45–75 characters for body text. Never exceed 80ch.

---

## 2. Spacing System

### 8pt Grid (Base Unit)
All spacing derives from an 8px base. Use multiples: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.

| Token | Value | Use |
|---|---|---|
| `--space-xs` | 4px | Inline gaps, icon padding |
| `--space-sm` | 8px | Tight element spacing |
| `--space-md` | 16px | Default component padding |
| `--space-lg` | 24px | Section padding, card padding |
| `--space-xl` | 32px | Group separation |
| `--space-2xl` | 48px | Major section separation |
| `--space-3xl` | 64px | Page section separation |
| `--space-4xl` | 96px | Hero padding, landing sections |

### Spacing Principles
- **Proximity = relationship** — elements closer together are perceived as related
- **Consistent rhythm** — use the same spacing token for the same relationship type
- **Outer > inner** — container padding should always exceed internal element gaps
- **Breathing room scales with viewport** — larger screens need proportionally more space

---

## 3. Color Theory

### Color Relationships
| Harmony | Definition | Use Case |
|---|---|---|
| Monochromatic | One hue, varying lightness/saturation | Elegant, focused UIs |
| Complementary | Opposite on color wheel | High contrast CTAs against backgrounds |
| Analogous | Adjacent hues | Harmonious, nature-inspired palettes |
| Split-complementary | One hue + two adjacent to its complement | Vibrant but balanced |
| Triadic | Three equidistant hues | Playful, diverse UIs |

### Color in UI — Functional Roles
| Role | Purpose | Rule |
|---|---|---|
| Primary | Brand identity, key actions | Max 10% of surface area |
| Secondary | Supporting elements, secondary actions | Complements primary |
| Neutral | Backgrounds, borders, text | 60-70% of the interface |
| Semantic | Status communication | Red=error, amber=warning, green=success, blue=info |
| Surface | Layered backgrounds | Use elevation (lighten/darken) to show depth |

### Contrast Requirements (WCAG 2.2 AA)
| Element | Minimum Ratio |
|---|---|
| Normal text (< 24px) | 4.5:1 |
| Large text (≥ 24px or 19px bold) | 3:1 |
| UI components & graphical objects | 3:1 |
| Focus indicators | 3:1 against adjacent colors |

### Dark Mode Color Principles
- Don't simply invert — remap surfaces to dark neutrals (not pure black)
- Reduce saturation of colors by 10-20% to avoid vibration on dark backgrounds
- Elevation = lighter (not darker) on dark backgrounds
- Test all semantic colors on dark surfaces for contrast compliance
- Use `oklch()` or `hsl()` for predictable color manipulation

---

## 4. Gestalt Principles

| Principle | Definition | UI Application |
|---|---|---|
| **Proximity** | Close elements are perceived as grouped | Form field + label spacing, card content grouping |
| **Similarity** | Similar elements are perceived as related | Consistent button styles, icon families, tag colors |
| **Closure** | Mind completes incomplete shapes | Progress indicators, implied containers, cropped images |
| **Continuity** | Eye follows smooth paths | Navigation flows, timeline layouts, step indicators |
| **Figure/Ground** | Elements are perceived as foreground or background | Modal overlays, elevated cards, selected states |
| **Common Region** | Elements within a boundary are grouped | Cards, panels, fieldsets, well backgrounds |
| **Uniform Connectedness** | Connected elements are related | Lines between flowchart steps, breadcrumb separators |

### Application Rules
- Use proximity BEFORE borders — if spacing communicates the grouping, you don't need a line
- Limit similarity variations — max 3 visual levels for any element type
- Leverage figure/ground for focus — dim background when presenting modal content
- Don't fight continuity — if users scan left-to-right, don't break the flow

---

## 5. Interaction Design Heuristics

### Nielsen's 10 Usability Heuristics (Applied)

| # | Heuristic | Design Checkpoint |
|---|---|---|
| 1 | **Visibility of system status** | Loading states, progress bars, save confirmations, real-time validation |
| 2 | **Match real world** | Use domain language, natural metaphors, familiar patterns |
| 3 | **User control & freedom** | Undo, back, cancel, close, escape routes always available |
| 4 | **Consistency & standards** | Same action = same appearance across the product |
| 5 | **Error prevention** | Constraints, confirmations for destructive actions, smart defaults |
| 6 | **Recognition over recall** | Visible options, recent items, autocomplete, contextual help |
| 7 | **Flexibility & efficiency** | Shortcuts for experts, progressive disclosure for novices |
| 8 | **Aesthetic & minimalist** | Every element competes for attention — remove the unnecessary |
| 9 | **Help users recover from errors** | Clear error messages with cause + solution, inline validation |
| 10 | **Help & documentation** | Contextual tooltips, onboarding, searchable help |

### Fitts's Law
**Time to target = f(distance / size)**
- Make primary actions large and close to the cursor's natural position
- Place destructive actions far from constructive ones
- Touch targets: minimum 44×44px (mobile), 32×32px (desktop)
- Place frequent actions at screen edges/corners (infinite target area)

### Hick's Law
**Decision time increases with number of choices**
- Limit options to 5-7 per group (chunk if more)
- Progressive disclosure: show basics first, reveal advanced on demand
- Highlight the recommended option to reduce decision paralysis
- Use categorization to reduce perceived complexity

### Jakob's Law
**Users spend most time on OTHER sites** — they expect your product to work like ones they already know.
- Follow platform conventions (tabs, navigation, form patterns)
- Innovate on content and value, not on interaction paradigms
- When deviating from convention, the benefit must be overwhelming and obvious

---

## 6. Responsive Design Strategy

### Breakpoint System

| Name | Min-width | Target |
|---|---|---|
| `xs` | 0 | Mobile portrait (320–479px) |
| `sm` | 480px | Mobile landscape / large phones |
| `md` | 768px | Tablets portrait |
| `lg` | 1024px | Tablets landscape / small laptops |
| `xl` | 1280px | Desktops |
| `2xl` | 1536px | Large desktops / ultrawide |

### Mobile-First Principles
1. **Design for constraints first** — mobile forces prioritization
2. **Content priority** — what matters most when space is scarce?
3. **Touch-first interactions** — 44px minimum targets, swipe-friendly
4. **Progressive enhancement** — add complexity with screen real estate
5. **Performance budget** — mobile users have slower connections

### Layout Strategies by Breakpoint
| Pattern | Mobile | Tablet | Desktop |
|---|---|---|---|
| Navigation | Bottom bar or hamburger | Side rail or top bar | Full sidebar or top nav |
| Grid | 1 column | 2 columns | 3-4 columns |
| Data tables | Card view or horizontal scroll | Condensed table | Full table |
| Forms | Stacked, full-width | 2-column for related fields | Multi-column with sidebar help |
| Modals | Full-screen sheet | Centered modal | Centered modal or slide-over |

### Container Queries (Modern Approach)
- Prefer container queries over media queries for components
- Components should be viewport-agnostic — they respond to their container
- Media queries for page layout; container queries for component layout

---

## 7. Accessibility Beyond Compliance

### The Four Principles (POUR)
| Principle | Meaning | Key Checks |
|---|---|---|
| **Perceivable** | Users can perceive content | Alt text, captions, sufficient contrast, scalable text |
| **Operable** | Users can interact | Keyboard navigable, no time limits, no seizure triggers |
| **Understandable** | Users can comprehend | Clear language, predictable behavior, error guidance |
| **Robust** | Works with assistive tech | Valid HTML, ARIA landmarks, tested with screen readers |

### Keyboard Navigation Pattern
- **Tab order** follows visual layout (top-to-bottom, left-to-right)
- **Focus indicators** are visible and have 3:1 contrast
- **Skip links** for repetitive navigation
- **Focus trapping** inside modals (tab cycles within, Escape closes)
- **Arrow keys** for widget navigation (tabs, menus, radio groups)
- **Enter/Space** for activation (buttons, links, toggles)

### ARIA Usage Rules
1. **Don't use ARIA if native HTML works** — `<button>` over `<div role="button">`
2. **Every ARIA role must have proper keyboard support** — role without behavior is worse than no role
3. **Use landmarks** — `<nav>`, `<main>`, `<aside>`, `<header>`, `<footer>`
4. **Live regions** for dynamic content — `aria-live="polite"` for non-urgent updates
5. **Label all interactive elements** — `aria-label`, `aria-labelledby`, or visible `<label>`

### Inclusive Design Patterns
- **Color is never the only indicator** — add icons, text, or patterns
- **Motion**: respect `prefers-reduced-motion` — provide static alternatives
- **Text resizing**: UI must work at 200% zoom without horizontal scrolling
- **Touch targets**: 44×44px minimum with 8px gap between targets
- **Error messages**: identify the field, describe the problem, suggest the fix

---

## 8. Component Design Principles

### Atomic Design Hierarchy
| Level | Examples | Reuse |
|---|---|---|
| Tokens | Colors, spacing, typography, shadows | Universal |
| Atoms | Button, input, label, icon, badge | Anywhere |
| Molecules | Form field (label + input + error), search bar | In context |
| Organisms | Navigation, card grid, form section | Page-level |
| Templates | Page layouts, dashboard shells | App-level |
| Pages | Assembled, populated views | Unique |

### State Design Checklist
Every interactive component must define:
- [ ] **Default** — resting state
- [ ] **Hover** — cursor interaction hint
- [ ] **Focus** — keyboard navigation indicator
- [ ] **Active/Pressed** — during interaction
- [ ] **Disabled** — unavailable (explain why)
- [ ] **Loading** — processing state
- [ ] **Error** — validation failure
- [ ] **Empty** — no content state
- [ ] **Skeleton** — loading placeholder

### Design Token Architecture
```
Global tokens → Alias tokens → Component tokens
(--blue-500)   (--color-primary)  (--button-bg)
```
- Global: raw values (colors, sizes, shadows)
- Alias: semantic meaning (primary, surface, border)
- Component: scoped application (button-bg, card-shadow)

---

## 9. Design Critique Methodology

### The STAR Framework for Design Feedback
| Step | Question |
|---|---|
| **S**ituation | What's the context? Who is the user? What's the goal? |
| **T**ask | What specific design problem is being solved? |
| **A**ction | What decisions were made and why? |
| **R**esult | Does it achieve the goal? What evidence supports this? |

### Critique Protocol
1. **Clarify intent** — "What were you trying to achieve with this?"
2. **Evaluate against principles** — Does it satisfy hierarchy, contrast, consistency?
3. **User lens** — Would the target user understand this without explanation?
4. **Edge cases** — How does this handle long text, empty states, errors, i18n?
5. **Suggest, don't prescribe** — "Have you considered..." over "You should..."

### Quality Gate (Pre-Handoff)
- [ ] Hierarchy is clear at arm's length (squint test)
- [ ] Spacing is consistent and uses the grid
- [ ] Colors pass contrast checks
- [ ] All interactive states are designed
- [ ] Responsive behavior is defined
- [ ] Accessibility annotations are present
- [ ] Edge cases (empty, error, loading, overflow) are handled
- [ ] Design is achievable with current tech constraints
