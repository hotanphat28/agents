---
brand:
  name: "hotanphat28"
  full_name: "hồ tấn phát"
  tagline: "chạm đến sự tối giản"
colors:
  primary: "#FFC90E"
  primary_dark: "#D4A800"
  primary_pale: "#3A3520"
  bg_dark: "#101010"
  bg_dark_mid: "#1A1A1A"
  bg_dark_deep: "#080808"
  bg_warm: "#1A1A1A"
  surface_0: "#101010"
  surface_1: "#1A1A1A"
  surface_2: "#222222"
  neutral_gray: "#646464"
  text_primary: "#F4F4F4"
  text_muted: "#888888"
  border: "#2A2A2A"
  success: "#22A861"
  success_light: "#0F2A1A"
  warning: "#E5A00D"
  warning_light: "#2A2210"
  error: "#DC3545"
  error_light: "#2A1215"
  info: "#3B82F6"
  info_light: "#101E2E"
typography:
  display: "Space Grotesk, sans-serif"
  body: "Space Grotesk, sans-serif"
  mono: "Space Mono, monospace"
spacing:
  space_1: "4px"
  space_2: "8px"
  space_3: "12px"
  space_4: "16px"
  space_6: "24px"
  space_8: "32px"
  space_12: "48px"
  space_16: "64px"
  space_24: "96px"
layout:
  mobile: "320px"
  tablet: "768px"
  desktop: "1024px"
  max_width: "1200px"
---

# hotanphat28 Design System Specification

> **Source of Truth:** This `DESIGN.md` file acts as the primary constraint engine for the hotanphat28 brand. AI tools and developers must strictly adhere to these rules.

## 1. Brand Identity & Overview
**Brand Personality:** Minimalist, intentional, premium, luxury-meets-tech. 
Every pixel earns its place. The brand relies on dark surfaces, gold accents, monospace data, and generous whitespace. 
**Tone:** Quiet confidence. Technical but accessible. Concise, never verbose.

## 2. Core Constraints (Do's & Don'ts)

These constraints are **critical rules** to prevent hallucinations or generic design choices. 
AI code generation must follow these without exception:

> [!CAUTION]
> - **Shadows:** NEVER use drop shadows or blur shadows on text or cards. Use the defined borders (`1px solid #2A2A2A`) and subtle inner glows instead.
> - **Colors:** NEVER use pure black (`#000000`) or pure white (`#FFFFFF`). Strictly use the defined surface (`#101010`) and text (`#F4F4F4`) tokens.
> - **Semantic Colors:** NEVER introduce new semantic colors outside the defined palette. If you need a "success" or "error" state, rely exclusively on the predefined status tokens.
> - **Typography:** NEVER use generic fonts like Arial, Roboto, or Inter. Always stick to `Space Grotesk` (for headings/body) and `Space Mono` (for data/code).
> - **Radii:** NEVER use ad-hoc border radii. Stick strictly to the defined scales: `8px` (small), `12px` (cards), `16px` (modals), or `9999px` (pills).

## 3. Layout & Grid System

The design uses an 8pt base grid for spacing.
- **Micro adjustments:** Use multiples of 4px.
- **Standard multiples:** 8px, 16px, 24px, 32px, 48px, 64px, 96px.

### Responsive Breakpoints
- **Mobile:** `320px` and above
- **Tablet:** `768px` and above
- **Desktop:** `1024px` and above
- **Container Max-Width:** `1200px` (Containers should be horizontally centered on larger screens).

## 4. Accessibility & Focus States

Accessibility is non-negotiable. 
- **Focus Rings:** For keyboard navigation, all interactive elements (buttons, links, form fields) MUST display a `2px solid #FFC90E` (Gold) outline with a `2px` offset. 
- Do not rely on default browser focus rings.

## 5. Color Guidelines

The background is *always* `#101010`. It is a dark-mode first design system.

- **Primary Action (Gold - `#FFC90E`):** Used sparingly. Think punctuation, not a paintbrush. Used for primary CTAs, active states, and key highlights.
- **Surface Elevation:**
  - `Surface 0 (#101010)`: Deepest background.
  - `Surface 1 (#1A1A1A)`: Elevated cards and panels.
  - `Surface 2 (#222222)`: Hover states and nested containers.
- **Borders:** Borders should be barely visible (`1px solid #2A2A2A`).

## 6. Typography Scale (Rem-based)
- **Display:** 3rem / 700 weight / -0.03em letter-spacing
- **H1:** 2rem / 700 weight / -0.02em
- **H2:** 1.5rem / 600 weight / -0.01em
- **H3:** 1.125rem / 600 weight
- **Body:** 0.9375rem / 400 weight / 1.6 line-height
- **Caption / Label:** 0.75rem / 500 weight / 0.04em letter-spacing / uppercase

## 7. Component Rules

### Buttons
- **Primary:** Background `#FFC90E`, Text `#101010`, No Border. Hover: `#D4A800`. *(Rule: One primary button per view)*.
- **Secondary:** Transparent Background, Text `#FFC90E`, Border `1px solid #FFC90E`.
- **Ghost:** Transparent Background, Text `#F4F4F4`, No Border.

### Inputs
- **Default:** Background `#1A1A1A`, Border `1px solid #2A2A2A`, Text `#F4F4F4`, Placeholder `#888888`.
- **Focus:** Background `#1A1A1A`, Border `1px solid #FFC90E`.

### Cards
- **Structure:** Background `#1A1A1A`, Border `1px solid #2A2A2A`, Border radius `12px`, Padding `24px`.
- **Highlight (Optional):** Top highlight using `1px solid rgba(255,255,255,0.06)`.

### Navigation
- **Sidebar:** Background `#1A1A1A`.
- **Active Tab/Item:** Text `#FFC90E` (Gold). Active tabs include a `2px solid #FFC90E` bottom border.

## 8. Data Visualization
- **Backgrounds:** `#1A1A1A`
- **Grid Lines:** `1px solid #2A2A2A`
- **Primary Series:** `#FFC90E`
- **Axis Labels:** `Space Mono`, 11px, `#646464`
- **Tooltips:** Dark panel, `#F4F4F4` text, 1px gold left border.

## 9. Default Patterns & Assets
- **Icons:** Lucide icons (`lucide lucide-{name}`).
- **Motion:** `150ms ease` for micro-interactions, `250ms ease` for panels, `350ms ease` for page-level transitions.
- **Glassmorphism:** `background: rgba(26,26,26,0.8); backdrop-filter: blur(12px)` — strictly for overlays on image backgrounds.
- **Logo Usage:** Never invert the golden logo mark. Scale proportionally without distortion. Minimum clear space equals the height of the circular mark.

## 10. Brand Identity & Contact
| Attribute | Value |
|-----------|-------|
| Website | hotanphat.com |
| Email | hello@hotanphat.com |
| Social | [X](http://x.com/hotanphat28) · [YouTube](https://youtube.com/@hotanphat28) · [TikTok](https://tiktok.com/@hotanphat28) · [GitHub](https://github.com/hotanphat28) · [LinkedIn](https://linkedin.com/in/hotanphat28/) · [Pexels](https://www.pexels.com/@hotanphat28) |

## 11. Typography Assets
### Google Fonts
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

## 12. Extended Component Theming

### Tables
| Part | Background | Color | Border |
|------|-----------|-------|--------|
| Header | `#222222` | `#F4F4F4` | — |
| Row | `#1A1A1A` | `#F4F4F4` | bottom `1px solid #2A2A2A` |
| Row hover | `#222222` | — | — |
| Zebra (even) | `#1E1E1E` | — | — |

### Other
| Component | Token | Value |
|-----------|-------|-------|
| Modal overlay | background | `rgba(0,0,0,0.6)` |
| Modal container | background | `#1A1A1A`, border `1px solid #2A2A2A` |
| Tooltip | bg / text | `#222222` / `#F4F4F4` |
| Status notifier | bg / border | `--status-*-light` / `1px solid --status-*` |

## 13. Screen Patterns
| Screen | Background | Description |
|--------|-----------|-------------|
| Home / Portfolio | `#101010` | Full-page dark surface. Hero with gold accent headline, Space Grotesk display type, minimal CTA. Scroll reveals project cards on `#1A1A1A` surfaces. |
| Dashboard | Sidebar `#1A1A1A` / Content `#101010` | App shell with sidebar nav, gold active state. Content cards on `#1A1A1A`. |
| Blog / Article | `#101010` | Dark reading surface. `#F4F4F4` body text, `#FFC90E` accent for links/highlights, `Space Mono` for code blocks. |
| Login / Auth | `#101010` | Centered card on `#1A1A1A`. Gold primary CTA, minimal fields. Logo above form. |
| Settings / Profile | `#101010` | Sectioned form layout. Cards on `#1A1A1A` with `#2A2A2A` dividers. |

## 14. Logo & Favicon
The hotanphat28 logo is a golden circular emblem mark alongside "hồ tấn phát" in lowercase.

| Variant | Usage | URL |
|---------|-------|-----|
| Golden logo (full) | Light or dark surfaces, favicon, all sizes | `https://hotanphat.com/assets/images/logo/20251017_logo_hotanphat28_golden.png` |

```html
<link rel="icon" href="https://hotanphat.com/assets/images/logo/20251017_logo_hotanphat28_golden.png" type="image/png">
```

## 15. Template Token Mapping

### HTML Template Variables
| Variable | Value |
|---|---|
| `{{FAVICON_URL}}` | `https://hotanphat.com/assets/images/logo/20251017_logo_hotanphat28_golden.png` |
| `{{FONT_IMPORT_URL}}` | `https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap` |
| `{{ICON_CDN_URL}}` | `https://unpkg.com/lucide-static@latest/font/lucide.min.css` |
| `{{BRAND_MARK}}` | `HP` |
| `{{BRAND_NAME}}` | `hotanphat28` |
| `{{BRAND_SUFFIX}}` | ` ` |
| `{{TITLE_SUFFIX}}` | `hotanphat28` |
| `{{LOGO_TEXT}}` | `hồ tấn phát` |

## 16. Brand Voice & Tone
Minimalist, intentional, premium, every word earns its place, like every pixel. Quiet confidence. Technical but accessible. Concise, never verbose. Think: the calm expert who doesn't need to prove themselves.

## 17. Quick Reference
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
