# ⚙️ Milestone 3 – Real-Time Speech-to-Speech Pipeline

| | |
|---|---|
| **Duration** | Weeks 5–6 |
| **Status** | ✅ Implemented (sentence-by-sentence) |
| **Code** | `src/realtime_pipeline.py` (also `src/pipeline_openai.py`, `src/pipeline_speech_translation.py`) |

## Objective
Connect recognition, translation and speech output into one pipeline that listens to English speech and speaks the translation in another language.

## Workflow
```
Microphone ─▶ Azure Speech-to-Text ─▶ Azure OpenAI translation ─▶ Azure Text-to-Speech ─▶ Speaker
```

## Tasks
- ✅ Combined speech recognition, translation and text-to-speech in one loop.
- ✅ Target language and voice are chosen from the command line (default: Spanish).
- ✅ Translation time is printed for each sentence.
- ✅ Speech output waits until playback finishes before listening again.
- ✅ Added an alternative pipeline (`pipeline_speech_translation.py`) that uses only Azure Speech's built-in translation.

## Tools & Libraries
- `azure-cognitiveservices-speech` (speech-to-text and text-to-speech)
- `openai` (Azure OpenAI translation)

## How to run
```bash
python src/realtime_pipeline.py             # English -> Spanish
python src/realtime_pipeline.py fr fr-FR    # English -> French
python src/realtime_pipeline.py hi hi-IN    # English -> Hindi
```

## Limitations
- Works **one sentence at a time** (recognise once, then translate, then speak), so it is near real-time, not word-by-word streaming.
- End-to-end latency has not been formally benchmarked.

## Future improvement
Use continuous recognition with small audio chunks and run translation and speech in parallel to reduce delay.

⬅️ [Milestone 2](milestone2.md) · ➡️ [Milestone 4](milestone4.md)
