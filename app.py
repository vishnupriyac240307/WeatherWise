import streamlit as st
import pandas as pd
import plotly.express as px
from weatherwise.api import geocode_city, get_forecast, get_historical
from weatherwise.analytics import daily_summary, monthly_climatology, temperature_kpis, precipitation_insights

st.set_page_config(page_title="WeatherWise | Climate Analytics", page_icon="🌦️", layout="wide")
st.markdown("""
<style>
.stApp {background: #0b1220; color: #e8eef8;}
[data-testid="stSidebar"] {background: #111c2e;}
[data-testid="stMetric"] {background: #142238; border: 1px solid #263b58; padding: 14px; border-radius: 12px;}
h1,h2,h3 {color: #e8f1ff;}
.small-muted {color:#9fb2cc;}
</style>
""", unsafe_allow_html=True)

st.title("🌦️ WeatherWise")
st.caption("Weather intelligence and climate analytics · Powered by Open-Meteo")
with st.sidebar:
    st.header("Explore a location")
    city = st.text_input("City or town", value="Coimbatore")
    days = st.slider("Forecast horizon", 1, 16, 7)
    history_days = st.selectbox("Historical window", [7, 14, 30, 90], index=2)
    units = st.radio("Temperature units", ["Celsius", "Fahrenheit"])
    load = st.button("Load weather", type="primary", use_container_width=True)
    st.markdown("---")
    st.caption("Data source: Open-Meteo. Internet connection required.")

if "weather_location" not in st.session_state:
    st.session_state.weather_location = "Coimbatore"
if load:
    st.session_state.weather_location = city.strip() or "Coimbatore"
city = st.session_state.weather_location

try:
    with st.spinner(f"Fetching weather for {city}..."):
        places = geocode_city(city)
        if not places:
            st.error(f"No location found for '{city}'. Try a nearby larger city.")
            st.stop()
        place = places[0]
        forecast = get_forecast(place["latitude"], place["longitude"], days)
        history = get_historical(place["latitude"], place["longitude"], history_days)
except Exception as exc:
    st.error(f"Weather data could not be loaded: {exc}")
    st.info("Check your internet connection and try again. The app uses the free Open-Meteo API and does not require an API key.")
    st.stop()

loc = ", ".join(x for x in [place.get("name"), place.get("admin1"), place.get("country")] if x)
st.subheader(loc)
st.markdown('<p class="small-muted">Live conditions, short-range forecast and recent observed weather</p>', unsafe_allow_html=True)

current = forecast["current"]
temp = current.get("temperature_2m")
apparent = current.get("apparent_temperature")
wind = current.get("wind_speed_10m")
rain = current.get("precipitation")
if units == "Fahrenheit":
    temp = temp * 9/5 + 32
    apparent = apparent * 9/5 + 32
unit = "°F" if units == "Fahrenheit" else "°C"
k1,k2,k3,k4 = st.columns(4)
k1.metric("Current temperature", f"{temp:.1f}{unit}")
k2.metric("Feels like", f"{apparent:.1f}{unit}")
k3.metric("Wind speed", f"{wind:.1f} km/h")
k4.metric("Current precipitation", f"{rain:.1f} mm")

fc = pd.DataFrame(forecast["daily"])
fc["temperature_unit"] = fc["temperature_2m_max"]
if units == "Fahrenheit":
    fc["temperature_2m_max"] = fc["temperature_2m_max"] * 9/5 + 32
    fc["temperature_2m_min"] = fc["temperature_2m_min"] * 9/5 + 32
st.subheader("Forecast")
left, right = st.columns([1.5, 1])
with left:
    fig = px.line(fc, x="time", y=["temperature_2m_max","temperature_2m_min"],
                  markers=True, labels={"value": f"Temperature ({unit})", "time":"Date", "variable":"Metric"},
                  title="Daily high and low temperatures")
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
with right:
    rain_fig = px.bar(fc, x="time", y="precipitation_sum", labels={"time":"Date","precipitation_sum":"Rain (mm)"},
                      title="Expected daily precipitation")
    rain_fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(rain_fig, use_container_width=True)

st.subheader("Recent weather analytics")
hist = pd.DataFrame(history["daily"])
summary = daily_summary(hist)
kpis = temperature_kpis(hist)
a,b,c,d = st.columns(4)
a.metric("Period average", f"{kpis['mean']:.1f} °C")
b.metric("Period maximum", f"{kpis['max']:.1f} °C")
c.metric("Period minimum", f"{kpis['min']:.1f} °C")
d.metric("Total rainfall", f"{kpis['rain_total']:.1f} mm")
hist_fig = px.line(summary, x="time", y=["temperature_2m_max","temperature_2m_min"],
                   markers=True, title="Observed daily temperature range",
                   labels={"value":"Temperature (°C)","time":"Date","variable":"Metric"})
hist_fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(hist_fig, use_container_width=True)

insights = precipitation_insights(hist)
st.info(insights)
clim = monthly_climatology(hist)
with st.expander("View data table and export"):
    st.dataframe(hist, use_container_width=True)
    st.download_button("Download historical data (CSV)", hist.to_csv(index=False).encode("utf-8"),
                       file_name="weatherwise_history.csv", mime="text/csv")
    st.download_button("Download forecast (CSV)", fc.to_csv(index=False).encode("utf-8"),
                       file_name="weatherwise_forecast.csv", mime="text/csv")
st.caption("WeatherWise is an educational analytics tool. Forecasts are model estimates, not official warnings.")
