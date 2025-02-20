# test_utils.py
import json
import unittest
from unittest.mock import mock_open, patch
from typing import Any

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):
    @patch("os.path.exists", return_value=True)
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 200.0, "currency": "USD"}]
        ),
    )
    def test_load_transactions_success(self, mock_file: Any, mock_exists: Any) -> None:
        """
        Тестируем успешную загрузку транзакций из файла.
        """
        result = load_transactions("data/operations.json")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 2)
        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")

    @patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists: Any) -> None:
        """
        Тестируем случай, когда файл не существует.
        """
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with("data/operations.json")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_transactions_empty_file(self, mock_file: Any, mock_exists: Any) -> None:
        """
        Тестируем случай, когда файл пустой.
        """
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    def test_load_transactions_invalid_json(self, mock_file: Any, mock_exists: Any) -> None:
        """
        Тестируем случай, когда файл содержит некорректный JSON.
        """
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
    def test_load_transactions_not_a_list(self, mock_file: Any, mock_exists: Any) -> None:
        """
        Тестируем случай, когда файл содержит JSON, но это не список.
        """
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
