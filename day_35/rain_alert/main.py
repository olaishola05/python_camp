import requests
from twilio.rest import Client
import os

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ['OWM_API_KEY']
account_sid = 'twilio_sid'
auth_token = 'twilio_auth_token'

weather_params = {
    "lat": 7.842958,
    "lon": 3.936844,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Its going to rain today, pls bring umbrella ☔️",
            from_='twilio generated phone number',
            to='Your verified number'
        )

    print(message.status)
