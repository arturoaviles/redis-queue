import json
import urllib.parse
import urllib.request

message = {"hello": "world"}

url = "http://0.0.0.0:11000"

req = urllib.request.Request(
    url=url
)
req.add_header('Content-Type', 'application/json; charset=utf-8')
json_data = json.dumps(message)
json_data_as_bytes = json_data.encode('utf-8')
req.add_header('Content-Length', len(json_data_as_bytes))

response = urllib.request.urlopen(req, json_data_as_bytes)

print(response.read())