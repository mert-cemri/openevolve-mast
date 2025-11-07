manual.md

```
# SpecialFilter

A Python function to filter numbers based on specific criteria.

## Introduction

The `specialFilter` function is designed to process an array of numbers and return the count of numbers that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

## Main Function

### specialFilter(nums)

- **Parameters**: 
  - `nums`: A list of integers.
  
- **Returns**: 
  - An integer representing the count of numbers in the list that satisfy the specified conditions.

- **Example**:
  ```python
  specialFilter([15, -73, 14, -15])  # Returns: 1
  specialFilter([33, -2, -3, 45, 21, 109])  # Returns: 2
  ```

## Installation

This project does not require any external dependencies. You only need Python installed on your system to use the `specialFilter` function.

## How to Use

1. **Clone the Repository**: 
   - If the code is hosted in a repository, clone it to your local machine.
   - Alternatively, you can directly copy the `specialFilter` function from the `main.py` file.

2. **Run the Function**:
   - Open a Python environment (like IDLE, Jupyter Notebook, or any Python IDE).
   - Copy the `specialFilter` function into your script or interactive environment.
   - Call the function with a list of integers to get the desired output.

3. **Example Usage**:
   ```python
   # Example usage of the specialFilter function
   numbers = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
   result = specialFilter(numbers)
   print("Count of numbers meeting the criteria:", result)
   ```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is straightforward and does not require additional libraries or frameworks.

Feel free to modify and adapt the function to suit your specific needs or integrate it into larger projects.
```