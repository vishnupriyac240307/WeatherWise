import pandas as pd
import pytest
from weatherwise.analytics import daily_summary, temperature_kpis, precipitation_insights, monthly_climatology

@pytest.fixture
def sample():
    return pd.DataFrame({
        "time": ["2025-01-02", "2025-01-01", "2025-01-03"],
        "temperature_2m_max": [30, 28, 32],
        "temperature_2m_min": [20, 18, 22],
        "precipitation_sum": [0, 2.5, 1.5],
    })

def test_daily_summary_sorts_dates(sample):
    result = daily_summary(sample)
    assert list(result["time"].dt.day) == [1, 2, 3]

def test_kpis(sample):
    result = temperature_kpis(sample)
    assert result["max"] == 32
    assert result["min"] == 18
    assert result["rain_total"] == 4.0
    assert result["mean"] == pytest.approx(25.0)

def test_precipitation_insight(sample):
    assert "2 of 3 days" in precipitation_insights(sample)
    assert "4.0 mm" in precipitation_insights(sample)

def test_missing_columns_raise():
    with pytest.raises(ValueError):
        daily_summary(pd.DataFrame({"time": ["2025-01-01"]}))

def test_monthly_climatology(sample):
    result = monthly_climatology(sample)
    assert len(result) == 1
    assert result.iloc[0]["month"] == 1
