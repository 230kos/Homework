import os
from unittest.mock import patch, MagicMock
from typing import Any
import pytest
from src.masks import get_mask_card_number, get_mask_account

# Создаем папку logs, если она не существует
log_dir = os.path.join("..", "logs")
os.makedirs(log_dir, exist_ok=True)

# Фикстура для мокирования логгера
@pytest.fixture(autouse=True)
def mock_logging() -> Any:
    with patch("logging.FileHandler"):
        yield


def test_get_mask_card_number_valid() -> None:
    """
    Тестируем функцию get_mask_card_number с корректным номером карты.
    """
    result: Any = get_mask_card_number("1234567890123456")
    assert result == "1234 56 ** **** 3456"


def test_get_mask_card_number_invalid() -> None:
    """
    Тестируем функцию get_mask_card_number с некорректным номером карты.
    """
    result: Any = get_mask_card_number("1234")
    assert result == "Номер карты введён неверно"


def test_get_mask_account_valid() -> None:
    """
    Тестируем функцию get_mask_account с корректным номером счёта.
    """
    result: Any = get_mask_account("12345678901234567890")
    assert result == "** 7890"


def test_get_mask_account_invalid() -> None:
    """
    Тестируем функцию get_mask_account с некорректным номером счёта.
    """
    result: Any = get_mask_account("1234")
    assert result == "Номер счёта введён неверно"


@patch("logging.Logger.info")
def test_get_mask_card_number_logging(mock_logger_info: MagicMock) -> None:
    """
    Тестируем логирование в функции get_mask_card_number.
    """
    result: Any = get_mask_card_number("1234567890123456")
    assert result == "1234 56 ** **** 3456"

    # Проверяем, что логи были вызваны с правильными сообщениями
    mock_logger_info.assert_any_call("Вызов функции get_mask_card_number с аргументом: 1234567890123456")
    mock_logger_info.assert_any_call("Маскированный номер карты: 1234 56 ** **** 3456")


@patch("logging.Logger.error")
def test_get_mask_card_number_invalid_logging(mock_logger_error: MagicMock) -> None:
    """
    Тестируем логирование ошибки в функции get_mask_card_number.
    """
    result: Any = get_mask_card_number("1234")
    assert result == "Номер карты введён неверно"

    # Проверяем, что логи были вызваны с правильными сообщениями
    mock_logger_error.assert_called_once_with("Номер карты введён неверно")


@patch("logging.Logger.info")
def test_get_mask_account_logging(mock_logger_info: MagicMock) -> None:
    """
    Тестируем логирование в функции get_mask_account.
    """
    result: Any = get_mask_account("12345678901234567890")
    assert result == "** 7890"

    # Проверяем, что логи были вызваны с правильными сообщениями
    mock_logger_info.assert_any_call("Вызов функции get_mask_account с аргументом: 12345678901234567890")
    mock_logger_info.assert_any_call("Маскированный номер счёта: ** 7890")


@patch("logging.Logger.error")
def test_get_mask_account_invalid_logging(mock_logger_error: MagicMock) -> None:
    """
    Тестируем логирование ошибки в функции get_mask_account.
    """
    result: Any = get_mask_account("1234")
    assert result == "Номер счёта введён неверно"

    # Проверяем, что логи были вызваны с правильными сообщениями
    mock_logger_error.assert_called_once_with("Номер счёта введён неверно")
