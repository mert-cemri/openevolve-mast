# Split Words Function

This software module provides a function `split_words` that processes a string according to specific rules: splitting on whitespace, splitting on commas, or counting lowercase letters with odd order in the alphabet.

## Main Function

### `split_words(txt)`

- **Description**: 
  - This function takes a string `txt` as input and processes it based on the following rules:
    1. If the string contains whitespace, it splits the string into a list of words based on the whitespace.
    2. If there are no whitespaces but there are commas, it splits the string into a list of words based on the commas.
    3. If there are neither whitespaces nor commas, it counts the number of lowercase letters in the string that have an odd order in the alphabet (where 'a' = 0, 'b' = 1, ..., 'z' = 25) and returns this count.

- **Examples**:
  - `split_words("Hello world!")` ➞ `["Hello", "world!"]`
  - `split_words("Hello,world!")` ➞ `["Hello", "world!"]`
  - `split_words("abcdef")` ➞ `3`

## Installation

There are no external dependencies required for this module, so you can directly use it in your Python environment.

## How to Use

1. **Clone the Repository**: 
   - If this module is part of a larger project, clone the repository to your local machine.

2. **Navigate to the Directory**:
   - Open your terminal or command prompt.
   - Navigate to the directory where `main.py` is located.

3. **Run the Function**:
   - Open a Python interpreter or create a Python script.
   - Import the `split_words` function from `main.py`.
   - Call the function with your desired input string.

   Example:
   ```python
   from main import split_words

   result = split_words("Hello world!")
   print(result)  # Output: ["Hello", "world!"]
   ```

## Additional Information

- **Documentation**: This function is self-contained and does not require any additional libraries or frameworks.
- **Support**: For any issues or questions, please contact the development team or refer to the project's documentation if available.

This module is designed to be simple and efficient, providing a straightforward solution to the problem of splitting strings based on specific criteria.