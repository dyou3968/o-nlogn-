from wolframAlphaFunction import *
from weatherFunction import *
from googleTranslateFunction import *


def process(text):
    text = text.lower()
    words = text.split(" ")
    if "homework" in words or "code" in words or "112" in words:
        return (f"Sorry, I cannot do that. That would be an academic integrity violation." + 
                f"Please ask the TAs for help. If you go any further down this path"
                f"I will have to get the real David Kosbie")
    if "language" in words or "translate" in words:
        translate = Translate()
        return translate.DAVIDtranslator(text)
    if "weather" in words or "temperature" in words:
        wf = WeatherAnswers()
        return wf.DAVIDweather(text)
    else:
        return DAVIDwolframalpha(text)

text = input("Input: ").lower()
while text != "break":
    print(process(text))
    text = input("Input: ").lower()
