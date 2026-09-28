
Speech to text · PY
"""Milestone 1: live microphone speech -> text using Azure Speech-to-Text."""
import os
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
 
load_dotenv()
 
SPEECH_KEY = os.environ["AZURE_SPEECH_KEY"]
SPEECH_REGION = os.environ["AZURE_SPEECH_REGION"]
SOURCE_LANGUAGE = os.getenv("SOURCE_LANGUAGE", "en-US")  # use "hi-IN" for Hindi
 
 
def main():
    config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    config.speech_recognition_language = SOURCE_LANGUAGE
    audio = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio)
 
    recognizer.recognizing.connect(lambda e: print(f"  ...{e.result.text}", end="\r"))
    recognizer.recognized.connect(
        lambda e: print(f"\n[{SOURCE_LANGUAGE}] {e.result.text}")
        if e.result.reason == speechsdk.ResultReason.RecognizedSpeech
        else None
    )
    recognizer.canceled.connect(lambda e: print(f"\nCanceled: {e.cancellation_details.error_details}"))
 
    print(f"Listening in {SOURCE_LANGUAGE}. Speak now. Press Ctrl+C to stop.")
    recognizer.start_continuous_recognition()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        recognizer.stop_continuous_recognition()
        print("\nStopped.")
 
 
if __name__ == "__main__":
    main()
 
