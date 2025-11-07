manual.md

```
# Fix Spaces Utility

## Introduction

The Fix Spaces Utility is a simple Python application designed to manipulate strings by replacing spaces with underscores and converting sequences of more than two consecutive spaces into a hyphen. This utility is useful for formatting text where spaces need to be standardized or replaced for consistency or compatibility reasons.

## Main Functions

The primary function of this utility is `fix_spaces(text)`, which processes a given string according to the following rules:

1. Replace all spaces with underscores.
2. If the string contains more than two consecutive spaces, replace all consecutive spaces with a hyphen.

### Example Usage

- `fix_spaces("Example")` returns `"Example"`
- `fix_spaces("Example 1")` returns `"Example_1"`
- `fix_spaces(" Example 2")` returns `"_Example_2"`
- `fix_spaces(" Example   3")` returns `"_Example-3"`

## Installation

This utility does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Quick Install

1. Clone the repository or download the `main.py` file to your local machine.

2. Navigate to the directory containing `main.py` using your command line interface.

3. Run the script using Python:
   ```bash
   python main.py
   ```

## How to Use

1. Open the `main.py` file in a text editor or IDE of your choice.

2. Locate the `fix_spaces` function to understand its implementation.

3. You can modify the example usage section at the bottom of the file to test the function with different input strings.

4. Run the script to see the output of the `fix_spaces` function with your test cases.

## Documentation

For further details on Python string manipulation and regular expressions, refer to the official Python documentation:

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

This utility is designed to be straightforward and requires no additional setup beyond having Python installed. Feel free to modify and extend the functionality as needed for your specific use case.
```