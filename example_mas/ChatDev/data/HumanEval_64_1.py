'''
This module contains the implementation of the vowels_count function
and its associated test cases.
'''
def vowels_count(s):
    """Count the number of vowels in a string.
    Vowels considered are 'a', 'e', 'i', 'o', 'u'. The letter 'y' is
    considered a vowel only if it appears at the end of the word.
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
    if s.endswith('y') or s.endswith('Y'):
        count += 1
    return count
def test_vowels_count():
    """Test cases for the vowels_count function."""
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("rhythm") == 0
    assert vowels_count("AEIOUY") == 6
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("") == 0
    assert vowels_count("bcdfg") == 0
    # Additional test cases
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 5
    assert vowels_count("quickly") == 3  # Fixed expected result
    assert vowels_count("QUICKLY") == 3
    assert vowels_count("crypt") == 0
    assert vowels_count("CRY") == 1
    print("All test cases passed.")
if __name__ == "__main__":
    test_vowels_count()