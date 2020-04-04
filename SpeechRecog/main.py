
import speech_recognition as sr
from wolframAlphaFunction import *
from weatherFunction import *
from googleTranslateFunction import *
#import weatherFunction as wf



def process(text):
    words = text.split(" ")
    keyWeatherWords = []
    keyGoogleTranslateWords = []
    print(text)
    if "translate" in words:
        trans = Translate()
        return trans.DAVIDtranslator(text)
    if "weather" in words:
        wf = WeatherAnswers()
        return wf.DAVIDweather(text)
    else:
        return DAVIDwolframalpha(text)

r = sr.Recognizer()
File = open("speechfile.txt","w+")
on = True
while on:
    with sr.Microphone() as source:
        # use the default microphone as the audio source
        # listen for the first phrase and extract it into audio data
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.record(source,duration=5)
        print("Running")
    try:
        audioInput = r.recognize_google(audio)
        #File.write(audioInput)    
        #File.close()
        print(process(audioInput))
        break
        # recognize speech using Google Speech Recognition
    except sr.UnknownValueError:                            
    #    # speech is unintelligible
        print("Could not understand audio")