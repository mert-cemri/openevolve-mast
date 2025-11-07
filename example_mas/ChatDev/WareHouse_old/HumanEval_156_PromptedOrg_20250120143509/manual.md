# Mini Roman Numeral Converter

This software provides a function to convert a given positive integer into its Roman numeral equivalent in lowercase. It is designed to handle numbers within the range of 1 to 1000.

## Main Functionality

The main function of this software is:

- `int_to_mini_roman(number)`: This function takes a positive integer as input and returns its Roman numeral equivalent as a lowercase string. The function is restricted to handle numbers between 1 and 1000 inclusive.

### Examples

- `int_to_mini_roman(19)` returns `'xix'`
- `int_to_mini_roman(152)` returns `'clii'`
- `int_to_mini_roman(426)` returns `'cdxxvi'`

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can run the code using Python. For example, open a Python shell or script and import the function:

    ```python
    from main import int_to_mini_roman
    
    print(int_to_mini_roman(19))  # Output: xix
    ```

## Usage

To use the `int_to_mini_roman` function, simply call it with a positive integer argument within the specified range. The function will return the Roman numeral representation in lowercase.

### Example Usage

```python
# Import the function from the module
from main import int_to_mini_roman

# Convert numbers to Roman numerals
print(int_to_mini_roman(19))   # Output: xix
print(int_to_mini_roman(152))  # Output: clii
print(int_to_mini_roman(426))  # Output: cdxxvi
```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The function is straightforward and does not require additional configuration or setup.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out to our support team. We are here to help you make the most out of this tool.