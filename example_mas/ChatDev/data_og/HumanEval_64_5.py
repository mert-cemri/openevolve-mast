'''
This script contains the function `vowels_count` which counts the number of vowels in a given string.
Additional test cases are provided to ensure the function works correctly.
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
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char.lower() == 'y' and i == len(s) - 1:
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
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("by") == 1
    assert vowels_count("BY") == 1
    assert vowels_count("bcdfg") == 0
    assert vowels_count("AEIOU") == 5
    assert vowels_count("") == 0
# Run test cases
test_vowels_count()