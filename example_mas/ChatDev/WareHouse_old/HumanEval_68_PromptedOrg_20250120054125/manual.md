# Pluck Function User Manual

Welcome to the user manual for the `pluck` function. This document will guide you through the main functionalities of the software, how to install the necessary environment dependencies, and how to use the function effectively.

## Introduction

The `pluck` function is designed to process an array of non-negative integers and identify the smallest even number within it. The function returns this number along with its index in the array. If there are multiple occurrences of the smallest even number, the function will return the first occurrence. If no even numbers are present, or if the array is empty, the function will return an empty list.

## Main Functionality

- **Identify Smallest Even Number**: The function scans through the provided array to find the smallest even number.
- **Return Index**: Along with the smallest even number, the function returns the index of its first occurrence.
- **Handle Edge Cases**: If the array is empty or contains no even numbers, the function returns an empty list.

## Installation

The `pluck` function is implemented in Python. To use it, you need to have Python installed on your system. There are no additional dependencies required for this function.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone or Download the Code**: Obtain the `main.py` file containing the `pluck` function. You can clone the repository or download the file directly.

3. **Run the Function**: You can run the function using any Python environment or directly from the command line.

## How to Use

1. **Import the Function**: If you are using the function in another script, make sure to import it:

   ```python
   from main import pluck
   ```

2. **Call the Function**: Pass an array of non-negative integers to the function:

   ```python
   result = pluck([4, 2, 3])
   print(result)  # Output: [2, 1]
   ```

3. **Interpret the Output**: The function will return a list containing the smallest even number and its index. If no even numbers are found, it will return an empty list.

   ```python
   result = pluck([1, 3, 5])
   print(result)  # Output: []
   ```

## Examples

- **Example 1**: Input: `[4, 2, 3]`  
  Output: `[2, 1]`  
  Explanation: 2 is the smallest even number and is at index 1.

- **Example 2**: Input: `[5, 0, 3, 0, 4, 2]`  
  Output: `[0, 1]`  
  Explanation: 0 is the smallest even number, and the first occurrence is at index 1.

- **Example 3**: Input: `[]`  
  Output: `[]`  
  Explanation: The array is empty, so the output is an empty list.

## Conclusion

The `pluck` function is a simple yet effective tool for identifying the smallest even number in an array of non-negative integers. It is easy to integrate into larger projects and requires no additional dependencies. We hope this manual helps you understand and utilize the function effectively. If you have any questions or need further assistance, please feel free to reach out.