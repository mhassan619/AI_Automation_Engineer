import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

class BookScrapper:
    def __init__(self):
        self.__base_url = "https://books.toscrape.com"
        self.__books = []
        self.__headers = {
            "User-Agent":"Mozilla/5.0 (Educational Scrapper)"
        }
    def __fetch_page(self,url):
        try:
            response = requests.get(url,headers=self.__headers,timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text,"lxml")
        except requests.exceptions.ConnectionError:
            print(f"Please check your internet connection!")
            return None
        except Exception as e:
            print(f" Error: {e}")
            return None
    def __parse_books(self,soup):
        books = []
        for book in soup.select(".product_pod"):
            title = book.select_one("h3 a")["title"]
            price = book.select_one(".price_color").text.strip()
            rating = book.select_one("p.star-rating")["class"][1]
            availability = book.select_one(".availability").text.strip()

            books.append({
                "title":title,
                "price":price,
                "rating":rating,
                "availability":availability
            })
        return books
    def scrape(self, pages=3):
        print(f" {pages} pages scrapping...")

        for page in range(1,pages + 1):
            if page == 1:
                url = f"{self.__base_url}/index.html"
            else:
                url = f"{self.__base_url}/catalogue/page-{page}.html"
            print(f" 📑  Page {page}...")
            soup = self.__fetch_page(url)
            if soup:
                books = self.__parse_books(soup)
                self.__books.extend(books)
                print(f" ✅  {len(books)} books found.")
            time.sleep(1)  # Polite scrapping
        print(f" \n🎉  Total: {len(self.__books)} books scrapped!")
    def filter_by_rating(self,rating):
        # Use a Generator
        for book in self.__books:
            if book['rating'] == rating:
                yield book
    def save(self, filename=None):
        if not filename:
            filename = f"books_{datetime.now().strftime('%Y-%m-%d')}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__books,f,indent=4)
            print(f" ✅ {len(self.__books)} books saved to {filename}")
    def report(self):
        if not self.__books:
            print(f"❌  Please Scrape First!")
            return 
        print(f"\n{'='*45}")
        print(f"  📚 BOOK SCRAPER REPORT")
        print(f"{'='*45}")
        print(f"  Total Books: {len(self.__books)}")

        # Rating distribution
        ratings = ["One","Two","Three","Four","Five"]
        print(f"\n 🌟  Rating Distribution:")
        for rating in ratings:
            books = list(self.filter_by_rating(rating))
            bar = "💈" * len(books)
            print(f"    {rating:<6}: {bar} ({len(books)})")
        print(f"{'='*45}")
# Now Run
scraper = BookScrapper()
scraper.scrape(pages=3)
scraper.report()
scraper.save()

# See Five star Books
print(f'\n 🌟  Five Star Books:')
for book in scraper.filter_by_rating("Five"):
    print(f"  --> {book['title']} - {book['price']}")