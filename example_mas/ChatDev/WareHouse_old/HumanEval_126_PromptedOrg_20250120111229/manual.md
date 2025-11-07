# is_sorted Function User Manual

## Introduction

The `is_sorted` function is a Python utility designed to determine if a list of integers is sorted in ascending order. Additionally, it checks if the list contains more than one duplicate of any number, in which case it returns `False`. This function is useful for validating data sequences where order and uniqueness are important.

## Main Functions

- **Check Ascending Order**: The function verifies if the list is sorted in ascending order.
- **Duplicate Check**: It ensures that no number appears more than twice in the list.

## Installation

### Environment Setup

The `is_sorted` function does not require any external dependencies, making it straightforward to integrate into any Python environment. Ensure you have Python installed on your system.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python scripts. Simply copy the function code into your script or module.

## Usage

### Function Definition

```python
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    # Check if the list is sorted in ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    # Check for more than one duplicate of the same number
    from collections import Counter
    count = Counter(lst)
    for value in count.values():
        if value > 2:
            return False
    return True
```

### How to Use

1. **Import the Function**: If you have saved the function in a separate module, import it into your script.

   ```python
   from your_module_name import is_sorted
   ```

2. **Call the Function**: Pass a list of integers to the `is_sorted` function.

   ```python
   result = is_sorted([1, 2, 3, 4, 5])
   print(result)  # Output: True
   ```

3. **Interpret the Result**: The function returns `True` if the list is sorted in ascending order and does not contain more than one duplicate of any number. Otherwise, it returns `False`.

### Examples

- **Example 1**: A sorted list with no duplicates.

  ```python
  is_sorted([1, 2, 3, 4, 5])  # Returns: True
  ```

- **Example 2**: A list with numbers not in order.

  ```python
  is_sorted([1, 3, 2, 4, 5])  # Returns: False
  ```

- **Example 3**: A list with more than one duplicate of a number.

  ```python
  is_sorted([1, 2, 2, 2, 3, 4])  # Returns: False
  ```

## Conclusion

The `is_sorted` function is a simple yet effective tool for checking the order and uniqueness of elements in a list. It can be easily integrated into any Python project without the need for additional libraries or dependencies.