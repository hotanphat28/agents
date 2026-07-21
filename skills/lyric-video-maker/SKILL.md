---
name: lyric-video-maker
description: Creates a polished, cinematic lyric video from an MP3 or WAV, a cover image, and a lyric.md file using HyperFrames, GSAP, and faster-whisper. Includes Vietnamese font support (DancingScript), word-level sync, animations, and thumbnail generation. Activate when the user wants a lyric video, music video with synced text, or karaoke-style visual from an audio file.
---

# Lyric Video Maker

Build cinematic lyric videos with word-level sync from audio files.

**Stack:** HyperFrames + GSAP + faster-whisper + demucs

---

## Required Inputs

Ensure the target directory contains:
1. Audio file (`song.mp3` or `.wav`)
2. Album cover image (`cover.png` or `.jpg`)
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
uvx demucs --two-stems=vocals "assets/song.mp3"
```

Output: `separated/htdemucs/song/vocals.wav`

### 3. Transcribe (Word-Level Timestamps)

Copy `examples/transcribe.py` to working directory, then run:

```bash
uv run --with faster-whisper python transcribe.py "separated/htdemucs/song/vocals.wav"
```

Output: `transcript.json`

### 4. Align and Generate HTML

Copy `examples/generate_lyric.py` to working directory, then run:

```bash
uv run python generate_lyric.py
```

Aligns `transcript.json` with `lyric.md` via `difflib.SequenceMatcher` and builds the HyperFrames HTML composition.

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
rm -rf separated/ transcript.json transcribe.py generate_lyric.py generate_thumbnail.py thumbnail.html
```
