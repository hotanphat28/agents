---
name: lyric-video-maker
description: Creates a polished, cinematic lyric video from an MP3, a cover image, and a lyric.md file using Hyperframes, GSAP, and faster-whisper. Includes perfect Vietnamese font support, synced animations, and thumbnail generation.
---

# lyric Video Maker

You are an expert at creating beautiful, cinematic lyric videos. When triggered, follow this workflow to build a lyric video for the user.

## Required Inputs
Ensure the target directory contains:
1. An audio file (`.mp3` or `.wav`).
2. An album cover image (`.png` or `.jpg`).
3. A `lyric.md` file containing the accurate lyric.

## Step 1: Initialize Project & Download Assets
1. Inside the target directory, create a `lyric-video` folder.
2. Initialize Hyperframes: `npx hyperframes@latest init lyric-video -y`
3. Download the full TTF of **Dancing Script** (for perfect Vietnamese support) into `lyric-video/assets/DancingScript-SemiBold.ttf`.
   *Python download snippet:*
   ```python
   import urllib.request
   import re, ssl
   ssl._create_default_https_context = ssl._create_unverified_context
   url = 'https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap'
   req = urllib.request.Request(url) # No User-Agent returns the full TTF
   with urllib.request.urlopen(req) as response:
       css = response.read().decode('utf-8')
   urls = re.findall(r'url\((.*?)\)', css)
   for font_url in urls:
       if 'ttf' in font_url:
           urllib.request.urlretrieve(font_url.strip("'\""), 'lyric-video/assets/DancingScript-SemiBold.ttf')
           break
   ```
4. Copy the audio file and cover image into `lyric-video/assets/`.

## Step 2: Transcribe Audio
Use `faster-whisper` to extract word-level timestamps from the audio.
*Transcription snippet (`transcribe.py`):*
```python
import sys
import json
from faster_whisper import WhisperModel

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

audio_file = sys.argv[1]
model = WhisperModel("large-v3", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_file, word_timestamps=True, language="vi")

transcript = []
for segment in segments:
    for word in segment.words:
        transcript.append({"word": word.word.strip(), "start": word.start, "end": word.end})

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(transcript, f, ensure_ascii=False, indent=2)
```

## Step 3: Align and Generate HTML
Read the accurate lyric from `lyric.md` and align them with the timestamps in `transcript.json`.
Generate the `index.html` composition with the following aesthetic rules:
- **Background**: The cover image scaled up to full screen and blurred (`filter: blur(40px) brightness(0.3)`).
- **Album Art**: Displayed in the bottom-left corner with a glass-border and a subtle floating animation (GSAP sine wave y-axis tween).
- **Typography**: Use the downloaded `Dancing Script` via `@font-face`.
- **Text Animation**: Each line fades in and scales slightly (`scale: 0.95` to `1`).
- **Highlights**: The last word of each phrase should be wrapped in `<em>` and styled with a glowing golden color (`#ffd700`).

*HTML Generation Snippet (adapt alignment logic as needed):*
```python
import json

# Load duration, transcript, and lyric.md here.
# Map lines from lyric.md to start/end times in transcript.json.

html_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {
        font-family: 'Dancing Script';
        font-style: normal; font-weight: 600; font-display: swap;
        src: url(assets/DancingScript-SemiBold.ttf) format('truetype');
      }
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1920px; height: 1080px; overflow: hidden; background: #000; font-family: 'Dancing Script', sans-serif; }
      #videoFrame { position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; z-index: 1; }
      #overlay { position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; background: rgba(0, 0, 0, 0.4); z-index: 2; }
      .album-art-container {
        position: absolute; bottom: 80px; left: 80px; width: 300px; height: 300px; z-index: 5;
        border-radius: 16px; box-shadow: 0 16px 48px -12px rgba(0,0,0,0.8), 0 0 24px rgba(255,255,255,0.15);
        overflow: hidden; border: 1px solid rgba(255,255,255,0.2);
      }
      .album-art { width: 100%; height: 100%; object-fit: cover; }
      .lyric-container {
        position: absolute; top: 0; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: center; z-index: 4;
      }
      .lyric-line {
        position: absolute; font-size: 110px; font-weight: 600; color: #ffffff; text-align: center; width: 80%; opacity: 0;
        text-shadow: 0 0 24px rgba(255,255,255,0.85), 0 0 50px rgba(255,255,255,0.55), 0 0 100px rgba(255,255,255,0.3);
      }
      .lyric-line em {
        font-style: normal; color: #ffd700;
        text-shadow: 0 0 24px rgba(255,215,0,0.85), 0 0 50px rgba(255,215,0,0.55), 0 0 100px rgba(255,215,0,0.3);
      }
      .vignette {
        position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; background: radial-gradient(circle, transparent 50%, rgba(0,0,0,0.7) 150%); z-index: 10; pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DURATION}" data-width="1920" data-height="1080">
      <!-- Blurred Background Image -->
      <div id="videoFrame">
        <img id="bg-blur" src="assets/{COVER_IMAGE}" style="width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.3); position: absolute; top: 0; left: 0; transform: scale(1.1);" />
      </div>
      <!-- Audio -->
      <audio id="stageAudio" class="clip" data-start="0.00" data-duration="{DURATION}" data-track-index="2" preload="auto" src="assets/{AUDIO_FILE}"></audio>
      <div id="overlay"></div><div class="vignette"></div>
      <!-- Album Art -->
      <div class="album-art-container"><img class="album-art" src="assets/{COVER_IMAGE}" /></div>
      <!-- lyric -->
      <div class="lyric-container">{lyric_HTML}</div>
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      tl.to(".album-art-container", { y: -15, duration: 3, yoyo: true, repeat: {REPEAT_ALBUM}, ease: "sine.inOut" }, 0);
      {lyric_GSAP}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
# ... build lyric_html and lyric_gsap ...
```

## Step 4: Lint and Render
1. Run `npx hyperframes@latest lint` to ensure no errors.
2. Render the final video: `npx hyperframes@latest render -o output_lyric.mp4 --fps 30 --quality high --crf 18`
3. Present the final video artifact to the user.

## Step 5: Generate Thumbnail
1. Create a `generate_thumbnail.py` script that outputs a static `thumbnail.html`. This HTML should use the same visual layout (blurred background, vignette, floating cover image) but place the song title in the center using the `Dancing Script` font, highlighted in golden `#ffd700` and sized larger (e.g., `160px`).
2. Render a 1-second video of the thumbnail:
   ```bash
   Rename-Item "index.html" "index.html.bak"
   Rename-Item "thumbnail.html" "index.html"
   npx hyperframes@latest render -o temp_thumb.mp4 --fps 30 --quality high
   ```
3. Extract the first frame as a high-resolution PNG using ffmpeg:
   ```bash
   ffmpeg -i temp_thumb.mp4 -vframes 1 thumbnail.png
   ```
4. Clean up the temporary MP4 and restore `index.html`:
   ```bash
   Rename-Item "index.html" "thumbnail.html"
   Rename-Item "index.html.bak" "index.html"
   Remove-Item "temp_thumb.mp4"
   ```
5. Present the `thumbnail.png` artifact to the user.

