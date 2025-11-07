'''
This module contains the function get_closest_vowel which finds the closest vowel
that stands between two consonants from the right side of a given word.
'''
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 
    You may assume that the given string contains English letter only.
    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiouAEIOU"
    length = len(word)
    # Iterate from the second last character to the second character
    for i in range(length - 2, 0, -1):
        if word[i] in vowels:
            # Check if the vowel is between two consonants
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]
    return ""