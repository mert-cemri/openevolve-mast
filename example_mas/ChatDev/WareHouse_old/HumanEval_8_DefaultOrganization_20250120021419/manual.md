# SumProduct Function User Manual

Welcome to the SumProduct Function User Manual. This document provides a comprehensive guide on how to use the `sum_product` function, which calculates the sum and product of a list of integers.

## Overview

The `sum_product` function is a simple utility that takes a list of integers as input and returns a tuple containing the sum and the product of all integers in the list. It is designed to handle empty lists gracefully by returning a sum of 0 and a product of 1.

## Main Functionality

- **Function Name**: `sum_product`
- **Input**: A list of integers (`List[int]`)
- **Output**: A tuple containing two integers (`Tuple[int, int]`), where the first integer is the sum of the list and the second integer is the product of the list.

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

There are no external dependencies required for this function. It is implemented using standard Python libraries. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Code**: You can clone the repository or download the `main.py` file containing the `sum_product` function.

## How to Use

1. **Import the Function**: Ensure that the `sum_product` function is available in your Python environment. You can do this by placing the `main.py` file in your working directory and importing the function.

2. **Call the Function**: Use the function by passing a list of integers as an argument. The function will return a tuple with the sum and product of the list.

### Example

```python
# Example usage of the sum_product function
result = sum_product([1, 2, 3, 4])
print(result)  # Output: (10, 24)

result_empty = sum_product([])
print(result_empty)  # Output: (0, 1)
```

## Conclusion

The `sum_product` function is a straightforward utility for calculating the sum and product of a list of integers. It is easy to use and requires no additional setup beyond having Python installed. This function is ideal for applications where you need to perform basic arithmetic operations on lists of numbers.