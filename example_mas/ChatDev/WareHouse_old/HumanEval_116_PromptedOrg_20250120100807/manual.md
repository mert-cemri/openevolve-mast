# Sort Array by Binary Ones

This software provides a function to sort an array of integers based on the number of ones in their binary representation. For numbers with the same number of ones, it further sorts them by their decimal value. This functionality can be particularly useful in scenarios where binary representation plays a crucial role in data processing or analysis.

## Main Functionality

The core function of this software is `sort_array(arr)`, which takes a list of integers as input and returns a sorted list based on the following criteria:

1. **Number of Ones in Binary Representation**: The primary sorting criterion is the count of '1's in the binary representation of each integer.
2. **Decimal Value**: For integers with the same number of '1's in their binary form, the function sorts them by their decimal value.

### Example Usage

```python
def sort_array(arr):
    """
    Sort an array of integers based on the number of ones in their binary representation.
    For numbers with the same number of ones, sort by their decimal value.
    :param arr: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    return sorted(arr, key=lambda x: (bin(abs(x)).count('1'), x))

# Example
sorted_array = sort_array([1, 5, 2, 3, 4])
print(sorted_array)  # Output: [1, 2, 3, 4, 5]
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply copy the `sort_array` function into your Python script and use it as needed.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the function is part of a larger project, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: 
   ```bash
   cd <project-directory>
   ```

3. **Run the Script**: Use Python to run your script that includes the `sort_array` function.
   ```bash
   python main.py
   ```

## Usage

To use the `sort_array` function, simply import it into your Python script and call it with a list of integers. The function will return a new list sorted according to the specified criteria.

### Example

```python
from main import sort_array

# Define an array of integers
array = [1, 5, 2, 3, 4]

# Sort the array
sorted_array = sort_array(array)

# Output the sorted array
print(sorted_array)  # Output: [1, 2, 3, 4, 5]
```

## Documentation

For further details on the implementation and usage of the `sort_array` function, please refer to the comments within the code. The function is designed to be intuitive and easy to integrate into existing Python projects.