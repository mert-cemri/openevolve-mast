manual.md

```
# Sort Array Application

This application provides a simple function to sort an array of non-negative integers based on specific criteria. The function, `sort_array`, sorts the array in ascending or descending order depending on the sum of the first and last elements of the array.

## Main Functionality

The main function provided by this application is `sort_array`. Here's how it works:

- **Input**: An array of non-negative integers.
- **Output**: A sorted copy of the input array.
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note**: The original array is not modified; a new sorted array is returned.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function in a Python environment by importing it.

   ```python
   from main import sort_array

   # Example usage
   result = sort_array([2, 4, 3, 0, 1, 5])
   print(result)  # Output: [0, 1, 2, 3, 4, 5]
   ```

## Usage

To use the `sort_array` function, simply import it into your Python script or interactive session and call it with the desired array of non-negative integers.

```python
from main import sort_array

# Example usage
array = [2, 4, 3, 0, 1, 5]
sorted_array = sort_array(array)
print(sorted_array)
```

## Documentation

For further details and examples, please refer to the function's docstring in the `main.py` file. The docstring provides comprehensive information on the function's behavior and usage.

```python
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    You will sort the given array in ascending order if the sum of the first index value and
    last index value is odd, or sort it in descending order if the sum is even.
    Note:
    * Don't change the given array.
    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
```

This manual provides all necessary information to effectively use the `sort_array` function within your projects.
```