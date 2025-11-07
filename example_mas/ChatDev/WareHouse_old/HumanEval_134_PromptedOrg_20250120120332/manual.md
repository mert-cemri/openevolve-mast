# Check If Last Char Is A Letter

This software provides a simple function to determine if the last character of a given string is an alphabetical character and is not part of a word. This can be useful in text processing tasks where you need to identify standalone characters at the end of strings.

## Main Functionality

The main function provided by this software is:

- `check_if_last_char_is_a_letter(txt)`: This function takes a string `txt` as input and returns `True` if the last character is an alphabetical character and is not part of a word. Otherwise, it returns `False`.

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

This software does not require any external dependencies, so you can use it directly without installing additional packages. Simply ensure you have Python installed on your system.

### Quick Start

1. **Clone the repository or download the `main.py` file** to your local machine.

2. **Run the Python script** where you want to use the function. You can import the function into your script as follows:

    ```python
    from main import check_if_last_char_is_a_letter
    ```

3. **Use the function** in your code:

    ```python
    result = check_if_last_char_is_a_letter("apple pi e")
    print(result)  # Output: True
    ```

## Usage

To use the function, simply call `check_if_last_char_is_a_letter(txt)` with your desired string as the argument. The function will return a boolean value indicating whether the last character is an alphabetical character and not part of a word.

## Documentation

For any further documentation or support, please refer to the comments within the `main.py` file, which provide detailed explanations of the function's logic and usage.

This software is designed to be lightweight and easy to integrate into your existing Python projects. If you have any questions or need further assistance, feel free to reach out to our support team.