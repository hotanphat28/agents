import json
import glob
import os

def get_asset_file(extensions, default):
    for ext in extensions:
        files = glob.glob(f"../assets/*{ext}")
        if files:
            return os.path.basename(files[0])
    return default

audio_files = glob.glob("separated/htdemucs/*/no_vocals.wav")
audio_file = audio_files[0] if audio_files else "../assets/song.mp3"

cover_file = get_asset_file(['.png', '.jpg', '.jpeg', '.webp'], "cover.png")

with open("../assets/lyric.md", "r", encoding="utf-8") as f:
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
        aligned_lines.append({'text': line, 'start': start_time, 'end': end_time, 'words': current_words})
    else:
        fallback_words = [{'word': w, 'start': duration + (i*0.5), 'end': duration + ((i+1)*0.5)} for i, w in enumerate(line_words)]
        aligned_lines.append({'text': line, 'start': duration, 'end': duration + (line_count * 0.5), 'words': fallback_words})
        duration += (line_count * 0.5)
        
    word_idx += line_count

duration += 5

# Ensure line ends don't overlap with start of the next-next line (same position)
# Classic karaoke: Line 0 (odd), Line 1 (even), Line 2 (odd). Line 2 must appear after Line 0 disappears.
for i in range(len(aligned_lines)):
    # Give a small buffer for the current line to stay on screen
    al = aligned_lines[i]
    al['fade_in_start'] = al['start'] - 2.0
    al['fade_out_start'] = al['end'] + 0.5
    
    # If this is not the first odd/even line, it must wait for the previous odd/even line to disappear
    if i >= 2:
        prev_al = aligned_lines[i-2]
        if prev_al['fade_out_start'] > al['fade_in_start']:
            # Adjust previous line fade out so it disappears in time
            prev_al['fade_out_start'] = al['fade_in_start'] - 0.2

    # Make sure fade in isn't before 0
    al['fade_in_start'] = max(0, al['fade_in_start'])

html_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1920px; height: 1080px; overflow: hidden; background: #000; font-family: 'Montserrat', sans-serif; }
      #videoFrame { position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; z-index: 1; }
      #overlay { position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; background: rgba(0, 0, 0, 0.4); z-index: 2; }
      .album-art-container {
        position: absolute; top: 80px; left: calc(50% - 150px); width: 300px; height: 300px; z-index: 5;
        border-radius: 16px; box-shadow: 0 16px 48px -12px rgba(0,0,0,0.8), 0 0 24px rgba(255,255,255,0.15);
        overflow: hidden; border: 1px solid rgba(255,255,255,0.2);
      }
      .album-art { width: 100%; height: 100%; object-fit: cover; }
      .lyric-container {
        position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 4;
      }
      .lyric-line {
        position: absolute; opacity: 0;
        display: flex; gap: 20px; flex-wrap: nowrap; white-space: nowrap;
        font-size: 70px; font-weight: 800; text-transform: uppercase;
        -webkit-text-stroke: 4px black; paint-order: stroke fill;
      }
      .lyric-line.odd {
        top: 65%; left: 5%; right: 5%; justify-content: flex-start;
      }
      .lyric-line.even {
        top: 80%; left: 5%; right: 5%; justify-content: flex-end;
      }
      .karaoke-word {
        position: relative; display: inline-block;
      }
      .karaoke-word .text {
        color: white;
      }
      .karaoke-word .fill {
        position: absolute; left: 0; top: 0; width: 0%; overflow: hidden;
        color: #ffd700; white-space: nowrap;
      }
      .vignette {
        position: absolute; top: 0; left: 0; width: 1920px; height: 1080px; background: radial-gradient(circle, transparent 50%, rgba(0,0,0,0.7) 150%); z-index: 10; pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DURATION}" data-width="1920" data-height="1080">
      <div id="videoFrame">
        <img id="bg-blur" src="../assets/{COVER_IMAGE}" style="width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.3); position: absolute; top: 0; left: 0; transform: scale(1.1);" />
      </div>
      <audio id="stageAudio" class="clip" data-start="0.00" data-duration="{DURATION}" data-track-index="2" preload="auto" src="{SONG_FILE}"></audio>
      <div id="overlay"></div><div class="vignette"></div>
      <div class="album-art-container"><img class="album-art" src="../assets/{COVER_IMAGE}" /></div>
      <div id="countdown" style="position: absolute; top: 45%; left: 0; width: 100%; text-align: center; font-size: 200px; font-weight: 800; color: #ffd700; -webkit-text-stroke: 6px black; paint-order: stroke fill; opacity: 0; z-index: 10;"></div>
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
global_word_idx = 0

for i, al in enumerate(aligned_lines):
    line_id = f"lyric-{i}"
    line_class = "odd" if i % 2 == 0 else "even"
    
    # HTML generation
    lyrics_html += f'        <div id="{line_id}" class="lyric-line {line_class}">\n'
    for w in al['words']:
        clean_word = w['word'].strip()
        lyrics_html += f'          <span id="word-{global_word_idx}" class="karaoke-word"><span class="fill">{clean_word}</span><span class="text">{clean_word}</span></span>\n'
        global_word_idx += 1
    lyrics_html += f'        </div>\n'
    
    # GSAP for Line (Fade in / out, no movement)
    lyrics_gsap += f'      tl.fromTo("#{line_id}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "none", overwrite: "auto" }}, {al["fade_in_start"]:.2f});\n'
    lyrics_gsap += f'      tl.to("#{line_id}", {{ opacity: 0, duration: 0.2, ease: "none", overwrite: "auto" }}, {al["fade_out_start"]:.2f});\n'

# GSAP for Words (Fill effect)
global_word_idx = 0
for al in aligned_lines:
    for word_i, w in enumerate(al['words']):
        w_start = w['start']
        w_dur = max(0.1, w['end'] - w_start)
        
        # Prevent the first word of a line from filling too slowly if there is an instrumental pause before it
        if word_i == 0 and w_dur > 0.5:
            w_dur = 0.4
            w_start = w['end'] - w_dur
            
        lyrics_gsap += f'      tl.to("#word-{global_word_idx} .fill", {{ width: "100%", duration: {w_dur:.3f}, ease: "none" }}, {w_start:.3f});\n'
        global_word_idx += 1

# GSAP Countdown
first_start = aligned_lines[0]['start']
if first_start > 3.0:
    lyrics_gsap += f'      tl.set("#countdown", {{ innerText: "3", opacity: 1 }}, {first_start - 3.0:.2f});\n'
    lyrics_gsap += f'      tl.to("#countdown", {{ opacity: 0, duration: 0.5 }}, {first_start - 2.5:.2f});\n'
    lyrics_gsap += f'      tl.set("#countdown", {{ innerText: "2", opacity: 1 }}, {first_start - 2.0:.2f});\n'
    lyrics_gsap += f'      tl.to("#countdown", {{ opacity: 0, duration: 0.5 }}, {first_start - 1.5:.2f});\n'
    lyrics_gsap += f'      tl.set("#countdown", {{ innerText: "1", opacity: 1 }}, {first_start - 1.0:.2f});\n'
    lyrics_gsap += f'      tl.to("#countdown", {{ opacity: 0, duration: 0.5 }}, {first_start - 0.5:.2f});\n'

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
