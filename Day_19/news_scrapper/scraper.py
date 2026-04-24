import requests
from bs4 import BeautifulSoup
import time

class HackerNewsScrapper:
    def __init__(self):
        self.__url = "https://news.ycombinator.com"
        self.__headers = {
            "User-Agent":"Mozilla/5.0 (Educational Project)"
        }
    def scrape(self,pages=2):
        all_stories = []
        for page in range(1,pages + 1):
            print(f" 🗒️ HackerNews Page {page}...")
            try:
                url = f"{self.__url}?p={page}"
                response = requests.get(
                    url,
                    headers=self.__headers,
                    timeout=10
                )
                response.raise_for_status()
                soup = BeautifulSoup(response.text,"lxml")
                stories = self.__parse(soup)
                all_stories.extend(stories)
                print(f" ✅ {len(stories)} Stories found.")
                time.sleep(1)
            except Exception as e:
                print(f" ❌ Error: {e}")
        return all_stories
    def __parse(self,soup):
        stories = []
        items = soup.select(".athing")
        for item in items:
            try:
                title_tag = item.select_one(".titleline a")
                if not title_tag:
                    continue
                title = title_tag.text.strip()
                link = title_tag.get("href","N/A")

                # Scores and comments are in next row
                subtext = item.find_next_sibling("tr")
                score_tag = subtext.select_one(".score") if subtext else None
                score = score_tag.text if score_tag else "0 Points"

                stories.append({
                    "source":"HackerNews",
                    "title":title,
                    "link":link,
                    "score":score
                })
            except Exception:
                continue
        return stories
class QuotesScraper:
    def __init__(self):
        self.__url = "https://qoutes.toscrape.com"
        self.__headers = {
            "User-Agent":"Mozilla/5.0 (Educational Project)"
        }
    def scrape(self,pages=2):
        all_qoutes = []
        for page in range(1, pages + 1):
            print(f" 🗒️ Qoutes page {page}...")
            try:
                url = f"{self.__url}/page/{page}"
                response = requests.get(
                    url,
                    headers=self.__headers,
                    timeout=10
                )
                soup = BeautifulSoup(response.text,"lxml")
                qoutes = self.__parse(soup)
                all_qoutes.extend(qoutes)
                print(f" ✅ {len(qoutes)} qoutes found!")
                time.sleep(1)
            except Exception as e:
                print(f" ❌ Error: {e}")
        return all_qoutes
    def __parse(self,soup):
        qoutes = []
        for q in soup.select(".qoute"):
            try:
                text = q.select_one(".text").text.strip()
                author = q.select_one(".author").text.strip()
                tags = [t.text for t in q.select(".tag")]
                qoutes.append({
                    "source":"QuotesToScrape",
                    "title":f"{text[:60]}...",
                    "author":author,
                    "tags":tags,
                    "link":"N/A"
                })
            except Exception:
                continue
        return qoutes