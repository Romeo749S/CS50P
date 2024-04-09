from twttr import shorten


def test_lower_input():
    assert shorten('maslo') == 'msl'


def test_upper_input():
    assert shorten('mAslO') == 'msl'

def test_numbers_input():
    assert shorten('maslo1') == 'msl1'

def test_punctuation_input():
    assert shorten('maslo,') == 'msl,'




