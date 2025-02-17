import os
from typing import Any

import pytest

from src.decorators import log


@pytest.fixture
def temp_file(tmp_path: Any) -> Any:
    filename = tmp_path / "mylog.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_console_success(capsys: Any) -> None:
    @log()
    def test_func(x: int, y: int) -> int:
        return x + y

    test_func(2, 3)
    captured = capsys.readouterr()
    output = captured.out
    assert "Function started" in output
    assert "Function finished" in output
    assert "test_func ok, result 5" in output


def test_log_to_file_success(temp_file: Any) -> None:
    @log(temp_file)
    def test_func(x: int, y: int) -> int:
        return x + y

    test_func(2, 3)
    with open(temp_file, "r") as file:
        content = file.read()
        assert "Function started" in content
        assert "Function finished" in content
        assert "test_func ok, result 5" in content


def test_log_to_console_error(capsys: Any) -> None:
    @log()
    def test_func(x: int, y: int) -> int:
        raise ValueError("Invalid input")

    with pytest.raises(ValueError):
        test_func(2, 3)
    captured = capsys.readouterr()
    output = captured.out
    assert "Function started" in output
    assert "Function finished" in output
    assert "test_func error: Invalid input" in output
    assert "Inputs: ((2, 3), {})" in output


def test_log_to_file_error(temp_file: Any) -> None:
    @log(temp_file)
    def test_func(x: int, y: int) -> int:
        raise ValueError("Invalid input")

    with pytest.raises(ValueError):
        test_func(2, 3)
    with open(temp_file, "r") as file:
        content = file.read()
        assert "Function started" in content
        assert "Function finished" in content
        assert "test_func error: Invalid input" in content
        assert "Inputs: ((2, 3), {})" in content
