manual.md

```
# CycPattern Check

This software provides a function to check if any rotation of a given second word is a substring of a given first word. It is a simple yet powerful utility for string manipulation and pattern matching.

## Main Functionality

The core functionality of this software is encapsulated in the `cycpattern_check` function. This function takes two input strings and checks if any rotation of the second string is a substring of the first string. 

### Function Signature

```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
```

### Example Usage

- `cycpattern_check("abcd","abd")` returns `False`
- `cycpattern_check("hello","ell")` returns `True`
- `cycpattern_check("whassup","psus")` returns `False`
- `cycpattern_check("abab","baa")` returns `True`
- `cycpattern_check("efef","eeff")` returns `False`
- `cycpattern_check("himenss","simen")` returns `True`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. Clone the repository or download the `main.py` file to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run a Python shell or script and import the function:

```python
from main import cycpattern_check

# Example usage
result = cycpattern_check("hello", "ell")
print(result)  # Output: True
```

4. You can now use the `cycpattern_check` function to check for cyclic patterns in your strings.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is well-documented to guide you through its usage and expected behavior.

```