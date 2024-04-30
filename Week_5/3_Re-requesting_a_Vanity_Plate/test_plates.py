from plates import is_valid

def main():
    # Call all test functions
    test_one()
    test_two()
    test_three()
    test_four()

# Test case to check if plate is valid when it contains only letters and digits, and starts with letters.
def test_one():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False

# Test case to check if plate is invalid when it contains other characters than letters and digits, or starts with digits.
def test_two():
    assert is_valid("cs50p") == False
    assert is_valid("PI3.14") == False

# Test case to check if plate is invalid when it has less than 2 characters.
def test_three():
    assert is_valid('O') == False
    assert is_valid('OUTATIMEasasasdasdasda') == False

# Test case to check if plate is invalid when it contains only digits.
def test_four():
    assert is_valid('5as5as0as5sdaf5da56d56a5d6a5d') == False
    assert is_valid('15050055454545454') == False

# Check if the script is executed directly, and if so, call the main function.
if __name__ == "__main__":
    main()
