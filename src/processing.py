from typing import List, Dict, Any

def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует транзакции по статусу."""
    return [t for t in transactions if t.get("state") == state]

def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)