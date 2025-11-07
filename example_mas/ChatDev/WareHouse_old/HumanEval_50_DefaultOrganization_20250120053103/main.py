'''
This script contains two functions: `encode_shift` and `decode_shift`.
- `encode_shift` encodes a string by shifting each character by 5 positions in the alphabet.
- `decode_shift` decodes a string that was encoded using `encode_shift` by reversing the shift.
'''
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
# Example usage
if __name__ == "__main__":
    original = "hello"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")