import pytest
from plates import is_valid

def test_valid():
    assert is_valid("A1") == False
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("Aa") == True
    assert is_valid("AAfffff") == False
    assert is_valid("Aaffff") == True
    assert is_valid("Aa22a") == False
    assert is_valid("Aa222") == True
    assert is_valid("Aa022") == False
    assert is_valid("Aa d") == False
    assert is_valid("Aa,d") == False
    assert is_valid("Aa.d") == False
    assert is_valid("Aa-d") == False
    assert is_valid("Aa_d") == False
