# alternate urls for if you want to specify a state or country code

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state}&appid={your api key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state},
# {country code}&appid={your api key}

"""
NOTE:
# strip punctuation 
# include the case where the person says "today" or "right now" after their 
# sentences 
"""

# Round Half Up Import
import decimal

# Web Scraping Imports
import json
import urllib
from urllib import request


# Taken https://www.cs.cmu.edu/~112/
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def weatherToString(text):
    sample = text.split(" ")
    index = sample.index("in")
    city = sample[index+1:]
    city = "+".join(city)
    # Openweathermap is the API we used to gather weather data. 
    # This site gave us information on how to access our weather data:
    # https://openweathermap.org/current
    my_url = f'''http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fea4bf62b107b32ea76781885181c0a0'''
    # TA Ping-Ya helped us with converting the text in my_url to a workable type
    # ig the next two lines 
    htmlText = urllib.request.urlopen(my_url)
    contents = htmlText.readlines()
    contents = contents[0]
    # The next line to convert from bytes to dictionaries came from this site:
    # https://www.geeksforgeeks.org/python-interconversion-between-dictionary-and-bytes/
    dictionaryContents = json.loads(contents.decode('utf-8'))
    return dictionaryContents

def kelvinToFarenheit(kelvin):
    return 32+9/5*(kelvin-273)

def DAVIDweather(text):
    report = weatherToString(text)
    weather = report["weather"][0]
    main = report["main"]
    temperature = roundHalfUp(kelvinToFarenheit((main['feels_like'])))
    city = report['name']
    weatherString = (f"Right now, the weather in {city} consists of {weather['description']}." + 
                    f' It feels like {temperature} degrees Fahrenheit.')
    return weatherString

text = "D.A.V.I.D., What's the weather like in Pittsburgh"
print(DAVIDweather(text))
