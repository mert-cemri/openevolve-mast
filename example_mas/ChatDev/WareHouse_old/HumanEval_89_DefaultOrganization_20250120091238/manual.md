manual.md

```
# Encrypt Function

This software provides a simple Python function to encrypt strings by rotating each letter in the input string by four places down the alphabet. This is a basic form of encryption known as a Caesar cipher with a fixed shift.

## Main Functionality

The main functionality of this software is to encrypt a given string using a specific rotation of the alphabet. The function `encrypt(s)` takes a string `s` as input and returns a new string where each lowercase letter is shifted four places forward in the alphabet. Non-lowercase characters remain unchanged.

### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

There are no external dependencies required for this project, so you can run the code directly without any additional installations.

### Running the Code

1. **Clone the Repository**: Clone the repository to your local machine using `git clone <repository-url>`.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: You can run the script using Python. Open a Python interpreter or create a Python script to import and use the `encrypt` function.

   ```python
   from main import encrypt

   # Example usage
   print(encrypt('hi'))  # Output: 'lm'
   print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
   print(encrypt('gf'))  # Output: 'kj'
   print(encrypt('et'))  # Output: 'ix'
   ```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The code is straightforward and well-commented to help you understand the logic behind the encryption process.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries you may have regarding the software.
```

This manual provides a comprehensive guide to using the `encrypt` function, including its purpose, usage examples, installation instructions, and support information.