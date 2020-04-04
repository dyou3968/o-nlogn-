import pyttsx3

# Taken from https://pypi.org/project/pyttsx3/
engine = pyttsx3.init()
#text='DAVID what is the weather like in Pittsburgh'
text = "Estoy haciendo mi proyecto"
engine.say(text)
engine.runAndWait()