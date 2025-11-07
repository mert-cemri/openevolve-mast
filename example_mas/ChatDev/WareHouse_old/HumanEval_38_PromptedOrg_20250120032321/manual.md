# Cyclic Encoder/Decoder

This software provides functions to encode and decode strings by cycling groups of three characters. It is designed to manipulate strings in a specific pattern, which can be useful for various applications such as data obfuscation or simple encryption.

## Main Functions

### `encode_cyclic(s: str) -> str`

- **Description**: This function takes a string as input and returns an encoded string by cycling groups of three characters.
- **Parameters**: 
  - `s` (str): The input string to be encoded.
- **Returns**: 
  - Encoded string where each group of three characters is cycled.

### `decode_cyclic(s: str) -> str`

- **Description**: This function takes an encoded string (produced by `encode_cyclic`) and returns the original string by reversing the cycling process.
- **Parameters**: 
  - `s` (str): The encoded string to be decoded.
- **Returns**: 
  - Decoded string where each group of three characters is reversed to its original order.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the `main.py` file.
3. No additional installation steps are required.

## How to Use

1. **Import the Functions**: First, ensure that the `main.py` file is in your working directory or in your Python path.

   ```python
   from main import encode_cyclic, decode_cyclic
   ```

2. **Encoding a String**: Use the `encode_cyclic` function to encode a string.

   ```python
   original_string = "abcdefghi"
   encoded_string = encode_cyclic(original_string)
   print(encoded_string)  # Output will be a cyclically encoded version of the original string
   ```

3. **Decoding a String**: Use the `decode_cyclic` function to decode a previously encoded string.

   ```python
   decoded_string = decode_cyclic(encoded_string)
   print(decoded_string)  # Output will be the original string "abcdefghi"
   ```

## Example

Here's a simple example demonstrating the encoding and decoding process:

```python
from main import encode_cyclic, decode_cyclic

# Original string
original = "HelloWorld"

# Encode the string
encoded = encode_cyclic(original)
print(f"Encoded: {encoded}")

# Decode the string
decoded = decode_cyclic(encoded)
print(f"Decoded: {decoded}")
```

This will output:

```
Encoded: eHllooWrdl
Decoded: HelloWorld
```

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to assist in understanding the cyclic encoding and decoding process.