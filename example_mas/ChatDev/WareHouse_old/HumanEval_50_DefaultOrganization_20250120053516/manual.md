manual.md

```
# Shift Encoder/Decoder

This software provides two main functions: `encode_shift` and `decode_shift`. These functions allow users to encode and decode strings by shifting each character by a specified number of positions in the alphabet.

## Main Functions

### encode_shift

- **Description**: Encodes a string by shifting each character by 5 positions forward in the alphabet.
- **Usage**: 
  ```python
  encoded_string = encode_shift("hello")
  ```
- **Example**: 
  - Input: `"hello"`
  - Output: `"mjqqt"`

### decode_shift

- **Description**: Decodes a string that was encoded using the `encode_shift` function by shifting each character back by 5 positions in the alphabet.
- **Usage**: 
  ```python
  decoded_string = decode_shift("mjqqt")
  ```
- **Example**: 
  - Input: `"mjqqt"`
  - Output: `"hello"`

## Installation

This project does not require any external dependencies. You can use the built-in Python functions to run the software.

### Quick Start

1. **Clone the Repository**: 
   - Use `git clone` to download the project files to your local machine.
   
2. **Navigate to the Project Directory**: 
   - Use `cd` to change into the project directory.

3. **Run the Script**: 
   - Use Python to run the `main.py` file.
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Functions**: 
   - Import the `encode_shift` and `decode_shift` functions from the `main.py` file.
   ```python
   from main import encode_shift, decode_shift
   ```

2. **Encode a String**: 
   - Call the `encode_shift` function with the string you want to encode.
   ```python
   encoded_string = encode_shift("your_string_here")
   ```

3. **Decode a String**: 
   - Call the `decode_shift` function with the encoded string to retrieve the original string.
   ```python
   decoded_string = decode_shift("your_encoded_string_here")
   ```

## Additional Information

- **Character Set**: The functions are designed to work with lowercase alphabetic characters. Non-alphabetic characters are not supported.
- **No External Libraries**: The software is implemented using Python's built-in functions and does not require any additional libraries.

For any further questions or support, please contact our support team.
```