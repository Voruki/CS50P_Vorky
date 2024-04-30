import pytest
from um import count

def test_input():
    # Test case where "Um" occurs once in the sentence
    assert count("Um, thanks for the album.") == 1
    # Test case where "um" occurs once in the sentence
    assert count("um") == 1
    # Test case where "Um" occurs twice in the sentence
    assert count("Um, thanks, um...") == 2
    # Test case where "Um" occurs once in the sentence, followed by a question mark
    assert count("Um?") == 1
