# Sort Array by Binary Ones

This software provides a function to sort an array of integers based on the number of ones in their binary representation. For numbers with the same number of ones, the function sorts them by their decimal value.

## Main Functionality

The main function provided by this software is `sort_array(arr)`, which takes a list of integers and returns a new list sorted according to the specified criteria.

### Function Details

- **Function Name**: `sort_array`
- **Parameters**: 
  - `arr`: A list of integers to be sorted.
- **Returns**: A new list of integers sorted by the number of ones in their binary representation. For numbers with the same number of ones, they are sorted by their decimal value.

### Examples

```python
>>> sort_array([1, 5, 2, 3, 4])
[1, 2, 3, 4, 5]

>>> sort_array([-2, -3, -4, -5, -6])
[-6, -5, -4, -3, -2]

>>> sort_array([1, 0, 2, 3, 4])
[0, 1, 2, 3, 4]
```

## Installation

This software is implemented in Python. To use it, ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Environment Setup

1. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv myenv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

3. **Install Required Dependencies**:
   This software does not have any external dependencies beyond Python's standard library.

## Usage

To use the `sort_array` function, simply import it into your Python script or interactive session and pass the list of integers you wish to sort.

### Example Usage

```python
from main import sort_array

# Example list of integers
numbers = [1, 5, 2, 3, 4]

# Sort the array
sorted_numbers = sort_array(numbers)

# Output the sorted list
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]
```

## Additional Information

This software is designed to be simple and efficient, leveraging Python's built-in sorting capabilities. It is suitable for educational purposes, small-scale applications, or as a utility in larger projects where sorting by binary representation is required.