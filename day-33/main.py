import requests
from datetime import datetime

MY_LAT = 23.810331
MY_LNG = 90.412521

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def if_iis_nearby(longitude, latitude):
    if (longitude < MY_LNG - 5 or longitude < MY_LNG + 5) and (latitude < MY_LAT - 5 or latitude < MY_LAT + 5):
        return True
    return False


iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_longitude, iss_latitude)
print(iss_position)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

if if_iis_nearby(latitude=iss_latitude, longitude=iss_longitude):
    if time_now > sunset:
        print()
