from src.masks import get_mask_card_number, get_mask_account

def test_card_mask():
    assert get_mask_card_number("1234567890123456") == "123456******3456"
    assert get_mask_card_number("1111222233334444") == "111122******4444"

def test_account_mask():
    assert get_mask_account("12345678") == "**5678"
    assert get_mask_account("9876543210") == "**3210"