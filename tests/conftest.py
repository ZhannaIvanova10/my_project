import pytest
import os

@pytest.fixture(autouse=True)
def set_test_api_key():
    """Устанавливаем тестовый API ключ для всех тестов"""
    os.environ['EXCHANGE_RATE_API_KEY'] = 'test_key'