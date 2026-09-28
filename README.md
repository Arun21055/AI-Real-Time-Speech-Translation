# 🎙️ AI-Powered Real-Time Speech Translation

A speech-to-speech translation system that converts live English/Hindi speech
(for example, sports commentary) into multiple languages using **Azure Speech**
and **Azure OpenAI**. Built during the **Infosys Springboard Virtual Internship 6.0 (AI Track)**.

## How it works

```
Live speech ─▶ Speech-to-Text ─▶ Translation ─▶ Text-to-Speech ─▶ Translated audio
              (Azure Speech)    (Azure OpenAI)   (Azure Speech)
```

1. **Recognize:** Azure Speech-to-Text converts microphone audio into text.
2. **Translate:** Azure OpenAI translates the text into the target language.
3. **Speak:** Azure neural voices read the translation aloud.

## Project structure

```
src/
├── speech_to_text.py                # Milestone 1: live speech recognition
├── translatemodel.py                # Milestone 2: Azure OpenAI translation
├── realtime_pipeline.py             # Milestone 3: real-time speech-to-speech loop
├── deploy_app.py                    # Milestone 4: FastAPI translation API (prototype)
├── pipeline_openai.py               # End-to-end: Azure Speech + Azure OpenAI
├── pipeline_speech_translation.py   # End-to-end: Azure Speech translation only
└── requirements.txt
```

## Milestones

| # | Focus | Status |
|---|-------|--------|
| 1 | Speech recognition and data collection | ✅ Implemented |
| 2 | Translation module (Azure OpenAI) | ✅ Implemented |
| 3 | Real-time speech-to-speech pipeline | ✅ Implemented (sentence-by-sentence) |
| 4 | FastAPI translation API | 🔄 Prototype (runs locally) |

**Future work:** cloud deployment (Azure App Service / Container Apps),
continuous audio streaming for lower latency, OTT player integration,
and formal evaluation (BLEU score and latency measurements).

## Setup

```bash
git clone https://github.com/Arun21055/AI-Real-Time-Speech-Translation.git
cd AI-Real-Time-Speech-Translation
pip install -r src/requirements.txt
```

Create a `.env` file in the project folder (never commit it):

```
AZURE_SPEECH_KEY=your_key
AZURE_SPEECH_REGION=your_region
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your_key
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
```

## Run

```bash
# Speech to text
python src/speech_to_text.py

# Translate typed text
python src/translatemodel.py

# Real-time speech to speech (English -> Spanish by default)
python src/realtime_pipeline.py
python src/realtime_pipeline.py fr fr-FR     # English -> French

# Speech translation using only Azure Speech
python src/pipeline_speech_translation.py en-US hi ta te

# Translation API (then open http://127.0.0.1:8000/docs)
uvicorn src.deploy_app:app --reload
```

### API example

```
POST /translate
{ "text": "Welcome to the live match!", "target_lang": "es" }
```

## Tech stack

Python · Azure Speech-to-Text · Azure OpenAI · FastAPI · Uvicorn · Git/GitHub

## Author

**P R Arun Kumar**, VIT-AP University
Infosys Virtual Internship 6.0 (AI Track)
