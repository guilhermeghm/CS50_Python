from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_convert():
    with pytest.raises(ValueError):
        convert("two/three")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    assert convert("2/4") == 50
    assert convert("4/4") == 100
