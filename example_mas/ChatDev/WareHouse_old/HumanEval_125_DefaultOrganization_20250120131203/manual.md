manual.md

```
# Split Words Utility

This software provides a utility function to process strings of text by splitting them into words based on specific criteria. It is designed to handle text input and return either a list of words or a count of specific characters based on the input's characteristics.

## Main Functionality

The main function provided by this software is `split_words(txt)`. This function processes a given string `txt` and returns:

- A list of words split on whitespace if whitespace characters are present.
- A list of words split on commas if no whitespace is present but commas are.
- The number of lowercase letters with odd order in the alphabet if neither whitespace nor commas are present.

### Examples

- `split_words("Hello world!")` returns `["Hello", "world!"]`
- `split_words("Hello,world!")` returns `["Hello", "world!"]`
- `split_words("abcdef")` returns `3`

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply download the `main.py` file and run it in any Python environment.

### Requirements

- Python 3.x

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the `split_words` function.

2. **Run the Function**: You can use the function by importing it into your Python script or by running the `main.py` file directly.

3. **Example Usage**:
   ```python
   from main import split_words

   # Example usage
   print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
   print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
   print(split_words("abcdef"))        # ➞ 3
   ```

## Documentation

The function is self-contained and does not require additional libraries or frameworks. It is designed to be simple and efficient for processing text strings according to the specified rules.

For any further questions or support, please contact our development team at ChatDev.
```
