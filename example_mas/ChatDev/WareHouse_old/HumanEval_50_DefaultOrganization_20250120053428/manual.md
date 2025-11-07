# Shift Encoder/Decoder

This software provides simple functions to encode and decode strings by shifting characters in the alphabet. It is designed to shift each character in a string by a fixed number of positions, specifically by 5 positions in this case.

## Main Functions

### 1. `encode_shift(s: str) -> str`

- **Description**: This function takes a string `s` as input and returns a new string where each character is shifted by 5 positions forward in the alphabet.
- **Usage**: 
  ```python
  encoded_string = encode_shift("hello")
  print(encoded_string)  # Output will be a string with each character shifted by 5 positions
  ```

### 2. `decode_shift(s: str) -> str`

- **Description**: This function takes a string `s` that has been encoded using the `encode_shift` function and returns the original string by shifting each character back by 5 positions.
- **Usage**: 
  ```python
  decoded_string = decode_shift(encoded_string)
  print(decoded_string)  # Output will be "hello"
  ```

## Installation

### Environment Setup

This project does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: 
   ```bash
   cd <project-directory>
   ```

3. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can check this by running:
   ```bash
   python --version
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the encoding and decoding functions.

## Usage

1. **Open the `main.py` file**: You can edit the `main.py` file to include the strings you want to encode or decode.

2. **Run the Script**: Execute the script using Python:
   ```bash
   python main.py
   ```

3. **Test the Functions**: Modify the script to test different strings and see the encoded and decoded results.

## Example

Here is a simple example of how you can use the functions in `main.py`:

```python
# Example usage of encode_shift and decode_shift functions
original_text = "hello"
encoded_text = encode_shift(original_text)
print(f"Encoded: {encoded_text}")

decoded_text = decode_shift(encoded_text)
print(f"Decoded: {decoded_text}")
```

This will output:
```
Encoded: mjqqt
Decoded: hello
```

## Conclusion

This software provides a straightforward way to encode and decode strings by shifting characters in the alphabet. It is easy to set up and use, requiring no additional dependencies beyond Python itself.