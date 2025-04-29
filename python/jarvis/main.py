import speech_recognition as sr
import webbrowser as wb
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        wb.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        wb.open("https://www.youtube.com")
    elif "open stack overflow" in c.lower():
        speak("Opening Stack Overflow")
        wb.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        speak("Opening GitHub")
        wb.open("https://github.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)
    
    
if(__name__ == "__main__"):
    speak("Initializing Jarvis...")

    while True:
        # listen for the wake word "Jarvis"
        r = sr.Recognizer()
        
        #recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            # print(command)
        except Exception as e:
            print("Error; {0}".format(e))

