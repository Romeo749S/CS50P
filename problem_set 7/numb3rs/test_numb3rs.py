from numb3rs import validate
import pytest

def test_regular_ip():
    assert validate('0.666.666.666') == 0
    assert validate('127.0.0.1') == 1
    assert validate('255.255.255.255') == 1
    assert validate('512.512.512.512') == 0
    assert validate('1.2.3.1000') == 0
    assert validate('cat') == 0
