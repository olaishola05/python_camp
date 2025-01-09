import requests
from dotenv import load_dotenv
import os

load_dotenv()
sheety_price_endpoint = os.environ["SHEETY_PRICE_ENDPOINT"]


class DataManager:
    def __init__(self):
        self.data = {}

    def get_destination_data(self):
        request = requests.get(url=sheety_price_endpoint)
        self.data = request.json()["prices"]
        return self.data

    def update_destination_code(self):
        for city in self.data:
            data = {
                "iataCode": city['iataCode']
            }
            response = requests.put(url=f"{sheety_price_endpoint}/{city['id']}", json={"price": data})
            print(response.text)
