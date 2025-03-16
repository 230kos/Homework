from typing import Any
import pytest


@pytest.fixture
def filtered_list_by_state() -> Any:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sorted_list_by_date() -> Any:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

@pytest.fixture
def json_data() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": 31957.58, "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
        },
        {
            "id": 441945886,
            "state": "CANCELED",
            "date": "2019-10-26T10:50:58.294041",
            "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 1596837868705200",
            "to": "Счет 64686473678894779200",
        },
    ]


@pytest.fixture
def csv_or_excel_data() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "amount": 31957.58,
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "amount": 100.00,
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
        },
        {
            "id": 441945886,
            "state": "CANCELED",
            "date": "2019-10-26T10:50:58.294041",
            "amount": 200.00,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "description": "Перевод с карты на карту",
            "from": "Maestro 1596837868705200",
            "to": "Счет 64686473678894779200",
        },
    ]