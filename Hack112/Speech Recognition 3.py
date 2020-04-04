
"""
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer() 
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")  
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)  
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
    print("Sphinx could not understand audio")  
except sr.RequestError as e:  
    print("Sphinx error; {0}".format(e))  

"""

import speech_recognition as sr
#sr.__version__
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    print("Running")
try:
    print("You said " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
