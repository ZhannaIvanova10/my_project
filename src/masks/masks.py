def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры.
    Формат: 123456******1234

    Args:
        card_number: Номер карты (16 цифр без пробелов)

    Returns:
        Маскированный номер (например, "123456******3456")

    Raises:
        ValueError: Если номер не содержит 16 цифр
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:6]}******{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры.
    Формат: **1234

    Args:
        account_number: Номер счета (минимум 4 цифры)

    Returns:
        Маскированный номер (например, "**7890")

    Raises:
        ValueError: Если номер короче 4 цифр
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
    """