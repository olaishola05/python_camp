import smtplib
import datetime as dt
import random


# if mail server equal gmail add port "port=587"

def send_email(to_email, subject, msg):
    user_email = "mula@mailer.com"
    password = "adsacascascQ23@.ccdcc"

    with smtplib.SMTP("smtp.mailprovider.com") as connection:
        connection.starttls()
        connection.login(user=user_email, password=password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{msg}"
        )


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file_data:
        quotes = file_data.readlines()
        quote = random.choice(quotes)
    send_email(to_email='helenofsparta@mail.com', subject="Monday Motivation", msg=quote)
