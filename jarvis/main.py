import pyttsx3
import  speech_recognition as sr
import datetime
import os
import requests
import cv2
import wikipedia
import webbrowser
import sys
import pywhatkit as kit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)

voice = voices[1]

engine.setProperty('voice', voice.id)

engine.runAndWait()
engine.stop()

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout = 1,phrase_time_limit = 5)
    try :
        print("recognizing....")
        query = r.recognize_google(audio,language = 'en-in')
        print(f" you said :{query}")
    except Exception as e:
        speak("say that again please ..")
        return None
    return query


def wish():
    hour  = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("good morning")
    elif hour > 12 and hour  <18:
        speak("good evening")
    else:
        speak("good night")
    speak("i am jarvis ,how can i help you sir!!")

if __name__=='__main__':
    # speak("this is jarvis")
    # takecommand()
    wish()
    while True:
        query = takecommand().lower()


        if "open notepad" in query.lower():
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("openning notepad")
        elif  "open visual studio" in query.lower():
            npath = "C:\\Users\\PIDUGU\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(npath)
            speak("openning visual studio")
        elif  "open my file" in query.lower():
            npath = "D:\\chaitanya"
            os.startfile(npath)
            speak("openning your file")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret ,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(58)
                if k ==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        

        elif "wikipedia" in query:
            query = query.replace("wikipedia ","")
            speak(f"searching about {query}..")
            results = wikipedia.summary(query,sentences = 2)
            speak("according wikipidia")
            speak(results)
            print(results)

        

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "open google" in query:
            speak("sir , what should i search on Google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play songs" in query:
            webbrowser.open("https://open.spotify.com/playlist/0WmSSSivbg7r2UmvYgQXx3")

        elif "send a message" in query:
            speak("sir , for whom should i send")
            ji =  takecommand().lower()
            contact = {"dad":+919063917425}

            qwe = contact.get(ji)
            speak(f"what meassage you want to send {qwe}")
            mes =  takecommand().lower()

            kit.sendwhatmsg(f"{ji}",f"{mes}",22,57)
        elif "no thanks" in query:
            speak("thanks  for using ")
            sys.exit()
        speak("sir , any other tasks??")
