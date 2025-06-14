import pytest

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00.000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"}
            }
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-02T15:30:00.000",
            "operationAmount": {
                "amount": "200.50",
                "currency": {"name": "EUR", "code": "EUR"}
            }
        }
    ]