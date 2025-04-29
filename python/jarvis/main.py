import speech_recognition as sr
import webbrowser as wb
import pyttsx3
# import requests
# from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

# openAI function
# def aiProcess(command):
#     client = OpenAI(
#         api_key = "",)
    
#     completion = client.chat.completions.create(
#     model = "gpt-3.5-turbo",
#     messages = [
#         {
#             "role": "system",
#             "content": "you are a virtual assistant named Jarvis. You are a helpful assistant."
#         },
#         {
#             "role": "user",
#             "content": command
#         }]
#     )

#     return completion.choices[0].message.content

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

    # elif "news" in c.lower():
    #     r = requests.get("https://newsapi.org") # News API Key
    #     if r.status_code == 200:
    #         data = r.json()
    #         articles = data.get('articles', [])
    #         for article in articles:
    #             speak(article['title']) 

    else:
        speak("Sorry, I didn't understand that.")
        # output = aiProcess(c)
        # speak(output)

    
    
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

