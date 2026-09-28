import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/1") == 100
    assert convert("1/4") == 25
    assert convert("1/5") == 20

def test_value_error():
    with pytest.raises(ValueError):
        convert("c/c")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-1/4")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(40) == "40%"
