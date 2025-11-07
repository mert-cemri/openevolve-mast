manual.md

```
# Shift Encoder/Decoder

This software provides functionality to encode and decode strings by shifting characters in the alphabet. It is designed to handle both uppercase and lowercase letters, while leaving non-alphabetic characters unchanged.

## Quick Install

This software does not require any external dependencies, so there is no need to install additional packages. Simply ensure you have Python installed on your system.

## 🤔 What is this?

The Shift Encoder/Decoder is a simple application that allows you to encode a string by shifting each character by 5 positions in the alphabet. It also provides a function to decode the string back to its original form. This can be useful for basic encryption and decryption tasks.

## Main Functions

### `encode_shift(s: str) -> str`

- **Description**: This function takes a string `s` as input and returns an encoded string by shifting every character by 5 positions in the alphabet. It handles both uppercase and lowercase letters and leaves non-alphabetic characters unchanged.

- **Parameters**: 
  - `s` (str): The input string to be encoded.

- **Returns**: 
  - (str): The encoded string.

### `decode_shift(s: str) -> str`

- **Description**: This function takes a string `s` that has been encoded with the `encode_shift` function and returns the decoded string, shifting characters back by 5 positions in the alphabet.

- **Parameters**: 
  - `s` (str): The encoded string to be decoded.

- **Returns**: 
  - (str): The decoded string.

## How to Use

1. **Prepare your environment**: Ensure you have Python installed on your system. No additional packages are required.

2. **Using the functions**: 
   - Import the functions from the `main.py` file.
   - Call `encode_shift` with your desired string to get the encoded version.
   - Call `decode_shift` with the encoded string to retrieve the original string.

### Example

```python
from main import encode_shift, decode_shift

# Encode a string
encoded = encode_shift("Hello World!")
print(encoded)  # Output: "Mjqqt Btwqi!"

# Decode the string
decoded = decode_shift(encoded)
print(decoded)  # Output: "Hello World!"
```

## Documentation

For further details on the implementation, please refer to the comments within the `main.py` file. The code is straightforward and self-explanatory, designed to be easily understood and modified if necessary.
```