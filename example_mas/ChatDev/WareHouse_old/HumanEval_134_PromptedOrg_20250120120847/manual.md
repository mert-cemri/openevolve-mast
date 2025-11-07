# Check If Last Char Is A Letter

This software module provides a simple function to check if the last character of a given string is an alphabetical character and is not a part of a word. This can be useful in text processing tasks where such a condition needs to be identified.

## Main Function

The main function provided by this module is:

- `check_if_last_char_is_a_letter(txt)`: This function takes a string `txt` as input and returns `True` if the last character of the string is an alphabetical character and is not part of a word. Otherwise, it returns `False`.

### Function Details

- **Input**: A string `txt`.
- **Output**: A boolean value (`True` or `False`).

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

This module does not require any external dependencies, making it easy to integrate into your existing Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment without any additional installation steps.

## How to Use

1. **Copy the Code**: Copy the function code from the `main.py` file into your Python script or interactive environment.

2. **Call the Function**: Use the function `check_if_last_char_is_a_letter(txt)` by passing a string as an argument.

```python
# Example usage
result = check_if_last_char_is_a_letter("apple pi e")
print(result)  # Output: True
```

3. **Interpret the Result**: The function will return `True` if the last character is an alphabetical character and not part of a word, otherwise `False`.

## Documentation

This module is straightforward and does not require extensive documentation. The function is self-contained and does not rely on any external libraries or dependencies. Simply ensure that your Python environment is set up and you can start using the function as described.

For any further questions or support, please contact our development team.