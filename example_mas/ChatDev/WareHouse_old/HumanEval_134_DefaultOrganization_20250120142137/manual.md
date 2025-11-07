# Check If Last Character Is a Letter

This software provides a simple function to determine if the last character of a given string is an alphabetical character and is not part of a word. This can be useful in text processing tasks where you need to identify standalone characters at the end of a string.

## Main Function

### `check_if_last_char_is_a_letter(txt)`

- **Description**: This function checks if the last character of the input string `txt` is an alphabetical character and is not part of a word. A "word" is defined as a group of characters separated by spaces.
- **Parameters**: 
  - `txt` (str): The input string to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the last character is an alphabetical character and not part of a word, otherwise returns `False`.

#### Examples

```python
check_if_last_char_is_a_letter("apple pie")  # ➞ False
check_if_last_char_is_a_letter("apple pi e")  # ➞ True
check_if_last_char_is_a_letter("apple pi e ")  # ➞ False
check_if_last_char_is_a_letter("")  # ➞ False
```

## Installation

This project does not require any external packages, so you can run it with a standard Python installation. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the project is located.
3. **Run the Code**: You can directly run the `main.py` file using Python.

```bash
python main.py
```

## Usage

To use the function, simply import it into your Python script and call it with the desired string as an argument. Here is an example of how you might use it in a script:

```python
from main import check_if_last_char_is_a_letter

result = check_if_last_char_is_a_letter("example string")
print(result)  # Output will depend on the input string
```

## Documentation

For further details on how the function works, you can refer to the docstring provided within the `main.py` file. This includes a description of the function, its parameters, return values, and example usage.

Feel free to modify and integrate this function into your own projects as needed. If you encounter any issues or have suggestions for improvements, please reach out to our support team.