manual.md

```
# Pluck Function

A simple Python utility to identify and return the smallest even value from an array of non-negative integers, along with its index. This function is particularly useful for applications that require quick identification of specific node values in data structures like trees.

## Main Functionality

The primary function provided by this software is `pluck(arr)`, which performs the following tasks:

- **Input**: Accepts an array of non-negative integers.
- **Output**: Returns a list containing the smallest even value and its index from the array. If no even values are present or the array is empty, it returns an empty list.

### Example Usage

1. **Input**: `[4, 2, 3]`
   - **Output**: `[2, 1]`
   - **Explanation**: 2 is the smallest even value and is located at index 1.

2. **Input**: `[1, 2, 3]`
   - **Output**: `[2, 1]`
   - **Explanation**: 2 is the smallest even value and is located at index 1.

3. **Input**: `[]`
   - **Output**: `[]`
   - **Explanation**: The array is empty, so no even values are present.

4. **Input**: `[5, 0, 3, 0, 4, 2]`
   - **Output**: `[0, 1]`
   - **Explanation**: 0 is the smallest even value, and the first occurrence is at index 1.

## Installation

To use the `pluck` function, ensure you have Python installed on your system. This function does not require any external libraries, so no additional dependencies are necessary.

### Quick Install

1. **Python Installation**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the `main.py` file containing the `pluck` function.

3. **Run the Function**: You can execute the function by running the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, import it using:

   ```python
   from main import pluck
   ```

2. **Call the Function**: Pass an array of non-negative integers to the `pluck` function.

   ```python
   result = pluck([4, 2, 3])
   print(result)  # Output: [2, 1]
   ```

## Documentation

For further details and examples, refer to the inline documentation within the `main.py` file. This documentation provides comprehensive explanations of the function's behavior and edge cases.

```

This manual provides a clear and concise guide on how to use the `pluck` function, including installation instructions and example usage scenarios.