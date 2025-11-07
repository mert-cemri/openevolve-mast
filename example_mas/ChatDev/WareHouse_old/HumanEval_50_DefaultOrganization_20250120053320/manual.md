manual.md

```
# Shift Encoder/Decoder

This software provides functions to encode and decode strings by shifting characters in the alphabet. It handles both uppercase and lowercase letters and leaves non-alphabetic characters unchanged.

## Main Functions

### encode_shift(s: str)

- **Description**: Encodes a given string by shifting every character by 5 positions in the alphabet.
- **Input**: A string `s` that you want to encode.
- **Output**: An encoded string with each character shifted by 5 positions.
- **Example**: 
  ```python
  encoded_text = encode_shift("Hello, World!")
  print(encoded_text)  # Outputs: "Mjqqt, Btwqi!"
  ```

### decode_shift(s: str)

- **Description**: Decodes a string that was encoded using the `encode_shift` function.
- **Input**: A string `s` that was encoded with the `encode_shift` function.
- **Output**: The original string before encoding.
- **Example**: 
  ```python
  decoded_text = decode_shift("Mjqqt, Btwqi!")
  print(decoded_text)  # Outputs: "Hello, World!"
  ```

## Installation

This software does not require any external dependencies. You can run it with a standard Python installation.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository containing the `main.py` file.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the script using Python:
   ```bash
   python main.py
   ```
4. The script will execute the example usage, encoding and then decoding the string "Hello, World!", and print the results to the console.

## Documentation

For further details on how the functions work, please refer to the comments within the `main.py` file. The code is documented to explain how each function processes the input and produces the output.

```