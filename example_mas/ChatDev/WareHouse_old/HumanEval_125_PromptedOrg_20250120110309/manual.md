manual.md

```
# Split Words Function

This software provides a utility function `split_words` that processes a string based on the presence of whitespaces, commas, or calculates a specific count of lowercase letters with odd order in the alphabet.

## Main Functions

The `split_words` function performs the following operations:

1. **Split on Whitespace**: If the input string contains whitespace, the function splits the string into a list of words based on the whitespace.

2. **Split on Commas**: If the input string does not contain whitespace but contains commas, the function splits the string into a list of words based on the commas.

3. **Count Lowercase Letters**: If the input string contains neither whitespace nor commas, the function returns the count of lowercase letters that have an odd order in the alphabet. The order is determined by `ord('a') = 0, ord('b') = 1, ... ord('z') = 25`.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Setup

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can run the function directly in a Python interpreter or script.

## Usage

To use the `split_words` function, follow these steps:

1. **Import the Function**: Ensure that the `split_words` function is accessible in your Python environment.

2. **Call the Function**: Pass a string to the `split_words` function and receive the processed output.

### Examples

```python
# Example 1: Split on whitespace
result = split_words("Hello world!")
print(result)  # Output: ["Hello", "world!"]

# Example 2: Split on commas
result = split_words("Hello,world!")
print(result)  # Output: ["Hello", "world!"]

# Example 3: Count lowercase letters with odd order
result = split_words("abcdef")
print(result)  # Output: 3
```

## Documentation

For further details on the implementation and usage of the `split_words` function, refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into existing Python projects.
```
