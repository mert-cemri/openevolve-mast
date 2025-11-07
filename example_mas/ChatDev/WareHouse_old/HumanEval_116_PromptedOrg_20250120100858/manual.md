# Sort Array User Manual

Welcome to the Sort Array software! This software provides a function to sort an array of integers based on specific criteria related to their binary representation. This manual will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to use the function effectively.

## Main Functions

The primary function of this software is `sort_array(arr)`, which sorts an array of integers according to the following rules:

1. **Non-negative Integers**: Sort by the number of `1`s in their binary representation in ascending order. If two numbers have the same number of `1`s, they are sorted by their decimal value.

2. **Negative Integers**: These are sorted by their absolute values in ascending order.

### Example Usage

- `sort_array([1, 5, 2, 3, 4])` will return `[1, 2, 3, 4, 5]`.
- `sort_array([-2, -3, -4, -5, -6])` will return `[-6, -5, -4, -3, -2]`.
- `sort_array([1, 0, 2, 3, 4])` will return `[0, 1, 2, 3, 4]`.

## Installation

### Environment Setup

To use the Sort Array software, you need to have Python installed on your system. The software does not require any additional dependencies beyond Python itself.

1. **Install Python**: If you do not have Python installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Verify Installation**: Open a terminal or command prompt and run the following command to verify that Python is installed correctly:
   ```bash
   python --version
   ```

### Quick Install

Since there are no additional dependencies, you can directly use the software after setting up Python.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `sort_array` function.

2. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment. Use the following command in your terminal or command prompt:
   ```bash
   python main.py
   ```

3. **Test Cases**: The `main.py` file includes test cases that demonstrate how the function works. You can modify these test cases or add new ones to test the function with different inputs.

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The comments provide insights into the logic and implementation of the `sort_array` function.

Thank you for using the Sort Array software! We hope it meets your needs for sorting arrays based on binary representation criteria. If you have any questions or need support, please feel free to reach out.