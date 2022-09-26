# Get your api: https://scrapestack.com/

import requests as req

api_key = 'YOUR_API_KEY'
url = 'https://www.amazom.com/'
param = {
    'access_key': api_key,
    'url': url,
}

response = req.get('http://api.scrapestack.com/scrape', param)

website_data = response.content
print(website_data)


# b'{\n  "success": false,\n  "error": {\n    "code": 101,\n    "type": "invalid_access_key",\n    "info": "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]"\n  }\n}\n'