
Pipeline speech translation · PY
"""
End-to-end real-time speech-to-speech translation using ONLY Azure Speech
(no Azure OpenAI needed). Speak -> recognize -> translate -> speak in target language.
Run:  python pipeline_speech_translation.py en-US hi ta te
"""
import os
import sys
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
 
load_dotenv()
 
SPEECH_KEY = os.environ["AZURE_SPEECH_KEY"]
SPEECH_REGION = os.environ["AZURE_SPEECH_REGION"]
 
# target language code -> Azure neural voice
VOICES = {
    "hi": "hi-IN-SwaraNeural", "ta": "ta-IN-PallaviNeural", "te": "te-IN-ShrutiNeural",
    "bn": "bn-IN-TanishaaNeural", "mr": "mr-IN-AarohiNeural", "gu": "gu-IN-DhwaniNeural",
    "kn": "kn-IN-SapnaNeural", "ml": "ml-IN-SobhanaNeural", "fr": "fr-FR-DeniseNeural",
    "es": "es-ES-ElviraNeural", "de": "de-DE-KatjaNeural", "ja": "ja-JP-NanamiNeural",
    "en": "en-US-JennyNeural",
}
 
 
def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "en-US"
    targets = sys.argv[2:] or ["hi"]
 
    trans_cfg = speechsdk.translation.SpeechTranslationConfig(
        subscription=SPEECH_KEY, region=SPEECH_REGION)
    trans_cfg.speech_recognition_language = source
    for lang in targets:
        trans_cfg.add_target_language(lang)
 
    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=trans_cfg,
        audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True))
 
    # One speech synthesizer per target language (plays through the default speaker)
    speakers = {}
    for lang in targets:
        cfg = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        cfg.speech_synthesis_voice_name = VOICES.get(lang, VOICES["en"])
        speakers[lang] = speechsdk.SpeechSynthesizer(speech_config=cfg)
 
    def on_recognized(evt):
        r = evt.result
        if r.reason != speechsdk.ResultReason.TranslatedSpeech:
            return
        print(f"\n[{source}] {r.text}")
        for lang, text in r.translations.items():
            print(f"  -> [{lang}] {text}")
            speakers[lang].speak_text_async(text).get()  # blocks until spoken
 
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
 
