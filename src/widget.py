from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: Union[str]) -> Union[str]:
    """принимает на вход информацию как о картах, так и о счетах и возвращает их маски"""
    data_type = ""
    digits = ""
    digits_count = 0
    for i in type_and_number:
        if i.isalpha():
            data_type += i
        elif i.isdigit():
            digits += i
            digits_count += 1
    if digits_count == 16:
        return f"{data_type} {get_mask_card_number(digits)}"
    elif digits_count == 20:
        return f"{data_type} {get_mask_account(digits)}"
    else:
        return "Неверный номер карты или счёта"


def get_date(user_date: str) -> str:
    """
    Преобразует строку с датой в формате ISO (с микросекундами или с Z) в строку с датой в формате ДД.ММ.ГГГГ.

    :param user_date: Строка с датой в формате ISO (например, '2020-01-01T05:03:33Z' или '2020-01-01T05:03:33.123456').
    :return: Строка с датой в формате ДД.ММ.ГГГГ.
    """
    try:
        # Пытаемся распарсить дату с микросекундами
        date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        try:
            # Если не получилось, пробуем распарсить дату с Z
            date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            # Если и это не получилось, возвращаем "N/A" или выбрасываем исключение
            return "N/A"

    # Преобразуем дату в формат ДД.ММ.ГГГГ
    return date_format.strftime("%d.%m.%Y")
