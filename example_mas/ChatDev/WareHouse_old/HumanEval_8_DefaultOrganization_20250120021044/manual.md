# SumProduct Function User Manual

Welcome to the SumProduct Function User Manual. This document will guide you through the installation, usage, and functionality of the `sum_product` function, which is designed to calculate the sum and product of a list of integers.

## Overview

The `sum_product` function is a simple utility that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. This function is particularly useful for mathematical computations where both the sum and product of a sequence of numbers are required.

### Main Functionality

- **Function Name**: `sum_product`
- **Input**: A list of integers (`List[int]`)
- **Output**: A tuple containing two integers (`Tuple[int, int]`), where the first integer is the sum of the list and the second integer is the product of the list.
- **Special Cases**:
  - If the input list is empty, the function returns `(0, 1)`.

### Example Usage

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number
    return total_sum, total_product
```

## Installation

To use the `sum_product` function, you need to have Python installed on your system. The function does not require any additional dependencies, so there is no need for a `requirements.txt` file.

### Quick Install

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up Your Environment**: You can use a virtual environment to manage your Python packages. Create a virtual environment using the following command:

   ```bash
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:

     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source myenv/bin/activate
     ```

4. **Run the Code**: Copy the `sum_product` function into a Python file (e.g., `main.py`) and execute it using:

   ```bash
   python main.py
   ```

## Usage

To use the `sum_product` function, simply call it with a list of integers as the argument. Here are some examples:

```python
# Example 1: Empty list
result = sum_product([])
print(result)  # Output: (0, 1)

# Example 2: List with integers
result = sum_product([1, 2, 3, 4])
print(result)  # Output: (10, 24)
```

## Conclusion

The `sum_product` function is a straightforward utility for calculating the sum and product of a list of integers. It is easy to integrate into your Python projects and requires no additional dependencies. We hope this manual helps you get started with using the function effectively. If you have any questions or need further assistance, please feel free to reach out.