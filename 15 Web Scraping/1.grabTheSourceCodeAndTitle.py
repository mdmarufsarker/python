import requests
import bs4

result = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(result.text, "lxml") # returns the source code
# print(soup)

websiteTitle = soup.select('title')[0].getText()
print(websiteTitle)

print(soup.select('p')[0].getText())