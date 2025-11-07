manual.md

```
# Shift Encoder/Decoder

This software provides two main functions to encode and decode strings by shifting lowercase characters in the alphabet. It is a simple utility that can be used to transform text by shifting each character by a fixed number of positions in the alphabet.

## Main Functions

### 1. `encode_shift(s: str) -> str`

- **Description**: This function takes a string as input and returns an encoded string by shifting every lowercase character by 5 positions forward in the alphabet. Non-lowercase characters remain unchanged.

- **Usage**:
  ```python
  encoded_string = encode_shift("hello world")
  print(encoded_string)  # Output: "mjqqt btwqi"
  ```

### 2. `decode_shift(s: str) -> str`

- **Description**: This function takes a string encoded with the `encode_shift` function and returns the decoded string by shifting every lowercase character by 5 positions backward in the alphabet. Non-lowercase characters remain unchanged.

- **Usage**:
  ```python
  decoded_string = decode_shift("mjqqt btwqi")
  print(decoded_string)  # Output: "hello world"
  ```

## Installation

This software does not require any external dependencies, making it simple and easy to use. You can directly use the functions in your Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can run the code directly in your Python environment. There are no additional installation steps required.

## How to Use

1. **Open your Python environment**: You can use any Python IDE or a simple command-line interface.

2. **Import the Functions**: Import the `encode_shift` and `decode_shift` functions from the `main.py` file.

   ```python
   from main import encode_shift, decode_shift
   ```

3. **Encode a String**: Use the `encode_shift` function to encode any string.

   ```python
   encoded = encode_shift("your text here")
   print(encoded)
   ```

4. **Decode a String**: Use the `decode_shift` function to decode any previously encoded string.

   ```python
   decoded = decode_shift(encoded)
   print(decoded)
   ```

## Notes

- The functions only shift lowercase alphabetic characters. Uppercase letters and non-alphabetic characters remain unchanged.
- The shift is fixed at 5 positions in the alphabet.

This software is a simple and effective tool for encoding and decoding text using a fixed shift in the alphabet. It can be easily integrated into larger applications or used as a standalone utility.
```