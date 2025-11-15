import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

#pip install pocketphinx

engine =pyttsx3.init()
newsapi="96716dd069684b549c1e3f325d3d2ac2"

def speak(text):
    engine.say( text)
    engine.runAndWait()

def processCommand(c):
    if"open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkdin.com")
    elif"open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/?utm_source=google&utm_medium=paidsearch_brand&utm_campaign=GOOG_C_SEM_GBR_Core_CHT_BAU_ACQ_PER_MIX_ALL_APAC_IN_EN_032525&utm_term=gpt&utm_content=177344202655&utm_ad=741704613330&utm_match=e&gad_source=1&gad_campaignid=22370388714&gbraid=0AAAAA-IW-UW5yHqyqDu6tw7IyCQRtD3lS&gclid=CjwKCAjw6vHHBhBwEiwAq4zvAzWkR8t94xp7gs6yKO10tgoiQn5Dv26Z0EAu1QbRzYk4uv5cChgh-xoCkfAQAvD_BwE")
    elif c.lower().startswith("play"):
        song=c.split(" ")[1]
        musiclibrary.music[song]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2025-10-28&sortBy=popularity&apiKey={newsapi}")
        if r.request_code == 200:
            #parse the JSON response
            data= r.json()
        
        # extract the article
        articles= data.get('articles',[])
        #Print the headlines
        for article in articles:
            speak(article['title'])

    else:
        # let open ai handel the request
        pass







if __name__ == "__main__":
    speak("Initializing Jarvis .......")
    while True:
        # Listen  for the wake word "Jervis"
        # Obtain audio from the microphone 

        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening ...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

                
        except Exception as e:
            print(" Error; {0}".format(e))