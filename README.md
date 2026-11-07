# 🌦️ WeatherWise – Weather Analytics Dashboard

An interactive weather analytics dashboard built using **Python, Streamlit, Pandas, and Plotly**. WeatherWise provides current weather conditions, upcoming forecasts, historical weather analysis, and interactive visualizations for locations around the world.

Powered by the **Open-Meteo API**, this project transforms weather data into meaningful insights through data analytics.

## 🚀 Live Demo

🌐 **Live Application:** https://weatherwise-dashboard.streamlit.app/

💻 **GitHub Repository:** https://github.com/vishnupriyac240307/WeatherWise

## 📸 Dashboard Preview

<!-- Add your dashboard screenshot here -->
<!-- Example: ![WeatherWise Dashboard](screenshots/dashboard.png) -->

## ✨ Features

- 🌍 **City Search:** Search for cities and towns around the world.
- 🌡️ **Current Weather:** View current temperature, feels-like temperature, wind speed, and precipitation.
- 📅 **Weather Forecast:** Explore weather forecasts for 1–16 days.
- 📊 **Historical Weather Analytics:** Analyze historical observations for 7, 14, 30, or 90 days.
- 📈 **Data Visualization:** Explore temperature and precipitation trends using interactive charts.
- 🧮 **Weather Insights:** Calculate average, maximum, and minimum temperatures and total rainfall.
- 🌡️ **Temperature Conversion:** Switch between Celsius and Fahrenheit.
- 📥 **CSV Export:** Download historical and forecast datasets.
- 🌙 **Dark Dashboard:** Clean and interactive user interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard development |
| Pandas | Data processing and analytics |
| Plotly | Interactive data visualization |
| Requests | API integration |
| Open-Meteo API | Weather data provider |
| Pytest | Automated testing |

## 📊 Dashboard Modules

### 1. Current Weather
Displays current weather conditions for the selected location, including temperature, apparent temperature, wind speed, and precipitation.

### 2. Weather Forecast
Provides upcoming weather information with daily maximum and minimum temperatures and precipitation details.

### 3. Historical Weather Analytics
Analyzes historical weather observations and calculates:
- Average temperature
- Maximum temperature
- Minimum temperature
- Total precipitation

### 4. Interactive Data Visualization
Uses Plotly charts to visualize weather patterns, temperature variations, and precipitation trends.

### 5. Data Export
Allows users to download historical and forecast weather datasets in CSV format for further analysis.

## 🏗️ Project Structure

```text
WeatherWise/
│
├── app.py
│
├── weatherwise/
│   ├── __init__.py
│   ├── api.py
│   └── analytics.py
│
├── tests/
│   ├── test_api.py
│   └── test_analytics.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/vishnupriyac240307/WeatherWise.git
```

### Step 2: Navigate to the Project Directory

```bash
cd WeatherWise
```

### Step 3: Create a Virtual Environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

## 🧪 Running Tests

Run the automated test suite:

```bash
pytest -q
```

The project includes tests for API request construction and weather analytics functions using mocked API responses.

**Latest test result:** 8 tests passed.

## 🌐 API Integration

WeatherWise uses the free public APIs provided by **Open-Meteo**.

| API | Purpose |
|---|---|
| Geocoding API | Search locations and retrieve coordinates |
| Forecast API | Retrieve current weather and forecast data |
| Archive API | Retrieve historical weather observations |

API Documentation: https://open-meteo.com/

No API key is required for the public endpoints used in this project. An active internet connection is required to retrieve weather data.

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

🔗 https://weatherwise-dashboard.streamlit.app/

## ⚠️ Limitations

- Weather information depends on the availability and accuracy of the Open-Meteo data provider.
- Historical data availability may vary depending on location and date.
- Historical analysis focuses on recent daily observations, not long-term climate normals.
- The application is intended for educational and analytical purposes, not emergency weather warnings.
- This project performs weather data analytics; it does not generate independent machine learning weather predictions.

## 🔮 Future Enhancements

- Multiple-city weather comparison.
- Weather anomaly detection.
- Long-term climate trend analysis.
- Seasonal weather pattern analysis.
- Saved locations and personalized dashboards.
- Machine learning-based weather analytics.

## 👩‍💻 Author

**Vishnu Priya**

B.Sc. Computer Science with Data Analytics

- **GitHub:** https://github.com/vishnupriyac240307
- **Live Project:** https://weatherwise-dashboard.streamlit.app/

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, Data Analytics, and curiosity about the weather. 💙**
