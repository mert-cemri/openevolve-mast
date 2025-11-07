'''
This file contains the implementation of the encrypt function which rotates
each letter in the input string by four places down the alphabet.
'''
def encrypt(s):
    """Encrypts the input string by rotating each letter four places down the alphabet."""
    encrypted_string = []
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            # Calculate the new character with a shift of 4
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            encrypted_string.append(new_char)
        else:
            encrypted_string.append(char)  # Non-lowercase characters remain unchanged
    return ''.join(encrypted_string)
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'