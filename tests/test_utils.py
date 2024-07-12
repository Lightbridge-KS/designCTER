import pytest
from calc._utils import parse_str_to_num_or_list


def test_single_number():
    assert parse_str_to_num_or_list(" 1.2 ") == 1.2

def test_multiple_numbers_spaces():
    assert parse_str_to_num_or_list(" 1.2   1.3 ") == [1.2, 1.3]

def test_multiple_numbers_commas():
    assert parse_str_to_num_or_list("1.2,1.3 ") == [1.2, 1.3]

def test_multiple_numbers_comma_space():
    assert parse_str_to_num_or_list("1.2, 1.3 ") == [1.2, 1.3]

def test_multiple_numbers_comma_multiple_spaces():
    assert parse_str_to_num_or_list("1.2,   1.3 ") == [1.2, 1.3]

def test_empty_string():
    assert parse_str_to_num_or_list("") is None

def test_invalid_input_not_string():
    with pytest.raises(ValueError):
        parse_str_to_num_or_list(123)

def test_invalid_input_non_numeric_string():
    with pytest.raises(ValueError):
        parse_str_to_num_or_list("abc")

def test_mixed_separators():
    assert parse_str_to_num_or_list("1.2,  1.3,   1.4") == [1.2, 1.3, 1.4]

def test_only_spaces():
    assert parse_str_to_num_or_list("   ") is None
