manual.md

```
# Encrypt Function

A simple Python application to encrypt strings by rotating the alphabet by a specified number of positions.

## Overview

The `encrypt` function takes a string as an argument and returns a string encrypted by rotating each letter in the alphabet by four positions. This rotation is achieved by shifting each letter down by two multiplied by two places. For example:
- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

This application does not require any external dependencies. It is implemented purely in Python, and you can run it in any environment that supports Python.

### Prerequisites

- Python 3.x

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. Navigate to the directory containing `main.py`.

## Usage

To use the `encrypt` function, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script using the command:
   ```bash
   python main.py
   ```

4. You can modify the script to test different strings by changing the input to the `encrypt` function in the example usage section of the script.

## Example

Here is an example of how to use the `encrypt` function:

```python
# Example usage:
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
```

## Documentation

The `encrypt` function is straightforward and does not require additional documentation. It processes each character in the input string, shifts it by four positions in the alphabet, and constructs the encrypted string.

For any further questions or support, please contact our support team.
```
