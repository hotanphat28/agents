import sys
import json
import os
from faster_whisper import WhisperModel

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Read prompt from lyric.md
prompt = ""
if os.path.exists("assets/lyric.md"):
    with open("assets/lyric.md", "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.read().splitlines() if l.strip() and not l.startswith('[') and not l.startswith('#')]
        prompt = " ".join(lines[:4])

audio_file = sys.argv[1]
model = WhisperModel("medium", device="cpu", compute_type="int8")

print("Running transcription...")
segments, info = model.transcribe(
    audio_file, 
    word_timestamps=True, 
    language="vi",
    vad_filter=True,
    condition_on_previous_text=False,
    initial_prompt=prompt if prompt else None,
    beam_size=5
)

transcript = []
for segment in segments:
    for word in segment.words:
        transcript.append({"word": word.word.strip(), "start": word.start, "end": word.end})

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(transcript, f, ensure_ascii=False, indent=2)
