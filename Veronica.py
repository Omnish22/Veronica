import pyttsx3
# import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

#-----------------------------------------------------

engine=pyttsx3.init('sapi5')

#===========================

''' set voice type '''
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

#********************************************

''' set rate '''
rate=engine.getProperty("rate")
engine.setProperty("rate",170)

#-------------------------------------------------------------------------------------

''' functions '''

def speak(audio):
    ''' this function will let your virtual assisstant speak '''
    engine.say(audio)
    engine.runAndWait()

#********************************************************************

def wishme():
    ''' this function help to wish the user '''
    hour=int(datetime.datetime.now().hour)

    if 0<hour<12:
        speak('Good Morning Omnish Sir')
    
    elif 12<=hour<17:
        speak('good afternoon Omnish Sir')
    
    else:
        speak('good evening Omnish Sir')
    
    speak('I am Veronica, virtual assisstant of this system, how may I help you')

#******************************************************************************************

def takecommand():
    ''' it takes user voice input via microphone and gives a string as output '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listining........')
        r.pause_threshold=1
        r.energy_threshold=500
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio=r.listen(source)
        print('Listining completed')

 
    try:
        print('Recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f'you said: {query}\n')
        # print(type(audio))

    except Exception:
        print('say that again please.....')
        return 'None'
    return query

#------------------------------------------------------------------------

if __name__ == "__main__":
    # print(sr.Microphone.list_microphone_names())
    wishme()
    while True:
        q=takecommand().lower()

        ''' functions based on input commands '''
        if 'wikipedia' in q:
            speak('searching wikipedia...')
            searching_item=q.replace('wikipedia','')
            results=wikipedia.summary(searching_item)
            speak(results)

        elif 'open youtube' in q:
            webbrowser.open('youtube.com')

        elif 'open google' in q:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in q:
            webbrowser.open('stackoverflow.com')

        elif 'open anime' in q:
            webbrowser.open('www1.9anime.to')

        elif 'play music' in q:
            song_no=random.randrange(0,111,1)
            file='F:\\MP3 Songs\\KK'
            songs=os.listdir(file)
            os.startfile(os.path.join(file,songs[song_no]))

        elif 'time' in q:
            time=datetime.datetime.now().strftime("%H %M")
            speak(time)

        elif 'open notepad' in q:
            file_path="C:\\Users\\MY LENOVO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(file_path)