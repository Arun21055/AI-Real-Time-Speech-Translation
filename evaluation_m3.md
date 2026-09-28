# 🧾 Evaluation – Milestone 3 (Real-Time Pipeline)

**Evaluation week:** 6

## Criteria and status

| Criterion | Target | Status |
|---|---|---|
| Speech → translation → speech pipeline works | End-to-end demo | ✅ Implemented (`realtime_pipeline.py`) |
| Audible playback in target language | Yes | ✅ Azure neural voice |
| Language switching | 3+ languages | ✅ Chosen at start-up via command-line arguments |
| End-to-end latency | < 3 s | 🔄 Translation time is printed; full end-to-end timing not yet benchmarked |
| Continuous streaming | Word-by-word | ⏳ Currently sentence-by-sentence |

## Deliverables
1. End-to-end code: `src/realtime_pipeline.py`
2. Alternative pipelines: `src/pipeline_openai.py`, `src/pipeline_speech_translation.py`
3. Dependencies: `src/requirements.txt`

## How to verify
```bash
python src/realtime_pipeline.py hi hi-IN
```
Speak an English sentence and confirm the Hindi translation is printed and spoken.
