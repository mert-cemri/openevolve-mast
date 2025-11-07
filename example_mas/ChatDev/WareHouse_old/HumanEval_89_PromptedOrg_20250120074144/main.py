'''
Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
'''
def encrypt(s):
    encrypted_string = ""
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            # Calculate the new character by shifting 4 positions
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            encrypted_string += new_char
        else:
            encrypted_string += char  # If not a lowercase letter, keep it unchanged
    return encrypted_string
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'