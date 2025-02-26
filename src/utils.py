import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях. Если файл пустой, не найден или содержит не список,
    возвращает пустой список.
    """
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        return []

    try:
        # Открываем файл и загружаем данные
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Проверяем, что данные являются списком
        if isinstance(data, list):
            return data
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        # Если файл пустой или содержит некорректный JSON
        return []


# Пример использования
if __name__ == "__main__":
    # Путь до файла operations.json
    file_path = os.path.join("data", "operations.json")
    transactions = load_transactions(file_path)
    print(transactions)
