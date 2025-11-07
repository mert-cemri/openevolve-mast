# Shift Encoder/Decoder

This software provides two main functions: `encode_shift` and `decode_shift`. These functions are used to encode and decode strings by shifting each character by a specified number of positions in the alphabet. This can be useful for simple encryption and decryption tasks.

## Main Functions

### encode_shift

- **Description**: Encodes a string by shifting each character by 5 positions in the alphabet. Non-alphabetic characters remain unchanged.
- **Usage**: `encode_shift(s: str) -> str`
- **Parameters**: 
  - `s`: The input string to be encoded.
- **Returns**: The encoded string with each character shifted by 5 positions.

### decode_shift

- **Description**: Decodes a string that was encoded using the `encode_shift` function by shifting each character back by 5 positions in the alphabet. Non-alphabetic characters remain unchanged.
- **Usage**: `decode_shift(s: str) -> str`
- **Parameters**: 
  - `s`: The input string to be decoded.
- **Returns**: The decoded string with each character shifted back by 5 positions.

## Installation

This project does not require any external dependencies, so you can run it with a standard Python installation.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone the repository or download the `main.py` file to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the Python interpreter and import the functions:

   ```bash
   python
   ```

   ```python
   from main import encode_shift, decode_shift
   ```

4. Use the functions to encode or decode strings:

   ```python
   encoded_string = encode_shift("hello")
   print(encoded_string)  # Outputs: "mjqqt"

   decoded_string = decode_shift(encoded_string)
   print(decoded_string)  # Outputs: "hello"
   ```

## Documentation

For further information on how to use these functions, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to help you understand the functionality and usage of each function.

Feel free to modify the code to suit your specific needs or to integrate it into larger projects.