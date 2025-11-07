'''
Given a string s and a natural number n, implement a function that returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s. If the string s is empty then the function should return an empty list. Note: you may assume the input string contains only letters and spaces.
'''
def select_words(s, n):
    # Define vowels
    vowels = set('aeiouAEIOU')
    # Split the string into words
    words = s.split()
    # Initialize the result list
    result = []
    # Iterate over each word
    for word in words:
        # Count consonants in the word
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        # If the consonant count matches n, add the word to the result
        if consonant_count == n:
            result.append(word)
    return result