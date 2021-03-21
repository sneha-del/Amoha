import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
#import pywhatkit
import cv2
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning !!')
    elif hour>=12 and hour<17:
        speak('good afternoon!!')
    else:
        speak(" good night! !")
        
    speak('I am your voice assistant ! amoha IS MY NAME!! how can I help you?')   

def takeCommand(self):
    #it takes microphone input from user and returns str
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        print(" Listening..")
        r.pause_threshold=1 #for any gap while speaking
        audio=r.listen(source) 
        
        try:
            print("Understanding")
            query=r.recognize_google(audio,language='en-in')
            print(f"you said: {query}\n")
        except Exception as e:
            print("say that again please....")
            return "None"
        return query


if __name__ == "__main__":
   wishMe()
   #speak("hey there sneha from amity university")
   while True:
    self.query = takeCommand().lower()
   #logic for executing task
    if 'wikipedia' in query:
       speak('searching wikipedia..')
       query =query.replace("wikipedia","")
       results=wikipedia.summary(query, sentences=2)
    #    print(results)
    #    speak(results)
       speak("According to wikipedia") 
       print(results)
       speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open codechef'in query:
        webbrowser.open("codechef.com")
    elif 'the time'in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is{strTime}")
    elif 'open code'in query:
        code_path="C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
        os.startfile(code_path)
    
    elif 'open camera' in query:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('WebCam',img)
            k=cv2.waitKey(50)
            if k==7:
                break;
        cap.release()
        cv2.destroyAllWindows()
    elif 'open google'in query:
        speak("What should I search on google ?")
        cm=takeCommand().lower()
        webbrowser.open(f"{cm}")
    # elif 'send message' in query:
    #     kit.sendwhatmsg("number","I am doing something with pythons so please ignore this and keep studying :)",15,28)
    elif 'alarm' in query:
        speak("please tell me the time to set alarm. For example, set alarm to 4:30 AM")
        tt=takeCommand()
        tt=tt.replace("set alarm to","")
        tt=tt.replace(".","")
        tt=tt.upper()
        import MyAlarm
        MyAlarm.alarm(tt)


    elif 'no thanks' in query:
        speak("have a good day")
        sys.exit()

    speak("Any other work for me ??")


        
        

        

        