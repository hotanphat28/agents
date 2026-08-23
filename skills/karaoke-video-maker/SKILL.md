---
name: karaoke-video-maker
description: Generate high-quality karaoke videos with hyperframes, featuring 2-line layout, vocal extraction, perfect word-level timing, GSAP countdown, and stroke/fill typography.
disable-model-invocation: true
---

# Karaoke Video Maker

## Prerequisites & Project Structure
This skill assumes the user has set up a directory structure like this:
```
project-folder/
|- assets/
|  |- lyric.md     (The lyrics text)
|  |- song.mp3     (Or .wav, the song audio)
|  |- cover.png    (Or .jpg, the album cover)
```

## Workflow

1. **Verify Assets**: Ensure `assets/lyric.md` and the audio file exist.
2. **Create Output Directory**: Create a `karaoke/` directory alongside `assets/` and enter it:
   ```bash
   mkdir -p karaoke
   cd karaoke
   ```
3. **Vocal Extraction**: Run `demucs` to isolate the vocals and generate the instrumental track. (We use `uvx` to ensure proper environments per user rules).
   ```bash
   uvx --with numpy demucs --two-stems=vocals ../assets/*.wav
   ```
   *(Adjust `.wav` to `.mp3` if needed)*
4. **Clean Lyrics**: The `lyric.md` file often contains timestamps or headers. Clean it to a plain text file inside `karaoke/`:
   ```bash
   grep -v "^\[" ../assets/lyric.md | grep -v "^#" | grep -v "^$" > lyric.txt
   ```
5. **Word-Level Alignment**: Use `stable-ts` to align the isolated vocals with the cleaned lyrics.
   ```bash
   uvx --with stable-ts stable-ts separated/htdemucs/*/vocals.wav -o aligned.json --align lyric.txt --language vi --model large-v3
   ```
   *(Note: Adjust the wildcard to match the demucs output folder name).*
6. **Copy Generator Script**: Copy the Python generator script from the skill's `scripts` directory to the `karaoke/` directory (replace `<skill-dir>` with the actual path to this skill):
   ```bash
   cp <skill-dir>/scripts/generate_karaoke.py .
   ```
7. **Generate HTML**: Run the script to generate `index.html`.
   ```bash
   uv run python generate_karaoke.py
   ```
8. **Render**: Use `hyperframes` to lint and render the final video.
   ```bash
   npx hyperframes@latest lint
   npx hyperframes@latest render -o renders/output_karaoke.mp4 --fps 30 --quality high --crf 18
   ```

## Script Details
The provided `generate_karaoke.py` uses `../assets/` to read the cover image, lyrics, and original song (if no_vocals isn't found). You do NOT need to create symlinks. The script outputs `index.html` with advanced GSAP animations and precise karaoke styling.
