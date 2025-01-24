from typing import Any


def get_mask_card_number(card_numbers: Any) -> Any:
    """принимает на вход номер карты и возвращает ее маску"""
    if card_numbers.isdigit() and len(card_numbers) == 16:
        return f"{card_numbers[:4]} {card_numbers[4:6]} ** **** {card_numbers[-4:]}"
    else:
        return "Номер карты введён неверно"


def get_mask_account(account_numbers: Any) -> Any:
    """принимает на вход номер счета и возвращает его маску"""
    if account_numbers.isdigit() and len(account_numbers) == 20:
        return f"** {account_numbers[-4:]}"
    else:
        return "Номер счёта введён неверно"
