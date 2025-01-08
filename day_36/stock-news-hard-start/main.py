import datetime as dt
import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

now = dt.datetime.now()
stock_apikey = os.getenv('STOCK_API_KEY')
news_apikey = os.getenv('NEWS_API_KEY')
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''

stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': stock_apikey
}

news_params = {
    'qInTitle': COMPANY_NAME,
    'from': now.date(),
    'sortBy': 'popularity',
    'apiKey': news_apikey
}

response = requests.get(STOCK_ENDPOINT, stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_closing_price = day_before_yesterday["4. close"]

price_diff = float(yesterday_closing_price) - float(day_before_closing_price)

up_down = None
if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_diff = round((price_diff / float(yesterday_closing_price)) * 100)

if abs(percentage_diff) > 2:  # for testing purpose base on current diff
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    articles = news_response.json()["articles"]
    first_three_articles = articles[:3]
    # article_list = [value for (key, value) in first_three_articles.items()]
    formatted_articles = [f"{STOCK}: {up_down}{price_diff}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                          first_three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='twilio virtual number',
            to='recipient number'
        )
