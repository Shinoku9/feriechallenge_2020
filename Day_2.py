import datetime
import requests
import random

city = input("Type in your city: ")

def get_weather(query):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q":query,"lang":"en","units":"metric"}

    headers = {
    'x-rapidapi-key': "4e195d20d8msh5d3ed9bbb8d48c5p145849jsn3e68c5380f4c",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

now = datetime.datetime.now()
weather_data = get_weather(city)
weather_main = weather_data["weather"][0]["main"]
weather_details = weather_data["weather"][0]["description"]
temperature = weather_data["main"]["temp"]
pressure = weather_data["main"]["pressure"]
humidity = weather_data["main"]["humidity"]

def get_quote():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)
    quotes = response.json()
    return random.choice(quotes)

quote = get_quote()

def callendar_page():
    print("Today is: " + datetime.datetime.strftime(now, "%d %B %Y"))
    print("Current time is: " + datetime.datetime.strftime(now, "%H:%M:%S"))

def current_weather():
    print("Current weather in: " + city)
    print("Weather: " + weather_main)
    print("Details: " + weather_details)
    print("Temperature: " + str(round(temperature)) + "C")
    print("Pressure: " + str(pressure) + "hPa")
    print("Humidity: " + str(humidity) + "%")

def random_quote():
    print("Quote for today is: " + quote["text"])
    print("Author: " + quote["author"])

callendar_page()
current_weather()
random_quote()
