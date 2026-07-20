---
name: podcast-video-maker
description: Creates audio-driven kinetic typography videos in HyperFrames — podcast clips, motivational reels, or narration visuals with bilingual subtitles. Uses a motion-graphics-only timeline (no video tracks), GSAP dummy-tween timer, and synchronous initialization. Activate when the user wants a podcast video, audio clip visualization, kinetic typography reel, or subtitle-driven video from an audio file.
---

# Podcast Video Maker

Build audio-driven kinetic typography videos with bilingual subtitles in HyperFrames.

**Stack:** HyperFrames + GSAP (motion-graphics only, no video tracks)

---

## Critical Architecture Rules

These rules prevent silent failures in the HyperFrames headless capture engine:

### Synchronous Timeline Registration

Build the timeline and assign `window.__timelines["main"] = tl` synchronously at the bottom of `<script>`. Do NOT use `window.addEventListener("load")` or `composition-ready` — the engine may fire interception events before parsing completes.

Load subtitle data synchronously via `<script src="captions.js">`. Do NOT use `await fetch()`.

### Dummy Tween Timer

The capture engine scrubs via `tl.seek()`, not real-time clock. An `onUpdate` on the main timeline config will freeze.

Fix: tween a dummy object explicitly:

```javascript
const timerObj = { t: 0 };
tl.to(timerObj, {
  t: duration, duration: duration, ease: "none",
  onUpdate: () => updateDOM(timerObj.t)
}, 0);
```

### Opacity, Not Visibility

Never animate `visibility: hidden → visible`. The headless engine mishandles visibility toggles during rapid seeking.

Fix: use `opacity: 0` in CSS, animate to `opacity: 1` via GSAP.

### Browser Fallback

Add at end of init (for direct browser playback outside HyperFrames):

```javascript
if (window.self === window.top) {
  window.__timelines["main"].play();
  const aud = document.getElementById('aud-main');
  if (aud) aud.play().catch(() => {});
}
```

---

## Reference Implementation

- `examples/index.html` — Full composition (background, overlays, timer, sync init)
- `examples/captions.js` — Global variable pattern for bilingual subtitle data

---

## Workflow

### 1. Scaffold Project

```bash
npx hyperframes init <name> --example blank
cd <name>
```

### 2. Setup Assets and Data

1. Place audio file in workspace (e.g., `assets/audio.mp3`)
2. Structure subtitle data as `window.CAPTIONS` array in `captions.js`:
   - Bilingual (e.g., Vietnamese + English) line-by-line with timestamps
   - Load synchronously in HTML

### 3. Profanity Filter

Review `captions.js` text and censor profanity for social media safety.

### 4. Build Composition

Build `index.html` with kinetic typography and ambient background:
- Apply all architecture rules above
- Load `captions.js` synchronously before timeline script
- Build CSS, layout, and GSAP animations

### 5. Lint and Render

```bash
npx hyperframes@latest lint
npx hyperframes@latest render -o renders/output.mp4 --fps 30 --quality high --crf 18
```

### 6. Generate Social Media Copy

Create YouTube-optimized titles and descriptions (English + Vietnamese) based on content context. Present to user.

### 7. Clean Up

After user approves, remove temp files: `meta.json`, test scripts, unused scaffolded assets, debug `node_modules`.
