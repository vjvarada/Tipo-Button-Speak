import pyttsx3
from config import PHRASES

def generate_audio_files():
    engine = pyttsx3.init()
    for phrase_id, phrase in PHRASES.items():
        filename = f"audio/phrase_{phrase_id}.wav"
        engine.save_to_file(phrase, filename)
    engine.runAndWait()

if __name__ == "__main__":
    generate_audio_files()