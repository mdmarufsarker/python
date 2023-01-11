# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

# This solution requires that the string "No quotes found!" only occurs on the last page.
# If for some reason this string was on the other pages, we would need to be more detailed.
# "No quotes found!" in res.text

import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

url = 'http://quotes.toscrape.com/page/'

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url + str(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to Next Page
    page += 1

print(authors)

'''
{'Harper Lee', 'John Lennon', 'Thomas A. Edison', 'Terry Pratchett', 'Dr. Seuss', 'Martin Luther King Jr.', 'J.D. Salinger', 'Ernest Hemingway', 'Charles M. Schulz', 'Steve Martin', 'Ayn Rand', 'William Nicholson', 'George Bernard Shaw', 'Ralph Waldo Emerson', 'Haruki Murakami', 'J.R.R. Tolkien', 'George Carlin', 'Albert Einstein', 'Jane Austen', 'Elie Wiesel', 'Pablo Neruda', 'Suzanne Collins', 'Charles Bukowski', 'Alfred Tennyson', 'E.E. Cummings', 'W.C. Fields', 'Douglas Adams', 'George R.R. Martin', 'Jim Henson', "Madeleine L'Engle", 'James Baldwin', 'Eleanor Roosevelt', 'C.S. Lewis', 'Friedrich Nietzsche', 'André Gide', 'Stephenie Meyer', 'Khaled Hosseini', 'J.K. Rowling', 'Garrison Keillor', 'George Eliot', 'Mark Twain', 'Alexandre Dumas fils', 'Mother Teresa', 'Jimi Hendrix', 'J.M. Barrie', 'Bob Marley', 'Jorge Luis Borges', 'Helen Keller', 'Allen Saunders', 'Marilyn Monroe'}
'''