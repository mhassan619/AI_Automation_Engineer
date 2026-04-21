import requests
from weather_app.config import API_KEY,BASE_URL,UNITS
class weatherService:
    def __init__(self):
        self.__api_key = API_KEY
        self.__base_url = BASE_URL
    def get_current(self,city):
        try:
            url = f"{self.__base_url}/weather"
            params = {
                'q':city,
                'appid':self.__api_key,
                'units':UNITS
            }
            response = requests.get(url,params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            if response.status_code == 404:
                print(f"❌ City '{city}' not found!")
            elif response.status_code == 401:
                print("❌ Invalid API key.")
            return None
        except requests.exceptions.ConnectionError:
            print(f"❌ Please check your internet connection.")
            return None
    def get_forecast(self,city):
        try:
            url = f"{self.__base_url}/forecast"
            params = {
                'q':city,
                'appid':self.__api_key,
                'units':UNITS,
                'cnt':5 # next 5 forecasts
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Forecast errror: {e}")
            return None