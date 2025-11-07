'''
This module contains the function `vowels_count` which counts the number of vowels in a given string.
Vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only if 'y' is at the end of the word).
'''
def vowels_count(s):
    """Counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it is at the end of the word.
    Args:
        s (str): The input string.
    Returns:
        int: The number of vowels in the string.
    """
    vowels = set('aeiou')
    count = 0
    s = s.lower()
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char == 'y' and i == len(s) - 1:
            count += 1
    return count
# Test cases
if __name__ == "__main__":
    # Basic test cases
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    # Additional test cases
    assert vowels_count("hello") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("rhythm") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOUY") == 6
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("bcd") == 0
    assert vowels_count("fly") == 1
    assert vowels_count("FLY") == 1
    print("All test cases passed!")