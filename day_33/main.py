import time
import requests
from datetime import datetime as dt
import smtplib

MY_LAT = 51.507351
MY_LNG = -0.127758


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position = response.json()

    iss_latitude = float(position["iss_position"]["latitude"])
    iss_longitude = float(position["iss_position"]["longitude"])

    # My position is within +5 or -5 degree of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]

    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        user_email = "mula@mailer.com"
        password = "adsacascascQ23@.ccdcc"

        with smtplib.SMTP("smtp.mailprovider.com") as connection:
            connection.starttls()
            connection.login(user=user_email, password=password)
            connection.sendmail(
                from_addr=user_email,
                to_addrs=user_email,
                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky!"
            )
