# tests/test_file_reader.py
from unittest.mock import mock_open, patch
from src.utils.file_reader import read_json_file

def test_read_valid_json():
    data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=data)):
        assert read_json_file("fake.json") == [{"id": 1, "amount": 100}]