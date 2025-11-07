# Cyclic Encoder/Decoder

This software provides two main functions: `encode_cyclic` and `decode_cyclic`. These functions are designed to encode and decode strings by cycling groups of three characters.

## Main Functions

### encode_cyclic

- **Purpose**: Encodes a string by cycling groups of three characters.
- **Usage**: 
  ```python
  encoded_string = encode_cyclic("your_string_here")
  ```
- **Description**: The function splits the input string into groups of three characters. Each group is then cycled such that the first character moves to the end of the group. If a group has fewer than three characters, it remains unchanged.

### decode_cyclic

- **Purpose**: Decodes a string that was encoded with the `encode_cyclic` function.
- **Usage**: 
  ```python
  decoded_string = decode_cyclic("your_encoded_string_here")
  ```
- **Description**: The function splits the encoded string into groups of three characters. Each group is then reverse-cycled such that the last character moves to the front of the group. If a group has fewer than three characters, it remains unchanged.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine to access the `main.py` file containing the functions.

2. **Run the Code**: You can use the functions by importing them into your Python script or interactive session.

   ```python
   from main import encode_cyclic, decode_cyclic

   # Example usage
   original_string = "abcdefghi"
   encoded = encode_cyclic(original_string)
   print("Encoded:", encoded)  # Output: "bcadefghi"

   decoded = decode_cyclic(encoded)
   print("Decoded:", decoded)  # Output: "abcdefghi"
   ```

3. **Testing**: You can test the functions with different strings to ensure they work as expected.

## Documentation

For further details on how the functions work, please refer to the comments within the `main.py` file. The code is straightforward and self-explanatory, designed to be easily understood and modified if necessary.

Feel free to reach out if you have any questions or need further assistance!