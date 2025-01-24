from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Maestro 1234567890123456", "Maestro 1234 56 ** **** 3456"),
        ("Visa 1234567890123456", "Visa 1234 56 ** **** 3456"),
        ("12345678901234567890", " ** 7890"),
        ("Мир 1234567890", "Неверный номер карты или счёта"),
        ("", "Неверный номер карты или счёта"),
    ],
)
def test_mask_account_card(string: Union[str], expected_result: Union[str]) -> None:
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(string: Union[str], expected_result: Union[str]) -> None:
    assert get_date(string) == expected_result
