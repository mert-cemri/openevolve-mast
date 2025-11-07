# Remove Vowels Function

This software provides a simple utility function to remove vowels from a given string. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The primary function provided by this software is `remove_vowels`, which takes a string as input and returns a new string with all vowels removed. This function is useful for text processing tasks where vowels need to be excluded from the text.

### Function Definition

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
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
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the source code is located.

4. **Run the Code**: You can directly run the `main.py` file using Python to test the function.

```bash
python main.py
```

## Usage

To use the `remove_vowels` function, you can import it into your Python script and call it with the desired string input. Here is an example of how to use the function:

```python
from main import remove_vowels

# Example usage
text = "Hello, World!"
result = remove_vowels(text)
print(result)  # Output: "Hll, Wrld!"
```

## Testing

The function includes several test cases in its docstring, which can be used to verify its correctness. You can run these tests using a Python testing framework like `doctest`.

To run the tests, execute the following command in your terminal:

```bash
python -m doctest main.py
```

This will run the embedded tests and report any failures.

## Documentation

For further documentation and examples, please refer to the comments and docstrings within the `main.py` file. The code is well-documented to provide clarity on its functionality and usage.

Feel free to modify and extend the function to suit your specific needs.