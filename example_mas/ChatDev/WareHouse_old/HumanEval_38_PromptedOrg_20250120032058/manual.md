# Cyclic Encoder/Decoder

This software provides functionality to encode and decode strings by cycling groups of three characters. It includes two main functions: `encode_cyclic` and `decode_cyclic`.

## Main Functions

### encode_cyclic

- **Purpose**: Encodes a given string by cycling groups of three characters.
- **Usage**: 
  ```python
  encoded_string = encode_cyclic("your_string_here")
  ```
- **Example**:
  ```python
  encoded_string = encode_cyclic("abcdef")  # Output will be "bcadef"
  ```

### decode_cyclic

- **Purpose**: Decodes a string that was encoded using the `encode_cyclic` function.
- **Usage**: 
  ```python
  decoded_string = decode_cyclic("your_encoded_string_here")
  ```
- **Example**:
  ```python
  decoded_string = decode_cyclic("bcadef")  # Output will be "abcdef"
  ```

## Installation

This project does not require any external dependencies, so you can directly use the provided Python code without installing additional packages.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the directory where the `main.py` file is located.
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can use the functions directly in your Python environment. Open a Python shell or create a new Python script and import the functions from `main.py`.

4. **Example Usage**:
   ```python
   from main import encode_cyclic, decode_cyclic

   # Encode a string
   encoded = encode_cyclic("hello world")
   print("Encoded:", encoded)

   # Decode the string
   decoded = decode_cyclic(encoded)
   print("Decoded:", decoded)
   ```

## Notes

- The `encode_cyclic` function processes the input string by splitting it into groups of three characters and cycling each group. If a group has fewer than three characters, it remains unchanged.
- The `decode_cyclic` function reverses the encoding process, restoring the original string.

This software is designed to be simple and efficient, providing a straightforward way to encode and decode strings using cyclic transformations.