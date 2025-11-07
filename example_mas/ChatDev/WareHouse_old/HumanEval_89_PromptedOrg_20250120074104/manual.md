# Encrypt Function User Manual

Welcome to the user manual for the `encrypt` function, a simple Python-based application designed to encrypt strings by rotating the alphabet. This manual will guide you through the main functions of the software, how to set up the environment, and how to use the function effectively.

## Main Functions

The `encrypt` function takes a string as an input and returns an encrypted string. The encryption is performed by rotating each lowercase letter in the string by four positions in the alphabet. Non-lowercase characters remain unchanged. This function is useful for simple encryption tasks where a basic alphabet rotation is sufficient.

### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

### Environment Setup

The `encrypt` function does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Installing Python

If you don't have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Download the Code**: Copy the code provided in `main.py` into a Python file on your local machine.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing your Python file, and run the file using the Python interpreter. For example:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the function by calling it with different strings and observing the output. You can add print statements to the end of your `main.py` file to see the results:

   ```python
   print(encrypt('hi'))  # Output: 'lm'
   print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
   print(encrypt('gf'))  # Output: 'kj'
   print(encrypt('et'))  # Output: 'ix'
   ```

## Conclusion

The `encrypt` function is a straightforward tool for encrypting strings using a simple alphabet rotation. With no external dependencies required, it is easy to set up and use. Whether you're looking to encrypt messages for fun or need a basic encryption method for a project, this function provides a quick and effective solution.