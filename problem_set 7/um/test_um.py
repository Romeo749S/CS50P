from um import count

def test_right_um():
    assert count('um um um um') == 4
    assert count(',um ,um .um. ') == 3

def test_wrong_um():
    assert count('umlet yummy') == 0
    assert count('umm uum ') == 0

def test_case_insensetively():
    assert count('um UM Um uM') == 4
    assert count('UUM uMM uuMM') == 0

