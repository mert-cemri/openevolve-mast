'''
This file contains the implementation of the encrypt function,
which rotates each letter in the input string by 4 positions in the alphabet.
'''
def encrypt(s):
    """Encrypts the input string by shifting each letter by 4 positions in the alphabet."""
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            # Calculate the new character position with wrap-around using modulo
            new_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)  # Non-alphabet characters are not changed
    return ''.join(result)
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'