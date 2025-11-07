# Check If Last Char Is A Letter

This software provides a simple utility function to determine if the last character of a given string is an alphabetical character and is not part of a word. This can be useful in text processing tasks where such checks are necessary.

## Main Functionality

The main function provided by this software is `check_if_last_char_is_a_letter(txt)`. This function takes a string `txt` as input and returns a boolean value:
- `True` if the last character of the string is an alphabetical character and is not part of a word.
- `False` otherwise.

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

This project does not require any external dependencies, so you can use it directly without installing additional packages. However, you need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository or download the script**: You can clone the repository using git or simply download the `main.py` file.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:

   ```bash
   cd <project-directory>
   ```

## Usage

To use the function, you can import it into your Python script or run it directly in a Python environment.

### Example Usage

```python
from main import check_if_last_char_is_a_letter

result = check_if_last_char_is_a_letter("apple pi e")
print(result)  # Output: True
```

### Running the Function

You can also run the function directly in a Python interactive shell:

1. Open a terminal or command prompt.
2. Run `python` to start the Python interactive shell.
3. Import the function and test it:

   ```python
   from main import check_if_last_char_is_a_letter

   print(check_if_last_char_is_a_letter("apple pi e"))  # Output: True
   ```

## Documentation

For further details on how the function works, you can refer to the docstring provided in the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects where text processing is required.

Feel free to modify and extend the function as needed for your specific use case.