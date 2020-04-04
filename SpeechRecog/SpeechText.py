#import speech_recognition as sr
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