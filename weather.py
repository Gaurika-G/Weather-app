import requests
import os
from dotenv import load_dotenv
import geocoder

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Fetch the API key securely

# Perplexity API URL
BASE_URL = "https://api.perplexity.ai/v1/query"

weather_icons = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "snow": "❄️",
    "thunderstorm": "⛈️",
    "mist": "🌫️",
}

def get_weather(city):
    """Fetches weather data using Perplexity API."""
    if not API_KEY:
        print("❌ Error: API_KEY not found. Make sure you have a .env file.")
        return

    query = f"What is the current weather in {city}?"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {"model": "llama-3-8b", "messages": [{"role": "user", "content": query}]}

    response = requests.post(BASE_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("🌤️ Weather Info:", result["output"])
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

def get_forecast(city):
    """Fetches 5-day weather forecast using Perplexity API."""
    query = f"What is the 5-day weather forecast for {city}?"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {"model": "llama-3-8b", "messages": [{"role": "user", "content": query}]}

    response = requests.post(BASE_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("📅 5-Day Forecast:", result["output"])
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

def display_weather(city):
    """Displays weather with icons."""
    weather_data = get_weather(city)  # Assume get_weather() returns a text summary
    for key, icon in weather_icons.items():
        if key in weather_data.lower():
            print(f"Weather in {city}: {icon} {weather_data}")
            return

    print(f"Weather in {city}: {weather_data}")

# Get user's location automatically
g = geocoder.ip("me")
city = g.city
print(f"Detected location: {city}")
get_weather(city)
get_forecast(city)
