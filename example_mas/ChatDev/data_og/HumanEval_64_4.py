'''
This module contains a function to count vowels in a given string and test cases to validate its functionality.
'''
def vowels_count(s):
    """Count the number of vowels in a string.
    Vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' if it is at the end of the word.
    Args:
        s (str): The input string.
    Returns:
        int: The number of vowels in the string.
    """
    vowels = set('aeiou')
    count = sum(1 for char in s.lower() if char in vowels)
    if s and s[-1].lower() == 'y':
        count += 1
    return count
# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2, "Test case 1 failed"
    assert vowels_count("ACEDY") == 3, "Test case 2 failed"
    assert vowels_count("hello") == 2, "Test case 3 failed"
    assert vowels_count("sky") == 1, "Test case 4 failed"
    assert vowels_count("rhythm") == 0, "Test case 5 failed"
    assert vowels_count("AEIOUY") == 6, "Test case 6 failed"
    assert vowels_count("y") == 1, "Test case 7 failed"
    assert vowels_count("Y") == 1, "Test case 8 failed"
    assert vowels_count("") == 0, "Test case 9 failed"
    assert vowels_count("bcdfg") == 0, "Test case 10 failed"
    assert vowels_count("aeiou") == 5, "Test case 11 failed"
    assert vowels_count("AEIOU") == 5, "Test case 12 failed"
    assert vowels_count("bcdY") == 1, "Test case 13 failed"
    assert vowels_count("BCD") == 0, "Test case 14 failed"
    print("All test cases passed!")
# Run test cases
test_vowels_count()