# Words String Splitter

This software provides a simple utility function to split a string of words separated by commas or spaces into an array of individual words. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `words_string(s)`, which takes a single string input `s` and returns a list of words. The function handles strings where words are separated by either commas or spaces.

### Example Usage

```python
# Example 1
result = words_string("Hi, my name is John")
print(result)  # Output: ["Hi", "my", "name", "is", "John"]

# Example 2
result = words_string("One, two, three, four, five, six")
print(result)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Installation

This software does not require any external libraries or dependencies, so there is no need to install anything beyond Python itself. Ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file from the repository where this software is hosted.

2. **Run the Script**: You can run the script directly using Python. Open a terminal or command prompt and navigate to the directory containing `main.py`.

3. **Execute the Function**: You can use the function `words_string(s)` within your Python scripts or interactively in a Python shell.

### Running the Function

To use the function, simply import it into your Python script or interactive session:

```python
from main import words_string

# Use the function with your desired input
result = words_string("Your, input, string, here")
print(result)
```

## Notes

- The function replaces commas with spaces and then splits the string by spaces to ensure that all words are correctly separated.
- This software is designed to handle basic cases of word separation and may not account for more complex punctuation or formatting scenarios.

## Support

For any issues or questions regarding this software, please contact the development team at ChatDev. We are committed to providing support and updates as needed.