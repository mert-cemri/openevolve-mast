# Change Base User Manual

Welcome to the Change Base software! This tool allows you to convert a given integer to a specified base and return its string representation. This is particularly useful for understanding how numbers are represented in different numeral systems.

## Main Functionality

The core functionality of this software is encapsulated in the `change_base` function. This function takes two arguments: an integer `x` and a `base` to which you want to convert the number. The function returns a string representation of the number in the specified base.

### Function Signature

```python
def change_base(x: int, base: int) -> str:
```

### Parameters

- `x (int)`: The number to be converted.
- `base (int)`: The base to convert the number to. The base should be less than 10.

### Returns

- `str`: The string representation of the number in the specified base.

### Examples

```python
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
```

## Installation

To use the Change Base software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run the code.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

3. **Navigate to the directory**: Open a terminal and navigate to the directory where `main.py` is located.

## Usage

Once you have the environment set up, you can use the `change_base` function by executing the `main.py` file or by importing the function into your own Python scripts.

### Running the Script

To run the script and see the function in action, open a terminal, navigate to the directory containing `main.py`, and execute the following command:

```bash
python main.py
```

### Importing the Function

If you wish to use the `change_base` function in your own scripts, you can import it as follows:

```python
from main import change_base

# Example usage
result = change_base(8, 3)
print(result)  # Output: '22'
```

## Documentation

For further information and documentation, please refer to the comments within the `main.py` file. The function is well-documented with examples to help you understand its usage.

We hope you find the Change Base software useful for your numeral system conversion needs! If you have any questions or need further assistance, please feel free to reach out.