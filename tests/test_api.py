from unittest.mock import patch
from weatherwise.api import geocode_city, get_forecast, get_historical

@patch("weatherwise.api._get", return_value={"results": [{"name": "Coimbatore"}]})
def test_geocode(mock):
    assert geocode_city("Coimbatore")[0]["name"] == "Coimbatore"
    mock.assert_called_once()

@patch("weatherwise.api._get", return_value={"current": {}, "daily": {}})
def test_forecast(mock):
    get_forecast(11.0, 76.9, 5)
    args = mock.call_args.args
    assert args[0].endswith("/forecast")
    assert mock.call_args.args[1]["forecast_days"] == 5

@patch("weatherwise.api._get", return_value={"daily": {}})
def test_history(mock):
    get_historical(11.0, 76.9, 7)
    assert mock.call_args.args[0] == "https://archive-api.open-meteo.com/v1/archive"
