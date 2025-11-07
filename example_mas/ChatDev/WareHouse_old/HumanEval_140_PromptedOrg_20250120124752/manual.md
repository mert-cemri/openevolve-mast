# Fix Spaces

This software provides a simple utility function `fix_spaces` that processes a string by replacing spaces with underscores and sequences of more than two consecutive spaces with a hyphen. This can be particularly useful for formatting text in a consistent manner.

## Main Functionality

The main function of this software is `fix_spaces`, which performs the following operations on a given string:

1. **Replace Spaces with Underscores**: All single spaces in the string are replaced with underscores (`_`).
2. **Replace Consecutive Spaces with Hyphen**: If there are more than two consecutive spaces, they are replaced with a hyphen (`-`).

### Examples

- `fix_spaces("Example")` returns `"Example"`
- `fix_spaces("Example 1")` returns `"Example_1"`
- `fix_spaces(" Example 2")` returns `"_Example_2"`
- `fix_spaces(" Example   3")` returns `"_Example-3"`

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.
   ```bash
   cd <repository-directory>
   ```

3. **Run the Script**: You can directly run the script using Python.
   ```bash
   python main.py
   ```

## Usage

To use the `fix_spaces` function, you can import it into your Python script or use it directly in the Python interactive shell.

### Example Usage

```python
from main import fix_spaces

# Example usage
text = " Example   3"
formatted_text = fix_spaces(text)
print(formatted_text)  # Output: "_Example-3"
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is well-documented to guide you through its usage and expected behavior.

## Support

If you encounter any issues or have questions about using this software, please contact our support team or refer to the documentation provided within the code. We are here to help you make the most out of this utility.