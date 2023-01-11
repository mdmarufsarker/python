# TASK: Get the names of all the authors on the first page.

import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

soup.select(".author")

# I used a set to not worry about repeat authors.
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

'''
{
    'Eleanor Roosevelt', 
    'André Gide', 
    'Albert Einstein', 
    'Thomas A. Edison', 
    'J.K. Rowling', 
    'Steve Martin', 
    'Jane Austen', 
    'Marilyn Monroe'
}
'''