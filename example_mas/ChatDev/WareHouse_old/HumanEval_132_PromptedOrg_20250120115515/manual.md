# is_nested Function User Manual

## Introduction

The `is_nested` function is a Python utility designed to determine if a string of square brackets contains a valid subsequence where at least one bracket is nested. This function is particularly useful for validating bracket sequences in programming and mathematical expressions.

## Main Functionality

The primary function provided by this software is:

- **is_nested(string)**: This function takes a single argument, `string`, which is a sequence of square brackets (`[` and `]`). It returns `True` if there is a valid subsequence of brackets where at least one bracket is nested, otherwise it returns `False`.

### Examples

- `is_nested('[[]]')` ➞ `True`
- `is_nested('[]]]]]]][[[[[]')` ➞ `False`
- `is_nested('[][]')` ➞ `False`
- `is_nested('[]')` ➞ `False`
- `is_nested('[[][]]')` ➞ `True`
- `is_nested('[[]][[')` ➞ `True`

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to use in any Python environment. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Quick Start

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `is_nested` function.

2. **Run the Function**: You can run the function directly in a Python environment. Open a terminal or command prompt and navigate to the directory containing `main.py`. Then, you can execute the script using Python:

   ```bash
   python main.py
   ```

3. **Use the Function in Your Code**: You can import the `is_nested` function into your own Python scripts by placing `main.py` in the same directory as your script and using the following import statement:

   ```python
   from main import is_nested
   ```

## Usage

To use the `is_nested` function, simply call it with a string of square brackets as the argument. The function will return a boolean value indicating whether there is a nested subsequence.

```python
# Example usage
result = is_nested('[[]]')
print(result)  # Output: True
```

## Conclusion

The `is_nested` function is a simple yet effective tool for checking nested bracket sequences. With no external dependencies, it is easy to integrate into any Python project. Whether you're validating expressions or parsing bracketed data, this function provides a reliable solution.