import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Zap!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Zap!")
    else:    
        speak("Good evening Zap!")
    speak("I'm Jarvis. How can I help you today?")