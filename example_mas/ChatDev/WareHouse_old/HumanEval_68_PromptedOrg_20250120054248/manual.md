# Pluck Function User Manual

## Introduction

The `pluck` function is a simple Python utility designed to process an array of non-negative integers and identify the smallest even number within the array. If multiple nodes with the same smallest even value are found, the function returns the node with the smallest index. This function is particularly useful for applications dealing with tree structures or any scenario where identifying specific nodes based on value and index is required.

## Main Functionality

- **Function Name**: `pluck`
- **Input**: A list of non-negative integers.
- **Output**: A list containing the smallest even value and its index in the format `[smallest_value, index]`. If no even values are present or the list is empty, it returns an empty list `[]`.

### Example Usages

1. **Example 1**:
   - **Input**: `[4, 2, 3]`
   - **Output**: `[2, 1]`
   - **Explanation**: The number 2 is the smallest even value and is located at index 1.

2. **Example 2**:
   - **Input**: `[1, 2, 3]`
   - **Output**: `[2, 1]`
   - **Explanation**: The number 2 is the smallest even value and is located at index 1.

3. **Example 3**:
   - **Input**: `[]`
   - **Output**: `[]`
   - **Explanation**: The input list is empty, so the function returns an empty list.

4. **Example 4**:
   - **Input**: `[5, 0, 3, 0, 4, 2]`
   - **Output**: `[0, 1]`
   - **Explanation**: The number 0 is the smallest even value. There are two zeros, but the first zero is at index 1.

## Installation

This function does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Python Installation

If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `pluck` function.

2. **Run the Function**: You can run the function in a Python environment by importing it or directly executing the script.

   ```python
   from main import pluck

   # Example usage
   result = pluck([4, 2, 3])
   print(result)  # Output: [2, 1]
   ```

3. **Modify the Input**: Change the input list to test different scenarios as needed.

## Documentation

For further details and advanced usage, refer to the comments within the `main.py` file. The function is well-documented to guide you through its logic and usage.

## Support

For any issues or questions, please contact our support team or refer to our documentation for further assistance. We are committed to providing comprehensive support to ensure the successful implementation and use of our software.