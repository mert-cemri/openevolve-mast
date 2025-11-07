manual.md

```
# Encrypt Function

The Encrypt Function is a simple Python application designed to encrypt strings by rotating each letter in the input string by 4 positions in the alphabet. This application is useful for basic encryption tasks where a simple letter shift is required.

## Main Functionality

The main functionality of this software is to take a string as input and return an encrypted string. Each letter in the input string is shifted by 4 positions in the alphabet. Non-alphabet characters remain unchanged.

### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py` using your command line interface.

## How to Use

1. Open the `main.py` file in a text editor or IDE of your choice.

2. You can directly run the file using Python to test the function. For example, in your command line, navigate to the directory containing `main.py` and run:

   ```bash
   python main.py
   ```

3. To use the `encrypt` function in your own projects, you can import it from `main.py`:

   ```python
   from main import encrypt

   encrypted_string = encrypt('your_string_here')
   print(encrypted_string)
   ```

4. Modify the input string in the `encrypt` function call to encrypt different strings as needed.

## Documentation

The `encrypt` function is straightforward to use and does not require additional documentation. The code is well-commented to help you understand its functionality and modify it if necessary.

For further assistance or questions, please contact our support team.

```