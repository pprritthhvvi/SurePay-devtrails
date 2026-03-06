import os
import requests

def calculate_weekly_premium(base=50, zone_risk=0, disruption_factor=0):
    return base + zone_risk + disruption_factor


def get_weather_disruption(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    rainfall = data.get("rain", {}).get("1h", 0)

    if rainfall > 20:
        return 15
    elif rainfall > 5:
        return 5
    else:
        return 0


def get_pollution_disruption(city):
    api_key = os.getenv("AQICN_API_KEY")

    url = f"https://api.waqi.info/feed/{city}/?token={api_key}"

    response = requests.get(url)

    try:
        data = response.json()
    except:
        print("Error: API did not return valid JSON")
        return 0

    # Check API status
    if data.get("status") != "ok":
        print("AQI API error:", data)
        return 0

    aqi = data["data"].get("aqi", 0)

    if aqi > 200:
        return 15
    elif aqi > 100:
        return 5
    else:
        return 0
    
def get_curfew_disruption():
    # Mock simulation: 1 = curfew active, 0 = no curfew
    curfew_active = 1  # change to 0 for no curfew
    if curfew_active:
        return 20   # add ₹20 if curfew is active
    else:
        return 0
