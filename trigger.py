import requests

url = "http://0.0.0.0:11000"
message = {"hello": "world"}

try:
    response = requests.post(url=url, json=message)
except requests.RequestException as error:
    print(error)
else:
    print(response.json())