manual.md

```
# Shift Encoder/Decoder

This software provides two main functions: `encode_shift` and `decode_shift`. These functions allow you to encode and decode strings by shifting each character by a specified number of positions in the alphabet.

## Main Functions

### encode_shift

- **Description**: Encodes a string by shifting each character by 5 positions in the alphabet.
- **Usage**: `encode_shift(s: str) -> str`
- **Parameters**: 
  - `s`: The input string to be encoded.
- **Returns**: A new string with each character shifted by 5 positions.

### decode_shift

- **Description**: Decodes a string that was encoded using the `encode_shift` function by reversing the shift.
- **Usage**: `decode_shift(s: str) -> str`
- **Parameters**: 
  - `s`: The input string that was encoded using `encode_shift`.
- **Returns**: The original string before encoding.

## Installation

This project does not require any external dependencies. You can run the software using Python without any additional installations.

### Quick Start

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. Open a terminal and navigate to the directory containing `main.py`.

4. Run the script using the command:
   ```
   python main.py
   ```

## Example Usage

The script includes an example usage of the `encode_shift` and `decode_shift` functions. When you run `main.py`, it will encode the string "hello" and then decode it back to the original string.

### Expected Output

```
Original: hello
Encoded: mjqqt
Decoded: hello
```

## Additional Information

- This software is designed to work with lowercase alphabetic characters. Non-alphabetic characters are not supported and may cause unexpected behavior.
- The shift value is hardcoded to 5 in this implementation. If you need a different shift value, you can modify the code accordingly.

Feel free to explore and modify the code to suit your needs!
```