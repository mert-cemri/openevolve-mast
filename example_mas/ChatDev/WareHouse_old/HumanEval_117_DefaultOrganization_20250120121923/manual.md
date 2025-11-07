manual.md

```
# Select Words by Consonant Count

This software provides a function to extract words from a given string that contain exactly a specified number of consonants. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `select_words(s, n)`. This function takes two parameters:
- `s`: A string containing words separated by spaces.
- `n`: A natural number representing the exact number of consonants a word must have to be included in the result.

The function returns a list of words from the string `s` that contain exactly `n` consonants, maintaining the order in which they appear in the string. If the string `s` is empty, the function returns an empty list.

### Examples

- `select_words("Mary had a little lamb", 4)` returns `["little"]`
- `select_words("Mary had a little lamb", 3)` returns `["Mary", "lamb"]`
- `select_words("simple white space", 2)` returns `[]`
- `select_words("Hello world", 4)` returns `["world"]`
- `select_words("Uncle sam", 3)` returns `["Uncle"]`

## Installation

There are no external dependencies required for this software. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Setup

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

4. Run the Python script using the command:
   ```
   python main.py
   ```

## Usage

To use the `select_words` function, you can import it into your Python script or interactive session. Here is an example of how to use it:

```python
from main import select_words

# Example usage
result = select_words("Mary had a little lamb", 4)
print(result)  # Output: ["little"]
```

This function is straightforward and does not require any additional setup or configuration. Simply provide the input string and the desired number of consonants, and the function will return the appropriate list of words.

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and make any necessary modifications.

Feel free to reach out for support if you encounter any issues or have questions about the functionality.
```