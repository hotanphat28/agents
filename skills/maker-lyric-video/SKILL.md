---
name: maker-lyric-video
description: Creates a polished, cinematic lyric video from an MP3 or WAV, a cover image, and a lyric.md file using HyperFrames, GSAP, and stable-ts. Includes Vietnamese font support (DancingScript), 100% accurate word-level sync, animations, and thumbnail generation.
disable-model-invocation: true
version: 1.0.0
---

# Lyric Video Maker

Build cinematic lyric videos with word-level sync from audio files.

**Stack:** HyperFrames + GSAP + stable-ts + demucs

---

## Required Inputs

Ensure the target directory contains:
1. Audio file (e.g. `song.mp3` or `song.wav`)
2. Album cover image (e.g. `cover.png` or `cover.jpg`)
3. `lyric.md` with accurate lyrics

---

## Workflow

### 1. Setup Assets

Ensure the parent directory has an `assets/` folder containing:
- Audio file
- Cover image
- `DancingScript-SemiBold.ttf` font (ask user if not present)
- `lyric.md`

Create a `lyric/` directory and enter it:

```bash
mkdir -p lyric
cd lyric
```

### 2. Vocal Extraction & Word-Level Alignment

Follow [Vocal Extraction & Word-Level Alignment](../VOCAL-ALIGNMENT.md) steps 1-3 from inside `lyric/`. Output: `aligned.json`.

### 3. Align and Generate HTML

Copy `examples/generate_lyric.py` to working directory, then run:

```bash
uv run python generate_lyric.py
```

Parses `aligned.json` and builds the HyperFrames HTML composition with 100% accurate word-level sync.

Output: `index.html`

### 4. Lint and Render

```bash
npx hyperframes@latest lint
mkdir -p renders && npx hyperframes@latest render -o renders/output_lyric.mp4 --fps 30 --quality high --crf 18
```

Present `renders/output_lyric.mp4` to user.

### 5. Generate Thumbnail

Copy `examples/generate_thumbnail.py`, update the song title constant, then run:

```bash
uv run python generate_thumbnail.py
```

Present `thumbnail.png` to user.

### 6. Clean Up

After user approves final output:

```bash
rm -rf separated/ aligned.json lyric.txt generate_lyric.py generate_thumbnail.py thumbnail.html
```
