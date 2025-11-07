'''
This module provides functions to encode and decode strings by shifting characters in the alphabet.
Handles both uppercase and lowercase letters, and leaves non-alphabetic characters unchanged.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    Handles both uppercase and lowercase letters, and leaves non-alphabetic characters unchanged.
    """
    encoded_chars = []
    for ch in s:
        if 'a' <= ch <= 'z':
            encoded_chars.append(chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a')))
        elif 'A' <= ch <= 'Z':
            encoded_chars.append(chr(((ord(ch) + 5 - ord('A')) % 26) + ord('A')))
        else:
            encoded_chars.append(ch)
    return "".join(encoded_chars)
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    Handles both uppercase and lowercase letters, and leaves non-alphabetic characters unchanged.
    """
    decoded_chars = []
    for ch in s:
        if 'a' <= ch <= 'z':
            decoded_chars.append(chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a')))
        elif 'A' <= ch <= 'Z':
            decoded_chars.append(chr(((ord(ch) - 5 - ord('A')) % 26) + ord('A')))
        else:
            decoded_chars.append(ch)
    return "".join(decoded_chars)
# Example usage
if __name__ == "__main__":
    original_text = "Hello, World!"
    encoded_text = encode_shift(original_text)
    decoded_text = decode_shift(encoded_text)
    print(f"Original: {original_text}")
    print(f"Encoded: {encoded_text}")
    print(f"Decoded: {decoded_text}")