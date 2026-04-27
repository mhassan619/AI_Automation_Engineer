import streamlit as st
import requests
import os

st.title("🌤️ Weather Dashboard")
API_KEY = st.text_input(
    "OpenWeatherMap API key",
    type="password",
    help="Get free API from openweathermap.org"
)
city = st.text_input("City Name","Lahore")
if st.button("🔎 Get Weather") and API_KEY:
    with st.spinner("Fetching weather..."):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q":city,
            "appid":API_KEY,
            "units": "metric"
        }
        response = requests.get(url,params=params)
        data = response.json()
    if response.status_code == 200:
        col1, col2,col3, col4 = st.columns(4)
        col1.metric("🌡️ Temperature", f"{data['main']['temp']}'C")
        col2.metric("🤔 Feels Like",f"{data['main']['feels_like']}'C")
        col3.metric("💧 Humidity", f"{data['main']['humidity']}%")
        col4.metric("🌬️ Wind",f"{data['wind']['speed']}m/s")

        st.info(f"💭 Condition: {data['weather'][0]['description'].title()}")
        st.success(f"🕯️ {data['name']},{data['sys']['country']}")
    else:
        st.error("❌ City not found or please check your api key")
elif st.button('🔎 Get Weather') and not API_KEY:
    st.warning("⚠️ Please enter your API key!")