import os
import subprocess

html_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <style>
      @font-face {
        font-family: 'Dancing Script';
        font-style: normal;
        font-weight: 600;
        font-display: swap;
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

      .lyrics-container {
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        display: flex; align-items: center; justify-content: center; z-index: 4;
      }
      
      .lyric-line {
        position: absolute; font-size: 160px; font-weight: 600; color: #ffd700; text-align: center; width: 80%;
        text-shadow: 0 0 24px rgba(255,215,0,0.85), 0 0 50px rgba(255,215,0,0.55), 0 0 100px rgba(255,215,0,0.3);
      }
      
      .vignette {
        position: absolute; top: 0; left: 0; width: 1920px; height: 1080px;
        background: radial-gradient(circle, transparent 50%, rgba(0,0,0,0.7) 150%);
        z-index: 10; pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="1" data-width="1920" data-height="1080">
      <div id="videoFrame">
        <img id="bg-blur" src="assets/cover.png" style="width: 100%; height: 100%; object-fit: cover; filter: blur(40px) brightness(0.3); position: absolute; top: 0; left: 0; transform: scale(1.1);" />
      </div>
      
      <div id="overlay"></div><div class="vignette"></div>
      
      <div class="album-art-container">
        <img class="album-art" src="assets/cover.png" />
      </div>

      <div class="lyrics-container">
        <div class="lyric-line">SONG TITLE HERE</div>
      </div>
    </div>
  </body>
</html>
"""

with open("thumbnail.html", "w", encoding="utf-8") as f:
    f.write(html_template)

if os.path.exists("index.html"):
    os.rename("index.html", "index.html.bak")
os.rename("thumbnail.html", "index.html")

try:
    npx = "npx.cmd" if os.name == "nt" else "npx"
    subprocess.run([npx, "hyperframes@latest", "render", "-o", "temp_thumb.mp4", "--fps", "30", "--quality", "high"], check=True)
    subprocess.run(["ffmpeg", "-y", "-i", "temp_thumb.mp4", "-vframes", "1", "thumbnail.png"], check=True)
finally:
    if os.path.exists("index.html"):
        os.rename("index.html", "thumbnail.html")
    if os.path.exists("index.html.bak"):
        os.rename("index.html.bak", "index.html")
    if os.path.exists("temp_thumb.mp4"):
        os.remove("temp_thumb.mp4")

print("Generated thumbnail.png successfully.")
