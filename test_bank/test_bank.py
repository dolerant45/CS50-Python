import pytest
from bank import value

def test_bank():
    assert value("Hi") == 20
    assert value("Hello") == 0
    assert value("happy") == 20
    assert value("hdfhjf, Fkdfk") == 20
    assert value("sfdtsfdt, sgvdgv, 1234") == 100
    assert value("      sfdtsfdt, sgvdgv, 1234        ") == 100
    assert value("HELLO sfdtsfdt, sgvdgv, 1234") == 0
