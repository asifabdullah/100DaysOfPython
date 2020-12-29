import smtplib
import datetime as dt
import random


def send_email(msg):
    my_email = "hidan.ndc@gmail.com"
    password = "asifCSE090104092"

    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="asif.ndc@gmail.com",
            msg=f"Subject:Monday Motivational\n\n{msg}"
        )

# import datetime as  dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)


# quotes_list = []
#
#
# # print(quotes_list)
#
day_of_the_week = dt.datetime.now().weekday()
if day_of_the_week == 1:
    with open(file="quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    print(quote)
    send_email(quote.encode("utf-8"))

