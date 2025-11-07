'''
This module provides functions to encode and decode strings by shifting characters in the alphabet.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    Handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.
    """
    encoded = []
    for ch in s:
        if 'a' <= ch <= 'z':
            encoded.append(chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a')))
        elif 'A' <= ch <= 'Z':
            encoded.append(chr(((ord(ch) + 5 - ord('A')) % 26) + ord('A')))
        else:
            encoded.append(ch)
    return "".join(encoded)
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    Handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.
    """
    decoded = []
    for ch in s:
        if 'a' <= ch <= 'z':
            decoded.append(chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a')))
        elif 'A' <= ch <= 'Z':
            decoded.append(chr(((ord(ch) - 5 - ord('A')) % 26) + ord('A')))
        else:
            decoded.append(ch)
    return "".join(decoded)