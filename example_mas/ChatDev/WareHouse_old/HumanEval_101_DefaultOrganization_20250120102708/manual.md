# Words String Splitter

This software module provides a simple function to split a string of words separated by commas or spaces into an array of words. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Function

The main function provided by this module is `words_string(s)`. This function takes a single string input and returns a list of words extracted from the input string. The words in the input string can be separated by either commas or spaces.

### Function Signature

```python
def words_string(s):
    """
    Splits a string into words separated by spaces or commas and returns them as a list.
    
    Parameters:
    s (str): The input string containing words separated by spaces or commas.
    
    Returns:
    list: A list of words extracted from the input string.
    """
```

### Examples

- `words_string("Hi, my name is John")` returns `["Hi", "my", "name", "is", "John"]`
- `words_string("One, two, three, four, five, six")` returns `["One", "two", "three", "four", "five", "six"]`

## Installation

This module does not require any external dependencies, making it easy to integrate into any Python environment. Simply download the `main.py` file and include it in your project.

## Usage

1. **Download the `main.py` file**: Ensure that the file is in your working directory or in a directory included in your Python path.

2. **Import the function**: In your Python script, import the `words_string` function from `main.py`.

    ```python
    from main import words_string
    ```

3. **Use the function**: Call the `words_string` function with your desired input string.

    ```python
    result = words_string("Hello, world, this is a test")
    print(result)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'test']
    ```

## Conclusion

This module provides a straightforward solution for splitting strings into words based on spaces or commas. Its simplicity and lack of dependencies make it an ideal choice for projects that require basic string manipulation without the overhead of additional libraries.