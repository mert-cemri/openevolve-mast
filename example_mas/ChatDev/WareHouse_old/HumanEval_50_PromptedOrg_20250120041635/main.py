'''
This module provides functions to encode and decode strings by shifting characters in the alphabet.
Handles both uppercase and lowercase letters, leaves non-alphabetic characters unchanged.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    Handles both uppercase and lowercase letters, leaves non-alphabetic characters unchanged.
    """
    def shift_char(ch, shift):
        if 'a' <= ch <= 'z':
            return chr(((ord(ch) + shift - ord('a')) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            return chr(((ord(ch) + shift - ord('A')) % 26) + ord('A'))
        else:
            return ch
    return "".join(shift_char(ch, 5) for ch in s)
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    Handles both uppercase and lowercase letters, leaves non-alphabetic characters unchanged.
    """
    def shift_char(ch, shift):
        if 'a' <= ch <= 'z':
            return chr(((ord(ch) - shift - ord('a')) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            return chr(((ord(ch) - shift - ord('A')) % 26) + ord('A'))
        else:
            return ch
    return "".join(shift_char(ch, 5) for ch in s)