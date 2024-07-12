import pytest
from calc.mean import calc_mean

def test_single_float():
    assert calc_mean(1.2) == 1.2

def test_list_of_floats():
    assert calc_mean([1.2, 1.3, 1.4]) == pytest.approx(1.3)

def test_empty_list():
    with pytest.raises(ZeroDivisionError):
        calc_mean([])

def test_none_input():
    assert calc_mean(None) == ""

def test_invalid_input_string():
    with pytest.raises(TypeError):
        calc_mean("abc")

def test_invalid_input_mixed_list():
    with pytest.raises(TypeError):
        calc_mean([1.2, "abc", 1.4])