# WeatherWise — Weather Analytics Dashboard

WeatherWise is an intermediate-level Python data analytics mini-project. It combines live weather conditions, short-term forecasts, recent observed weather, interactive charts, simple analytics and CSV exports in a dark Streamlit dashboard.

## Features

- Search cities and towns using Open-Meteo geocoding.
- Current conditions: temperature, feels-like temperature, wind speed and precipitation.
- 1–16 day forecast with daily high/low temperatures, rainfall and precipitation probability data.
- Recent historical observations for 7, 14, 30 or 90 days.
- Temperature and rainfall KPIs plus readable rainfall insight.
- Interactive Plotly charts.
- CSV downloads for historical and forecast data.
- Celsius/Fahrenheit display conversion.
- Automated tests for analytics and API request construction.

## Technology

Python 3.10+, Streamlit, Pandas, Plotly, Requests, Pytest, Open-Meteo Forecast/Geocoding/Archive APIs.

## Requirements

- Python 3.10 or newer
- Internet connection
- No API key required (Open-Meteo endpoints used by this project are public)

## Run locally

```bash
# 1. Extract the project and enter its directory
cd WeatherWise

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows PowerShell

# 3. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Streamlit prints a local URL, normally http://localhost:8501.

## Run tests

From the project root with the virtual environment activated:

```bash
pytest -q
```

The test suite covers sorting and validation, temperature/rainfall metrics, precipitation insights, monthly aggregation, and API client request construction. API tests are mocked and do not require internet access.

## How it works

1. The city search calls Open-Meteo Geocoding and selects the first matching result.
2. Coordinates are sent to the Forecast API for current conditions and forecast data.
3. Coordinates and a date range are sent to the Archive API for recent historical daily observations.
4. Pandas transforms the returned daily series into KPIs and insights.
5. Plotly renders interactive charts; Streamlit provides filters and CSV exports.

## Project structure

```text
WeatherWise/
├── app.py
├── weatherwise/
│   ├── __init__.py
│   ├── api.py
│   └── analytics.py
├── tests/
│   ├── test_analytics.py
│   └── test_api.py
├── .streamlit/
│   └── config.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Data and limitations

- Weather data is provided by Open-Meteo. Consult its documentation and attribution/licensing terms before public or commercial redistribution.
- Archive data availability can vary by location and date. A provider/API error is displayed rather than fabricated data.
- The historical window is recent daily observations, not a long-term climate-normal dataset.
- This is an educational analytics application, not an emergency alert system. Forecasts are estimates and should not replace official warnings.
- Fahrenheit conversion applies to displayed temperatures; API data and exported source values remain in Celsius.

## Portfolio extensions

- Add saved locations and compare cities.
- Add seasonal and year-over-year climatology using longer historical ranges.
- Add anomaly detection for unusually hot/cold days.
- Add user accounts and saved dashboards.
- Deploy with Streamlit Community Cloud.

## Author

Add your name, GitHub profile and project demo link here before publishing.
