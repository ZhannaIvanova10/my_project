from datetime import datetime
from masks import mask_account_number, mask_card_number

def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета.
    Пример: 'Visa Platinum 7000792289606361' → 'Visa Platinum 7000 79** **** 6361'
    """
    if "Счет" in account_info:
        number = account_info.split()[-1]
        return f"Счет {mask_account_number(number)}"
    else:
        parts = account_info.rsplit(" ", 1)
        return f"{parts[0]} {mask_card_number(parts[1])}"

def get_date(date_str: str) -> str:
    """
    Форматирует дату из ISO в 'ДД.ММ.ГГГГ'.
    Пример: '2024-03-11T02:26:18.671407' → '11.03.2024'
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")