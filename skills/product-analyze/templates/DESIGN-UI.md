# Design-Quality UI — CSS Implementation Contract
How to render theme tokens to CSS variables and apply them to components.

## Token Flow
```
Brand Theme File -> CSS Variables (:root) -> Component Styles -> Rendered UI
```

## CSS Variable Mapping
Load theme from `~/.agents/themes/` or `~/.claude/themes/` and map to `:root`:

```css
:root {
  --primary: /* from theme */;
  --primary-dark: /* from theme */;
  --primary-pale: /* from theme */;
  --bg-dark: /* from theme */;
  --bg-dark-mid: /* from theme */;
  --bg-dark-deep: /* from theme */;
  --bg-warm: /* from theme */;
  --accent: /* from theme */;
  --font-display: /* from theme */;
  --font-body: /* from theme */;
  --font-mono: /* from theme */;
}
```

## Derived Values (Compute at Build/Runtime)
```css
--primary-glow: rgba(PRIMARY, .10);
--primary-chip-bg: rgba(PRIMARY, .16);
--primary-chip-border: rgba(PRIMARY, .28);
--primary-hover: /* 10% darker than --primary */
--primary-active: /* 15% darker than --primary */
--dark-shadow-xs: rgba(BG_DARK, .04);
--dark-shadow-sm: rgba(BG_DARK, .05);
--dark-shadow-md: rgba(BG_DARK, .07);
--dark-shadow-lg: rgba(BG_DARK, .22);
```

## Status Colors (Universal — Never Override)
`--status-success` #22A861, `--status-warning` #E5A00D, `--status-error` #DC3545, `--status-info` #3B82F6, `--status-neutral` #6B7280.

## Akkuro App Layout Wiring
For Akkuro apps, load matching layout from `~/.claude/templates/akkuro-app-layouts/` and apply akkuro theme variables. Design system details in `~/.claude/themes/akkuro-design-systems/`.

## Key Rules
* Use `font-display: swap` for Google Fonts
* System font fallback: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
* 4px spacing base unit
* Respect `prefers-reduced-motion` for all animations
* Dark mode: use `prefers-color-scheme` media query or `.dark` class toggle
