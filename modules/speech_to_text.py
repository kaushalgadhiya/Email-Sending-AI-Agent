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
