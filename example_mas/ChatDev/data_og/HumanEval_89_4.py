'''
Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
'''
def encrypt(s):
    result = []
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            # Calculate the shifted character
            shifted = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result.append(shifted)
        else:
            result.append(char)  # Non-alphabetic characters are not changed
    return ''.join(result)
# Example usage:
# print(encrypt('hi'))  # Output: 'lm'
# print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
# print(encrypt('gf'))  # Output: 'kj'
# print(encrypt('et'))  # Output: 'ix'