import os
import requests
from typing import Dict, Optional, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict[str, Any]) -> Optional[float]:
    """Convert transaction amount to RUB.

    Args:
        transaction: Dictionary with transaction data

    Returns:
        Amount in RUB or None if error occurs
    """
    if not transaction.get('amount'):
        return None

    try:
        currency = transaction.get('currency', 'RUB').upper()
        amount = float(transaction['amount'])

        if currency == 'RUB':
            return amount

        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=5
        )
        response.raise_for_status()
        return round(amount * response.json()['rates']['RUB'], 2)
    except (requests.RequestException, KeyError, ValueError):
        return None
