import speech_recognition as sr
#sr.__version__
r = sr.Recognizer()
File = open("speechfile.txt","w+")
on = True
while on:
    with sr.Microphone() as source:
        # use the default microphone as the audio source
        # listen for the first phrase and extract it into audio data
        audio = r.listen(source)
        print("Running")
    try:
        audioInput = r.recognize_google(audio)
        File.write(audioInput+'_')    
        if (audioInput == "stop"):
            on = False
            File.close()
        # recognize speech using Google Speech Recognition
    except sr.UnknownValueError:                            
    #    # speech is unintelligible
        print("Could not understand audio")
        