import speech_recognition as sr
import wikipedia as wiki
import psutil
import subprocess
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, cannot understand')
        except sr.RequestError:
            speak('Sorry my service is down')
        return voice_data



def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    battery = psutil.sensors_battery()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if 'what is your name' in voice_data:
        speak('I am AUTOBOT , your personal assistant :-) ')
    if 'time' in voice_data:
        speak(current_time)
    if 'search' in voice_data:
        search=record_audio('What do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('This is what I found for '+ search)
    if 'find location' in voice_data:
        locate=record_audio('What do you want to locate ?')
        url = 'https://google.nl/maps/place/' + locate + '/&amp'
        webbrowser.get().open(url)
        speak('LOCATION LOCATED '+ locate)
    if 'article' in voice_data:
        query = record_audio('what do you want to know ?')
        speak((wiki.summary("" + query, sentences=2)))
    if 'calculate' in voice_data:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        speak('calculator opened')
    if 'battery' in voice_data:
        bat =str(battery.percent)
        speak('power remaining ' + bat +' percentage')
    if 'note' in voice_data:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        speak('notepad opened')
    if 'my name' in voice_data:
        speak('Your good name is Vishwa')
    if 'social' in voice_data:
        url='https://www.instagram.com/vizz_01_official/'
        webbrowser.get().open(url)
        speak('your instagram profile')
    if 'exit' or 'bye' in voice_data:
        exit()

    
time.sleep(2)
speak('How can I help you ?')
while 1:
    voice_data = record_audio()
    respond(voice_data)