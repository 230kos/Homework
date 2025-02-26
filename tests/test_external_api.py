import unittest
from typing import Any, Dict
from unittest.mock import Mock, patch

import requests

# Импортируем функции, которые будем тестировать
from src.external_api import convert_to_rub, get_amount_in_rub


class TestCurrencyConversion(unittest.TestCase):
    @patch("requests.get")
    def test_convert_to_rub_usd(self, mock_get: Mock) -> None:
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем функцию и проверяем результат
        result: float = convert_to_rub(100.0, "USD")
        self.assertEqual(result, 7500.0)

    @patch("requests.get")
    def test_convert_to_rub_eur(self, mock_get: Mock) -> None:
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 85.0}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем функцию и проверяем результат
        result: float = convert_to_rub(100.0, "EUR")
        self.assertEqual(result, 8500.0)

    def test_convert_to_rub_rub(self) -> None:
        # Если валюта уже в рублях, возвращаем сумму без изменений
        result: float = convert_to_rub(100.0, "RUB")
        self.assertEqual(result, 100.0)

    @patch("requests.get")
    def test_convert_to_rub_api_error(self, mock_get: Mock) -> None:
        # Мокируем ошибку запроса
        mock_get.side_effect = requests.RequestException("API Error")

        # Вызываем функцию и проверяем, что возвращается 0.0
        result: float = convert_to_rub(100.0, "USD")
        self.assertEqual(result, 0.0)

    def test_get_amount_in_rub_rub(self) -> None:
        # Транзакция уже в рублях
        transaction: Dict[str, Any] = {"amount": 100.0, "currency": "RUB"}
        result: float = get_amount_in_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch("requests.get")
    def test_get_amount_in_rub_usd(self, mock_get: Mock) -> None:
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Транзакция в USD
        transaction: Dict[str, Any] = {"amount": 100.0, "currency": "USD"}
        result: float = get_amount_in_rub(transaction)
        self.assertEqual(result, 7500.0)

    def test_get_amount_in_rub_unsupported_currency(self) -> None:
        # Транзакция с неподдерживаемой валютой
        transaction: Dict[str, Any] = {"amount": 100.0, "currency": "GBP"}
        with self.assertRaises(ValueError):
            get_amount_in_rub(transaction)
