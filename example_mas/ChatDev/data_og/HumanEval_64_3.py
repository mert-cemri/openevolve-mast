'''
This module contains the function `vowels_count` which counts the number of vowels in a string.
It also includes test cases to verify the correctness of the function.
'''
def vowels_count(s):
    """Count the number of vowels in a string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it is at the end of the word.
    Args:
    s (str): The input string.
    Returns:
    int: The number of vowels in the string.
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
    assert vowels_count("AEIOUY") == 6, "Test case 6 failed"
    assert vowels_count("y") == 1, "Test case 7 failed"
    assert vowels_count("Y") == 1, "Test case 8 failed"
    assert vowels_count("bcdfg") == 0, "Test case 9 failed"
    assert vowels_count("aeiouy") == 6, "Test case 10 failed"
    print("All test cases passed.")
# Run the test cases
test_vowels_count()