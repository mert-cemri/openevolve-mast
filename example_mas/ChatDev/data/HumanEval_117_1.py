'''
Given a string s and a natural number n, implement a function that returns a list of all words from string s that contain exactly n consonants, in the order these words appear in the string s. If the string s is empty, the function should return an empty list. Assume the input string contains only letters and spaces.
'''
def select_words(s, n):
    vowels = set('aeiouAEIOU')
    words = s.split()
    result = []
    for word in words:
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)
    return result