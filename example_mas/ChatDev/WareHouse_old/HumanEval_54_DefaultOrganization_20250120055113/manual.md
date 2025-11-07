manual.md

```
# Same Characters Checker

This software provides a simple function to check if two strings contain the same set of characters. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `same_chars` function. This function takes two strings as input and returns a boolean value indicating whether the two strings contain the same set of characters.

### Function Definition

```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
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

This project does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system, and you can run the code directly.

### Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can test the function by running the Python interpreter and calling the `same_chars` function with your desired input strings.

### Example

```bash
python
>>> from main import same_chars
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
```

## Conclusion

This software provides a straightforward solution for checking if two strings have the same characters. With no external dependencies, it is easy to integrate into any Python project. Feel free to modify and extend the functionality as needed for your specific use case.
```