# SumProduct Function User Manual

## Introduction

The `sum_product` function is a simple Python utility designed to calculate the sum and product of a list of integers. This function is particularly useful in scenarios where you need to quickly compute these two values from a list of numbers, with special handling for empty lists.

## Main Functions

The primary function provided by this software is:

- **sum_product(numbers: List[int]) -> Tuple[int, int]**: This function takes a list of integers as input and returns a tuple containing the sum and product of the integers. If the list is empty, it returns `(0, 1)` as the sum and product respectively.

## Quick Install

No external dependencies are required for this software. It is implemented purely in Python and can be run in any standard Python environment.

## How to Use

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

Since there are no external dependencies, you don't need to install any additional packages. Simply ensure that your Python environment is set up.

### Running the Function

1. **Clone or Download the Code**: Obtain the `main.py` file containing the `sum_product` function.

2. **Execute the Function**: You can use the function in a Python script or an interactive Python session. Here's an example of how to use it:

   ```python
   from main import sum_product

   # Example usage
   result = sum_product([1, 2, 3, 4])
   print(result)  # Output: (10, 24)

   # Handling an empty list
   result = sum_product([])
   print(result)  # Output: (0, 1)
   ```

### Testing

You can test the function using Python's built-in `doctest` module to ensure it behaves as expected. Run the following command in your terminal:

```bash
python -m doctest main.py
```

This will execute the examples provided in the function's docstring and verify that the output matches the expected results.

## Documentation

For further information and examples, refer to the comments and docstrings within the `main.py` file. The function is straightforward and should be easy to integrate into your projects.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any challenges you might face while using the `sum_product` function.