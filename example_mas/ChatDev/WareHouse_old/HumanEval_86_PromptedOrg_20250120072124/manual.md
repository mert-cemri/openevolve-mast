# Anti-Shuffle Function

This software provides a Python function named `anti_shuffle` that takes a string and returns an ordered version of it. Each word in the string is replaced by a new word where all the characters are arranged in ascending order based on ASCII value, while maintaining the order of words and spaces.

## Main Functionality

The main functionality of this software is to reorder the characters of each word in a given string based on their ASCII values. The function ensures that the order of words and spaces in the sentence is preserved.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository** (if applicable) or download the `main.py` file containing the `anti_shuffle` function.

3. **No additional packages are required**: Since there are no external dependencies, you don't need to install any packages via `pip` or `conda`.

## How to Use

1. **Open the `main.py` file**: This file contains the `anti_shuffle` function.

2. **Call the `anti_shuffle` function**: You can call this function with any string input to get the ordered version of the string.

   ```python
   from main import anti_shuffle

   result = anti_shuffle('Hello World!!!')
   print(result)  # Output: 'Hello !!!Wdlor'
   ```

3. **Modify as needed**: You can modify the input string to test different cases and see how the function orders the characters.

## Documentation

For further details on how the function works, you can refer to the comments within the `main.py` file. The function uses regular expressions to split the string into words and spaces, sorts each word, and then joins the parts back together to form the final ordered string.

Feel free to explore and modify the code to suit your needs!