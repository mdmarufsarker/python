# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.

import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

for item in soup.select(".tag-item"):
    print(item.text)

'''
love


inspirational


life


humor


books


reading


friendship


friends


truth


simile
'''