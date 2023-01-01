
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from ecapture import ecapture as ec
import sys
import wolframalpha
import pywhatkit





print("initializing Pixel")
MASTER="Saptaswa"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+MASTER)
        print("Good Morning!"+MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+MASTER)   
        print("Good Afternoon!"+MASTER)   

    else:
        speak("Good Evening!"+MASTER)  
        print("Good Evening!"+MASTER)  

    speak("initializing Pixel. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('login emailId','password')
    server.sendmail('chakrabartisaptaswa18@gmail.com', to, content)
    server.close()

 

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("sir, what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'my music' in query:
            music_dir = 'C:\\Users\\Saptaswa\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Saptaswa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chakrabartisaptaswa18@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com//home//headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            

        elif "take a photo" in query:
            # ec.capture(0,"robo camera","img.jpg")
            # ec.capture(0,"test","img.jpg")
             ec.capture(0, "pixel Camera ", "img.jpg")

        elif "no thanks" in query:
            speak("thanks for using me sir,have aa good day")
            sys.exit()

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am pixel your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Saptaswa")
            print("I was built by Saptaswa")

        elif 'ask' in query or 'question'in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="3KR25H-TY4W8QPJGA"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif  'play' in query:
            song=query.replace('play',' ')
            speak('playing'+song)
            pywhatkit.playonyt(song)


        speak("Sir,do you have any other work")

        

                   
        




        
                    

        
        
