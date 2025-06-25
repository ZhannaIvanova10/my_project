import json
import os

import pytest

from src.utils import read_json_file


def test_read_valid_json(tmp_path):
    file_path = tmp_path / "test.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([{"id": 1, "amount": 100}], f)
    assert read_json_file(file_path) == [{"id": 1, "amount": 100}]


def test_read_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('[]')
    assert read_json_file(file_path) == []


def test_read_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('invalid json')
    assert read_json_file(file_path) == []


def test_read_nonexistent_file():
    assert read_json_file("nonexistent.json") == []
