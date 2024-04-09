from seasons import format_check , date_time_check  , nums_to_words
import pytest


def test_format_time():
    with pytest.raises(SystemExit):
        format_check('January 1, 2004')
        
def test_time_date():
    with pytest.raises(SystemExit):
        date_time_check(2004, 13 , 31)

def test_nums_to_words():
    assert nums_to_words(43) == 'Forty-three minutes'


    