from fuel import convert, gauge
import pytest

def main():
    # Call all test functions
    test_one()
    test_two()
    test_excepts()

# Test case to check conversion and gauge representation for valid inputs.
def test_one():
    assert gauge(convert('100/1000')) == '10%'
    assert gauge(convert('5/10')) == '50%'

# Test case to check gauge representation for edge cases.
def test_two():
    assert gauge(convert('1/1000')) == 'E'
    assert gauge(convert('5000/5000')) == 'F'
    assert gauge(convert('9999/10000')) == 'F'

# Test case to check exception handling for invalid inputs.
def test_excepts():
    # Test for ZeroDivisionError when denominator is zero.
    with pytest.raises(ZeroDivisionError):
        convert('10/0')

    # Test for ValueError when input format is invalid.
    with pytest.raises(ValueError):
        convert('moao/as')

# Check if the script is executed directly, and if so, call the main function.
if __name__ == "__main__":
    main()
