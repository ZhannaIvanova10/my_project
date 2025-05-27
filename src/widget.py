from datetime import datetime
from masks import mask_account_number, mask_card_number  # Импорт из вашего модуля masks.py


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.

    Args:
        account_info: Строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Returns:
        Строка с замаскированным номером (например, "Visa Platinum 7000 79** **** 6361").
    """
    if "Счет" in account_info:
        # Маскировка счета
        number = account_info.split()[-1]
        masked_number = mask_account_number(number)
        return f"Счет {masked_number}"
    else:
        # Маскировка карты
        card_parts = account_info.rsplit(" ", 1)
        card_type = card_parts[0]
        card_number = card_parts[1]
        masked_number = mask_card_number(card_number)
        return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в строку "ДД.ММ.ГГГГ".

    Args:
        date_str: Дата в формате "2024-03-11T02:26:18.671407".

    Returns:
        Строка с датой в формате "11.03.2024".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")