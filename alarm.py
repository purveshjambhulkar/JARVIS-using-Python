import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Read the time from Alarm.txt
with open("Alarm.txt", "r") as file:
    Alarmtime = file.read().strip()

print(f"Alarm Time Set: {Alarmtime}")

def ring(Alarmtime):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Current Time: {current_time}")  # Debugging
        if current_time == Alarmtime:
            speak("Alarm ringing!")
            os.startfile("notificatiomn.wav")  # Ensure this file exists
            break

ring(Alarmtime)
