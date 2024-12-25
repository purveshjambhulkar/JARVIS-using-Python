import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import pyautogui
from plyer import notification 
from pygame import mixer
import speedtest

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
        
from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query

def set_alarm(time_string):
    """Write alarm time to a file for Alarm.py."""
    try:
        with open("Alarm.txt", "w") as alarm_file:
            alarm_file.write(time_string)
        os.startfile("Alarm.py")
        speak("Alarm set successfully.")
    except Exception as e:
        speak("Failed to set the alarm. Please try again.")
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok zap , you can call me anytime")
                    break

                elif "how are you" in query:
                    speak("I'm fine, thank you for asking. How about you ?")
                
                elif "i am fine" in query:
                    speak("That's great to hear. How can i help you today ?")
                
                elif "thank you" in query:
                    speak("You're welcome. Anytime")
                    
                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")

                elif "play" in query:
                    pyautogui.press("k") 
                    speak("Video played")  

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video unmuted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    volumeup()
                    speak("Volume increased")

                elif "volume down" in query:
                    from keyboard import volumedown
                    volumedown()
                    speak("Volume decreased")


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("jarvis", "").strip()
                    speak("You told me to remember: " + rememberMessage)
                    with open("Remember.txt", "w") as remember_file:
                        remember_file.write(rememberMessage)

                elif "do you remember anything" in query:
                    try:
                        with open("Remember.txt", "r") as remember_file:
                            remembered_text = remember_file.read().strip()
                            if remembered_text:
                                speak("I remember you told me: " + remembered_text)
                            else:
                                speak("I don't remember anything. You haven't told me to remember anything yet.")
                    except FileNotFoundError:
                        speak("I don't have anything remembered yet.")


                elif "news" in query:
                      from NewsRead import latestnews
                      latestnews()
                    
                elif "calulate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calulate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)
                
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                
                
                elif "schedule my day" in query:
                    tasks = []  # Empty list to store tasks
                    speak("Do you want to clear old tasks? Please say YES or NO.")
                    query = takeCommand().lower()
                    
                    if "yes" in query:
                        # Overwrite the tasks file if the user says YES
                        with open("tasks.txt", "w") as file:  # Open the file in 'w' mode to clear it
                            file.write("")  # Clear the content of the file
                        speak("Old tasks cleared. Please enter new tasks.")
                        
                        # Prompt the user to enter new tasks
                        no_tasks = int(input("Enter the number of tasks: "))
                        for i in range(no_tasks):
                            task = input(f"Enter task {i+1}: ")
                            tasks.append(task)
                            with open("tasks.txt", "a") as file:  # Append new tasks to the file
                                file.write(f"{i+1}. {tasks[i]}\n")
                                
                    elif "no" in query:
                        # Just add tasks without clearing the old ones
                        no_tasks = int(input("Enter the number of tasks: "))
                        for i in range(no_tasks):
                            task = input(f"Enter task {i+1}: ")
                            tasks.append(task)
                            with open("tasks.txt", "a") as file:  # Append tasks to the existing file
                                file.write(f"{i+1}. {tasks[i]}\n")

                
                elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notificatiomn.wav")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                        speak("I have shown your schedule")
                        
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                    
                elif "close" in query:
                    query = query.replace("close","")
                    query = query.replace("jarvis","")
                    pyautogui.hotkey("alt", "f4")
                    speak(f"{query} closed successfully")
                
                
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    
                elif "screenshot" in query:
                    import pyautogui 
                    im = pyautogui.screenshot()
                    im.save("screenshot.jpg")
                    speak("Screenshot taken successfully")
                
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(1)
                    speak("Smile please")
                    pyautogui.press("enter")
                    
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\Purvesh\\JARVIS\\FocusMode.py")
                        exit()

                    
                    else:
                        pass
                
                
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                    
                elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("jarvis","")
                        query = query.replace("translate","")
                        translategl(query)                  

                    
                
###################################################33       
                elif "exit" in query:
                        speak("Goodbye zap. Have a nice day!")
                        exit()

                elif "set an alarm" in query:
                    speak("Please say the alarm time in HH and MM format.")
                    print("Example input: 10 and 30 for 10:30.")
                    time_string = input("Enter time: ").strip()
                    set_alarm(time_string)
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                    
                elif "shutdown" in query:
                    speak("Are you sure you want to shutdown your computer ?")
                    query = takeCommand().lower()
                    if "yes" in query:
                        os.system("shutdown /s /t 1")
                    elif "no" in query:
                        speak("Shutdown cancelled")
                 
                 
                 
                    



                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)



                elif "google" in query:
                    speak("Searching on Google")
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    speak("Searching on YouTube")
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    speak("Searching on Wikipedia")
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "weather in Jambhul, Pune, Maharashtra"
                    url = "http://www.google.com/search?q="+search
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The temperature outside is {temp}")

                elif "weather" in query:
                    search = "weather in Jambhul, Pune, Maharashtra"
                    url = "http://www.google.com/search?q="+search
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The temperature outside is {temp}")

                elif "the time" in query:
                    strTime = datetime.now().strftime("%I:%M:%S %p")
                    speak(f"The time is {strTime}")