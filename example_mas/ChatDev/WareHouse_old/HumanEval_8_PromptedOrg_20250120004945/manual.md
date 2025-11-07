# SumProduct Function User Manual

Welcome to the SumProduct function user manual. This document provides detailed instructions on how to use the `sum_product` function, including its main features, installation requirements, and usage examples.

## Overview

The `sum_product` function is a simple Python function designed to calculate the sum and product of a list of integers. It returns a tuple containing the sum and the product of the integers in the list. If the list is empty, it returns a sum of 0 and a product of 1.

## Main Functionality

- **Function Name:** `sum_product`
- **Input:** A list of integers (`List[int]`)
- **Output:** A tuple containing two integers (`Tuple[int, int]`), where the first integer is the sum of the list and the second integer is the product of the list.

### Example Usage

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    total_product = 1
    for number in numbers:
        total_sum += number
        total_product *= number
    return total_sum, total_product

# Example calls
print(sum_product([]))          # Output: (0, 1)
print(sum_product([1, 2, 3, 4])) # Output: (10, 24)
```

## Installation

The `sum_product` function does not require any external dependencies, making it easy to integrate into any Python environment. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** You can download and install Python from the official website: [python.org](https://www.python.org/).

2. **No additional packages required:** Since there are no external dependencies, you can directly use the function in your Python scripts.

## How to Use

1. **Import the Function:**
   - Copy the `sum_product` function code into your Python script or module.

2. **Call the Function:**
   - Pass a list of integers to the `sum_product` function to get the sum and product.

3. **Handle the Output:**
   - The function returns a tuple. You can unpack the tuple to get the sum and product separately.

### Example

```python
# Import the function (if it's in a separate module)
# from your_module import sum_product

# Use the function
result = sum_product([1, 2, 3, 4])
print(f"Sum: {result[0]}, Product: {result[1]}")
```

## Conclusion

The `sum_product` function is a straightforward tool for calculating the sum and product of a list of integers. With no external dependencies, it is easy to use and integrate into any Python project. Whether you're working on a small script or a larger application, this function can be a useful addition to your toolkit.