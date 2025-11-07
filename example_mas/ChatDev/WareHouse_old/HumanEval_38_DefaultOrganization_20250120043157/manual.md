# Cyclic Encoder/Decoder

This software provides functions to encode and decode strings by cycling groups of three characters. It is a simple yet effective way to transform strings for encoding and decoding purposes.

## Quick Install

This software does not require any external dependencies. You can simply download the `main.py` file and run it using Python.

## 🤔 What is this?

The cyclic encoder/decoder is a utility that allows you to encode a string by cycling groups of three characters. This means that for every group of three characters in the string, the characters are rotated to the left. The decoder function reverses this process, allowing you to retrieve the original string.

## Main Functions

### `encode_cyclic(s: str) -> str`

- **Description**: This function takes a string `s` as input and returns an encoded string by cycling groups of three characters.
- **Usage**: 
  ```python
  encoded_string = encode_cyclic("abcdefghi")
  print(encoded_string)  # Output: "bcaefdhig"
  ```

### `decode_cyclic(s: str) -> str`

- **Description**: This function takes an encoded string `s` (encoded with `encode_cyclic`) as input and returns the decoded original string.
- **Usage**: 
  ```python
  decoded_string = decode_cyclic("bcaefdhig")
  print(decoded_string)  # Output: "abcdefghi"
  ```

## How to Use

1. **Download the Code**: Save the `main.py` file to your local machine.

2. **Run the Code**: Use Python to run the file. You can use the functions `encode_cyclic` and `decode_cyclic` as demonstrated in the usage examples above.

3. **Example**: 
   ```python
   from main import encode_cyclic, decode_cyclic

   original = "helloworld"
   encoded = encode_cyclic(original)
   print(f"Encoded: {encoded}")

   decoded = decode_cyclic(encoded)
   print(f"Decoded: {decoded}")
   ```

## Documentation

For further details on how the functions work, you can refer to the docstrings provided within the `main.py` file. These docstrings offer a concise explanation of the purpose and usage of each function. 

This software is designed to be straightforward and easy to use, making it ideal for quick encoding and decoding tasks without the need for complex dependencies or setups.