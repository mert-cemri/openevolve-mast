# Encrypt Function User Manual

Welcome to the user manual for the Encrypt Function. This document will guide you through the main functions of the software, how to install the environment dependencies, and how to use the function effectively.

## Overview

The Encrypt Function is a simple Python script designed to encrypt a given string by rotating the alphabet. The rotation is performed such that each letter in the string is shifted down by four places in the alphabet. This is achieved by multiplying the shift factor (2) by two, resulting in a total shift of four places.

## Main Functionality

- **encrypt(s):** This function takes a string `s` as an argument and returns a new string where each lowercase letter is shifted by four places in the alphabet. Non-lowercase characters remain unchanged.

### Example Usage

```python
# Example usage of the encrypt function
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
```

## Installation

The Encrypt Function does not require any external dependencies. It is implemented purely in Python, and you can run it using any standard Python environment.

### Quick Install

1. **Ensure Python is installed:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository or download the script:** You can either clone the repository containing the script or download the `main.py` file directly.

3. **Run the script:** Navigate to the directory containing the `main.py` file and execute it using Python.

```bash
python main.py
```

## How to Use

1. **Open the `main.py` file:** You can edit the file to include your own test cases or modify the existing ones.

2. **Call the `encrypt` function:** Use the `encrypt` function by passing a string argument to it. The function will return the encrypted version of the string.

3. **View the output:** The encrypted string will be printed to the console or can be stored in a variable for further use.

## Conclusion

The Encrypt Function is a straightforward tool for encrypting strings by rotating the alphabet. It is easy to use and requires no additional setup beyond having Python installed. Feel free to modify the script to suit your needs or integrate it into larger projects. If you have any questions or need further assistance, please reach out to our support team.