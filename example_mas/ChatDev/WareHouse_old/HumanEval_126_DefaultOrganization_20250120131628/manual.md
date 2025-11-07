# is_sorted Function User Manual

## Introduction

The `is_sorted` function is a simple utility designed to determine whether a given list of integers is sorted in ascending order. Additionally, it checks for duplicates and returns `False` if any number appears more than once consecutively. This function is useful for validating data sequences where order and uniqueness are important.

## Main Functionality

- **Check Ascending Order**: The function verifies if the numbers in the list are in non-decreasing order.
- **Duplicate Check**: It ensures that no number appears more than once consecutively in the list.

## Installation

This project does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Setup

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the source files.

3. **Run the Code**: You can execute the `main.py` file directly in your Python environment.

## Usage

To use the `is_sorted` function, follow these steps:

1. **Open the `main.py` file**: This file contains the implementation of the `is_sorted` function.

2. **Call the Function**: Pass a list of integers to the `is_sorted` function to check if it is sorted and meets the duplicate criteria.

### Example

```python
# Example usage of the is_sorted function
print(is_sorted([5]))  # Output: True
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # Output: True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # Output: False
```

## Documentation

The function is straightforward and does not require additional documentation beyond the comments provided in the code. However, if you have any questions or need further assistance, feel free to reach out.

## Support

For any issues or questions regarding the `is_sorted` function, please contact our support team. We are here to help you ensure that your data sequences are correctly validated.

---

This manual provides all the necessary information to understand, install, and use the `is_sorted` function effectively. Enjoy seamless data validation with this simple yet powerful utility!