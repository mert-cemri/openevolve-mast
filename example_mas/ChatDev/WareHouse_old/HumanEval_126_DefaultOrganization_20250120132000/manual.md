# is_sorted Function User Manual

## Introduction

The `is_sorted` function is a simple Python utility designed to determine if a list of integers is sorted in ascending order. Additionally, it checks for duplicate numbers within the list and returns `False` if any number appears more than twice. This function assumes that the list contains only non-negative integers.

## Main Functions

- **Check Ascending Order**: The function verifies if the list is sorted in ascending order.
- **Duplicate Check**: It ensures that no number appears more than twice in the list.

## Installation

This function does not require any external dependencies. You can use it directly in your Python environment. Ensure you have Python installed on your system.

## How to Use

1. **Copy the Code**: Copy the `is_sorted` function code into your Python script or interactive environment.

   ```python
   def is_sorted(lst):
       # Check if the list is sorted in ascending order
       for i in range(len(lst) - 1):
           if lst[i] > lst[i + 1]:
               return False
       # Check for more than one duplicate of the same number
       count = {}
       for num in lst:
           if num in count:
               count[num] += 1
               if count[num] > 2:
                   return False
           else:
               count[num] = 1
       return True
   ```

2. **Run the Function**: Call the `is_sorted` function with a list of integers as an argument.

   ```python
   print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
   print(is_sorted([1, 3, 2, 4, 5]))  # Output: False
   print(is_sorted([1, 2, 2, 3, 3, 4]))  # Output: True
   print(is_sorted([1, 2, 2, 2, 3, 4]))  # Output: False
   ```

3. **Interpret the Results**: The function returns `True` if the list is sorted in ascending order and no number appears more than twice. Otherwise, it returns `False`.

## Example Usage

```python
# Example 1: Sorted list with no duplicates
result1 = is_sorted([1, 2, 3, 4, 5])
print(result1)  # Output: True

# Example 2: Unsorted list
result2 = is_sorted([1, 3, 2, 4, 5])
print(result2)  # Output: False

# Example 3: Sorted list with duplicates
result3 = is_sorted([1, 2, 2, 3, 3, 4])
print(result3)  # Output: True

# Example 4: Sorted list with more than two duplicates
result4 = is_sorted([1, 2, 2, 2, 3, 4])
print(result4)  # Output: False
```

## Conclusion

The `is_sorted` function is a straightforward tool for checking the order and duplicates in a list of integers. It is easy to integrate into any Python project without the need for additional libraries or dependencies.