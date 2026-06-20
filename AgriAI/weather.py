import requests
import os
from config
import WEATHER_API_KEY

API_KEY = os.getenv("API_KEY")
city = input("Think of a city AYUSH: ")

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aq>

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(f"\nWeather for {data['location']['name']}, {data['location']['co>
    print("Temperature:", data['current']['temp_c'], "°C")
    print("Condition:", data['current']['condition']['text'])
    print("Humidity:", data['current']['humidity'], "%")
    print("Wind:", data['current']['wind_kph'], "km/h")
    print("Feels Like:", data['current']['feelslike_c'], "°C")
    print("UV index:", data['current']['uv'], " ")
    print("Last updated:", data['current']['last_updated'], "IST")
else:
    print("Error:", response.status_code)
    print(response.text)
 
