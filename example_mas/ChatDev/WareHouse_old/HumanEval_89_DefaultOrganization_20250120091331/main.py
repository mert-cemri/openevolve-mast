'''
This module contains the encrypt function which takes a string as an argument
and returns a string encrypted with the alphabet being rotated by 4 positions.
'''
def encrypt(s):
    """Encrypts the input string by rotating each letter by 4 positions in the alphabet."""
    result = []
    for char in s:
        if char.isalpha():
            # Calculate the new character by shifting 4 positions
            new_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'