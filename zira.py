import pyttsx3;
import datetime;
import speech_recognition as sr;
import pyaudio;
import wikipedia;
import webbrowser
import os;

engine=pyttsx3.init("sapi5");
voices=engine.getProperty('voices');
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio);
    engine.runAndWait();
    pass
def wishme():
    hour=int(datetime.datetime.now().hour);
    if(hour>=0 and hour<12):
        print("Zira: good morning sir")
        speak("good morning sir")
    elif(hour>=12 and hour<18):
        print("Zira : good afternoon sir ")
        speak("good afternoon sir ");
    else:
        print(" Zira : good evening sir ")
        speak("good evening sir");
    print(" i am Zira please Tell me how may i help you")
    speak(" i am Zira please Tell me how may i help you")
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)  
            query = r.recognize_google(audio, language="en-US")
            print(f"User Said: {query}")
        except Exception as e:
            print("Please say agian");
            speak("sorry for inconvience  please speak again ")
            return 'None'
        return query
if __name__=='__main__':
    wishme();
    while(True):
        query=takeCommand().lower();
        if 'wikipedia' in query:
            speak("searching in wikipedia");
            query=query.replace("wikipedia","");
            results=wikipedia.summary(query,sentences=2);
            print("Zira  :",results)
            speak("According to wikipedia ");
            speak(results)
        elif 'open google' in query:
            print("Zira: opening google")
            webbrowser.open("www.google.com")
        elif 'open youtube' in query:
            print("Zira:opening youtube")
            speak("opening youtube");
            webbrowser.open("www.youtube.com")
        elif 'open chatgpt' in query:
            print("Zira : opening chatgpt")
            speak("opening chatgpt");
            webbrowser.open("www.chatgpt.com");
        elif 'open stackoverflow' in query:
            print("Zira : opening stackoverflow")
            speak("opening stackoverflow");
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in query:
            music_dir="C:\Music";
            songs=os.listdir(music_dir);
            print(songs);
            os.startfile(os.path.join(music_dir,songs[0]));
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Zira:sir the time is {strTime}")
            speak(f"sir the time is {strTime}");
        elif "close this chat" in query:
            speak("Had a great time with you sir, have a good day Bye");
            break;
        
      