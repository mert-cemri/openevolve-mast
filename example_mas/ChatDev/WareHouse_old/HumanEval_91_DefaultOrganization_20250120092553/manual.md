manual.md

```
# Boredom Counter

This software is designed to count the number of sentences that start with the word "I" in a given string. These sentences are referred to as "boredoms". The software is implemented in Python and does not require any external dependencies.

## Main Functionality

The main functionality of this software is provided by the `is_bored` function, which takes a string as input and returns the number of sentences that start with the word "I". Sentences are considered to be delimited by '.', '?' or '!'.

### Example Usage

```python
from main import is_bored

# Example 1
result1 = is_bored("Hello world")
print(result1)  # Output: 0

# Example 2
result2 = is_bored("The sky is blue. The sun is shining. I love this weather")
print(result2)  # Output: 1
```

## Installation

Since this software does not require any external dependencies, you can simply download the `main.py` file to your local machine.

## How to Use

1. **Download the Code**: Ensure you have the `main.py` file in your working directory.

2. **Run the Code**: You can use the function `is_bored` by importing it into your Python script or interactive session.

3. **Input String**: Pass a string to the `is_bored` function. The function will return an integer representing the number of sentences starting with "I".

### Running the Function

- Open a Python environment (such as a terminal or an IDE like PyCharm or VSCode).
- Import the `is_bored` function from the `main.py` file.
- Call the function with a string input to get the count of "boredoms".

## Notes

- Ensure that the input string is properly formatted with sentences ending in '.', '?' or '!' for accurate results.
- The function is case-sensitive and will only count sentences starting with an uppercase "I".

## Troubleshooting

- If you encounter any issues, ensure that your Python environment is correctly set up and that you have the correct version of Python installed (Python 3.x is recommended).
- Check that the input string is correctly formatted and does not contain unexpected characters that might affect sentence splitting.

```