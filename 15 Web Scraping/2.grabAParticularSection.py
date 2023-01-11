import requests
import bs4

# req to get a response
res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

# grab the source code
soup = bs4.BeautifulSoup(res.text, "lxml")

# select all the classes named toclevel-1
contents = soup.select('.toclevel-1')

for i in contents:
    print(i.text)