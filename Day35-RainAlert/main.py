import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

# This code block is required only for running in office
# proxyDict = {
#           'http': '192.168.51.61',
#           'https': '192.168.51.61'
#         }

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0d352bb3bfeda987d667d015ba4055d2"
account_sid = "AC33b4664f185f7c1a99cb212e81f2e946"
auth_token = "53bf38020cb5b27897cd2046f5929fc5"
from_mobile_no = "+12674406073"

weather_parameters = {
    "lat": 39.047344,
    "lon": -95.675156,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
# This one for office with proxy
# response = requests.get(url=OWM_Endpoint, params=weather_parameters, proxies=proxyDict)
# This one for home without proxy
response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Please bring an ☂",
            from_=from_mobile_no,
            to="+8801975247474"
        )
    print(message.status)
