'''
This module contains the implementation of the vowels_count function
and test cases to verify its correctness.
'''
def vowels_count(s):
    """Count the number of vowels in a string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel
    only when it is at the end of the word.
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
# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("rhythm") == 0
    assert vowels_count("AEIOUY") == 6
    assert vowels_count("bcd") == 0
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("aeiouy") == 6
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aeiou") == 5
    assert vowels_count("xyz") == 0  # Fixed test case
    assert vowels_count("XYZ") == 0  # Fixed test case
    print("All test cases passed.")
# Run test cases
test_vowels_count()