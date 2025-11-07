'''
This module contains the encrypt function which encrypts a string by rotating
each letter in the alphabet by 4 positions.
'''
def encrypt(s):
    """Encrypts the input string by shifting each letter 4 positions forward in the alphabet.
    Args:
        s (str): The input string to be encrypted.
    Returns:
        str: The encrypted string with each letter shifted 4 positions.
    Examples:
        encrypt('hi') returns 'lm'
        encrypt('asdfghjkl') returns 'ewhjklnop'
        encrypt('gf') returns 'kj'
        encrypt('et') returns 'ix'
    """
    encrypted_string = []
    for char in s:
        if 'a' <= char <= 'z':
            # Shift character by 4 positions
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            encrypted_string.append(new_char)
        else:
            # If not a lowercase letter, append as is (though examples suggest only lowercase)
            encrypted_string.append(char)
    return ''.join(encrypted_string)