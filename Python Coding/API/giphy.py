# Get Your API : https://developers.giphy.com/

import json
import requests

api_key = 'YOUR_API_KEY'
url = 'https://api.giphy.com/v1/gifs'

param = {
    'q': 'funny cat',
    'api_key': api_key,
    'limit': "10"
}

response = requests.get(url, params = param)
data = json.loads(response.text)

result = json.dumps(data, indent = 4, sort_keys = True)

print(result)

# {
#     "data": [],
#     "meta": {
#         "msg": "Unauthorized",
#         "response_id": "",
#         "status": 401
#     }
# }