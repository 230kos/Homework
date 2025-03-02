import os
import json
import logging
from unittest.mock import patch, mock_open, MagicMock
from typing import List, Dict, Any
import pytest
from src.utils import load_transactions

# Создаем папку logs, если она не существует
log_dir = os.path.join("..", "logs")
os.makedirs(log_dir, exist_ok=True)

# Фикстура для мокирования логгера
@pytest.fixture(autouse=True)
def mock_logging() -> Any:
    with patch("logging.FileHandler"):
        yield


@patch("os.path.exists", return_value=True)
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=json.dumps(
        [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 200.0, "currency": "USD"}]
    ),
)
def test_load_transactions_success(mock_file: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестируем успешную загрузку транзакций из файла.
    """
    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
    mock_exists.assert_called_once_with("data/operations.json")


@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found(mock_exists: MagicMock) -> None:
    """
    Тестируем случай, когда файл не существует.
    """
    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert result == []
    mock_exists.assert_called_once_with("data/operations.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_load_transactions_empty_file(mock_file: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестируем случай, когда файл пустой.
    """
    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert result == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
    mock_exists.assert_called_once_with("data/operations.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_load_transactions_invalid_json(mock_file: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестируем случай, когда файл содержит некорректный JSON.
    """
    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert result == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
    mock_exists.assert_called_once_with("data/operations.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
def test_load_transactions_not_a_list(mock_file: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестируем случай, когда файл содержит JSON, но это не список.
    """
    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert result == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
    mock_exists.assert_called_once_with("data/operations.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "amount": 100.0}]))
def test_load_transactions_logging(
    mock_file: MagicMock, mock_exists: MagicMock, caplog: pytest.LogCaptureFixture
) -> None:
    """
    Тестируем логирование при успешной загрузке транзакций.
    """
    caplog.set_level(logging.INFO)  # Устанавливаем уровень логирования

    result: List[Dict[str, Any]] = load_transactions("data/operations.json")
    assert len(result) == 1
    assert result[0]["id"] == 1

    # Проверяем логи
    assert "Вызов функции load_transactions с аргументом: data/operations.json" in caplog.text
    assert "Успешно загружено 1 транзакций из файла: data/operations.json" in caplog.text
