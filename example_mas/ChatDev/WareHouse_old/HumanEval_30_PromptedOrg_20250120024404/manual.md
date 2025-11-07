# get_positive Function User Manual

This manual provides detailed instructions on how to use the `get_positive` function, which is designed to filter and return only the positive numbers from a given list.

## Overview

The `get_positive` function is a simple Python function that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. This function is useful for data processing tasks where you need to isolate positive values from a dataset.

## Main Functionality

- **Function Name:** `get_positive`
- **Input:** A list of numbers (integers or floats).
- **Output:** A list containing only the positive numbers from the input list.

### Example Usage

```python
# Example 1
result = get_positive([-1, 2, -4, 5, 6])
print(result)  # Output: [2, 5, 6]

# Example 2
result = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]
```

## Installation and Setup

### Environment Setup

This function does not require any external dependencies or libraries. It is implemented using standard Python, so you only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download and install it from the official Python website: [Python.org](https://www.python.org/downloads/).

### Running the Code

1. **Create a Python File:**
   - Create a file named `main.py` and paste the following code:

   ```python
   def get_positive(l: list):
       """Return only positive numbers in the list."""
       return [num for num in l if num > 0]
   ```

2. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where your `main.py` file is located.
   - Run the script using the following command:

   ```bash
   python main.py
   ```

3. **Testing the Function:**
   - You can test the function by calling it with different lists and printing the results, as shown in the example usage section.

## Conclusion

The `get_positive` function is a straightforward and efficient way to filter positive numbers from a list. With no external dependencies, it is easy to integrate into any Python project. Simply define the function in your script and call it with the desired list to obtain the positive numbers.