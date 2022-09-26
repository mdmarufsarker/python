# Get your API: abstractapi.com/api/ip-geolocation-api

import requests as req
import json

api_key = 'YOUR_API_KEY'
url = 'https://ipgeolocation.abstractapi.com/v1/?api_key='

ip = input("Enter IP Address: ")
result = req.get(url + api_key + "&ip_address=" + ip)

data = json.loads(result.text)

print(data)