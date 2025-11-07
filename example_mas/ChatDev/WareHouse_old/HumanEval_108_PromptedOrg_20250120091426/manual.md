# Count Nums

A Python function to count the number of elements in an array of integers where the sum of the digits is greater than zero.

## Overview

The `count_nums` function is designed to process an array of integers and determine how many of those integers have a sum of digits greater than zero. This function considers the sign of the first digit in negative numbers.

## Main Functionality

- **count_nums(arr):** This function takes an array of integers as input and returns the count of numbers whose sum of digits is greater than zero.

## Installation

This software does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your machine. You can download it from [python.org](https://www.python.org/downloads/).

3. **No additional packages are required**, so you can directly use the function in your Python environment.

## Usage

1. **Open your Python environment** (e.g., terminal, command prompt, or an IDE like PyCharm or VSCode).

2. **Import the function** from the `main.py` file:

    ```python
    from main import count_nums
    ```

3. **Call the function** with an array of integers:

    ```python
    result = count_nums([-1, 11, -11])
    print(result)  # Output: 1
    ```

4. **Test with different arrays** to see how the function performs:

    ```python
    print(count_nums([]))  # Output: 0
    print(count_nums([1, 1, 2]))  # Output: 3
    ```

## Example

Here's a quick example to demonstrate the functionality:

```python
from main import count_nums

# Example array
arr = [-1, 11, -11, 123, -456]

# Count numbers with digit sum > 0
result = count_nums(arr)

print(f"The number of elements with a sum of digits > 0 is: {result}")
```

This will output:

```
The number of elements with a sum of digits > 0 is: 3
```

## Documentation

For further details on how the function works, please refer to the docstring within the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects where similar functionality is required.