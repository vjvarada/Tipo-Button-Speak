import subprocess
from config import PHRASES

def speak_phrase(phrase_id):
    phrase = PHRASES[phrase_id]
    subprocess.run(["espeak", phrase])