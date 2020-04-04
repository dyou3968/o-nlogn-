"""
#recognize_sphinx() -->CMU speech recog, can be used offline
                                               # NOTE: this requires PyAudio because it uses the Microphone class

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

"""

import speech_recognition as sr
import json


r = sr.Recognizer() 
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    #text = r.recognize_bing(audio, language = "en-US", show_all = True)
    #text = r.recognize_sphinx(audio)
    #text = r.recognize_google(audio)
    print(text)
    # sFinalResult = r.recognize_google(audio, language='en-US', show_all = True)
    # response = json.dumps(sFinalResult, ensure_ascii=False).encode('utf8')
    # print(response)
    #print("++++++++++++++++++ " + response + " ++++++++++++++++++++++++")



"""
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)

        speech = r.recognize_google(audio, language = 'pt')

        print('Você disse: ', speech)
"""


"""
    print("Speak Anything :")
    audio = r.listen(source)
    print('a')
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
"""


"""
sr.Microphone.list_microphone_names()
['Built-in Microphone', 'Built-in Output']

"""