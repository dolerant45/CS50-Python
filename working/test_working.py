import pytest
from working import convert

def test_working():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM 11:00 PM")

