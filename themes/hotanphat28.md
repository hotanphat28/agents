# hotanphat28 Theme

> **Shared reference document.** Other skills load this file when they need hotanphat28's brand tokens, visual standards, and theme rules.

---

## Brand Identity

| Attribute | Value |
|-----------|-------|
| Brand name | hotanphat28 |
| Full name | hồ tấn phát |
| Website | hotanphat.com |
| Email | hello@hotanphat.com |
| Social | [X](http://x.com/hotanphat28) · [YouTube](https://youtube.com/@hotanphat28) · [GitHub](https://github.com/hotanphat28) · [LinkedIn](https://linkedin.com/in/hotanphat28/) |

**Tagline variants:**
- VI: "chạm đến sự tối giản"
- EN: "to reach the simplicity"

**Brand personality:** Personal tech brand with premium, minimalist, luxury-meets-tech identity. Dark surfaces, gold accents, monospace data, generous whitespace. Every pixel earns its place.

---

## Color Palette

| Role | Token | Value | Usage |
|---|---|---|---|
| Primary | `--color-gold` | `#FFC90E` | CTAs, key highlights, active states |
| Surface 0 | `--color-black` | `#101010` | Page backgrounds, deepest surface |
| Surface 1 | `--color-surface` | `#1A1A1A` | Cards, panels, elevated surfaces |
| Surface 2 | `--color-surface-raised` | `#222222` | Hover states, nested containers |
| Neutral | `--color-gray` | `#646464` | Secondary text, borders, icons |
| Text Primary | `--color-white` | `#F4F4F4` | Primary text |
| Text Muted | `--color-muted` | `#888888` | Captions, placeholder, disabled |
| Border | `--color-border` | `#2A2A2A` | Dividers, subtle outlines |
| Success | `--status-success` | `#22A861` | Confirmations, positive metrics |
| Success Light | `--status-success-light` | `#0F2A1A` | Success background tint |
| Warning | `--status-warning` | `#E5A00D` | Caution states, pending actions |
| Warning Light | `--status-warning-light` | `#2A2210` | Warning background tint |
| Error | `--status-error` | `#DC3545` | Errors, destructive actions |
| Error Light | `--status-error-light` | `#2A1215` | Error background tint |
| Info | `--status-info` | `#3B82F6` | Informational highlights, links |
| Info Light | `--status-info-light` | `#101E2E` | Info background tint |
| Neutral | `--status-neutral` | `#6B7280` | Neutral/disabled border, muted label |
| Neutral Light | `--status-neutral-light` | `#1E1E1E` | Neutral background tint |

**Color rules:**
- Background is always `#101010` — never white unless asked for a light mode
- Gold (`#FFC90E`) is used *sparingly* — think punctuation, not paintbrush
- Never use pure black `#000000` or pure white `#FFFFFF`
- Borders should be barely visible — `1px solid #2A2A2A` is standard

---

## Typography

| Role | Font | Usage |
|---|---|---|
| Display / Headings | `Space Grotesk` | H1–H4, nav labels, card titles |
| Body / UI labels | `Space Grotesk` | Paragraphs, descriptions, form labels |
| Data / Code / Mono | `Space Mono` | Numbers, metrics, timestamps, code, IDs |

**Type scale (rem-based):**
- Display: 3rem / 700 weight / -0.03em letter-spacing
- H1: 2rem / 700 weight / -0.02em
- H2: 1.5rem / 600 weight / -0.01em
- H3: 1.125rem / 600 weight
- Body: 0.9375rem / 400 weight / 1.6 line-height
- Caption / Label: 0.75rem / 500 weight / 0.04em letter-spacing / uppercase

**Google Fonts:**
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

---

## Spacing System

8pt grid base. All spacing multiples of 8 (or 4 for micro-adjustments).

| Token | Value | Use |
|---|---|---|
| `--space-1` | 4px | Micro: icon gap, tight inline padding |
| `--space-2` | 8px | Small: badge padding, list item gap |
| `--space-3` | 12px | Compact UI: button padding |
| `--space-4` | 16px | Default: card padding, form gap |
| `--space-6` | 24px | Section gap, sidebar padding |
| `--space-8` | 32px | Section header margin |
| `--space-12` | 48px | Large section separation |
| `--space-16` | 64px | Page-level vertical rhythm |
| `--space-24` | 96px | Hero sections, generous breathing room |

---

## Component Theming

Theme-specific color values for standard components. See design/dev skills for component patterns and anatomy.

### Buttons

| Variant | Background | Color | Border | Hover |
|---------|-----------|-------|--------|-------|
| Primary | `#FFC90E` | `#101010` | none | bg `#D4A800` |
| Secondary | transparent | `#FFC90E` | `1px solid #FFC90E` | — |
| Ghost | transparent | `#F4F4F4` | none | — |
| Danger | transparent | `#DC3545` | `1px solid #DC3545` | — |

**Rule:** One primary button per primary action per view.

### Inputs

| State | Border | Background | Color |
|-------|--------|-----------|-------|
| Default | `1px solid #2A2A2A` | `#1A1A1A` | `#F4F4F4` |
| Focus | `1px solid #FFC90E` | `#1A1A1A` | `#F4F4F4` |
| Disabled | `1px solid #2A2A2A` | `#222222` | `#888888` |
| Invalid | `1px solid #DC3545` | `#1A1A1A` | `#F4F4F4` |

Label: `#F4F4F4` — Placeholder: `#888888`

### Cards

| Token | Value |
|---|---|
| Background | `#1A1A1A` |
| Border | `1px solid #2A2A2A` |
| Border radius | `12px` |
| Padding | `24px` |
| Top highlight (optional) | `1px solid rgba(255,255,255,0.06)` |

### Tables

| Part | Background | Color | Border |
|------|-----------|-------|--------|
| Header | `#222222` | `#F4F4F4` | — |
| Row | `#1A1A1A` | `#F4F4F4` | bottom `1px solid #2A2A2A` |
| Row hover | `#222222` | — | — |
| Zebra (even) | `#1E1E1E` | — | — |

### Navigation

| Element | Value |
|---------|-------|
| Sidebar bg | `#1A1A1A` |
| Item text | `#F4F4F4` |
| Active item | `#FFC90E` |
| Tab inactive | `#888888` |
| Tab active | `#FFC90E`, border-bottom `2px solid #FFC90E` |
| Breadcrumb | `#888888`, active `#FFC90E` |

### Other

| Component | Token | Value |
|-----------|-------|-------|
| Modal overlay | background | `rgba(0,0,0,0.6)` |
| Modal container | background | `#1A1A1A`, border `1px solid #2A2A2A` |
| Tooltip | bg / text | `#222222` / `#F4F4F4` |
| Status notifier | bg / border | `--status-*-light` / `1px solid --status-*` |

---

## Data Visualization

| Element | Value |
|---------|-------|
| Chart background | `#1A1A1A` |
| Grid lines | `1px solid #2A2A2A` |
| Primary series | `#FFC90E` (gold) |
| Secondary series | `#888888` |
| Tertiary+ | `#3B82F6`, `#22A861`, `#DC3545` |
| Axis labels | `Space Mono`, 11px, `#646464` |
| Tooltips | dark panel, `#F4F4F4` text, 1px gold left border |

Always include chart title and axis labels.

---

## Screen Patterns

| Screen | Background | Description |
|--------|-----------|-------------|
| Home / Portfolio | `#101010` | Full-page dark surface. Hero with gold accent headline, Space Grotesk display type, minimal CTA. Scroll reveals project cards on `#1A1A1A` surfaces. |
| Dashboard | Sidebar `#1A1A1A` / Content `#101010` | App shell with sidebar nav, gold active state. Content cards on `#1A1A1A`. |
| Blog / Article | `#101010` | Dark reading surface. `#F4F4F4` body text, `#FFC90E` accent for links/highlights, `Space Mono` for code blocks. |
| Login / Auth | `#101010` | Centered card on `#1A1A1A`. Gold primary CTA, minimal fields. Logo above form. |
| Settings / Profile | `#101010` | Sectioned form layout. Cards on `#1A1A1A` with `#2A2A2A` dividers. |

---

## Default Patterns

| Pattern | Value |
|---------|-------|
| Icons | Lucide (`lucide lucide-{name}`) |
| Border radius | `8px` small elements, `12px` cards/panels, `16px` modals/drawers, `9999px` pills/tags |
| Shadows | Avoid drop shadows — use `1px solid #2A2A2A` + subtle inner glow |
| Motion | `150ms ease` micro, `250ms ease` panels, `350ms ease` page-level |
| Glassmorphism | `background: rgba(26,26,26,0.8); backdrop-filter: blur(12px)` — overlays on image backgrounds |
| Skeleton loading | `#2A2A2A` base with `#333333` shimmer |

---

## Logo

The hotanphat28 logo is a golden circular emblem mark alongside "hồ tấn phát" in lowercase.

| Variant | Usage | URL |
|---------|-------|-----|
| Golden logo (full) | Light or dark surfaces | `https://hotanphat.com/wp-content/uploads/2026/01/20251017_logo_hotanphat28_golden.png` |
| Favicon (32×32) | Browser tab | `https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-32x32.png` |
| Favicon (192×192) | Android/PWA | `https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-192x192.png` |
| Apple Touch Icon | iOS home screen | `https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-180x180.png` |

**Logo rules:**
- Gold (`#FFC90E`) palette — naturally belongs on dark surfaces
- On light surfaces, the gold mark still works — do not invert
- Scale proportionally — never distort
- Minimum clear space: height of circular mark on all sides

---

## Favicon & OG Image

```html
<link rel="icon" href="https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-32x32.png" sizes="32x32">
<link rel="icon" href="https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-192x192.png" sizes="192x192">
<link rel="apple-touch-icon" href="https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-180x180.png">
```

---

## Template Token Mapping

### CSS Custom Properties

| Contract Token | Value |
|---|---|
| `--primary` | `#FFC90E` |
| `--primary-dark` | `#D4A800` |
| `--primary-pale` | `#3A3520` |
| `--bg-dark` | `#101010` |
| `--bg-dark-mid` | `#1A1A1A` |
| `--bg-dark-deep` | `#080808` |
| `--bg-warm` | `#1A1A1A` |
| `--accent` | `#FFC90E` |
| `--font-display` | `'Space Grotesk', sans-serif` |
| `--font-body` | `'Space Grotesk', sans-serif` |
| `--font-mono` | `'Space Mono', monospace` |
| `--primary-glow` | `rgba(255, 201, 14, .10)` |
| `--primary-chip-bg` | `rgba(255, 201, 14, .16)` |
| `--primary-chip-border` | `rgba(255, 201, 14, .28)` |
| `--dark-shadow-xs` | `rgba(16, 16, 16, .04)` |
| `--dark-shadow-sm` | `rgba(16, 16, 16, .05)` |
| `--dark-shadow-md` | `rgba(16, 16, 16, .07)` |
| `--dark-shadow-lg` | `rgba(16, 16, 16, .22)` |

### HTML Template Variables

| Variable | Value |
|---|---|
| `{{FAVICON_URL}}` | `https://hotanphat.com/wp-content/uploads/2026/01/cropped-20251017_logo_hotanphat28_golden-32x32.png` |
| `{{FONT_IMPORT_URL}}` | `https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap` |
| `{{ICON_CDN_URL}}` | `https://unpkg.com/lucide-static@latest/font/lucide.min.css` |
| `{{BRAND_MARK}}` | `HP` |
| `{{BRAND_NAME}}` | `hotanphat28` |
| `{{BRAND_SUFFIX}}` | ` ` |
| `{{TITLE_SUFFIX}}` | `hotanphat28` |
| `{{LOGO_TEXT}}` | `hồ tấn phát` |

---

## Brand Voice & Tone

**Personality:** Minimalist, intentional, premium. Every word earns its place — like every pixel.

**Tone:** Quiet confidence. Technical but accessible. Concise, never verbose. Think: the calm expert who doesn't need to prove themselves.

---

## Theme Extras

No additional theme-specific assets.

---

## Quick Reference

```
Fonts:         Space Grotesk (headings + body) / Space Mono (data)
Primary color: #FFC90E  (Gold)
Primary hover: #D4A800
Surface bg:    #101010  (Near-black)
Card bg:       #1A1A1A
Raised bg:     #222222
Text primary:  #F4F4F4
Text muted:    #888888
Border:        #2A2A2A
```
