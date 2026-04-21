from weather_app.weather import weatherService
from weather_app.display import WeatherDisplay
import json
class WeatherApp:
    def __init__(self):
        self.__service = weatherService()
        self.__display = WeatherDisplay()
        self.__history = []  # search history
    def search(self,city):
        print(f"\n🔍 '{city}'s' weather is fetching...") 
        # current weather
        current = self.__service.get_current(city)
        self.__display.current(current)

        # Forecast
        forecast = self.__service.get_forecast(city)
        self.__display.forecast(forecast)

        # Save in History
        if current:
            self.__history.append({
                "city":city,
                "temp":current['main']['temp'],
                "condition": current['weather'][0]['description']
            })
    def search_history(self):
        if not self.__history:
            print(f"❌ There is nothing searched yet.")
            return
        print(f"\n🗒️  Search History:")
        for i, item in enumerate(self.__history, 1):
            print(f" {i}. {item['city']} - {item['temp']}'C - {item['condition']}")
    def save_history(self):
        with open("Weather_history.json", "w") as f:
            json.dump(self.__history,f,indent=4)
        print("✅ History Saved.")
    def run(self):
        print("🌤️ Welcome to Weather App!")
        print("Commands: search, history, save, quit")
        while True:
            command = input("\n ").strip().lower()
            if command == 'quit':
                print("👋 Allah Hafiz!")
                break
            elif command == "search":
                city = input("City Name: ").strip()
                self.search(city)
            elif command == "history":
                self.search_history()
            elif command == "save":
                self.save_history()
            else:
                print(f"❌ Invalid Command!")
# Run the App
app = WeatherApp()
app.run()