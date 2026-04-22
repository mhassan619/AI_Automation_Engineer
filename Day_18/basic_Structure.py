import requests
from bs4 import BeautifulSoup

# Fetch Page
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

# Extract Title
title = soup.find("title").text
print("\n"+ title)

## Understanding HTML Structure

# Find Single Element
heading = soup.find("h1")
print("\n"+ heading.text)

# Find all elements
all_h3 = soup.find_all("h3")
for h in all_h3:
    print(h.text)

# Find from class
price = soup.find("p", class_="price_color")
print("\n"+ price.text)

# Use CSS selector
items = soup.select(".product_pod")
for item in items:
    print(item.select_one("h3 a")["title"])