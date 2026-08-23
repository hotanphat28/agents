import json
import glob
import os
import sys

def get_asset_file(extensions, default):
    for ext in extensions:
        files = glob.glob(f"assets/*{ext}")
        if files:
            return os.path.basename(files[0])
    return default

audio_file = get_asset_file(['.mp3', '.wav', '.m4a'], "song.mp3")
cover_file = get_asset_file(['.png', '.jpg', '.jpeg', '.webp'], "cover.png")
with open("assets/lyric.md", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.read().splitlines() if l.strip() and not l.startswith('[') and not l.startswith('#')]

with open("aligned.json", "r", encoding="utf-8") as f:
    data = json.load(f)

transcript_words = []
for segment in data.get("segments", []):
    for word_info in segment.get("words", []):
        word = word_info.get("word", "").strip()
        start = word_info.get("start", 0.0)
        end = word_info.get("end", 0.0)
        if word:
            transcript_words.append({"word": word, "start": start, "end": end})

aligned_lines = []
word_idx = 0
duration = 0

for line in lines:
    line_words = line.split()
    line_count = len(line_words)
    if line_count == 0:
        continue
    
    current_words = transcript_words[word_idx:word_idx+line_count]
    
    if current_words:
        start_time = current_words[0]['start']
        end_time = current_words[-1]['end']
        duration = max(duration, end_time)
        aligned_lines.append({'text': line, 'start': start_time, 'end': end_time})
    else:
        # Fallback if mismatch
        aligned_lines.append({'text': line, 'start': duration, 'end': duration + 2})
        duration += 2
        
    word_idx += line_count

duration += 5

for i in range(1, len(aligned_lines)):
    if aligned_lines[i]['start'] <= aligned_lines[i-1]['start']:
        aligned_lines[i]['start'] = aligned_lines[i-1]['start'] + 0.1
    if aligned_lines[i-1]['end'] > aligned_lines[i]['start']:
        aligned_lines[i-1]['end'] = aligned_lines[i]['start']
    if aligned_lines[i]['end'] <= aligned_lines[i]['start']:
        aligned_lines[i]['end'] = aligned_lines[i]['start'] + 0.1

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
      <div id="videoFrame">
        <img id="bg-blur" src="assets/{COVER_IMAGE}" style="width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.3); position: absolute; top: 0; left: 0; transform: scale(1.1);" />
      </div>
      <audio id="stageAudio" class="clip" data-start="0.00" data-duration="{DURATION}" data-track-index="2" preload="auto" src="assets/{SONG_FILE}"></audio>
      <div id="overlay"></div><div class="vignette"></div>
      <div class="album-art-container"><img class="album-art" src="assets/{COVER_IMAGE}" /></div>
      <div class="lyric-container">
{LYRICS_HTML}      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      tl.to(".album-art-container", { y: -15, duration: 3, yoyo: true, repeat: {REPEAT_ALBUM}, ease: "sine.inOut" }, 0);
{LYRICS_GSAP}      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""

lyrics_html = ""
lyrics_gsap = ""

for i, al in enumerate(aligned_lines):
    start = al['start']
    end = al['end']
    text = al['text']
    line_id = f"lyric-{i}"
    
    words = text.split()
    if len(words) > 0:
        words[-1] = f"<em>{words[-1]}</em>"
    formatted_text = " ".join(words)
    
    dur = min(0.4, max(0.05, (end - start) / 3))
    
    lyrics_html += f'        <div id="{line_id}" class="lyric-line">{formatted_text}</div>\n'
    
    lyrics_gsap += f'      tl.fromTo("#{line_id}", {{ opacity: 0, scale: 0.95, y: 20 }}, {{ opacity: 1, scale: 1, y: 0, duration: {dur:.2f}, ease: "power2.out", overwrite: "auto" }}, {start:.2f});\n'
    lyrics_gsap += f'      tl.to("#{line_id}", {{ opacity: 0, scale: 1.05, y: -20, duration: {dur:.2f}, ease: "power2.in", overwrite: "auto" }}, {end - dur:.2f});\n'

repeat_album = int(duration / 6)

final_html = html_template.replace("{DURATION}", f"{duration:.2f}") \
    .replace("{COVER_IMAGE}", cover_file) \
    .replace("{SONG_FILE}", audio_file) \
    .replace("{LYRICS_HTML}", lyrics_html) \
    .replace("{LYRICS_GSAP}", lyrics_gsap) \
    .replace("{REPEAT_ALBUM}", str(repeat_album))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated index.html successfully.")
