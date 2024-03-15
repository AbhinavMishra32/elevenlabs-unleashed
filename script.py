from src.elevenlabs_unleashed.tts import UnleashedTTS

tts = UnleashedTTS(nb_accounts=2, create_accounts_threads=1)
"""
Will automatically generate 2 accounts in 2 threads. Takes a few seconds.
"""

tts.speak("Hello world!", voice="Josh", model="eleven_multilingual_v1", save = True)