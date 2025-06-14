from datetime import datetime  # ✅ Стандартный импорт

def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    return [t for t in transactions if t.get("state") == state]

def sort_by_date(transactions: list[dict], reverse: bool = False) -> list[dict]:
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )