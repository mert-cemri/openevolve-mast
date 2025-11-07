'''
You are given a word. Your task is to find the closest vowel that stands between 
two consonants from the right side of the word (case sensitive).
Vowels in the beginning and ending doesn't count. Return empty string if you didn't
find any vowel met the above condition. 
You may assume that the given string contains English letter only.
Example:
get_closest_vowel("yogurt") ==> "u"
get_closest_vowel("FULL") ==> "U"
get_closest_vowel("quick") ==> ""
get_closest_vowel("ab") ==> ""
'''
def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    length = len(word)
    # Start from the second last character and move to the second character
    for i in range(length - 2, 0, -1):
        if word[i] in vowels:
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                return word[i]
    return ""
# Example usage
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""