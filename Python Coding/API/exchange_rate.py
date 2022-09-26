# Get Your API: https://currencyapi.com/docs/

import requests as req

api_key = 'YOUR_API_KEY'
url = 'https://api.currencyapi.net/v3/latest?apiKey='

result = req.get(url + api_key)
data = result.json()['rates']

for currency in data:
    print(currency, " : ", data[currency]['rate'])