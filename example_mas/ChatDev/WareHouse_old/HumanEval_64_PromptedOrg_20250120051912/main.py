'''
This module contains the implementation of the vowels_count function
and its associated test cases.
'''
def vowels_count(s):
    """Count the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only
    if it appears at the end of the word.
    Args:
        s (str): The input string.
    Returns:
        int: The number of vowels in the string.
    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = set('aeiouAEIOU')
    count = sum(1 for char in s if char in vowels)
    if len(s) > 0 and (s[-1] == 'y' or s[-1] == 'Y'):
        count += 1
    return count
def test_vowels_count():
    """Test cases for the vowels_count function."""
    assert vowels_count("abcde") == 2, "Test case 1 failed"
    assert vowels_count("ACEDY") == 3, "Test case 2 failed"
    assert vowels_count("hello") == 2, "Test case 3 failed"
    assert vowels_count("sky") == 1, "Test case 4 failed"
    assert vowels_count("rhythm") == 0, "Test case 5 failed"
    assert vowels_count("Y") == 1, "Test case 6 failed"
    assert vowels_count("AEIOUY") == 6, "Test case 7 failed"
    assert vowels_count("") == 0, "Test case 8 failed"
    assert vowels_count("bcdfg") == 0, "Test case 9 failed"
    assert vowels_count("aeiou") == 5, "Test case 10 failed"
    assert vowels_count("AEIOU") == 5, "Test case 11 failed"
    assert vowels_count("y") == 1, "Test case 12 failed"
    assert vowels_count("Yay") == 2, "Test case 13 failed"
    assert vowels_count("crypt") == 0, "Test case 14 failed"
    assert vowels_count("bY") == 1, "Test case 15 failed"
    print("All test cases passed.")
# Run the test cases
test_vowels_count()