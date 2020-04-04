from wolframAlphaFunction import *
from weatherFunction import *
from googleTranslateFunction import *


def process(text):
    words = text.split(" ")
    keyWeatherWords = []
    keyGoogleTranslateWords = []
    if "translate" in words:
        return DAVIDtranslator(text)
    if "weather" in words:
        return DAVIDweather(text)
    else:
        return DAVIDwolframalpha(text)

text = input("Input: ").lower()
while text != "break":
    print(process(text))
    text = input("Input: ").lower()

        