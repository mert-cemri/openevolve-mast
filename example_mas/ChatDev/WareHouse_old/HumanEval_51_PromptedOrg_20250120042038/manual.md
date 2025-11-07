# Remove Vowels Function

This software provides a simple utility function to remove vowels from a given string. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `remove_vowels`, which takes a string as input and returns a new string with all vowels removed. The function is case-insensitive and removes both uppercase and lowercase vowels.

### Function Signature

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    """
```

### Example Usage

```python
>>> remove_vowels('')
''
>>> remove_vowels("abcdef\nghijklm")
'bcdf\nghjklm'
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python. To use the function, simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `remove_vowels` function.

## How to Use

1. **Open a Python environment**: You can use a Python interpreter, a script, or an IDE like PyCharm or VSCode.

2. **Import the function**: If you are using the function in another script, import it using:
   ```python
   from main import remove_vowels
   ```

3. **Call the function**: Pass a string to the `remove_vowels` function to get a new string with vowels removed.
   ```python
   result = remove_vowels("Your input string here")
   print(result)
   ```

## Documentation

The function is documented with examples in the docstring. You can view the documentation by using Python's built-in help function:
```python
help(remove_vowels)
```

This will display the function's docstring, including usage examples.

## Support

For any issues or questions regarding the usage of this software, please contact our support team. We are here to assist you with any inquiries you may have.