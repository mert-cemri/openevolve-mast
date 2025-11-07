# Words String Splitter

This software module provides a simple function to split a given string of words separated by commas or spaces into an array of individual words. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this module is encapsulated in the `words_string` function. This function takes a single string input and returns a list of words. The input string can contain words separated by either commas or spaces, and the function will handle both separators seamlessly.

### Function Definition

```python
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Replace commas with spaces to unify the separators
    s = s.replace(',', ' ')
    # Split the string by spaces and filter out any empty strings
    words = [word for word in s.split() if word]
    return words
```

## Installation

This module does not require any external libraries or dependencies, making it easy to integrate into any Python project. Simply include the `main.py` file in your project directory.

## Usage

To use the `words_string` function, follow these steps:

1. Ensure that the `main.py` file is in your project directory.
2. Import the function into your Python script:

    ```python
    from main import words_string
    ```

3. Call the function with a string input:

    ```python
    result = words_string("Hi, my name is John")
    print(result)  # Output: ["Hi", "my", "name", "is", "John"]
    ```

4. The function will return a list of words extracted from the input string.

## Example

Here is an example of how to use the `words_string` function:

```python
from main import words_string

# Example input
input_string = "One, two, three, four, five, six"

# Get the list of words
words_list = words_string(input_string)

# Output the result
print(words_list)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Conclusion

The Words String Splitter module is a simple yet effective tool for processing strings of words separated by commas or spaces. With no external dependencies, it is easy to use and integrate into any Python project.