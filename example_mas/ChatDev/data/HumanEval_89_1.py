'''
This module contains a function to encrypt a string by rotating each letter
in the alphabet by a specified number of positions. The rotation is by 4 positions.
'''
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places (i.e., 4 places).
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result.append(new_char)
        else:
            result.append(char)  # Non-lowercase characters are not encrypted
    return ''.join(result)
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'