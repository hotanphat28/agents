---
name: lyric-video-maker
description: Creates a polished, cinematic lyric video from an MP3 or a WAV, a cover image, and a lyric.md file using Hyperframes, GSAP, and faster-whisper. Includes perfect Vietnamese font support, synced animations, and thumbnail generation.
---

# Lyric Video Maker

You are an expert at creating beautiful, cinematic lyric videos. When triggered, follow this workflow to build a lyric video for the user.

## Required Inputs
Ensure the target directory contains:
1. An audio file (e.g., `song.mp3` or `.wav`).
2. An album cover image (e.g., `cover.png` or `.jpg`).
3. A `lyric.md` file containing the accurate lyric.

## Step 1: Setup Assets
Ensure the target directory has an `assets/` folder containing:
1. The audio file.
2. The album cover image.
3. The `DancingScript-SemiBold.ttf` font file (the user will provide it, or you can ask for it).
4. The `lyric.md` file.

## Step 2: Extract Vocals (Crucial for heavy music)
To guarantee that the AI transcription tool doesn't hallucinate or get confused by background music, use `demucs` to isolate the vocals first.
```bash
uvx demucs --two-stems=vocals "assets/song.mp3"
```
This will generate the pure vocal track at: `separated/htdemucs/song/vocals.wav`

## Step 3: Transcription
Use `faster-whisper` to extract word-level timestamps from the isolated vocals.
1. Copy the script from `examples/transcribe.py` to the working directory.
2. Run it using `uv`:
```bash
uv run --with faster-whisper python transcribe.py "separated/htdemucs/song/vocals.wav"
```
This generates `transcript.json`.

## Step 4: Align and Generate HTML
1. Copy the script from `examples/generate_lyric.py` to the working directory.
2. Run the script to generate `index.html`:
```bash
python generate_lyric.py
```
This script aligns the `transcript.json` with `lyric.md` using `difflib.SequenceMatcher` and builds the Hyperframes HTML composition.

## Step 5: Lint and Render
1. Run `npx hyperframes@latest lint` to ensure no errors.
2. Render the final video: 
```bash
mkdir -p renders && npx hyperframes@latest render -o renders/output_lyric.mp4 --fps 30 --quality high --crf 18
```
3. Present the final video artifact (`renders/output_lyric.mp4`) to the user.

## Step 6: Generate Thumbnail
1. Copy the script from `examples/generate_thumbnail.py` to the working directory. 
2. Edit the script to replace "SONG TITLE HERE" with the actual song title, and then run it:
```bash
python generate_thumbnail.py
```
3. Present the `thumbnail.png` artifact to the user.

## Step 7: Clean Up (IMPORTANT)
Once the final video and thumbnail are successfully generated and approved by the user, clean up all the intermediate files so the project directory remains neat:
```bash
rm -rf separated/ transcript.json transcribe.py generate_lyric.py generate_thumbnail.py thumbnail.html
```
