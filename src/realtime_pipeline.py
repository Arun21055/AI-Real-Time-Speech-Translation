"""
Real-Time Speech-to-Speech Translation Pipeline - Milestone 3
Requires: Azure Speech SDK + Azure OpenAI

Usage:
    python src/realtime_pipeline.py            # English -> Spanish (default)
    python src/realtime_pipeline.py fr fr-FR   # English -> French
    python src/realtime_pipeline.py hi hi-IN   # English -> Hindi
"""

import os
import sys
import time
import azure.cognitiveservices.speech as speechsdk
from openai import AzureOpenAI

# ---------- CONFIGURATION ----------
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY", "YOUR_AZURE_SPEECH_KEY")
SERVICE_REGION = os.getenv("AZURE_SERVICE_REGION") or os.getenv("AZURE_SPEECH_REGION", "YOUR_REGION")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_OPENAI_KEY")
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")  # your deployment name

# ---------- INITIALISE CLIENTS ----------
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
speech_config.speech_recognition_language = "en-IN"
translation_client = AzureOpenAI(
    api_key=OPENAI_KEY,
    api_version="2024-06-01",
    azure_endpoint=OPENAI_ENDPOINT,
)


# ---------- TRANSLATION FUNCTION ----------
def translate_text(text, target_lang="es"):
    response = translation_client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        temperature=0.2,
        messages=[
            {"role": "system", "content":
                f"Translate the user's English text to {target_lang}. Reply with ONLY the translation."},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content.strip()


# ---------- TEXT-TO-SPEECH FUNCTION ----------
def speak_text(text, lang_code="es-ES"):
    tts_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
    tts_config.speech_synthesis_language = lang_code
    tts_audio = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=tts_config, audio_config=tts_audio)
    synthesizer.speak_text_async(text).get()  # .get() waits until audio finishes playing


# ---------- MAIN LOOP ----------
def run_pipeline(target_lang="es", voice_lang="es-ES"):
    print(f"Speak in English - translating to '{target_lang}' and speaking back. Ctrl+C to stop.")
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    try:
        while True:
            print("\nListening...")
            result = recognizer.recognize_once_async().get()

            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                original = result.text
                print(f"Recognised: {original}")

                start = time.time()
                translated = translate_text(original, target_lang)
                print(f"Translated: {translated}  ({time.time() - start:.2f}s)")

                speak_text(translated, voice_lang)
                time.sleep(0.5)
            elif result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech detected.")
            elif result.reason == speechsdk.ResultReason.Canceled:
                details = result.cancellation_details
                print(f"Cancelled: {details.reason} - {details.error_details}")
                break
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "es"
    voice = sys.argv[2] if len(sys.argv) > 2 else "es-ES"
    run_pipeline(lang, voice)
