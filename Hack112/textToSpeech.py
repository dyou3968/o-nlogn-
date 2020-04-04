import pyttsx3

# Taken from https://pypi.org/project/pyttsx3/
engine = pyttsx3.init()
#text='DAVID what is the weather like in Pittsburgh'
text = (f"Sorry, I cannot do that. That would be an academic integrity violation." + 
        f"Please ask the TAs for help. If you go any further down this path"
        f"I will have to get the real David Kosbie")
engine.say(text)
engine.runAndWait()