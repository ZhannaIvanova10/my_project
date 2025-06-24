import pytest
import os
from decorators import log


def test_log_to_console(capsys):
    """Тестирование вывода логов в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert result == 3


def test_log_to_file(tmp_path):
    """Тестирование записи логов в файл"""
    log_file = os.path.join(tmp_path, "test.log")

    @log(filename=log_file)
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "multiply ok" in content
    assert result == 12


def test_log_error_handling(capsys):
    """Тестирование обработки ошибок"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out
