import os
from typing import Any, Dict, List

import pandas as pd


def load_transactions_csv(file_path: str) -> list[dict[Any, Any]]:
    """
    Загружает данные о финансовых транзакциях из CSV-файла.

    :param file_path: Путь до CSV-файла.
    :return: Список словарей с данными о транзакциях. Если файл пустой или не найден,
    возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        # Чтение CSV-файла
        df: pd.DataFrame = pd.read_csv(file_path)
        # Преобразование DataFrame в список словарей
        return df.to_dict("records")
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return []


def load_transactions_excel(file_path: str) -> list[dict[Any, Any]]:
    """
    Загружает данные о финансовых транзакциях из Excel-файла.

    :param file_path: Путь до Excel-файла.
    :return: Список словарей с данными о транзакциях. Если файл пустой или не найден,
    возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        # Чтение Excel-файла
        df: pd.DataFrame = pd.read_excel(file_path)
        # Преобразование DataFrame в список словарей
        return df.to_dict("records")
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return []


# Пример использования
if __name__ == "__main__":
    # Путь до файла transactions.csv
    csv_file_path: str = os.path.join("..", "data", "transactions.csv")
    csv_transactions: List[Dict[str, Any]] = load_transactions_csv(csv_file_path)
    print(csv_transactions)

    # Путь до файла transactions_excel.xlsx
    excel_file_path: str = os.path.join("..", "data", "transactions_excel.xlsx")
    excel_transactions: List[Dict[str, Any]] = load_transactions_excel(excel_file_path)
    print(excel_transactions)
