import pytest
from working import convert

def test_errors():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
        convert('9 AM - 17 PM')

def test_regular():
    assert convert('2:00 AM to 5:00 PM') == '02:00 to 17:00'
    assert convert('2:00 PM to 5:00 AM') == '14:00 to 05:00'

def test_no_minutes():
    assert convert('2 AM to 5 PM') == '02:00 to 17:00'
    assert convert('2 PM to 5 AM') == '14:00 to 05:00'
    assert convert('2 PM to 3:00 AM') == '14:00 to 03:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

def test_out_of_range():
    with pytest.raises(ValueError):
        convert('2:70 AM to 6:80 PM')
        
    

    
        

