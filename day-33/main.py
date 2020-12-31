import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 23.810331
MY_LNG = 90.412521
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def send_email():
    my_email = "hidan.ndc@gmail.com"
    password = "asifCSE090104092"

    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="asif.ndc@gmail.com",
            msg="Subject:Happy Birthday!!\n\nThe ISS is above you in the sky."
        )


def is_iis_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LNG - 5 <= iss_longitude <= MY_LNG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT +5 :
        return True
    return False


def is_night():
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

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iis_overhead() and is_night():
        send_email()
