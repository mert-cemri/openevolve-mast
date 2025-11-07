manual.md

```
# SortArray

SortArray is a Python module designed to sort an array of non-negative integers based on the sum of the first and last elements of the array. The sorting order is determined by whether this sum is odd or even.

## Main Functionality

The main function provided by this module is `sort_array(array)`, which performs the following operations:

- **Input**: An array of non-negative integers.
- **Output**: A new array that is a sorted copy of the input array.
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note**: The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

To use the SortArray module, you need to have Python installed on your system. The module does not require any additional dependencies beyond the Python standard library.

### Quick Install

1. **Clone the Repository**: If the module is part of a larger project, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the directory containing the `main.py` file.

   ```bash
   cd <project-directory>
   ```

3. **Run the Python Script**: You can directly run the script using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: In your Python script, import the `sort_array` function from the module.

   ```python
   from main import sort_array
   ```

2. **Call the Function**: Pass an array of non-negative integers to the function and capture the sorted result.

   ```python
   sorted_array = sort_array([2, 4, 3, 0, 1, 5])
   print(sorted_array)  # Output: [0, 1, 2, 3, 4, 5]
   ```

## Documentation

For more information on how to use the SortArray module, please refer to the inline comments and docstrings within the `main.py` file. These provide detailed explanations of the function's behavior and usage examples.

```