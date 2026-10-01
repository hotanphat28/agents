# Vocal Extraction & Word-Level Alignment

Shared reference for `maker-karaoke-video` and `maker-lyric-video`: isolating vocals and force-aligning them to known lyrics. Run from inside the skill's working directory (e.g. `karaoke/` or `lyric/`), one level below `assets/`.

## 1. Extract vocals
Isolate vocals to prevent transcription hallucinations from background music:
```bash
uvx --with numpy demucs --two-stems=vocals ../assets/*.{mp3,wav,m4a}
```
Output: `separated/htdemucs/<song>/vocals.wav`

## 2. Clean lyrics
Strip timestamps/headers from `lyric.md` down to plain text:
```bash
grep -v "^\[" ../assets/lyric.md | grep -v "^#" | grep -v "^$" > lyric.txt
```

## 3. Word-level alignment
Force-align the isolated vocals against the cleaned lyrics with `stable-ts`:
```bash
uvx --with stable-ts stable-ts separated/htdemucs/*/vocals.wav -o aligned.json --align lyric.txt --language vi --model large-v3
```
Adjust the wildcard to match the actual demucs output folder name. Output: `aligned.json`.

## Fallback: no reliable lyric.md
If `lyric.md` is missing or too inaccurate to force-align against, transcribe the isolated vocals directly instead of force-aligning: run `maker-lyric-video/examples/transcribe.py <vocals.wav>` (faster-whisper, word-level timestamps) to produce `transcript.json`, then build `aligned.json` from that transcript instead of step 3.
