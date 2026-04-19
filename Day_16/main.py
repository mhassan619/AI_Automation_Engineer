import requests
# Like OpenWeatherMap nested JSON
weather_data = {
    "city":"Lahore",
    "main":{
        "temp":35.5,
        "humidity":60,
        "feels_like":38.2
    },
    "weather":[
        {"description":"sunny","icon":"01d"}
    ],
    "wind":{
        "speed":5.2
    }
}
# Now Access Nested Data
temp = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
description = weather_data['weather'][0]['description']
wind = weather_data['wind']['speed']
icon = weather_data['weather'][0]['icon']
feels_like = weather_data['main']['feels_like']
city = weather_data['city']

print(f"Temperature: {temp} C")
print(f"Humidity: {humidity}")
print(f"Description: {description}")
print(f"Wind: {wind}")
print(f"Icon : {icon}")
print(f"Feels_like: {feels_like}")
print(f"City: {city}")

# For safe data access by using .get()
# .get() is safe when key is not found - prevents from crash
name = weather_data.get("name","Unknown")
location = weather_data.get("location","N/A")

# For nested
temp = weather_data.get("main",{}).get("temp",0)
print(f"name:{name} - location:{location} - temp:{temp}")