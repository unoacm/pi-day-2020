import urllib.parse
import urllib.request
import json
from gpiozero import LED
from signal import pause

# GPIO for each LED
red = LED(18)
green = LED(23)
blue = LED(25)

# calling API
#TODO: Accept input from user as to which city they want weather for
url = 'http://dataservice.accuweather.com/currentconditions/v1/349291?apikey=erQ27hOkCc4pKYcahzToxMAtLbS1wEfM'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    resp = json.loads(response.read())
    
    if resp[0]['HasPrecipitation'] == 'True':
        blue.on()
        pause()
    elif resp[0]['WeatherText'] == 'Cloudy':
        green.on()
        pause()
    else:
        red.on()
        pause()