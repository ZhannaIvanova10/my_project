from src.masks import get_mask_card_number

def test_mask():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"