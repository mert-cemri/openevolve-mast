manual.md

```
# Remove Vowels Function

This software provides a simple Python function to remove vowels from a given string. It is designed to be lightweight and efficient, handling both uppercase and lowercase vowels.

## Main Functionality

The main function provided by this software is `remove_vowels(text)`. This function takes a string input and returns a new string with all vowels removed. It handles both uppercase and lowercase vowels and preserves the original order of the non-vowel characters.

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

This software does not require any external dependencies beyond a standard Python installation. To use the function, simply ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Clone the repository or download the `main.py` file where the function is implemented.

## How to Use

1. **Open your Python Environment**: You can use any Python environment such as IDLE, PyCharm, VSCode, or simply the command line.

2. **Import the Function**: If you have the function in a file named `main.py`, you can import it using:
   ```python
   from main import remove_vowels
   ```

3. **Call the Function**: Use the function by passing a string to it:
   ```python
   result = remove_vowels("Your input string here")
   print(result)
   ```

## Documentation

This function is straightforward and does not require additional documentation. The docstring within the function provides examples of usage and expected output.

For any further assistance or queries, please contact our support team.
```