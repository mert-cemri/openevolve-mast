# Sort Even Function User Manual

Welcome to the Sort Even Function user manual. This document provides a comprehensive guide on how to use the `sort_even` function, which is designed to sort elements at even indices of a list while keeping the odd indices unchanged.

## Overview

The `sort_even` function is a Python utility that processes a list by sorting the elements located at even indices. The function maintains the original order of elements at odd indices, ensuring that only the even-indexed elements are sorted.

### Functionality

- **Input**: A list of integers.
- **Output**: A new list where the elements at even indices are sorted, while the elements at odd indices remain in their original order.

### Example Usage

```python
# Example 1
input_list = [1, 2, 3]
output_list = sort_even(input_list)
print(output_list)  # Output: [1, 2, 3]

# Example 2
input_list = [5, 6, 3, 4]
output_list = sort_even(input_list)
print(output_list)  # Output: [3, 6, 5, 4]
```

## Installation

### Environment Setup

The `sort_even` function is implemented in Python and does not require any external dependencies. You can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `sort_even` function.

2. **Run the Function**: Use a Python interpreter to execute the `main.py` file.

```bash
python main.py
```

## How to Use

1. **Prepare Your List**: Create a list of integers that you want to process using the `sort_even` function.

2. **Call the Function**: Pass your list as an argument to the `sort_even` function.

3. **Receive the Output**: The function will return a new list with sorted even-indexed elements.

## Documentation

For further details on the implementation and usage of the `sort_even` function, please refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects.

## Support

If you encounter any issues or have questions regarding the `sort_even` function, please feel free to reach out for support. We are committed to providing assistance to ensure a smooth experience with our software.

Thank you for using the Sort Even Function!