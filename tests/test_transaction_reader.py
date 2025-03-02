from unittest.mock import patch, MagicMock
import pandas as pd
from typing import List, Dict, Any
from src.transaction_reader import load_transactions_csv, load_transactions_excel


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_load_transactions_csv_success(mock_read_csv: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует успешное чтение данных из CSV-файла.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок данных CSV
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200], "description": ["Payment", "Refund"]})
    mock_read_csv.return_value = mock_data

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_csv("dummy_path.csv")

    # Проверка результата
    assert result == [
        {"id": 1, "amount": 100, "description": "Payment"},
        {"id": 2, "amount": 200, "description": "Refund"},
    ]


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_load_transactions_csv_file_not_found(mock_read_csv: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда CSV-файл не найден.
    """
    # Мок для os.path.exists
    mock_exists.return_value = False

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_csv("non_existent.csv")

    # Проверка результата
    assert result == []


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_load_transactions_csv_empty_file(mock_read_csv: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда CSV-файл пустой.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок для пустого файла
    mock_read_csv.side_effect = pd.errors.EmptyDataError

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_csv("empty.csv")

    # Проверка результата
    assert result == []


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_load_transactions_excel_success(mock_read_excel: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует успешное чтение данных из Excel-файла.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок данных Excel
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200], "description": ["Payment", "Refund"]})
    mock_read_excel.return_value = mock_data

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_excel("dummy_path.xlsx")

    # Проверка результата
    assert result == [
        {"id": 1, "amount": 100, "description": "Payment"},
        {"id": 2, "amount": 200, "description": "Refund"},
    ]


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_load_transactions_excel_file_not_found(mock_read_excel: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда Excel-файл не найден.
    """
    # Мок для os.path.exists
    mock_exists.return_value = False

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_excel("non_existent.xlsx")

    # Проверка результата
    assert result == []


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_load_transactions_excel_empty_file(mock_read_excel: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда Excel-файл пустой.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок для пустого файла
    mock_read_excel.side_effect = pd.errors.EmptyDataError

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_excel("empty.xlsx")

    # Проверка результата
    assert result == []


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_load_transactions_csv_invalid_data(mock_read_csv: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда CSV-файл содержит некорректные данные.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок для некорректных данных
    mock_read_csv.side_effect = pd.errors.ParserError

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_csv("invalid.csv")

    # Проверка результата
    assert result == []


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_load_transactions_excel_invalid_data(mock_read_excel: MagicMock, mock_exists: MagicMock) -> None:
    """
    Тестирует случай, когда Excel-файл содержит некорректные данные.
    """
    # Мок для os.path.exists
    mock_exists.return_value = True

    # Мок для некорректных данных
    mock_read_excel.side_effect = pd.errors.ParserError

    # Вызов функции
    result: List[Dict[str, Any]] = load_transactions_excel("invalid.xlsx")

    # Проверка результата
    assert result == []
