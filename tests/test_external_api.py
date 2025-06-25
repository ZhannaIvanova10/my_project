from unittest.mock import patch, Mock
import pytest
from src.external_api import convert_to_rub

def test_convert_rub():
    assert convert_to_rub({'amount': '100', 'currency': 'RUB'}) == 100.0

@patch('src.external_api.requests.get')
def test_convert_usd(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.5}}
    mock_get.return_value = mock_response
    assert convert_to_rub({'amount': '100', 'currency': 'USD'}) == 7550.0

def test_invalid_data():
    assert convert_to_rub({'amount': 'invalid'}) is None
    assert convert_to_rub({}) is None

    @patch('requests.get')
    def test_api_error_handling(mock_get):
        mock_get.side_effect = requests.RequestException("API недоступно")
        result = convert_to_rub({'amount': '100', 'currency': 'USD'})
        assert result is None
