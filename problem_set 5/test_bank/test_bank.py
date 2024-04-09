from bank import value

def test_hello():
    assert value('hello') == 0

def test_h():
     assert value('h') == 20

def test_nothing():
     assert value('nigg') == 100

def test_upper():
     assert value('hEllo') == 0

def test_phrase():
     assert value('hello nigga') == 0



