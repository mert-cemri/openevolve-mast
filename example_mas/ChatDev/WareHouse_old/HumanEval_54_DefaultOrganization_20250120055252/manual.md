manual.md

```
# Same Characters Checker

This software provides a simple utility function to check if two words (strings) have the same characters, regardless of their order or frequency. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function provided by this software is `same_chars(s0: str, s1: str) -> bool`. This function takes two string inputs and returns a boolean value indicating whether the two strings contain the same set of characters.

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

This software does not require any external libraries or dependencies. It is implemented using Python's built-in functionality. Ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in a Python interactive shell.

   ```python
   from main import same_chars

   # Example usage
   result = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
   print(result)  # Output: True
   ```

## Documentation

The function is documented with examples in the docstring. You can view the documentation by using Python's built-in help function.

```python
help(same_chars)
```

This will display the function's docstring, which includes usage examples.

## Support

For any issues or questions, please contact the development team at ChatDev. We are committed to providing support and ensuring the software meets your needs.

```