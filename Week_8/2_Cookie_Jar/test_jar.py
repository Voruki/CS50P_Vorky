import pytest
from jar import Jar

def test_init():
    # Test initialization of Jar object.
    jar = Jar()

def test_str():
    # Test string representation of Jar object.
    jar = Jar()
    assert str(jar) == ""  # Test empty jar.
    jar.deposit(1)
    assert str(jar) == "🍪"  # Test jar with one cookie.
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # Test jar with multiple cookies.

def test_deposit():
    # Test depositing cookies into the jar.
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1  # Check size after depositing one cookie.
    with pytest.raises(ValueError):
        jar.deposit(20)  # Test depositing more cookies than the jar's capacity.

def test_withdraw():
    # Test withdrawing cookies from the jar.
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3  # Check size after withdrawing one cookie.
    with pytest.raises(ValueError):
        jar.withdraw(100)  # Test withdrawing more cookies than available in the jar.

