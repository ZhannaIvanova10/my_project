from typing import List, Dict, Any, Optional


def filter_by_state(
    transactions: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по статусу.

    Args:
        transactions: Список словарей с транзакциями
        state: Статус транзакции для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список транзакций с указанным статусом
    """
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(
    transactions: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Args:
        transactions: Список словарей с транзакциями
        reverse: Порядок сортировки (по умолчанию True - по убыванию)

    Returns:
        Отсортированный список транзакций
    """
    return sorted(
        transactions, key=lambda x: x.get("date", ""), reverse=reverse
    )