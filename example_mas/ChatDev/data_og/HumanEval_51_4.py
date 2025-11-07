'''
remove_vowels is a function that takes a string and returns a string without vowels.
'''
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])
# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))  # Output: ''
    print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # Output: 'bcdf'
    print(remove_vowels('aaaaa'))  # Output: ''
    print(remove_vowels('aaBAA'))  # Output: 'B'
    print(remove_vowels('zbcd'))  # Output: 'zbcd'