# Encrypt Function User Manual

Welcome to the user manual for the `encrypt` function, a simple Python-based application designed to encrypt strings by rotating each letter of the alphabet by four positions. This manual will guide you through the main functions of the software, how to set up the environment, and how to use the function effectively.

## Main Functions

The primary function of this software is to encrypt a given string by shifting each letter in the string by four positions in the alphabet. This is achieved through the `encrypt` function, which processes each character of the input string and returns the encrypted result.

### Functionality

- **Input**: A string consisting of lowercase alphabetic characters.
- **Output**: An encrypted string where each letter is shifted by four positions in the alphabet.

#### Example Usage

- `encrypt('hi')` returns `'lm'`
- `encrypt('asdfghjkl')` returns `'ewhjklnop'`
- `encrypt('gf')` returns `'kj'`
- `encrypt('et')` returns `'ix'`

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to where the `main.py` file is located:
   ```bash
   cd <project-directory>
   ```

## How to Use

To use the `encrypt` function, follow these steps:

1. **Open the `main.py` File**: Use a text editor or an IDE to open the `main.py` file.

2. **Call the Function**: You can call the `encrypt` function with your desired input string. For example:
   ```python
   print(encrypt('yourstring'))
   ```

3. **Run the Script**: Execute the script using Python to see the encrypted output:
   ```bash
   python main.py
   ```

## Conclusion

The `encrypt` function is a simple yet effective tool for encrypting strings by rotating the alphabet. With no external dependencies, it is easy to set up and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out.