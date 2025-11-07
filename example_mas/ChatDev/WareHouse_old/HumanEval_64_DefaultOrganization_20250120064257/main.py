'''
This module contains a function to count vowels in a given string and a set of test cases to verify its correctness.
'''
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiou"
    count = 0
    s = s.lower()  # Convert to lowercase to handle case insensitivity
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char == 'y' and i == len(s) - 1:
            count += 1
    return count
def test_vowels_count():
    """Test cases for the vowels_count function."""
    assert vowels_count("abcde") == 2, "Test case 1 failed"
    assert vowels_count("ACEDY") == 3, "Test case 2 failed"
    assert vowels_count("hello") == 2, "Test case 3 failed"
    assert vowels_count("sky") == 1, "Test case 4 failed"
    assert vowels_count("rhythm") == 0, "Test case 5 failed"
    assert vowels_count("aeiou") == 5, "Test case 6 failed"
    assert vowels_count("AEIOUY") == 6, "Test case 7 failed"
    assert vowels_count("y") == 1, "Test case 8 failed"
    assert vowels_count("Y") == 1, "Test case 9 failed"
    assert vowels_count("") == 0, "Test case 10 failed"
    assert vowels_count("bcd") == 0, "Test case 11 failed"
    assert vowels_count("aeiouy") == 6, "Test case 12 failed"
    assert vowels_count("AEIOU") == 5, "Test case 13 failed"
    assert vowels_count("yoyo") == 2, "Test case 14 failed"
    assert vowels_count("crypt") == 0, "Test case 15 failed"
    assert vowels_count("YELLOW") == 2, "Test case 16 failed"
    assert vowels_count("university") == 5, "Test case 17 failed"
    assert vowels_count("PYTHON") == 1, "Test case 18 failed"
    print("All test cases passed!")
# Run the test cases
test_vowels_count()