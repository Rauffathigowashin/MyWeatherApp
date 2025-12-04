import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY_NAME = str(input("Şəhər adı daxil edin: ")).strip()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if not API_KEY:
    print("❌ Xəta: API Açarı (.env faylından) yüklənmədi.")
    exit()

parameters = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'az'
}
print(f"🌍 {CITY_NAME} üçün hava haqqında məlumat alınır...")


try:
    response = requests.get(BASE_URL, params=parameters)
    response.raise_for_status()

    weather_data = response.json()

    main_data = weather_data.get('main', {})
    sicaklik = main_data.get('temp')
    weather_description = weather_data['weather'][0].get('description')

    print("\n--- Hava haqqında məlumat ---")
    print(f"Şəhər: {CITY_NAME}")
    print(f"Havanın vəziyyəti: {weather_description.capitalize()}")
    print(f"istilik(°C ilə): {sicaklik}°C")

except requests.exceptions.HTTPError as err:
    print(f"❌ HTTP Xətası: {err}")
    print("API açarınızı və ya şəhər adını kontrol edin.")
except requests.exceptions.RequestException as e:
    print(f"❌ Qoşularkən xəta baş verdi: {e}")


