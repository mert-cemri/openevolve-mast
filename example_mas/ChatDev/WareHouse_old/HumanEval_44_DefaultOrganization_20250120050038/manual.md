# Change Base Software

This software provides a simple utility to convert a given integer from base 10 to another specified base, where the base is less than 10. The conversion results in a string representation of the number in the new base.

## Main Functions

The main function of this software is `change_base(x: int, base: int) -> str`. This function takes two parameters:
- `x`: The integer number in base 10 that you want to convert.
- `base`: The base to which you want to convert the number `x`. The base must be between 2 and 9, inclusive.

### Example Usage

```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your machine.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file from the repository.

3. **Run the script**: You can execute the script using Python from your command line or terminal.

```bash
python main.py
```

## How to Use

1. **Open the `main.py` file**: You can edit this file to change the input values for testing.

2. **Modify the example usage**: Change the values in the `print` statements to test the function with different numbers and bases.

3. **Run the script**: Execute the script to see the output of the base conversion.

## Additional Information

- **Error Handling**: The function raises a `ValueError` if the base is not between 2 and 9.
- **Zero Handling**: If the input number `x` is zero, the function will return "0".

This software provides a straightforward and efficient way to convert numbers between bases, suitable for educational purposes or simple applications where base conversion is needed.