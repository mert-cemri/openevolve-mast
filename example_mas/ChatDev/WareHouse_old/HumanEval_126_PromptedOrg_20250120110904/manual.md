# is_sorted Function User Manual

## Introduction

The `is_sorted` function is a simple Python utility designed to determine whether a given list of integers is sorted in ascending order. Additionally, it checks for duplicate values and returns `False` if any number appears more than once consecutively. This function is useful for validating sorted data with specific constraints on duplicates.

## Main Functionality

- **is_sorted(lst):** This function takes a list of integers as input and returns a boolean value:
  - `True` if the list is sorted in ascending order and no integer appears more than once consecutively.
  - `False` if the list is not sorted or if any integer appears more than once consecutively.

### Examples

- `is_sorted([5])` ➞ `True`
- `is_sorted([1, 2, 3, 4, 5])` ➞ `True`
- `is_sorted([1, 3, 2, 4, 5])` ➞ `False`
- `is_sorted([1, 2, 2, 3, 3, 4])` ➞ `True`
- `is_sorted([1, 2, 2, 2, 3, 4])` ➞ `False`

## Installation

The `is_sorted` function does not require any external dependencies, making it easy to integrate into any Python project. Simply copy the function code into your Python script or module.

## Usage

1. **Copy the Code:**
   - Copy the `is_sorted` function code into your Python file.

2. **Call the Function:**
   - Use the function by passing a list of integers as an argument.
   ```python
   result = is_sorted([1, 2, 3, 4, 5])
   print(result)  # Output: True
   ```

3. **Interpret the Result:**
   - The function returns `True` if the list is sorted in ascending order with no more than one duplicate of any number.
   - It returns `False` if the list is not sorted or if any number appears more than once consecutively.

## Conclusion

The `is_sorted` function is a straightforward tool for checking the order and duplicate constraints of a list of integers. It is easy to use and integrate into existing Python projects, providing a quick way to validate sorted data with specific rules on duplicates.