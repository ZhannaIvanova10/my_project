import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_num, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("1234", "1234"),
])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected

@pytest.mark.parametrize("account, expected", [
    ("1234567890", "**7890"),
    ("9876543210", "**3210"),
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected