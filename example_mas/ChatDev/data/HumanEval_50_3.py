'''
This module provides functions to encode and decode strings by shifting characters in the alphabet.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every lowercase alphabetic character by 5 in the alphabet.
    Non-alphabetic characters remain unchanged.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if 'a' <= ch <= 'z' else ch for ch in s])
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    Non-alphabetic characters remain unchanged.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if 'a' <= ch <= 'z' else ch for ch in s])