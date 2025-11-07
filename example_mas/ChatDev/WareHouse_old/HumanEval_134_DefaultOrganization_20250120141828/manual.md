# Check If Last Char Is A Letter

This software module provides a function to determine if the last character of a given string is an alphabetical character and is not part of a word. This is useful for text processing tasks where you need to identify standalone letters at the end of strings.

## Main Function

The main function provided by this module is:

### `check_if_last_char_is_a_letter(txt)`

- **Description**: This function checks if the last character of the input string `txt` is an alphabetical character and is not part of a word. A "word" is defined as a group of characters separated by spaces.

- **Parameters**: 
  - `txt` (str): The input string to be checked.

- **Returns**: 
  - `bool`: Returns `True` if the last character is an alphabetical character and is not part of a word. Returns `False` otherwise.

- **Examples**:
  ```python
  check_if_last_char_is_a_letter("apple pie") ➞ False
  check_if_last_char_is_a_letter("apple pi e") ➞ True
  check_if_last_char_is_a_letter("apple pi e ") ➞ False
  check_if_last_char_is_a_letter("") ➞ False
  ```

## Installation

This module does not require any external dependencies, making it straightforward to use. You can simply copy the `main.py` file into your project and start using the function.

## Usage

1. **Copy the Code**: Copy the `main.py` file into your project directory.

2. **Import the Function**: Import the function into your script or application where you need to use it.

   ```python
   from main import check_if_last_char_is_a_letter
   ```

3. **Call the Function**: Use the function by passing a string as an argument.

   ```python
   result = check_if_last_char_is_a_letter("your string here")
   print(result)  # Outputs: True or False
   ```

## Example

Here's a quick example of how to use the function in a Python script:

```python
from main import check_if_last_char_is_a_letter

# Example strings
strings = [
    "apple pie",
    "apple pi e",
    "apple pi e ",
    ""
]

# Check each string
for s in strings:
    result = check_if_last_char_is_a_letter(s)
    print(f"'{s}' ➞ {result}")
```

This will output:

```
'apple pie' ➞ False
'apple pi e' ➞ True
'apple pi e ' ➞ False
'' ➞ False
```

## Conclusion

This module provides a simple yet effective way to check if the last character of a string is an isolated alphabetical character. It is easy to integrate into any Python project and requires no additional setup or dependencies.