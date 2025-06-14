from src.masks import get_mask_card_number, get_mask_account  # ✅ Абсолютный импорт

def mask_account_card(data: str) -> str:
    if "Счет" in data:
        return f"Счет {get_mask_account(data.split()[-1])}"
    else:
        return f"{' '.join(data.split()[:-1])} {get_mask_card_number(data.split()[-1])}"

def get_date(date_str: str) -> str:
    from datetime import datetime  # Локальный импорт
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return date_str