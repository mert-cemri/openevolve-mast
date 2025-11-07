manual.md

```
# String Length Calculator

This software provides a simple utility function to calculate the length of a given string in Python. It is designed to be straightforward and efficient, with no external dependencies required.

## Quick Install

Since this project does not require any external dependencies, you can directly use the provided Python script without any additional installation steps.

## 🤔 What is this?

The String Length Calculator is a minimalistic Python function that returns the length of a given string. It is useful for developers who need a quick and reliable way to determine string lengths in their applications.

## Main Function

The main function provided by this software is `strlen`, which takes a single string as input and returns its length as an integer.

### Function Signature

```python
def strlen(string: str) -> int:
    """ Return length of given string """
```

### Example Usage

```python
# Example 1: Empty string
print(strlen(''))  # Output: 0

# Example 2: Non-empty string
print(strlen('abc'))  # Output: 3
```

## How to Use

1. **Download the Script**: Save the `main.py` file to your local machine.

2. **Run the Script**: You can run the script in any Python environment. Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the script using Python.

   ```bash
   python main.py
   ```

3. **Use the Function**: Import the `strlen` function into your Python project and use it to calculate the length of strings as needed.

   ```python
   from main import strlen

   # Calculate string length
   length = strlen("Hello, World!")
   print(length)  # Output: 13
   ```

## Documentation

This function is self-contained and does not require additional documentation. The code is simple and includes inline comments to explain its functionality.

For any further questions or support, please contact our development team.

```