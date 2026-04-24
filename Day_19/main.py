from news_scrapper.scraper import HackerNewsScrapper, QuotesScraper
from news_scrapper.storage import Storage
from news_scrapper.display import Display
from config import SAVE_FILE

class NewsApp:
    def __init__(self):
        self.__storage = Storage(SAVE_FILE)
        self.__display = Display()
    def run(self):
        print(f"🗒️ News Scraper App")
        print("Commands: scrape, load, search, show, save, quit")

        while True:
            command = input("\n ").strip().lower()
            if command == "quit":
                print("👋 Good Bye!")
                break
            elif command == "scrape":
                print("\n Scraping Begin....")

                # HackerNews
                hn = HackerNewsScrapper()
                hn_stories = hn.scrape(pages=2)
                self.__storage.add(hn_stories)

                # Qoutes
                qt = QuotesScraper()
                qt_qoutes = qt.scrape(pages=2)
                self.__storage.add(qt_qoutes)

                print(f"\n ✅Total scraped: {len(self.__storage.get_all())}")
            elif command == "show":
                items = self.__storage.get_all()
                if items:
                    self.__display.items(items[:10],"Latest Items")
                else:
                    print("❌ Please Scrape!")
            elif command == "search":
                keyword = input("keyword: ").strip()
                results = list(
                    self.__storage.filter_by_keyword(keyword)
                )
                if results:
                    self.__storage.items(results, f"'{keyword}' Results")
                else:
                    print(f"❌ No result found from '{keyword}'")
            elif command == 'save':
                self.__storage.save()
            elif command == "load":
                self.__storage.load()
            else:
                print("❌ Invalid command1 (scrape/show/search/save/load/quit)")
app = NewsApp()
app.run()