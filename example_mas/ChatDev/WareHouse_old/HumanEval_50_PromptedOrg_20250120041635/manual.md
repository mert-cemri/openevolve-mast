# Encode-Decode Shift Manual

This software provides functions to encode and decode strings by shifting characters in the alphabet. It handles both uppercase and lowercase letters and leaves non-alphabetic characters unchanged.

## Main Functions

### 1. `encode_shift(s: str) -> str`

- **Description**: This function takes a string `s` as input and returns an encoded string by shifting every character by 5 positions in the alphabet.
- **Handles**: 
  - Both uppercase and lowercase letters.
  - Non-alphabetic characters remain unchanged.

### 2. `decode_shift(s: str) -> str`

- **Description**: This function takes an encoded string `s` (encoded using the `encode_shift` function) as input and returns the decoded string by reversing the shift.
- **Handles**: 
  - Both uppercase and lowercase letters.
  - Non-alphabetic characters remain unchanged.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the `main.py` file.
3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. **Import the Functions**: Import the `encode_shift` and `decode_shift` functions from the `main.py` file into your Python script or interactive session.

   ```python
   from main import encode_shift, decode_shift
   ```

2. **Encoding a String**: Use the `encode_shift` function to encode a string.

   ```python
   encoded_string = encode_shift("Hello, World!")
   print(encoded_string)  # Output will be the encoded version of "Hello, World!"
   ```

3. **Decoding a String**: Use the `decode_shift` function to decode a previously encoded string.

   ```python
   decoded_string = decode_shift(encoded_string)
   print(decoded_string)  # Output will be "Hello, World!"
   ```

## Example

```python
# Example usage
original_text = "Hello, World!"
encoded_text = encode_shift(original_text)
print(f"Encoded: {encoded_text}")

decoded_text = decode_shift(encoded_text)
print(f"Decoded: {decoded_text}")
```

This example demonstrates encoding and decoding a simple string. The encoded text will show the shifted characters, and the decoded text will return to the original string.

## Documentation

For further details, refer to the comments and docstrings within the `main.py` file. These provide additional insights into the implementation and usage of the functions.