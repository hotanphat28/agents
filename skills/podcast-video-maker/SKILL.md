---
name: podcast-video-maker
description: Author a "podcast"-style audio-driven kinetic typography video in HyperFrames. Uses a purely motion-graphics timeline (no video tracks) with bilingual subtitles, a robust GSAP dummy-tween timer, and asynchronous-safe synchronous initialization.
disable-model-invocation: true
---

# Podcast Video Maker
This skill defines the architecture and workflow for building a **Podcast Video** — an audio-driven HyperFrames composition featuring kinetic typography (subtitles that slam/drift in sync with the audio), a running timer, and ambient background visuals, without relying on actual video footage.

## IMPORTANT: Bypass Planning Mode
When invoked to build or modify a podcast video, execute the task directly. Build the composition and present the final walkthrough directly without waiting for user approval.

## Core Architectural Rules
Follow these rules to ensure the composition captures correctly in headless preview and rendering engines:

### Video Dimensions
You must **always** build the video as a **long-form horizontal video (1920x1080)**. Do not generate vertical (9:16) podcast clips. Set the root composition dimensions to `1920x1080` (e.g., `width: 1920px; height: 1080px;` and `data-width="1920" data-height="1080"`).

### Synchronous Timeline
Build the timeline and execute `window.__timelines["main"] = tl` **synchronously** at the very bottom of your `<script>` tag. The HyperFrames engine fires its interception events quickly; async triggers will cause the timeline registration to silently fail. Load all subtitle data synchronously (e.g., `<script src="captions.js"></script>`). Rely on synchronous loading instead of deferred construction like `await fetch()`.

### Dummy Tween Timer
The HyperFrames capture engine scrubs the timeline (`tl.seek()`) rather than letting the global clock tick normally. An `onUpdate` callback attached directly to the main timeline configuration will leave the timer frozen. Create a dummy object `const timerObj = { t: 0 }` and tween it explicitly on the timeline:

```javascript
tl.to(timerObj, {
  t: duration,
  duration: duration,
  ease: "none",
  onUpdate: () => updateDOM(timerObj.t)
}, 0);
```

### Safe Kinetic Timings
Standard fixed durations (like `0.4s` enter) will cause negative durations or overlapping GSAP tweens when animating short chunks of text. Calculate safe durations based on the chunk's actual duration:
```javascript
const enterDur = Math.min(0.4, duration * 0.4);
const exitDur = Math.min(0.2, duration * 0.2);
const driftDur = duration - enterDur - exitDur;
```

### Opacity for Visibility
Use `opacity: 0` to hide elements, and animate/set `opacity: 1` when they should appear. The headless screenshot engine struggles with visibility toggles during rapid seeking.

### Direct Browser Fallback
Since the `window.__hyperframes` API is only injected by the preview server or CLI renderer, include a fallback block at the end of `initAnimation()` to ensure the timeline auto-plays if the user opens the HTML file directly in their browser:

```javascript
if (window.self === window.top) { // Not inside an iframe
  window.__timelines["main"].play();
  const aud = document.getElementById('aud-main');
  if (aud) aud.play().catch(e => console.log("Autoplay blocked:", e));
}
```

## Execution Workflow
When tasked with building a podcast video, execute the following steps precisely:

### Step 1: Scaffold Project
Run `npx hyperframes init <name> --example blank` to set up the base project directory. Navigate into it.

### Step 2: Setup Assets and Data
1. Ensure the primary audio file is placed in the workspace (e.g., `assets/audio.mp3`).
2. Transcribe the audio and group the output into **full sentences** rather than short chunks to make translation checking easier.
3. Identify the main language of the audio (support is limited to English and Vietnamese). Transcribe the main language first, then translate the captions to the other language. Ensure translations are natural and contextual.
4. Structure the subtitle data as a global `window.CAPTIONS` array in `captions.js`, using explicit keys for both languages:
```javascript
window.CAPTIONS = [
  { textEN: "Hello world", textVN: "Chào thế giới", duration: 2.5 },
  // ...
];
```
5. Load `captions.js` synchronously in the HTML.

### Step 3: Profanity Filter
Review the `captions.js` text and censor any profanity to ensure the content is safe for social media publishing.

### Step 4: Build Composition
Build the kinetic typography and ambient background in `index.html`, ensuring it perfectly matches the established podcast brand aesthetic.

1. **Fonts & Background:** Use `Space Grotesk` and `Space Mono` fonts. Set the background to dark `#101010` and include a subtle yellow radial glow (`.ambient-glow`) alongside an animated noise grid (`.ambient-noise`).
2. **Global Overlays:** Include a top `.metadata-bar` containing `[ REC ]`, the episode title (e.g., `EP.09 — TITLE`), and a tabular monospace timer (`00:00:00:00`). Include the `.podcast-logo` (`hồ tấn phát` with a yellow circle) in the bottom right corner.
3. **Styling Bilingual Captions:** Vietnamese text must be styled as large, bold, uppercase, and golden (`#FFC90E`) using `Space Grotesk`. English text must be smaller, monospace, uppercase, and muted white (`#A0A0A0`) using `Space Mono`.
4. **GSAP Animations:** Captions should enter using a "Kinetic Slam" animation (e.g., slamming in from `scale: 3, rotation: -2` to `scale: 1, rotation: 0`), drift slowly, and exit using the safe opacity and timing rules defined above.

### Step 5: Lint and Preview
1. Run `npx hyperframes@latest lint` (if applicable) or verify the timeline locally.
2. Run `npx hyperframes preview` to open preview mode.

### Step 6: Clean Up and Generate Social Media Description
* Clean up unused folders and files after completed rendering (user will request rendering manually).
* After cleaning up, generate highly concise, YouTube-optimized Titles and Descriptions (in both English and Vietnamese) based on the context of the podcast video. Present this to the user.
