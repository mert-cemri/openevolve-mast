manual.md

```
# Select Words by Consonant Count

This software provides a function to filter words from a given string based on the number of consonants they contain. It is designed to help users extract words with a specific number of consonants from any input string.

## Main Functionality

The core function of this software is `select_words(s, n)`, which takes two parameters:
- `s`: A string containing words separated by spaces.
- `n`: A natural number representing the exact number of consonants a word must have to be included in the output list.

### Function Behavior

- The function returns a list of words from the string `s` that contain exactly `n` consonants.
- If the input string `s` is empty, the function returns an empty list.
- The function assumes that the input string contains only letters and spaces.

### Examples

```python
select_words("Mary had a little lamb", 4)  # Returns: ["little"]
select_words("Mary had a little lamb", 3)  # Returns: ["Mary", "lamb"]
select_words("simple white space", 2)     # Returns: []
select_words("Hello world", 4)            # Returns: ["world"]
select_words("Uncle sam", 3)              # Returns: ["Uncle"]
```

## Installation

This software does not require any external dependencies. It is implemented in pure Python and can be used in any Python environment.

### Quick Setup

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. There are no additional packages to install, so you can directly use the function in your Python scripts.

## Usage

To use the `select_words` function, follow these steps:

1. Open your Python environment (e.g., Python shell, Jupyter Notebook, or any Python IDE).

2. Import the function from the `main.py` file:

   ```python
   from main import select_words
   ```

3. Call the `select_words` function with your desired string and consonant count:

   ```python
   result = select_words("Your input string here", 3)
   print(result)
   ```

4. The output will be a list of words from the input string that contain exactly the specified number of consonants.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is documented with examples to guide you through its usage.

Feel free to modify and adapt the code to fit your specific needs.
```