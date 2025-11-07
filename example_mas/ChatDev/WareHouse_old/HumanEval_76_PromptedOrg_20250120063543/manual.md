# Simple Power Checker

This software provides a function to determine if a number \( x \) is a simple power of another number \( n \). Specifically, it checks if there exists an integer \( k \) such that \( n^k = x \).

## Main Functionality

The main function provided by this software is `is_simple_power(x, n)`. This function returns `True` if \( x \) is a simple power of \( n \), and `False` otherwise.

### Function Definition

```python
def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if there exists an integer k such that n**k = x.
    :param x: The number to check.
    :param n: The base number.
    :return: True if x is a simple power of n, False otherwise.
    """
    if x == 1:
        return True
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power *= n
        if power == x:
            return True
    return False
```

### Example Usage

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This software does not require any external dependencies. It is implemented in pure Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

No additional installation steps are required.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can use the Python interpreter to run the `main.py` file and test the `is_simple_power` function.

   ```bash
   python main.py
   ```

4. **Test the Function**: You can modify the `main.py` file to include test cases or use an interactive Python shell to test the function with different inputs.

## Documentation

For further documentation or any updates, please refer to the source code comments within the `main.py` file. The function is well-documented to help you understand its usage and logic.

This software is designed to be simple and straightforward, focusing on solving the specific problem of determining if a number is a simple power of another number.