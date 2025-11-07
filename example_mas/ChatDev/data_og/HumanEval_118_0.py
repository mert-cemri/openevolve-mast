'''
This function finds the closest vowel that stands between two consonants from the right side of the word.
Vowels at the beginning and end of the word do not count. If no such vowel is found, it returns an empty string.
'''
def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    length = len(word)
    # Iterate from the second last character to the second character
    for i in range(length - 2, 0, -1):
        if word[i] in vowels:
            # Check if the surrounding characters are consonants
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]
    return ""
# Example usage
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""