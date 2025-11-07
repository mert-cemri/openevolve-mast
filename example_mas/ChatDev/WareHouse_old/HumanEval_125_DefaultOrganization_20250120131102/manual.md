# Split Words Software

This software provides a function `split_words` that processes a string to split it based on whitespace, commas, or counts lowercase letters with odd order in the alphabet. It is designed to handle text input and return a list of words or a count based on specific conditions.

## Main Functionality

The main function provided by this software is `split_words(txt)`. Here's how it works:

1. **Whitespace Splitting**: If the input string contains whitespace, the function will split the string into a list of words based on the whitespace.

2. **Comma Splitting**: If there are no whitespaces but commas are present, the function will split the string into a list of words based on the commas.

3. **Counting Lowercase Letters**: If neither whitespaces nor commas are present, the function will count the number of lowercase letters in the string that have an odd order in the alphabet. For example, 'b' (order 1), 'd' (order 3), etc.

### Examples

- `split_words("Hello world!")` ➞ `["Hello", "world!"]`
- `split_words("Hello,world!")` ➞ `["Hello", "world!"]`
- `split_words("abcdef")` ➞ `3` (since 'b', 'd', and 'f' are in odd positions)

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory where the code is located.
   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can run the code directly using Python.
   ```bash
   python main.py
   ```

## Usage

To use the `split_words` function, simply import it into your Python script and call it with the desired string input.

```python
from main import split_words

# Example usage
result = split_words("Hello world!")
print(result)  # Output: ["Hello", "world!"]

result = split_words("abcdef")
print(result)  # Output: 3
```

## Documentation

For further details on how to use the function and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

Feel free to modify and extend the functionality as needed for your specific use case. If you encounter any issues or have questions, please reach out to our support team.