from unittest.mock import patch, Mock
import pytest
from src.external_api import convert_currency_to_rub


@patch('src.external_api.requests.get')
def test_convert_rub(mock_get):
    """Тест конвертации RUB в RUB (без вызова API)"""
    result = convert_currency_to_rub({'amount': '100', 'currency': 'RUB'})
    assert result == 100.0
    mock_get.assert_not_called()


@patch('src.external_api.requests.get')
def test_convert_usd(mock_get):
    """Тест успешной конвертации USD в RUB"""
    # Настройка мок-ответа
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = convert_currency_to_rub({'amount': '100', 'currency': 'USD'})

    assert result == 7500.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/latest",
        params={'base': 'USD', 'symbols': 'RUB'},
        headers={'apikey': 'test_key'},
        timeout=10
    )


@patch('src.external_api.requests.get')
def test_convert_api_error(mock_get):
    """Тест обработки ошибки API"""
    # Настройка мок-ошибки
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API error")
    mock_get.return_value = mock_response

    result = convert_currency_to_rub({'amount': '100', 'currency': 'USD'})
    assert result is None


def test_convert_invalid_currency():
    """Тест не поддерживаемой валюты"""
    result = convert_currency_to_rub({'amount': '100', 'currency': 'GBP'})
    assert result is None


@patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': ''})
def test_convert_missing_api_key():
    """Тест отсутствия API ключа"""
    result = convert_currency_to_rub({'amount': '100', 'currency': 'USD'})
    assert result is None