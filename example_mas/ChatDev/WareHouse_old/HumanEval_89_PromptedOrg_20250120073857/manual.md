# Encrypt Function User Manual

Welcome to the user manual for the `encrypt` function. This document will guide you through the main features of the software, how to set up your environment, and how to use the function effectively.

## Overview

The `encrypt` function is a simple Python utility designed to encrypt a string by rotating each letter in the alphabet by a specified number of positions. In this case, each letter is rotated by four positions. This function is particularly useful for basic encryption tasks where a simple letter shift is required.

## Features

- **Alphabet Rotation**: The function rotates each lowercase letter in the input string by four positions in the alphabet.
- **Preservation of Non-Letters**: Characters that are not lowercase letters (e.g., numbers, punctuation) are not altered by the encryption process.

## Installation

### Environment Setup

The `encrypt` function does not require any external packages or dependencies, making it easy to integrate into any Python environment. To get started, ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Directory**: Change to the directory containing the `main.py` file:
   ```bash
   cd <directory-name>
   ```
   Replace `<directory-name>` with the name of the directory where `main.py` is located.

## Usage

### Running the Encrypt Function

To use the `encrypt` function, follow these steps:

1. **Open a Terminal or Command Prompt**: Navigate to the directory containing the `main.py` file.

2. **Execute the Python Script**: Run the script using Python:
   ```bash
   python main.py
   ```

3. **Example Usage**: You can test the function by modifying the `main.py` file to include example usage. For instance:
   ```python
   print(encrypt('hi'))  # Output: 'lm'
   print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
   print(encrypt('gf'))  # Output: 'kj'
   print(encrypt('et'))  # Output: 'ix'
   ```

### Function Definition

Here is the function definition for reference:

```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places (i.e., 4 places).
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result.append(new_char)
        else:
            result.append(char)  # Non-lowercase characters are not encrypted
    return ''.join(result)
```

## Conclusion

The `encrypt` function is a straightforward tool for basic string encryption using alphabet rotation. It is easy to use and requires no additional setup beyond having Python installed. Feel free to integrate it into your projects where simple encryption is needed. If you have any questions or need further assistance, please contact our support team.