import requests
import datetime as dt
import os


APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
HOST = os.environ['NUTRITION_HOST']
NUTRITION_ENDPOINT = f"{HOST}/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
TOKEN = os.environ['TOKEN']

req_headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

is_running = True

while is_running:
    exercise = input("Tell me which exercise you did: ")

    if len(exercise) > 0:
        params = {
            "query": exercise,
        }

        request = requests.post(NUTRITION_ENDPOINT, json=params, headers=req_headers)
        request.raise_for_status()
        exercises = request.json()['exercises']

        for exercise in exercises:
            now = dt.datetime.now()
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")

            name = exercise['name'].title()
            calorie = exercise['nf_calories']
            duration = exercise['duration_min']

            data = {
                'date': date,
                'time': time,
                'exercise': name,
                'duration': duration,
                'calories': calorie
            }

            create_row = requests.post(SHEETY_ENDPOINT, json={"workout": data}, headers=sheety_headers)
            if create_row.status_code == 200:
                print('New row added')
            elif create_row.status_code == 402:
                print("You have exhausted the free tiers for the month!")
            else:
                print(create_row.text)
    else:
        is_running = False
