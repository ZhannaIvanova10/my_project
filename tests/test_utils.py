import pytest
from src.utils import read_transactions
from unittest.mock import mock_open, patch

@pytest.mark.parametrize("content,expected", [
    ('[{"id": 1}]', [{"id": 1}]),
    ('[]', []),
    ('{}', []),
    ('invalid', []),
    ('[{"a": 1}, {"b": 2}]', [{"a": 1}, {"b": 2}]),
])
def test_read_transactions(content, expected):
    with patch('builtins.open', mock_open(read_data=content)), \
         patch('pathlib.Path.open', mock_open(read_data=content)):
        result = read_transactions('any_path')
        assert result == expected
