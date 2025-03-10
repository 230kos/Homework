import json
import logging
import os
from typing import Any, Dict, List

# Создаем папку logs, если она не существует
log_dir = os.path.join("..", "logs")
os.makedirs(log_dir, exist_ok=True)

# Настройка логгера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень DEBUG

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(os.path.join("..", "logs", "utils.log"))  # Лог-файл в папке log
file_handler.setLevel(logging.DEBUG)

# Создание форматтера для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях. Если файл пустой, не найден или содержит не список,
    возвращает пустой список.
    """
    logger.info(f"Вызов функции load_transactions с аргументом: {file_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        # Открываем файл и загружаем данные
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Проверяем, что данные являются списком
        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций из файла: {file_path}")
            return data
        else:
            logger.error(f"Файл {file_path} содержит некорректные данные (ожидался список)")
            return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        # Если файл пустой или содержит некорректный JSON
        logger.error(f"Ошибка при загрузке файла {file_path}: {str(e)}")
        return []


"""
# Пример использования
if __name__ == "__main__":
    # Путь до файла operations.json
    file_path = os.path.join("..", "data", "operations.json")
    transactions = load_transactions(file_path)
    print(transactions)
"""
