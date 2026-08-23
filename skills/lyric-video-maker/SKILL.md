---
name: lyric-video-maker
description: Creates a polished, cinematic lyric video from an MP3 or WAV, a cover image, and a lyric.md file using HyperFrames, GSAP, and stable-ts. Includes Vietnamese font support (DancingScript), 100% accurate word-level sync, animations, and thumbnail generation. Activate when the user wants a lyric video, music video with synced text, or karaoke-style visual from an audio file.
disable-model-invocation: true
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

Create `assets/` folder containing:
- Audio file
- Cover image
- `DancingScript-SemiBold.ttf` font (ask user if not present)
- `lyric.md`

### 2. Extract Vocals

Isolate vocals to prevent transcription hallucinations from background music:

```bash
uvx --with numpy demucs --two-stems=vocals assets/*.{mp3,wav,m4a}
```

Output: `separated/htdemucs/song/vocals.wav`

### 3. Align (Word-Level Timestamps)

Extract text and run `stable-ts` forced alignment:

```bash
grep -v "^\[" assets/lyric.md | grep -v "^#" | grep -v "^$" > assets/lyric.txt
uvx --with stable-ts stable-ts separated/htdemucs/*/vocals.wav -o aligned.json --align assets/lyric.txt --language vi --model large-v3
```

Output: `aligned.json`

### 4. Align and Generate HTML

Copy `examples/generate_lyric.py` to working directory, then run:

```bash
uv run python generate_lyric.py
```

Parses `aligned.json` and builds the HyperFrames HTML composition with 100% accurate word-level sync.

Output: `index.html`

### 5. Lint and Render

```bash
npx hyperframes@latest lint
mkdir -p renders && npx hyperframes@latest render -o renders/output_lyric.mp4 --fps 30 --quality high --crf 18
```

Present `renders/output_lyric.mp4` to user.

### 6. Generate Thumbnail

Copy `examples/generate_thumbnail.py`, update the song title constant, then run:

```bash
uv run python generate_thumbnail.py
```

Present `thumbnail.png` to user.

### 7. Clean Up

After user approves final output:

```bash
rm -rf separated/ aligned.json assets/lyric.txt generate_lyric.py generate_thumbnail.py thumbnail.html
```
