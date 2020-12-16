import speech_recognition as sr 
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()

def record_audio(ask = False):
    with sr. Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            alexis_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')    
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'your name' in voice_data:
        alexis_speak('Me aapka assistant Gopal')
    if 'what is the time' in voice_data:
        alexis_speak("khud dekh le jayada maje me aa raha hai kya")
        alexis_speak("chal thik hai me tera assistant hu bata raha hu verna khali peeli me kisi ko nahi batata ...! le dekh le")
        alexis_speak(ctime())    
    if 'how are you' in voice_data:
        alexis_speak('katt rahi hai zindagi meri to sir! aap bataye aapki kesi katt rhi hai') 
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?') 
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)  
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location) 
     
    if 'exit' in voice_data:
        print("thik hai ja raha hu") 
        exit()   
        
             

time.sleep(1)
alexis_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
        

    
                    
     
   