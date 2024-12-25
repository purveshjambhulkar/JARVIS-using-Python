from deep_translator import GoogleTranslator
from time import sleep
import pyttsx3
import speech_recognition
import os
from playsound import playsound
import time
from gtts import gTTS

# Initialize pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take command using speech recognition
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Function to translate the text
def translategl(query):
    speak("SURE SIR")
    
    # Create an instance of GoogleTranslator to access methods
    translator = GoogleTranslator()
    
    # Get supported languages by creating an instance
    supported_languages = translator.get_supported_languages()
    print("Supported Languages: ")
    print(supported_languages)
    
    speak("Choose the language in which you want to translate")
    b = input("To_Lang: ")  # Get target language input

    try:
        # Translate using deep-translator
        translated_text = GoogleTranslator(source='auto', target=b).translate(query)
        speak(f"Translated text: {translated_text}")
        
        # Convert translated text to speech using gTTS
        speakgl = gTTS(text=translated_text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        
        # Play the translated audio
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")  # Clean up by removing the saved file
    except Exception as e:
        print(f"Unable to translate: {str(e)}")