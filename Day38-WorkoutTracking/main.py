import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "160"
AGE = "31"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
exercises = response.json()["exercises"]
for exercise in exercises:
    url = SHEET_ENDPOINT
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "workout":{
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=url, json=params, headers=headers)
    print(response.text)
# print(result)

# #No Authentication  
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
  
# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint, 
#   json=sheet_inputs, 
#   auth=(
#       YOUR USERNAME, 
#       YOUR PASSWORD,
#   )
# )

# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     headers=bearer_headers
# )
