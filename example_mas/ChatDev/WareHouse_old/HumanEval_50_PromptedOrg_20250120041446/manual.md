manual.md

```
# Shift Encoder/Decoder

This software provides functions to encode and decode strings by shifting characters in the alphabet. It is designed to handle lowercase alphabetic characters by shifting them, while non-alphabetic characters remain unchanged.

## Main Functions

### encode_shift(s: str)

- **Description**: This function encodes a given string by shifting every lowercase alphabetic character by 5 positions forward in the alphabet. Non-alphabetic characters remain unchanged.
- **Parameters**: 
  - `s` (str): The input string to be encoded.
- **Returns**: 
  - A string with each lowercase alphabetic character shifted by 5 positions.

### decode_shift(s: str)

- **Description**: This function decodes a string that was encoded using the `encode_shift` function. It shifts every lowercase alphabetic character by 5 positions backward in the alphabet. Non-alphabetic characters remain unchanged.
- **Parameters**: 
  - `s` (str): The input string to be decoded.
- **Returns**: 
  - A string with each lowercase alphabetic character shifted back by 5 positions.

## Installation

This software does not require any external dependencies beyond the standard Python library. Therefore, no additional installation steps are necessary.

## Usage

1. **Clone the Repository**: 
   - Clone the repository to your local machine using `git clone <repository-url>`.

2. **Navigate to the Directory**:
   - Change into the directory containing the `main.py` file.

3. **Run the Functions**:
   - You can use the functions by importing them into your Python script or interactive session. For example:

```python
from main import encode_shift, decode_shift

# Example usage
encoded_string = encode_shift("hello world")
print(encoded_string)  # Output: "mjqqt btwqi"

decoded_string = decode_shift(encoded_string)
print(decoded_string)  # Output: "hello world"
```

4. **Execute the Script**:
   - You can also execute the script directly if you have added test cases or examples within the `main.py` file.

## Notes

- The functions are designed to handle only lowercase alphabetic characters for shifting. Uppercase characters and non-alphabetic characters will remain unchanged.
- Ensure that the input strings are in lowercase if you want them to be encoded or decoded.

This software provides a simple and efficient way to encode and decode messages using a basic shift cipher. It can be used for educational purposes or simple encryption tasks.
```