# Encrypt Function User Manual

Welcome to the user manual for the `encrypt` function, a simple Python utility designed to encrypt strings by rotating the alphabet. This manual will guide you through the main functions of the software, how to install any necessary environment dependencies, and how to use the function effectively.

## Main Functionality

The `encrypt` function takes a string as an argument and returns a new string where each lowercase letter is shifted down the alphabet by four positions. This is achieved by rotating the alphabet, ensuring that the transformation wraps around from 'z' back to 'a'. Non-lowercase characters remain unchanged.

### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

There are no external dependencies required for this function, so you can use it directly in any Python environment without additional installations.

### Quick Start

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up Your Environment**: You can use any Python IDE or text editor to run the script. Popular choices include PyCharm, VSCode, or even a simple text editor with command line execution.

## How to Use

1. **Copy the Code**: Copy the `encrypt` function code into your Python script or interactive environment.

    ```python
    def encrypt(s):
        encrypted_string = ""
        for char in s:
            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
                # Calculate the new character by shifting 4 positions
                new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
                encrypted_string += new_char
            else:
                encrypted_string += char  # If not a lowercase letter, keep it unchanged
        return encrypted_string
    ```

2. **Call the Function**: Use the function by passing a string argument to it. For example:

    ```python
    result = encrypt('hello world')
    print(result)  # Output: 'lipps asvph'
    ```

3. **Modify and Experiment**: Feel free to modify the input string and observe how the function encrypts it.

## Conclusion

The `encrypt` function is a straightforward tool for basic string encryption using alphabet rotation. It is easy to integrate into larger projects or use as a standalone utility for educational purposes. Enjoy exploring the possibilities with this simple yet effective encryption method!