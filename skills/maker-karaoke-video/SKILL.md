---
name: maker-karaoke-video
description: Generate high-quality karaoke videos with hyperframes, featuring 2-line layout, vocal extraction, perfect word-level timing, GSAP countdown, and stroke/fill typography.
disable-model-invocation: true
version: 1.0.0
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
3. **Vocal Extraction & Word-Level Alignment**: follow [Vocal Extraction & Word-Level Alignment](../VOCAL-ALIGNMENT.md) steps 1-3 from inside `karaoke/`.
4. **Copy Generator Script**: Copy the Python generator script from the skill's `scripts` directory to the `karaoke/` directory:
   ```bash
   cp ~/.agents/skills/maker-karaoke-video/scripts/generate_karaoke.py .
   ```
5. **Generate HTML**: Run the script to generate `index.html`.
   ```bash
   uv run python generate_karaoke.py
   ```
6. **Render**: Use `hyperframes` to lint and render the final video.
   ```bash
   npx hyperframes@latest lint
   npx hyperframes@latest render -o renders/output_karaoke.mp4 --fps 30 --quality high --crf 18
   ```

## Script Details
The provided `generate_karaoke.py` uses `../assets/` to read the cover image, lyrics, and original song (if no_vocals isn't found). You do NOT need to create symlinks. The script outputs `index.html` with advanced GSAP animations and precise karaoke styling.
