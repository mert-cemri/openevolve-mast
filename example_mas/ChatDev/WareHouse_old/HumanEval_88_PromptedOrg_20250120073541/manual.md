# Sort Array User Manual

## Introduction

The `sort_array` function is a Python utility designed to sort an array of non-negative integers based on specific criteria. The function returns a sorted copy of the input array without modifying the original array. The sorting order is determined by the sum of the first and last elements of the array:

- If the sum is odd, the array is sorted in ascending order.
- If the sum is even, the array is sorted in descending order.

## Main Functionality

### sort_array Function

```python
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort the array in ascending order if the sum of the first and last index values is odd,
    or in descending order if the sum is even.
    
    Note:
    * The original array is not modified.
    
    Parameters:
    - array (list): A list of non-negative integers.
    
    Returns:
    - list: A sorted copy of the input array.
    """
```

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository**

   Clone the repository containing the `sort_array` function to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   The `sort_array` function does not require any external Python packages. Ensure your Python environment is set up correctly.

## Usage

1. **Open a Python Interpreter or Script**

   You can use the `sort_array` function in a Python script or directly in a Python interpreter.

2. **Import the Function**

   If using a script, ensure you import the function from the file where it is defined.

   ```python
   from main import sort_array
   ```

3. **Call the Function**

   Pass an array of non-negative integers to the `sort_array` function and capture the returned sorted array.

   ```python
   sorted_array = sort_array([2, 4, 3, 0, 1, 5])
   print(sorted_array)  # Output: [0, 1, 2, 3, 4, 5]
   ```

## Documentation

For further details and advanced usage, please refer to the inline comments and docstrings within the `main.py` file. This documentation provides a comprehensive guide to understanding and utilizing the `sort_array` function effectively.

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) to open an issue. We are here to assist you in making the most out of the `sort_array` function.