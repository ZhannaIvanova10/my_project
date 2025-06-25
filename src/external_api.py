import requests
import os
from typing import Dict, Optional


class CurrencyConverter:
    BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"

    @classmethod
    def convert_to_rub(cls, transaction: Dict) -> Optional[float]:
        try:
            amount = float(transaction.get('amount', 0))
            currency = transaction.get('currency', 'RUB').upper()

            if currency == 'RUB':
                return amount

            response = requests.get(
                cls.BASE_URL,
                params={'base': currency, 'symbols': 'RUB'},
                headers={'apikey': os.getenv('EXCHANGE_RATE_API_KEY')},
                timeout=10
            )
            response.raise_for_status()
            return amount * response.json()['rates']['RUB']

        except Exception:
            return None


def convert_currency_to_rub(transaction: Dict) -> Optional[float]:
    return CurrencyConverter.convert_to_rub(transaction)
