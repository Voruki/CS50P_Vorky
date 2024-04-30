import pytest
from working import convert

def test_convert():
    # Test cases for valid input formats
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error():
    # Test cases for invalid input formats that should raise ValueError
    with pytest.raises(ValueError):
        convert("9AM - 5PM")  # Incorrect separator
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Incorrect input format
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")  # Invalid hours
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Invalid minutes

