"""Pure analytics helpers, deliberately separated from the UI."""
import pandas as pd

def daily_summary(frame):
    required = {"time", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required weather columns: {', '.join(sorted(missing))}")
    result = frame.copy()
    result["time"] = pd.to_datetime(result["time"])
    return result.sort_values("time").reset_index(drop=True)

def temperature_kpis(frame):
    clean = daily_summary(frame)
    highs = pd.to_numeric(clean["temperature_2m_max"], errors="coerce")
    lows = pd.to_numeric(clean["temperature_2m_min"], errors="coerce")
    rain = pd.to_numeric(clean["precipitation_sum"], errors="coerce").fillna(0)
    if highs.notna().sum() == 0 or lows.notna().sum() == 0:
        raise ValueError("No valid temperature observations found.")
    return {
        "mean": float(pd.concat([highs, lows]).mean()),
        "max": float(highs.max()),
        "min": float(lows.min()),
        "rain_total": float(rain.sum())
    }

def precipitation_insights(frame):
    clean = daily_summary(frame)
    rain = pd.to_numeric(clean["precipitation_sum"], errors="coerce").fillna(0)
    wet_days = int((rain > 0).sum())
    total = float(rain.sum())
    if total == 0:
        return f"No measurable precipitation was recorded across {len(clean)} days."
    wettest = clean.loc[rain.idxmax(), "time"]
    return (f"{wet_days} of {len(clean)} days recorded precipitation, totaling {total:.1f} mm. "
            f"The wettest day in this period was {wettest:%d %b %Y}.")

def monthly_climatology(frame):
    clean = daily_summary(frame)
    clean["month"] = clean["time"].dt.month
    return clean.groupby("month", as_index=False).agg(
        avg_high=("temperature_2m_max", "mean"),
        avg_low=("temperature_2m_min", "mean"),
        rainfall=("precipitation_sum", "sum")
    )
