#import SpeechRecognition as sr
import speech_recognition as sr
def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand."
    except sr.RequestError:
        return "Speech service error."
# 

# # Step 1: Initialize the recognizer
# recognizer = sr.Recognizer()

# # Step 2: Use the microphone to capture audio
# with sr.Microphone() as source:
#     print("🎤 Speak something...")
#     audio = recognizer.listen(source)

#     try:
#         # Step 3: Convert audio to text using Google API
#         text = recognizer.recognize_google(audio)
#         print("📝 You said:", text)

#     except sr.UnknownValueError:
#         print("Sorry, I could not understand what you said.")
#     except sr.RequestError:
#         print("Sorry, there was a problem connecting to the service.")
# modules/speech_to_text.py

# import whisper
# import sounddevice as sd
# import numpy as np
# import tempfile
# import scipy.io.wavfile

# model = whisper.load_model("base")  # Or use "small", "medium", "large"

# def capture_voice():
#     fs = 16000  # Sampling rate
#     duration = 5  # Seconds to record

#     print("Recording...")
#     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()
#     print("Recording done.")

#     # Save to temporary WAV file
#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
#         scipy.io.wavfile.write(tmp.name, fs, recording)
#         result = model.transcribe(tmp.name)
#         return result["text"]


