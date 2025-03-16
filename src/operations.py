import re
from collections import Counter


def filter_transactions_by_description(transactions: list, string_to_find: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    found_transactions = []
    for transaction in transactions:
        if re.findall(string_to_find.lower(), str(transaction.get("description")).lower()):
            found_transactions.append(transaction)
    return found_transactions


def count_transactions_by_category(transactions: list, categories: list) -> dict:
    """Функция подсчитывает количество транзакций из переданного списка по каждой категории из переданного списка."""
    categories_lower = [cat.lower() for cat in categories]
    transactions_to_count = []
    for transaction in transactions:
        if str(transaction.get("description")).lower() in categories_lower:
            transactions_to_count.append(transaction.get("description"))
    counted_categories = Counter(transactions_to_count)
    return counted_categories
