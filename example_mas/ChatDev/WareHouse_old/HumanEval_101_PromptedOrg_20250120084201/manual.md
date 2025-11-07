# Words String Splitter

This software module provides a simple function to split a string of words separated by commas or spaces into an array of words. It is designed to handle strings with mixed delimiters and return a clean list of words.

## Main Functionality

The primary function of this module is `words_string(s)`, which takes a single string input and returns a list of words. The function processes the input string by replacing commas with spaces and then splitting the string based on spaces. This ensures that all words are correctly extracted, regardless of whether they are separated by commas or spaces.

### Example Usage

```python
from main import words_string

# Example 1
result1 = words_string("Hi, my name is John")
print(result1)  # Output: ["Hi", "my", "name", "is", "John"]

# Example 2
result2 = words_string("One, two, three, four, five, six")
print(result2)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Installation

There are no external dependencies required for this module, so you can directly use it in your Python environment. Simply ensure that you have Python installed on your system.

### Quick Start

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Code**: Use the function `words_string(s)` in your Python scripts as shown in the example usage above.

## Documentation

### Function: `words_string(s)`

- **Input**: A string `s` containing words separated by commas or spaces.
- **Output**: A list of words extracted from the input string.

The function works by:
1. Replacing all commas in the string with spaces.
2. Splitting the modified string by spaces.
3. Filtering out any empty strings that may result from consecutive spaces.

This approach ensures that the output is a clean list of words without any empty entries.

## Additional Information

For any further questions or support, please contact our support team or refer to the documentation provided within the code comments. This module is designed to be straightforward and easy to integrate into any Python project that requires basic string manipulation for word extraction.