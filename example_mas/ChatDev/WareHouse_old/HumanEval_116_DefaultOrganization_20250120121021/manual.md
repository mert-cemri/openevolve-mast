# Sort Array User Manual

Welcome to the Sort Array software! This tool is designed to sort arrays of integers based on the number of ones in their binary representation, with additional sorting by decimal value for numbers with the same number of ones. Negative numbers are sorted purely by their decimal value.

## Main Functions

The main function provided by this software is `sort_array`, which takes a list of integers and returns a sorted list according to the specified criteria.

### Function: `sort_array(arr)`

- **Description**: Sorts an array of integers based on the number of ones in their binary representation. For numbers with the same number of ones, it sorts them by their decimal value. Negative numbers are sorted by their decimal value.
- **Parameters**: 
  - `arr` (list): A list of integers to be sorted.
- **Returns**: 
  - A sorted list of integers.
- **Examples**:
  - `sort_array([1, 5, 2, 3, 4])` returns `[1, 2, 3, 4, 5]`
  - `sort_array([-2, -3, -4, -5, -6])` returns `[-6, -5, -4, -3, -2]`
  - `sort_array([1, 0, 2, 3, 4])` returns `[0, 1, 2, 3, 4]`

## Installation

To use the Sort Array software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run the code provided.

### Steps to Install Python

1. **Download Python**: Visit the official [Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
2. **Install Python**: Follow the installation instructions provided on the website to install Python on your system.
3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Create a Python File**: Copy the provided code into a file named `main.py`.
2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:
   ```bash
   python main.py
   ```
3. **Test the Function**: The `main.py` file includes example usage of the `sort_array` function. You can modify the input arrays in the `if __name__ == "__main__":` block to test the function with different inputs.

## Example Usage

```python
# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
```

Feel free to modify the input arrays to test the sorting functionality with different data sets. The function will handle both non-negative and negative integers as described.

Thank you for using the Sort Array software! If you have any questions or need further assistance, please reach out to our support team.