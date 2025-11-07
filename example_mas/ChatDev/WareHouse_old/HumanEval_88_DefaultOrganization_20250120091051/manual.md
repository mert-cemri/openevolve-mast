manual.md

```
# Sort Array Application

This application provides a function to sort an array of non-negative integers based on the sum of the first and last elements of the array. The sorting order is determined by whether this sum is odd or even.

## Main Functionality

The main function of this application is `sort_array(array)`, which performs the following:

- **Input:** An array of non-negative integers.
- **Output:** A sorted copy of the input array.
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note:** The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

To use this application, you need to have Python installed on your system. The application does not require any additional dependencies, so there is no need for a `requirements.txt` file.

### Quick Install

1. **Ensure Python is installed:** You can download Python from [python.org](https://www.python.org/downloads/).
2. **Clone the repository or download the script:** Obtain the `main.py` file containing the `sort_array` function.

## How to Use

1. **Open a terminal or command prompt.**
2. **Navigate to the directory containing `main.py`.**
3. **Run Python in interactive mode or execute a script that imports `sort_array`.**

### Example Usage

```python
# Import the function from the script
from main import sort_array

# Example array
array = [2, 4, 3, 0, 1, 5]

# Call the function and print the result
sorted_array = sort_array(array)
print(sorted_array)  # Output: [0, 1, 2, 3, 4, 5]
```

## Documentation

For further details on using the function and additional examples, please refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into other Python scripts or applications.

```