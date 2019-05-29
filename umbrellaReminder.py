#! python
# umbrellaReminder.py - runs daily in the morning to check http://weather.gov
# of weather forecasts and sends umbrella text reminder if it will rain

import time, datetime, requests, bs4
from twilio.rest import TwilioRestClient

# Set Twilio accountSID, authorization Token, Twilio Number, Cell Number info
accountSID='ACfb6d6ec79beca5f2e1e3ee82a8a34eb3'
authToken='77094d8ec4bf9415372a0c1bbdff207d'
myTwilioNumber='+12245071928'
myCellPhone='+12246190036'

# Set program to run daily
currentTime=datetime.datetime.now()
startTime=currentTime.replace(day=currentTime.day+1, hour=4, minute=30, second=0, microsecond=0)

#while datetime.datetime.now() < startTime:
#    time.sleep(1)

while True:
    # Sets url to local forecast page, downloads page, create bs4 object
    url='''https://forecast.weather.gov/MapClick.php?lat=43.45968000000005
           &lon=-88.83970999999997#.XO6jfihKhPY'''
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html5lib')

    # Local daily forecast element, get forecast description attribute
    forecastImgElem=soup.find_all('p>img')
    print(forecastImgElem)
    forecastText=forecastImgElem[0].get('alt')

    # Send umbrella reminder text via twilio if forecast includes rain
    if 'chance of showers' in forecastText:
        twilioCli= TwilioRestClient(accountSID, authToken)
        message=twilioCli.messages.create(body='''Chance of showers today;
        remember to pack an umbrella!''', from_=myTwilioNumber, to=myCellPhone)
    time.sleep(datetime.timedelta(days=1).total_seconds())

    
