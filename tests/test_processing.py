import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_sort_by_date(sample_transactions):
    result = sort_by_date(sample_transactions)
    assert result[0]["id"] == 1