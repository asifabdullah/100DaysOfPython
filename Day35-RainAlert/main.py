import requests

# This code block is required only for running in office
proxyDict = {
          'http': '192.168.51.61',
          'https': '192.168.51.61'
        }

api_key = "0d352bb3bfeda987d667d015ba4055d2"

parameters = {
    "lat": "23.810331",
    "lon": "90.412521",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters, proxies=proxyDict)
response.raise_for_status()

print(response.json())
