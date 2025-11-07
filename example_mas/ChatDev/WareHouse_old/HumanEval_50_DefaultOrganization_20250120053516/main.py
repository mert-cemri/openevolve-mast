'''
This script contains two functions: encode_shift and decode_shift.
- encode_shift: Encodes a string by shifting each character by 5 positions in the alphabet.
- decode_shift: Decodes a string encoded by encode_shift by shifting each character back by 5 positions.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])