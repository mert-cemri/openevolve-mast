# Pluck Function User Manual

Welcome to the user manual for the "Pluck" function, a simple yet efficient Python function designed to find and return the smallest even number from a given array along with its index. This document will guide you through the main features of the software, how to set up your environment, and how to use the function effectively.

## Main Functionality

The "Pluck" function is designed to:

- **Identify the Smallest Even Value**: Given an array of non-negative integers, the function will locate the smallest even number.
- **Return the Smallest Index**: If multiple nodes have the same smallest even value, the function will return the node with the smallest index.
- **Output Format**: The function returns a list containing the smallest even value and its index. If no even values are present or the array is empty, it returns an empty list.

### Example Usage

- **Input**: `[4, 2, 3]`
  - **Output**: `[2, 1]`
- **Input**: `[1, 2, 3]`
  - **Output**: `[2, 1]`
- **Input**: `[]`
  - **Output**: `[]`
- **Input**: `[5, 0, 3, 0, 4, 2]`
  - **Output**: `[0, 1]`

## Installation

The "Pluck" function does not require any external dependencies, making it easy to integrate into your existing Python projects. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.
3. **Run the Function**: You can directly run the function in a Python environment or integrate it into your project.

## How to Use

1. **Import the Function**: If you are integrating the function into another project, import it using:
   ```python
   from main import pluck
   ```

2. **Call the Function**: Pass an array of non-negative integers to the `pluck` function:
   ```python
   result = pluck([4, 2, 3])
   print(result)  # Output: [2, 1]
   ```

3. **Handle the Output**: The function returns a list containing the smallest even value and its index, or an empty list if no even values are found.

## Documentation

For further details on the function's implementation and examples, please refer to the comments within the `main.py` file. The code is well-documented to provide clarity on its logic and usage.

## Support

For any issues or questions regarding the "Pluck" function, please contact our support team or refer to the documentation provided in the code comments.

Thank you for using the "Pluck" function. We hope it meets your needs for efficient data processing in your projects.