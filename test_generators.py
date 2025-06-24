import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD", "name": "US Dollar"}
            },
            "description": "Payment 1",
            "from": "Card 1234",
            "to": "Account 5678"
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "EUR", "name": "Euro"}
            },
            "description": "Payment 2",
            "from": "Card 4321",
            "to": "Account 8765"
        }
    ]

def test_filter_by_currency(sample_transactions):
    # Тестируем фильтрацию по USD
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["id"] == 1

    # Тестируем фильтрацию по EUR
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]["id"] == 2

    # Тестируем несуществующую валюту
    empty_result = list(filter_by_currency(sample_transactions, "GBP"))
    assert len(empty_result) == 0

def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2"]

@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"
    ])
])
def test_card_number_generator(start, end, expected):
    generated = list(card_number_generator(start, end))
    assert generated == expected