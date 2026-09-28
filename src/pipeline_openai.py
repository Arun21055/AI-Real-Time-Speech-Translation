"""
Speech -> Azure Speech-to-Text -> Azure OpenAI translation -> Azure text-to-speech.
This matches the architecture in the README (Azure Speech + Azure OpenAI).
Run:  python pipeline_openai.py en-US Hindi Tamil
(the last arguments are target language NAMES; voices are mapped below)
"""
import os
import sys
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

SPEECH_KEY = os.environ["AZURE_SPEECH_KEY"]
SPEECH_REGION = os.environ["AZURE_SPEECH_REGION"]

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_KEY"],
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01"),
)
DEPLOYMENT = os.environ["AZURE_OPENAI_DEPLOYMENT"]

VOICES = {
    "Hindi": "hi-IN-SwaraNeural", "Tamil": "ta-IN-PallaviNeural", "Telugu": "te-IN-ShrutiNeural",
    "Bengali": "bn-IN-TanishaaNeural", "Marathi": "mr-IN-AarohiNeural",
    "Gujarati": "gu-IN-DhwaniNeural", "Kannada": "kn-IN-SapnaNeural",
    "Malayalam": "ml-IN-SobhanaNeural", "French": "fr-FR-DeniseNeural",
    "Spanish": "es-ES-ElviraNeural", "German": "de-DE-KatjaNeural",
    "Japanese": "ja-JP-NanamiNeural", "English": "en-US-JennyNeural",
}


def translate(text, target_language):
    resp = client.chat.completions.create(
        model=DEPLOYMENT,
        temperature=0.2,
        messages=[
            {"role": "system", "content":
                f"You are a live commentary translator. Translate the user's text into "
                f"{target_language}. Keep names and scores accurate. Reply with ONLY the translation."},
            {"role": "user", "content": text},
        ],
    )
    return resp.choices[0].message.content.strip()


def make_speaker(voice):
    cfg = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    cfg.speech_synthesis_voice_name = voice
    return speechsdk.SpeechSynthesizer(speech_config=cfg)


def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "en-US"
    targets = sys.argv[2:] or ["Hindi"]
    speakers = {t: make_speaker(VOICES[t]) for t in targets}

    stt_cfg = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    stt_cfg.speech_recognition_language = source
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=stt_cfg,
        audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True))

    def on_recognized(evt):
        if evt.result.reason != speechsdk.ResultReason.RecognizedSpeech:
            return
        text = evt.result.text
        print(f"\n[{source}] {text}")
        for lang in targets:
            start = time.time()
            translated = translate(text, lang)
            print(f"  -> [{lang}] {translated}  ({time.time() - start:.2f}s translation latency)")
            speakers[lang].speak_text_async(translated).get()

    recognizer.recognized.connect(on_recognized)
    recognizer.canceled.connect(lambda e: print(f"Canceled: {e.cancellation_details.error_details}"))

    print(f"Speak in {source}; translating to {targets}. Ctrl+C to stop.")
    recognizer.start_continuous_recognition()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        recognizer.stop_continuous_recognition()
        print("\nStopped.")


if __name__ == "__main__":
    main()
