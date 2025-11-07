'''
This module contains the implementation of the vowels_count function
and test cases to verify its correctness.
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
    vowels = set('aeiou')
    count = 0
    s = s.lower()  # Convert to lowercase to handle case insensitivity
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char == 'y' and i == len(s) - 1:
            count += 1
    return count
# Test cases
def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("hello") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("rhythm") == 0
    assert vowels_count("AEIOU") == 5
    assert vowels_count("y") == 1
    assert vowels_count("bcd") == 0
    assert vowels_count("Y") == 1
    assert vowels_count("aeiouy") == 6
    assert vowels_count("syzygy") == 1
    assert vowels_count("crypt") == 0
    assert vowels_count("encyclopedia") == 5  # Corrected expected count
# Run test cases
if __name__ == "__main__":
    test_vowels_count()
    print("All test cases passed.")