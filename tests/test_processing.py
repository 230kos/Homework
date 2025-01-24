from typing import Any

from src.processing import data_list, filter_by_state, sort_by_date


def test_filter_by_state(filtered_list_by_state: Any)-> None:
    assert (filter_by_state(data_list)) == filtered_list_by_state


def test_sort_by_date(sorted_list_by_date: Any)-> None:
    assert sort_by_date(data_list) == sorted_list_by_date
