import os
import pyautogui
import webbrowser
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Updated dictionary with additional applications and websites
dictapp = {
    "commandprompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "vscode": "code",  # Command to launch Visual Studio Code
    "spotify": "spotify",  # Spotify executable
    "filemanager": "explorer",  # File Explorer
    "linkedin": "https://www.linkedin.com"  # LinkedIn URL
}

def openappweb(query):
    speak("Launching, Zap!")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "").replace("launch", "").replace("jarvis", "").strip()
        webbrowser.open("https://www." + query)
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                if "https://" in dictapp[app]:
                    webbrowser.open(dictapp[app])
                else:
                    try:
                        os.system(dictapp[app])
                    except Exception as e:
                        speak(f"Unable to launch {app}. Please check if it's installed.")

def closeappweb(query):
    speak("Closing, Zap!")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
    elif "two tabs" in query or "2 tabs" in query:
        pyautogui.hotkey("ctrl", "w", "ctrl", "w")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query and not dictapp[app].startswith("https://"):
                try:
                    os.system("taskkill /f /im " + dictapp[app] + ".exe")
                except Exception as e:
                    speak(f"Unable to close {app}. Please check if it's running.")
