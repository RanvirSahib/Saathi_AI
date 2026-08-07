import pyttsx3
import threading

speech_lock = threading.Lock()

def speak(text):

    with speech_lock:

        try:

            engine = pyttsx3.init()

            

            voices = engine.getProperty("voices")

            if len(voices) > 1:
                engine.setProperty(
                    "voice",
                    voices[1].id
                )

            engine.setProperty(
                "rate",
                140
            )

            engine.setProperty(
                "volume",
                1.0
            )

            engine.say(text)

            engine.runAndWait()

            engine.stop()

        except Exception as e:

            print("TTS Error:", e)