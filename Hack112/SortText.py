from wolframAlphaFunction import *
from weatherFunction import *
from googleTranslateFunction import *


def process(text):
    text = text.lower()
    words = text.split(" ")
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
