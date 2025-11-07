# Sort Array User Manual

Welcome to the Sort Array software, a simple yet efficient tool designed to sort arrays of non-negative integers based on the number of ones in their binary representation. This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The Sort Array software provides a single main function:

### `sort_array(arr)`

- **Purpose**: Sorts an array of non-negative integers according to the number of ones in their binary representation in ascending order. If two numbers have the same number of ones, they are sorted based on their decimal value.
- **Parameters**: 
  - `arr` (list): A list of non-negative integers to be sorted.
- **Returns**: 
  - A list of integers sorted based on the criteria mentioned above.
- **Examples**:
  ```python
  >>> sort_array([1, 5, 2, 3, 4])
  [1, 2, 4, 3, 5]
  
  >>> sort_array([1, 0, 2, 3, 4])
  [0, 1, 2, 4, 3]
  ```

## Installation

The Sort Array software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Code**: Obtain the `main.py` file containing the `sort_array` function.

3. **Run the Code**: You can run the code directly using Python.

## How to Use

1. **Prepare Your Array**: Create a list of non-negative integers that you wish to sort.

2. **Call the Function**: Use the `sort_array` function to sort your array. Pass your list as an argument to the function.

3. **View the Results**: The function will return a new list that is sorted according to the specified criteria.

### Example Usage

```python
# Import the function from the module
from main import sort_array

# Define your array
my_array = [1, 5, 2, 3, 4]

# Sort the array
sorted_array = sort_array(my_array)

# Print the sorted array
print(sorted_array)  # Output: [1, 2, 4, 3, 5]
```

## Conclusion

The Sort Array software is a straightforward tool designed to help you sort arrays based on binary representation efficiently. With no external dependencies required, it is easy to set up and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out.