'''
remove_vowels is a function that takes a string and returns a string without vowels.
'''
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)