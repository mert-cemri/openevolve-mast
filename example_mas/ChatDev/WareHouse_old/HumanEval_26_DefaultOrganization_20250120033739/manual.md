# Remove Duplicates

A Python utility to remove duplicate integers from a list, keeping only elements that appear once and maintaining their order.

## Main Functionality

The software provides a single function:

- `remove_duplicates(numbers: List[int]) -> List[int]`: This function takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of the remaining elements is preserved as in the input list.

### Example Usage

```python
from main import remove_duplicates

numbers = [1, 2, 3, 2, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 3, 4]
```

## Installation

### Environment Setup

This software does not require any external dependencies beyond the Python standard library. Ensure you have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

### Running the Software

1. Clone or download the repository containing the `main.py` file.
2. Navigate to the directory containing `main.py` in your terminal or command prompt.
3. Run your Python script that imports and uses the `remove_duplicates` function.

## How to Use

1. Import the `remove_duplicates` function from the `main.py` file.
2. Pass a list of integers to the function.
3. The function will return a new list with duplicates removed, preserving the order of the first occurrence of each unique element.

### Example

```python
from main import remove_duplicates

# Define a list of numbers with duplicates
numbers = [4, 5, 6, 7, 5, 8, 9, 4]

# Call the function to remove duplicates
unique_numbers = remove_duplicates(numbers)

# Output the result
print(unique_numbers)  # Output: [6, 7, 8, 9]
```

## Documentation

For more detailed information on how the function works, refer to the docstring within the `main.py` file. The function is designed to be simple and efficient, leveraging a dictionary to count occurrences and a list comprehension to filter out duplicates.

Feel free to modify and extend the functionality as needed for your specific use case.