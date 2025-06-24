from unittest.mock import patch
from my_project.src.external_api.currency_converter import convert_to_rub

def test_convert_rub():
    assert convert_to_rub({"amount": "100", "currency": "RUB"}) == 100.0

@patch('requests.get')
def test_convert_usd(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    assert convert_to_rub({"amount": "100", "currency": "USD"}) == 7500.0

def test_invalid_currency():
    assert convert_to_rub({"amount": "100", "currency": "GBP"}) is None