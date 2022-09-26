# Get your API: https://cutt.ly/cuttly-api
# pip3 install cuttpy

from cuttpy import Cuttpy

api_key = 'YOUR_API_KEY'
cuttly = Cuttpy(api_key)

response = cuttly.shorten('https://www.google.com/')
print(response)

# <cuttpy.response.CuttpyResponse object at 0x7f65082d7610>