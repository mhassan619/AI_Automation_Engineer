import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

st.title("📚 Book Data Visualizer")

pages = st.slider("How many pages you want to scrape?",1,5,2)

if st.button("🔎 Scrape Books"):
    books = []
    progress = st.progress(0)
    status = st.empty()

    for page in range(1, pages + 1):
        status.text(f"📃 Page {page} scrapping...")
        progress.progress(page / pages)
        
        if page == 1:
            url = "https://books.toscrape.com/index.html"
        else:
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")

        for book in soup.select(".product_pod"):
            title = book.select_one("h3 a")["title"]
            price_raw = book.select_one(".price_color").text
            price_cleaned = "".join(char for char in price_raw if char.isdigit() or char == ".")
            price = float(price_cleaned)
            rating = book.select_one("p.star-rating")['class'][1]
            books.append({
                "Title":title[:40],
                "Price": price,
                "Rating": rating
            })
        time.sleep(0.5)

    status.text("✅ Complete!")
    df = pd.DataFrame(books)

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("📚 Total Books", len(df))
    col2.metric("💰 Avg Price",f"${df['Price'].mean():.2f}")
    col3.metric("⭐ Five Star", len(df[df['Rating'] == 'Five']))

    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⭐ Rating Distribution")
        rating_counts = df['Rating'].value_counts()
        st.bar_chart(rating_counts)
    with col2:
        st.subheader("📗 All Books")
        st.dataframe(df,use_container_width=True)