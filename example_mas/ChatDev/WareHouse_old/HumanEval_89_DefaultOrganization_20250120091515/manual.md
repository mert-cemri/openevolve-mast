# Encrypt Function User Manual

Welcome to the user manual for the Encrypt Function, a simple Python-based application designed to encrypt strings by rotating the alphabet. This manual will guide you through the main functions of the software, how to set up your environment, and how to use the function.

## Overview

The Encrypt Function is a Python function that takes a string as an argument and returns an encrypted string. The encryption is performed by rotating each letter of the alphabet by a fixed number of positions. Specifically, each letter is shifted down by two multiplied by two places (i.e., four positions).

### Main Functionality

- **encrypt(s):** This function takes a string `s` as input and returns a new string where each alphabetic character is shifted by four positions in the alphabet. Non-alphabetic characters remain unchanged.

### Examples

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

### Environment Setup

The Encrypt Function does not require any external dependencies, making it straightforward to set up. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:**
   - Clone or download the code files to your local machine.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## Usage

To use the Encrypt Function, follow these steps:

1. **Open the Terminal:**
   - Open your terminal or command prompt.

2. **Run the Python Script:**
   - Execute the script by running the following command:
     ```bash
     python main.py
     ```

3. **Modify the Script for Custom Input:**
   - To encrypt a custom string, you can modify the `main.py` file to include your desired input. For example, you can add:
     ```python
     print(encrypt('your_string_here'))
     ```
   - Replace `'your_string_here'` with the string you want to encrypt.

4. **View the Output:**
   - The encrypted string will be printed to the console.

## Conclusion

The Encrypt Function is a simple yet effective tool for encrypting strings by rotating the alphabet. With no external dependencies required, it is easy to set up and use. Modify the script to encrypt any string of your choice and see the results instantly. Enjoy using the Encrypt Function!