# Check If Last Char Is A Letter

This software provides a simple function to determine if the last character of a given string is an alphabetical character and is not part of a word. A "word" is defined as a group of characters separated by spaces.

## Main Functionality

The primary function of this software is:

- `check_if_last_char_is_a_letter(txt)`: This function takes a string `txt` as input and returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise.

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

There are no external dependencies required for this software. You can use it directly in any Python environment.

### Quick Install

Since there are no external dependencies, you only need to ensure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function by importing it into your Python script or interactive shell.

   ```python
   from main import check_if_last_char_is_a_letter

   # Example usage
   result = check_if_last_char_is_a_letter("apple pi e")
   print(result)  # Output: True
   ```

4. **Testing**: You can test the function with different strings to see how it behaves with various inputs.

## Documentation

The function is straightforward and does not require additional setup or configuration. For further information or support, you can refer to the comments within the `main.py` file, which provide a detailed explanation of the function's logic and usage.

Feel free to reach out for any questions or support related to the software.