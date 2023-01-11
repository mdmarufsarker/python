import requests
import bs4

# req to get a response
res = requests.get("https://books.toscrape.com/")

# grab the source code
soup = bs4.BeautifulSoup(res.text, "lxml")

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# print(base_url.format('20'))

# for page in range(1, 51):
#     # print(base_url.format(page))
#     data = requests.get(base_url.format(page))
#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     products = soup.select('.product_pod')

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# products = soup.select('.product_pod')
# # print(products)
# example = products[0]
# stars = example.select('.star-rating.Three')
# # print(stars)
#
# title = example.select('a')[1]['title']
# print(title)

print('Loading...')

five_star_books = []
four_star_books = []
three_star_books = []
two_star_books = []
one_star_books = []

for i in range(1, 51):
    # data = requests.get(base_url.format(i))
    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")
#
    for book in books:
        if len(book.select('.star-rating.Five')) != 0:
            book_title = book.select('a')[1]['title'] # a means <a> tag
            five_star_books.append(book_title)
            print(book_title)
        elif len(book.select('.star-rating.Four')) != 0:
            book_title = book.select('a')[1]['title']
            four_star_books.append(book_title)
            print(book_title)
        elif len(book.select('.star-rating.Three')) != 0:
            book_title = book.select('a')[1]['title']
            three_star_books.append(book_title)
            print(book_title)
        elif len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_books.append(book_title)
            print(book_title)
        elif len(book.select('.star-rating.One')) != 0:
            book_title = book.select('a')[1]['title']
            one_star_books.append(book_title)
            print(book_title)

# print(five_star_books)

