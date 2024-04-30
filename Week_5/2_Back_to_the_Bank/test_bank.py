from bank import value

# Test case to check if the function correctly returns a value of 20 for inputs that start with 'H' or 'h' followed by any other character.
def test_20():
    assert value("HY MIKE") == 20
    assert value("HOW ?") == 20

# Test case to check if the function correctly returns a value of 100 for inputs that do not start with 'hello' and do not start with 'H' or 'h'.
def test_100():
    assert value("very nice") == 100
    assert value("zodiac") == 100

# Test case to check if the function correctly returns a value of 0 for inputs that start with 'hello' (case-insensitive).
def test_0():
    assert value("Hello Temp") == 0
    assert value("HelLo temp") == 0
    assert value("HELLO temp") == 0
