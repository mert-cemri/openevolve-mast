# Encrypt Function User Manual

Welcome to the user manual for the `encrypt` function. This software is designed to encrypt a string by rotating each letter in the alphabet by a specified number of positions. In this case, each letter is shifted by 4 positions forward in the alphabet.

## Main Functionality

The main function of this software is to encrypt a given string using a simple letter rotation (Caesar cipher) technique. The function processes each character in the string and shifts it by 4 positions in the alphabet. If the character is not a lowercase letter, it remains unchanged.

### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the official website [here](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `encrypt` function.

3. **Run the script**: You can execute the script using a Python interpreter.

## How to Use

1. **Open your terminal or command prompt**.

2. **Navigate to the directory** where `main.py` is located.

3. **Run the Python script** with the desired input string. For example:

   ```bash
   python -c "from main import encrypt; print(encrypt('your_string_here'))"
   ```

   Replace `'your_string_here'` with the string you want to encrypt.

## Additional Information

- **Character Handling**: The function is designed to handle lowercase alphabetic characters. Non-alphabetic characters are not altered.

- **No External Libraries**: The function is implemented using only Python's built-in capabilities, ensuring compatibility and ease of use.

For any further questions or support, please contact our support team. We hope you find this software useful for your encryption needs!