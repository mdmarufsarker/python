# Get your API: https://www.voicerss.org/api/

import requests

api_key = 'YOUR_API_KEY'
url = 'https://api.voicerss.org/'

Text = "Hello, this is a test"

response = requests.get(url + "?key=" + api_key + "&hl=en-us&v=Amy&src=" + Text)

# Download the audio file
with open('audio.mp3', 'wb') as f:
    f.write(response.content)

