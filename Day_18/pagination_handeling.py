import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    books = []

    for book in soup.select(".product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").text
        rating = book.select_one("p")["class"][1]

        books.append({
            "title":title,
            "price":price,
            "rating":rating
        })
    return books

# Scrape Multiple Pages
all_books = []
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1,4):  # 3 pages
    print(f"📑  Page {page} scraping....")
    books = scrape_page(base_url.format(page))
    all_books.extend(books)
    time.sleep(1)  # Polite Scraping - server overload na ho

print(f"✅  Total books: {len(all_books)}")