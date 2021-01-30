import requests
# from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = "YVCVPXK97J5P1LPQ"
NEWS_API_KEY = "4ef6044b996c4f34851524a1e3c5258a"

account_sid = "AC33b4664f185f7c1a99cb212e81f2e946"
auth_token = "9df651e3574dc10afd0a758f0219959b"
from_mobile_no = "+12674406073"

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_api_parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
# print(stock_data["Time Series (Daily)"])

#today = datetime.today().strftime('%Y-%m-%d')
# yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
# day_before_yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
# yesterday_closing_price = stock_data[yesterday]["4. close"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
# day_before_yesterday_closing_price = stock_data[day_before_yesterday]["4. close"]
# print(day_before_yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference < 0:
    up_down = "🔻"
else:
    up_down = "🔺"
# print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((difference / float(yesterday_closing_price) * 100))
# print(diff_percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percentage) >= 5:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    # print(three_articles)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percentage}% \nHeadline:{article['title']}\nBreif:{article['description']}" for article in three_articles]
    # print(formatted_article)
    # client = Client(account_sid, auth_token)
    # for article in formatted_article:
    #     message = client.messages \
    #         .create(
    #             body=article,
    #             from_=from_mobile_no,
    #             to="+8801975247474"
    #         )
    #     print(message.status)
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

