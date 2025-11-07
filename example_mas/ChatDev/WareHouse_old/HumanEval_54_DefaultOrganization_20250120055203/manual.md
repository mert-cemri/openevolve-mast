manual.md

```
# Same Characters Checker

This software provides a simple utility function to check if two words (strings) have the same characters, regardless of their order or frequency. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The main function provided by this software is `same_chars`. This function takes two strings as input and returns a boolean value indicating whether the two strings contain the same set of characters.

### Function Signature

```python
def same_chars(s0: str, s1: str) -> bool:
```

### Example Usage

```python
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
>>> same_chars('abcd', 'dddddddabc')
True
>>> same_chars('dddddddabc', 'abcd')
True
>>> same_chars('eabcd', 'dddddddabc')
False
>>> same_chars('abcd', 'dddddddabce')
False
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
False
```

## Installation

To use this software, you need to have Python installed on your system. The code does not require any external dependencies, so you don't need to install any additional packages.

### Steps to Install Python

1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the instructions provided on the website to install Python on your system. Make sure to check the option to add Python to your system's PATH during installation.

3. **Verify Installation**: Open a command prompt or terminal and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `same_chars` function.

2. **Run the Function**: You can run the function in a Python environment (such as IDLE, PyCharm, or a Jupyter notebook) by importing the function and passing the desired strings as arguments.

3. **Example**: Open a Python shell or script and use the function as shown in the example usage section.

## Additional Information

- **No External Dependencies**: This software does not require any external libraries or dependencies, making it lightweight and easy to use.

- **No GUI**: The software is designed to be used as a backend utility and does not include any graphical user interface components.

- **License**: This software is provided as-is, without any warranty or guarantee of functionality.

For any further questions or support, please contact the development team at ChatDev.
```