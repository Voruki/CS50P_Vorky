from seasons import convert

def test_date():
    # Test case for a large number of minutes
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    # Test case for a small number of minutes
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
