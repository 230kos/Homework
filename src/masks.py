import logging
import os
from typing import Any

# Настройка логгера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Уровень DEBUG

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(os.path.join("..", "logs", "masks.log"))  # Лог-файл в папке log
file_handler.setLevel(logging.DEBUG)

# Создание форматтера для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_mask_card_number(card_numbers: Any) -> Any:
    """Принимает на вход номер карты и возвращает ее маску."""
    logger.info(f"Вызов функции get_mask_card_number с аргументом: {card_numbers}")

    if card_numbers.isdigit() and len(card_numbers) == 16:
        masked_number = f"{card_numbers[:4]} {card_numbers[4:6]} ** **** {card_numbers[-4:]}"
        logger.info(f"Маскированный номер карты: {masked_number}")
        return masked_number
    else:
        logger.error("Номер карты введён неверно")
        return "Номер карты введён неверно"


def get_mask_account(account_numbers: Any) -> Any:
    """Принимает на вход номер счета и возвращает его маску."""
    logger.info(f"Вызов функции get_mask_account с аргументом: {account_numbers}")

    if account_numbers.isdigit() and len(account_numbers) == 20:
        masked_account = f"** {account_numbers[-4:]}"
        logger.info(f"Маскированный номер счёта: {masked_account}")
        return masked_account
    else:
        logger.error("Номер счёта введён неверно")
        return "Номер счёта введён неверно"


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))  # Корректный номер карты
    print(get_mask_card_number("1234"))  # Некорректный номер карты
    print(get_mask_account("12345678901234567890"))  # Корректный номер счёта
    print(get_mask_account("1234"))  # Некорректный номер счёта
