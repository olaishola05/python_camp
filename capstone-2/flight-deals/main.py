from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]['iataCode'] == '' or len(sheet_data[0]['iataCode']) < 0:
    for data in sheet_data:
        data['iataCode'] = flight_search.get_destination_code(data['city'])
    print(sheet_data)

    data_manager.data = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
