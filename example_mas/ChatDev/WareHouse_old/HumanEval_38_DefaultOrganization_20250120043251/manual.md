manual.md

```
# Cyclic Encoder/Decoder

This software provides functionality to encode and decode strings by cycling groups of three characters. It is a simple yet effective way to transform strings for various applications such as data obfuscation or simple encryption.

## Main Functions

### encode_cyclic

- **Purpose**: Encodes a given string by cycling groups of three characters.
- **Input**: A string `s`.
- **Output**: An encoded string where each group of three characters is rotated.

### decode_cyclic

- **Purpose**: Decodes a string that was encoded using the `encode_cyclic` function.
- **Input**: A string `s` that was encoded using `encode_cyclic`.
- **Output**: The original string before encoding.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository**: Download or clone the repository to your local machine.
2. **Navigate to the directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

## Usage

To use the cyclic encoder/decoder, follow these steps:

1. **Open a terminal**: Navigate to the directory containing `main.py`.
2. **Run the script**: Execute the script using Python by running the command:
   ```
   python main.py
   ```
3. **Example Output**: The script will print the original, encoded, and decoded strings to the console. For example:
   ```
   Original: abcdefghi
   Encoded: bcadefghi
   Decoded: abcdefghi
   ```

## How It Works

- **Encoding**: The `encode_cyclic` function splits the input string into groups of three characters. Each group is then rotated such that the first character moves to the end of the group.
- **Decoding**: The `decode_cyclic` function reverses the process by rotating each group of three characters back to its original order.

This software is designed to be simple and efficient, providing a straightforward method for encoding and decoding strings using cyclic transformations.
```