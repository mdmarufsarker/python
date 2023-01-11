# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

url = 'http://quotes.toscrape.com/page/'

authors = set()

for page in range(1,10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)

'''
{'Bob Marley', 'J.R.R. Tolkien', 'W.C. Fields', 'J.D. Salinger', 'Suzanne Collins', 'George Eliot', 'George Bernard Shaw', 'James Baldwin', 'Elie Wiesel', 'Dr. Seuss', 'Ayn Rand', 'C.S. Lewis', 'John Lennon', 'Allen Saunders', 'Friedrich Nietzsche', 'George R.R. Martin', 'J.K. Rowling', 'Albert Einstein', 'Helen Keller', 'Alfred Tennyson', 'Stephenie Meyer', 'André Gide', 'Alexandre Dumas fils', 'Mother Teresa', 'William Nicholson', 'Douglas Adams', 'Jane Austen', 'Charles M. Schulz', 'Haruki Murakami', 'Marilyn Monroe', 'Charles Bukowski', 'Garrison Keillor', 'Pablo Neruda', 'Terry Pratchett', 'Eleanor Roosevelt', 'Thomas A. Edison', 'Jim Henson', 'Mark Twain', 'Steve Martin', 'Jorge Luis Borges', 'Ralph Waldo Emerson', 'Martin Luther King Jr.', 'Ernest Hemingway', 'George Carlin'}
'''