import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("invalid", "invalid"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected