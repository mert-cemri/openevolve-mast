# Change Base Software

This software provides a function to convert a given integer from base 10 to another numerical base (less than 10). The function returns the string representation of the number in the new base.

## Main Functionality

The main function of this software is:

- **change_base(x: int, base: int) -> str**: This function takes an integer `x` and converts it to a string representation in the specified `base`. The base must be less than 10. If `x` is 0, the function returns "0". Otherwise, it calculates the representation by repeatedly dividing `x` by the base and collecting the remainders, which are then reversed to form the final result.

### Example Usage

```python
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so there is no need for a `requirements.txt` file.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository or download the code**: You can clone the repository using git or download the code directly.

3. **Run the code**: You can run the code using a Python interpreter. Simply open a terminal, navigate to the directory containing `main.py`, and run:

   ```bash
   python main.py
   ```

## Usage

To use the `change_base` function, you can import it into your Python script or interactive session. Here is an example of how to use it:

```python
from main import change_base

# Convert number 8 from base 10 to base 3
result = change_base(8, 3)
print(result)  # Output: '22'

# Convert number 8 from base 10 to base 2
result = change_base(8, 2)
print(result)  # Output: '1000'

# Convert number 7 from base 10 to base 2
result = change_base(7, 2)
print(result)  # Output: '111'
```

This software is designed to be simple and efficient for converting numbers to bases less than 10. It is suitable for educational purposes, small projects, or as a utility in larger applications.