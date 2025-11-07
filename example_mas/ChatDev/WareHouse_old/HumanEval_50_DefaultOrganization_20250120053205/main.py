'''
This module contains functions to encode and decode strings by shifting characters in the alphabet.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.islower() else
                    chr(((ord(ch) + 5 - ord("A")) % 26) + ord("A")) if ch.isupper() else ch for ch in s])
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.islower() else
                    chr(((ord(ch) - 5 - ord("A")) % 26) + ord("A")) if ch.isupper() else ch for ch in s])