import pytest
from twttr import shorten

def test_twttr():
    assert shorten("Instagram") == "nstgrm"
    assert shorten("Wow, thanks1") == "Ww, thnks1"
