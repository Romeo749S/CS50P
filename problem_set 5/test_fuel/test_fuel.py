from fuel import convert , gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('2/1')
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    assert convert('1/4') == 25

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

    

    