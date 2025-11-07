'''
This file contains two functions: encode_shift and decode_shift.
- encode_shift: Encodes a string by shifting each character by 5 positions in the alphabet.
- decode_shift: Decodes a string that was encoded using the encode_shift function by shifting each character back by 5 positions in the alphabet.
Non-alphabetic characters remain unchanged in both functions.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    Non-alphabetic characters remain unchanged.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if 'a' <= ch <= 'z' else ch for ch in s])
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    Non-alphabetic characters remain unchanged.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if 'a' <= ch <= 'z' else ch for ch in s])