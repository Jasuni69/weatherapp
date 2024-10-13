import requests
from config import WEATHERSTACK_API_KEY

#WEATHERSTACK_API_KEY = "406885e44fb4b78e8d62f10c30bd76f4"

def get_weather(location: str):
    api_key = WEATHERSTACK_API_KEY
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    querystring = {"query": location}
    response = requests.get(url, params=querystring)
    data = response.json()

  
    data_list = data["current"]
    temperature = data_list["temperature"]
    weather_description = data_list["weather_descriptions"][0]
    print(f"The weather in {location} is {weather_description}")
    print(f"The temperature in {location} is {temperature} C°")

place = input("Where do you want to see the weather? For example Stockholm or London.: ")
get_weather(location=place)



