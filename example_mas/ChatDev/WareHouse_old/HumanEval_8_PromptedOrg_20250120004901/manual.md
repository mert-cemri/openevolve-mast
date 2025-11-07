# SumProduct Function User Manual

Welcome to the SumProduct Function User Manual. This document provides detailed instructions on how to use the `sum_product` function, which calculates the sum and product of a list of integers.

## Overview

The `sum_product` function is a simple utility that takes a list of integers as input and returns a tuple containing the sum and product of those integers. It is designed to handle empty lists by returning a sum of 0 and a product of 1.

## Main Functionality

- **Function Name:** `sum_product`
- **Input:** A list of integers (`List[int]`)
- **Output:** A tuple containing two integers (`Tuple[int, int]`), where the first integer is the sum of the list and the second is the product of the list.

### Example Usage

```python
from main import sum_product

# Example 1: Empty list
result = sum_product([])
print(result)  # Output: (0, 1)

# Example 2: List with integers
result = sum_product([1, 2, 3, 4])
print(result)  # Output: (10, 24)
```

## Installation

The `sum_product` function is implemented in Python and does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. **Import the Function:**

   Ensure that the `main.py` file is in your working directory. Import the `sum_product` function into your Python script or interactive session.

   ```python
   from main import sum_product
   ```

2. **Call the Function:**

   Pass a list of integers to the `sum_product` function and capture the returned tuple.

   ```python
   result = sum_product([1, 2, 3, 4])
   print(result)  # Output: (10, 24)
   ```

3. **Handle Edge Cases:**

   The function is designed to handle an empty list by returning `(0, 1)`.

   ```python
   result = sum_product([])
   print(result)  # Output: (0, 1)
   ```

## Documentation

For further details and examples, refer to the docstring within the `main.py` file. The function is self-documented with examples of usage.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any inquiries related to the `sum_product` function.