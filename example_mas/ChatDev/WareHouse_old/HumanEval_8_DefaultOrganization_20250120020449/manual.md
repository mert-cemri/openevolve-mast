# Sum and Product Calculator

This software module provides a simple function to calculate the sum and product of a list of integers. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Functionality

The primary function provided by this module is `sum_product`, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. If the list is empty, the function returns a sum of 0 and a product of 1.

### Function Details

- **Function Name:** `sum_product`
- **Input:** A list of integers (`List[int]`)
- **Output:** A tuple containing two integers (`Tuple[int, int]`), where the first integer is the sum of the list and the second integer is the product of the list.

#### Example Usage

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

This module does not require any external dependencies, making it easy to integrate into your existing Python environment.

### Quick Install

Since there are no external dependencies, you can simply download the `main.py` file and include it in your project directory.

## How to Use

1. **Download the `main.py` file**: Ensure that the `main.py` file is in your project directory.

2. **Import the Function**: Use the `from main import sum_product` statement to import the function into your Python script.

3. **Call the Function**: Pass a list of integers to the `sum_product` function to get the sum and product.

4. **Handle the Output**: The function returns a tuple, which you can unpack or use directly in your code.

## Additional Information

- **No External Libraries Required**: This module is self-contained and does not require any additional Python packages.
- **Python Version**: Ensure you are using Python 3.6 or later to support type annotations.

This module is designed to be simple and efficient, providing a basic utility for calculating the sum and product of a list of integers. If you have any questions or need further assistance, please feel free to reach out.