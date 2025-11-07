manual.md

```
# Fix Spaces Utility

A simple Python utility to transform spaces in a string according to specific rules. This utility replaces all spaces with underscores, and if there are more than two consecutive spaces, it replaces them with a hyphen.

## Main Functions

The main function provided by this utility is `fix_spaces(text)`, which processes a given string `text` by:

- Replacing all spaces with underscores.
- Replacing sequences of more than two consecutive spaces with a hyphen.

### Example Usage

```python
from main import fix_spaces

print(fix_spaces("Example"))          # Output: "Example"
print(fix_spaces("Example 1"))        # Output: "Example_1"
print(fix_spaces(" Example 2"))       # Output: "_Example_2"
print(fix_spaces(" Example   3"))     # Output: "_Example-3"
```

## Installation

This utility does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: You can directly run the script using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: Import the `fix_spaces` function from the `main.py` file in your Python script.

2. **Call the Function**: Pass the string you want to process as an argument to the `fix_spaces` function.

3. **Get the Result**: The function will return the processed string with spaces replaced according to the specified rules.

## Documentation

For further details on how the function works or to contribute to the project, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to facilitate understanding and modification.

```