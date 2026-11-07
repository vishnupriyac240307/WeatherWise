"""Open-Meteo API client. No API key required."""
import requests
from datetime import date, timedelta

BASE = "https://api.open-meteo.com/v1"
ARCHIVE = "https://archive-api.open-meteo.com/v1"
GEO = "https://geocoding-api.open-meteo.com/v1"

def _get(url, params):
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    return response.json()

def geocode_city(name):
    data = _get(f"{GEO}/search", {"name": name, "count": 5, "language": "en", "format": "json"})
    return data.get("results", [])

def get_forecast(latitude, longitude, days=7):
    return _get(f"{BASE}/forecast", {
        "latitude": latitude, "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max",
        "forecast_days": days, "timezone": "auto"
    })

def get_historical(latitude, longitude, days=30):
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=days-1)
    return _get(f"{ARCHIVE}/archive", {
        "latitude": latitude, "longitude": longitude,
        "start_date": start.isoformat(), "end_date": end.isoformat(),
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    })
