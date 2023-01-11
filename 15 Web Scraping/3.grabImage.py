import requests
import bs4

# req to get a response
res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

# grab the source code
soup = bs4.BeautifulSoup(res.text, "lxml")

# link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/121px-Python-logo-notext.svg.png')
# print(link.content)

pythonImgTag = soup.select('.image img')[0] # grab the image
pythonImg = requests.get('https:' + pythonImgTag['src']) # req to the image url
print(pythonImg.content) # binary text of the image

# save image into filesystem
f = open('./img/python.png', 'wb') # write binary
f.write(pythonImg.content)
f.close()
