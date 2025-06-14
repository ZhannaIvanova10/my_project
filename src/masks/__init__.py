def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты (16 цифр) в формате XXXX XX** **** XXXX"""
    if len(card_number) != 16 or not card_number.isdigit():
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account: str) -> str:
    """Маскирует номер счета (20 цифр), оставляя последние 4 цифры"""
    if len(account) < 4 or not account.isdigit():
        return account
    return f"**{account[-4:]}"