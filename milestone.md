# 🎯 Milestone 1 – Speech Recognition

| | |
|---|---|
| **Duration** | Weeks 1–2 |
| **Status** | ✅ Implemented |
| **Code** | `src/speech_to_text.py` |

## Objective
Capture live microphone speech and convert it to text in real time using **Azure Speech-to-Text**, with a configurable source language (English or Hindi).

## Tasks
- ✅ Set up an Azure Speech resource and connected it through the Azure Speech SDK.
- ✅ Implemented live microphone recognition with **continuous recognition** (interim and final results).
- ✅ Made the source language configurable (`en-US`, `hi-IN`, …) through an environment variable.
- ✅ Loaded credentials from environment variables (`.env`) instead of hardcoding them.

## Tools & Libraries
- `azure-cognitiveservices-speech`
- `python-dotenv`

## How to run
```bash
pip install -r src/requirements.txt
python src/speech_to_text.py
```
Speak into the microphone; recognised text is printed as you talk. Press `Ctrl+C` to stop.

## Output
```
Listening in en-US. Speak now. Press Ctrl+C to stop.
[en-US] Welcome to the live cricket match.
```

## Limitations
- Accuracy depends on microphone quality, accents and background noise.
- A formal word error rate (WER) measurement has not been done yet.

➡️ Next: [Milestone 2 – Translation](milestone2.md)
