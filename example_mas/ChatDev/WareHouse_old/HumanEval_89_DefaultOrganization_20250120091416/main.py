'''
This file contains the implementation of the encrypt function, which encrypts a string by rotating the alphabet by 4 positions.
'''
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_string = ""
    for char in s:
        # Calculate the new character by shifting 4 positions
        new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
        encrypted_string += new_char
    return encrypted_string
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'