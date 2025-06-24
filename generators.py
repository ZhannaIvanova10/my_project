from typing import Iterator, Dict, Any, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанной валюте.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, "USD")

    Yields:
        Словари транзакций, где валюта соответствует заданной
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер (включительно)
        end: Конечный номер (включительно)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"