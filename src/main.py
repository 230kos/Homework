from typing import Any

from src.generators import filter_by_currency
from src.operations import filter_transactions_by_description
from src.processing import filter_by_state, sort_by_date
from src.transaction_reader import load_transactions_csv, load_transactions_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> Any:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        transactions = load_transactions("../data/operations.json")
        print("Для обработки выбран JSON-файл")
    elif choice == "2":
        transactions = load_transactions_csv("../data/transactions.csv")
        print("Для обработки выбран CSV-файл")
    elif choice == "3":
        transactions = load_transactions_excel("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")
    else:
        print("Неверный выбор. Программа завершена.")
        return

    while True:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        ).upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, state)
            print(f"Операции отфильтрованы по статусу {state}")
            break
        else:
            print(f"Статус операции {state} недоступен.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if order == "по возрастанию":
            transactions = sort_by_date(transactions, reverse=False)
        elif order == "по убыванию":
            transactions = sort_by_date(transactions, reverse=True)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_description == "да":
        search_string = input("Введите слово для поиска: ")
        transactions = filter_transactions_by_description(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for item in transactions:
            # Безопасный доступ к ключам
            date_str = get_date(item.get("date", "N/A"))
            descr_str = item.get("description", "N/A")
            from_str = mask_account_card(str(item.get("from", "N/A"))) + " -> " if item.get("from") else ""
            to_str = mask_account_card(item.get("to", "N/A"))
            summa_str = item.get("amount") or item.get("operationAmount", {}).get("amount")
            currency_str = item.get("currency_code") or item.get("operationAmount", {}).get("currency", {}).get("code")
            print(f"{date_str} {descr_str}\n{from_str}{to_str}\nСумма: {summa_str} {currency_str}\n")


if __name__ == "__main__":
    main()
