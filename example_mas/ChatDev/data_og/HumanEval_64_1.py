'''
This module contains a function to count vowels in a given string and test cases to verify its correctness.
'''
def vowels_count(s):
    """Count the number of vowels in a string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it is at the end of the word.
    Args:
    s (str): The input string.
    Returns:
    int: The number of vowels in the string.
    """
    vowels = set('aeiou')
    count = sum(1 for char in s.lower() if char in vowels)
    if s.lower().endswith('y') and count == 0:
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
    assert vowels_count("bcd") == 0, "Test case 7 failed"
    assert vowels_count("y") == 1, "Test case 8 failed"
    assert vowels_count("Y") == 1, "Test case 9 failed"
    assert vowels_count("aeiouy") == 6, "Test case 10 failed"
    assert vowels_count("crypt") == 1, "Test case 11 failed"
    assert vowels_count("syzygy") == 1, "Test case 12 failed"
    assert vowels_count("queue") == 4, "Test case 13 failed"
    assert vowels_count("rhythms") == 0, "Test case 14 failed"
# Run test cases
test_vowels_count()
print("All test cases passed.")