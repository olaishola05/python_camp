import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
today_tuple = (now.month, now.day)

quote = {}

try:
    df = pandas.read_csv('birthdays.csv')
except FileNotFoundError:
    print('File not found')
else:
    quote = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}


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


if today_tuple in quote:
    celebrant = quote[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", celebrant['name'])
    send_email(celebrant['email'], subject="Happy Birthday!", msg=letter)
