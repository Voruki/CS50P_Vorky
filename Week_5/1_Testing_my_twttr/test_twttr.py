from twttr import shorten

# Test case to check if the function correctly shortens the string "twitter" to "twttr".
def test_strings():
    assert shorten("twitter") == 'twttr'

# Test case to check if the function correctly shortens the uppercase string "TWITTER" to "TWTTR".
def test_names():
    assert shorten("TWITTER") == 'TWTTR'

# Test cases to check if the function handles numeric input correctly.
# Since numbers do not contain vowels, the function should return the same input string.
def test_numbers():
    assert shorten("123987") == '123987'
    assert shorten("123456879") == '123456879'

# Test case to check if the function correctly shortens a string containing both uppercase and lowercase characters ("hello twitter") to "hll twttr".
def test_uppercase():
    assert shorten("hello twitter") == 'hll twttr'
