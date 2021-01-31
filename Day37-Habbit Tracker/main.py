import requests
from datetime import datetime
USERNAME = "asif"
TOKEN = "12334456"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":	"Coding Hours",
    "unit": "hours",
    "type": "float",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# today =datetime(year=2021, month=1,day=30)
today =datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?")
}
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_update = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_update, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)