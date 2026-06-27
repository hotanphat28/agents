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
