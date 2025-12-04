import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY_NAME = str(input("Enter City Name: ")).strip()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if not API_KEY:
    print("❌ Error: API Key (form .env) Not Found.")
    exit()

parameters = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'en'
}
print(f"🌍 Weather information for {CITY_NAME}")


try:
    response = requests.get(BASE_URL, params=parameters)
    response.raise_for_status()

    weather_data = response.json()

    main_data = weather_data.get('main', {})
    sicaklik = main_data.get('temp')
    weather_description = weather_data['weather'][0].get('description')

    print("\n--- Weather Information ---")
    print(f"City: {CITY_NAME}")
    print(f"Weather Info: {weather_description.capitalize()}")
    print(f"Temp(°C): {sicaklik}°C")

except requests.exceptions.HTTPError as err:
    print(f"❌ HTTP Error: {err}")
    print("Control your API key and try again.")
except requests.exceptions.RequestException as e:
    print(f"❌ Connection Error: {e}")


