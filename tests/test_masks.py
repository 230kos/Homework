from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number()-> None:
    assert get_mask_card_number("1234567890123456") == "1234 56 ** **** 3456"
    assert get_mask_card_number("1234567890") == "Номер карты введён неверно"
    assert get_mask_card_number("") == "Номер карты введён неверно"
    assert get_mask_card_number("python") == "Номер карты введён неверно"


def test_get_mask_account()-> None:
    assert get_mask_account("12345678901234567890") == "** 7890"
    assert get_mask_account("12345") == "Номер счёта введён неверно"
    assert get_mask_account("") == "Номер счёта введён неверно"
    assert get_mask_account("homework") == "Номер счёта введён неверно"
