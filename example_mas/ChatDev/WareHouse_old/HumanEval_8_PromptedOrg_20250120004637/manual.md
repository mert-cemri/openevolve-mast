# SumProduct Function User Manual

This manual provides guidance on using the `sum_product` function, a simple Python function designed to calculate the sum and product of a list of integers.

## Overview

The `sum_product` function takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It handles edge cases such as an empty list by returning a sum of 0 and a product of 1.

### Main Functionality

- **Sum Calculation**: Computes the sum of all integers in the provided list.
- **Product Calculation**: Computes the product of all integers in the provided list.
- **Edge Case Handling**: Returns (0, 1) for an empty list.

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

### Environment Setup

This project does not require any external dependencies, making setup straightforward. Ensure you have Python installed on your system.

1. **Python Installation**: Make sure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted on a version control system, clone the repository to your local machine.

3. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

### Running the Function

1. **Open a Python Interpreter**: You can use any Python IDE or simply run Python in your terminal.

2. **Import the Function**: Ensure the `main.py` file is in your working directory, then import the function:

   ```python
   from main import sum_product
   ```

3. **Execute the Function**: Call the function with a list of integers:

   ```python
   result = sum_product([1, 2, 3, 4])
   print(result)  # Output: (10, 24)
   ```

## Conclusion

The `sum_product` function is a simple yet effective tool for calculating the sum and product of a list of integers. With no external dependencies, it is easy to integrate into any Python project. For any questions or further assistance, please contact our support team.