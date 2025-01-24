import datetime
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


def get_date(user_date: Union[str]) -> Union[str]:
    """функция, которая принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407 и
    возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
