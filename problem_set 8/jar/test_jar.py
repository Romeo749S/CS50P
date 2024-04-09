from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(1.3)
        Jar(-2)
    


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    


def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    jar.withdraw(1)
    assert jar.size == 0
    

    
        

