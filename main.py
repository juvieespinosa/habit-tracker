import requests
from datetime import datetime

TOKEN = "YOUR TOKEM"
USERNAME = "YOUR USERNAME"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Intermittent Fasting Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you fast today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

#REFERENCES:
#TO UPDATE DATA:
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# put_config = {
#     "quantity": "17.00"
# }

# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)


#TO DELETE DATA:
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)