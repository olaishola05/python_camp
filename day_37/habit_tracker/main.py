import datetime as dt

import requests

USERNAME = "anon12345"
TOKEN = "somethingrandomnessatnature2233@4444Wddd.,@"

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_body = {
    "id": "graph1",
    "name": "Posting Content",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graphs_endpoint, json=graph_body, headers=headers)
# print(graph_response.text)

graphs_request = requests.get(url=graphs_endpoint, headers=headers)
graphs_id = graphs_request.json()['graphs'][0]['id']

now = dt.datetime.now()
date = now.strftime("%Y%m%d")

pixel_body = {
    "date": date,
    "quantity": input("How many content did you post today? ")
}

pixel_response = requests.post(url=f"{graphs_endpoint}/{graphs_id}", json=pixel_body, headers=headers)
print(pixel_response.text)

# update_endpoint = f"{graphs_endpoint}/{graphs_id}/{date}"
# pixel_update_response = requests.put(url=update_endpoint, json={"quantity": "8"}, headers=headers)
# print(pixel_update_response.text)

