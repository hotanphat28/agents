---
name: podcast-video-maker
description: Author a "podcast"-style audio-driven kinetic typography video in HyperFrames. Uses a purely motion-graphics timeline (no video tracks) with bilingual subtitles, a robust GSAP dummy-tween timer, and asynchronous-safe synchronous initialization.
---

# Podcast Video Maker

This skill defines the architecture and workflow for building a **Podcast Video** — an audio-driven HyperFrames composition featuring kinetic typography (subtitles that slam/drift in sync with the audio), a running timer, and ambient background visuals, without relying on actual video footage.

## 🏗️ Core Architectural Rules

When authoring a podcast video, you must **strictly** follow these rules to ensure the composition captures correctly in headless preview and rendering engines:

### 1. Synchronous Timeline Registration
Do **NOT** use `window.addEventListener("load")` or `composition-ready` to trigger timeline building. The HyperFrames engine may fire its interception events before the browser completes parsing, causing the timeline registration to silently fail.
*   **Fix:** Build the timeline and execute `window.__timelines["main"] = tl` **synchronously** at the very bottom of your `<script>` tag.
*   **Data Loading:** Ensure all subtitle data is loaded synchronously (e.g., `<script src="captions.js"></script>`). Do **NOT** use `await fetch("captions.json")`, as it defers timeline construction and breaks the engine.

### 2. Robust Timer Implementation (Dummy Tween)
The HyperFrames capture engine scrubs the timeline (`tl.seek()`) rather than letting the global clock tick normally. Relying on an `onUpdate` callback attached directly to the main timeline configuration will fail and leave the timer frozen.
*   **Fix:** Create a dummy object `const timerObj = { t: 0 }` and tween it explicitly on the timeline:
    ```javascript
    tl.to(timerObj, {
      t: duration,
      duration: duration,
      ease: "none",
      onUpdate: () => updateDOM(timerObj.t)
    }, 0);
    ```

### 3. Visibility Animation Ban
Do **NOT** animate `visibility: hidden` to `visible` (in CSS or GSAP `tl.set`). The headless screenshot engine struggles with `visibility` toggles during rapid seeking, causing elements to remain permanently invisible in the final render.
*   **Fix:** Use `opacity: 0` in CSS, and animate/set `opacity: 1` when the element should appear.

### 4. Direct Browser Fallback
Since the `window.__hyperframes` API is only injected by the preview server or CLI renderer, include a fallback block at the end of `initAnimation()`. This ensures the timeline auto-plays if the user opens the HTML file directly in their browser:
```javascript
if (window.self === window.top) { // Not inside an iframe
  window.__timelines["main"].play();
  const aud = document.getElementById('aud-main');
  if (aud) aud.play().catch(e => console.log("Autoplay blocked:", e));
}
```

---

## 📂 Reference Implementation

A perfect reference implementation is provided in the `examples/` directory:
*   `examples/index.html` - The core composition featuring the ambient background, global overlays, timer dummy tween, and synchronous GSAP initialization.
*   `examples/captions.js` - The synchronous global variable assignment pattern for bilingual subtitle data.

---

## 🚀 Execution Workflow

When tasked with building a podcast video, execute the following steps:

1.  **Scaffold**: Initialize a blank HyperFrames project (`npx hyperframes init <name> --example blank`).
2.  **Assets**: Drop the primary audio file into the workspace.
3.  **Data Structure**: Structure the subtitle data as a global `window.CAPTIONS` array inside `captions.js` (and ensure it is loaded synchronously in the HTML).
4.  **Profanity Filter**: Review the `captions.js` text and filter any profanity.
5.  **Build**: Replicate the architectural patterns from `examples/index.html` to build the composition.
6.  **Preview/Render**: Render the video via `npx hyperframes preview` or `npx hyperframes render`.
7.  **Cleanup**: Delete temporary or scaffolded files (e.g., `meta.json`, test scripts, unused images, or downloaded `node_modules` used for debugging).
8.  **Social Media Copy**: Generate highly concise, YouTube-optimized Titles and Descriptions (in both English and Vietnamese) based on the video context for the user to publish.
