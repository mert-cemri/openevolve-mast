# String Shift Encoder/Decoder

This software provides functions to encode and decode strings by shifting characters in the alphabet. It supports both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.

## Main Functions

### 1. `encode_shift(s: str) -> str`

- **Description**: This function takes a string as input and returns an encoded string by shifting every character by 5 positions in the alphabet. It handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.

- **Usage**:
  ```python
  encoded_string = encode_shift("Hello, World!")
  print(encoded_string)  # Outputs: "Mjqqt, Btwqi!"
  ```

### 2. `decode_shift(s: str) -> str`

- **Description**: This function takes a string encoded with the `encode_shift` function and returns the decoded string. It handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.

- **Usage**:
  ```python
  decoded_string = decode_shift("Mjqqt, Btwqi!")
  print(decoded_string)  # Outputs: "Hello, World!"
  ```

## Installation

To use this software, you need to have Python installed on your system. Follow the steps below to set up your environment:

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

3. **Set Up Environment**: Navigate to the directory where `main.py` is located.

4. **Install Dependencies**: There are no additional dependencies required for this software, so you can directly run the Python script.

## How to Use

1. **Open a Terminal**: Navigate to the directory containing the `main.py` file.

2. **Run the Script**: You can run the script using Python. For example:
   ```bash
   python main.py
   ```

3. **Use the Functions**: You can import the functions `encode_shift` and `decode_shift` from `main.py` into your own scripts to encode and decode strings as needed.

## Example

Here's a simple example of how you can use the functions in a Python script:

```python
from main import encode_shift, decode_shift

# Encode a string
original_text = "Hello, World!"
encoded_text = encode_shift(original_text)
print(f"Encoded: {encoded_text}")

# Decode the string
decoded_text = decode_shift(encoded_text)
print(f"Decoded: {decoded_text}")
```

This will output:
```
Encoded: Mjqqt, Btwqi!
Decoded: Hello, World!
```

Feel free to modify and use the functions as per your requirements. If you encounter any issues, ensure that your Python environment is correctly set up and that you are using the correct version of Python.