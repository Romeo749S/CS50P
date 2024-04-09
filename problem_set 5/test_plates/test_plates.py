from plates import is_valid

def test_first_letters():
    assert is_valid('bb') == 1
    assert is_valid('11') == 0

def test_min_max_length():
    assert is_valid('b') == 0
    assert is_valid('bbb1234') == 0

def test_ends_with_num():
    assert is_valid('bb123b') == 0
    assert is_valid('bb1234') == 1

def test_punctuation_spaces():
    assert is_valid('bb ,12') == 0

def test_zero():
    assert is_valid('bb012') == 0
    assert is_valid('bb1012') == 1


