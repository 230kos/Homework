import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму в указанной валюте в рубли.

    :param amount: Сумма для конвертации.
    :param currency: Исходная валюта (например, "USD" или "EUR").
    :return: Сумма в рублях (тип float).
    """
    if currency == "RUB":
        return amount  # Если валюта уже в рублях, возвращаем сумму без изменений

    # Заголовки для запроса к API
    headers = {"apikey": API_KEY}

    # Параметры запроса
    params = {"base": currency, "symbols": "RUB"}  # Исходная валюта  # Целевая валюта

    try:
        # Выполняем запрос к API
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Проверяем, что запрос успешен

        # Получаем курс валюты
        data = response.json()
        rate = data["rates"]["RUB"]

        # Конвертируем сумму в рубли
        return float(amount * rate)
    except (requests.RequestException, KeyError) as e:
        # В случае ошибки возвращаем 0 или можно выбросить исключение
        print(f"Ошибка при конвертации валюты: {e}")
        return 0.0


def get_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма в рублях (тип float).
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency not in ["RUB", "USD", "EUR"]:
        raise ValueError(f"Неподдерживаемая валюта: {currency}")

    if currency == "RUB":
        return float(amount)
    else:
        return convert_to_rub(amount, currency)


# Пример использования
if __name__ == "__main__":
    # Пример транзакции
    transaction = {"id": 1, "date": "2023-10-01", "amount": 100.0, "currency": "USD", "description": "Покупка товара"}

    # Получаем сумму в рублях
    amount_in_rub = get_amount_in_rub(transaction)
    amount_in_rub_rounded = round(amount_in_rub, 2)
    print(f"Сумма транзакции в рублях: {amount_in_rub_rounded}")
