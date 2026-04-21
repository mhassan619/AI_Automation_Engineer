class WeatherDisplay:
    @staticmethod
    def current(data):
        if not data:
            return 
        print(f"\n{'='*45}")
        print(f"  🌥️ WEATHER REPORT")
        print(f"{'='*45}")
        print(f"  🏢 City   : {data['name']},{data['sys']['country']}")
        print(f"  ☀️ Temp   : {data['main']['temp']}'C")
        print(f"  🤔 Feels   : {data['main']['feels_like']}'C")
        print(f"  💧 Humidity   : {data['main']['humidity']}%")
        print(f"  🌬️ Wind   : {data['wind']['speed']} m/s")
        print(f"  ☁️ Condition  : {data['weather'][0]['description'].title()}")
        print(f"{'='*45}")
    @staticmethod
    def forecast(data):
        if not data:
            return
        print(f"\n{'='*45}")
        print(f"  📆 5-STEP FORECAST")
        print(f"{'='*45}")
        for item in data['list']:
            time = item['dt_txt']
            temp = item['main']['temp']
            desc = item['weather'][0]['description']
            print(f"  {time} | {temp}'C | {desc.title()}")
        print(f"{'='*45}")