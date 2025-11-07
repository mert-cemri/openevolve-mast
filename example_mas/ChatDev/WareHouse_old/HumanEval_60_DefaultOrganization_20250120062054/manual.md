# Sum to N Function User Manual

Welcome to the user manual for the `sum_to_n` function. This document will guide you through understanding the main function of the software, how to set up your environment, and how to use the function effectively.

## Overview

The `sum_to_n` function is a simple Python function designed to calculate the sum of all integers from 1 to a given number `n`. This function is efficient and leverages a mathematical formula to compute the sum in constant time.

### Main Function

- **Function Name**: `sum_to_n`
- **Purpose**: To calculate the sum of all integers from 1 to `n`.
- **Input**: A single integer `n`.
- **Output**: The sum of all integers from 1 to `n`.

#### Example Usage

```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
```

## Installation

### Environment Setup

The `sum_to_n` function does not require any external dependencies, making it very easy to set up and use. You only need to have Python installed on your system.

#### Step-by-Step Installation

1. **Install Python**: Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Verify Python Installation**: Open your terminal or command prompt and type the following command to verify the installation:
   ```bash
   python --version
   ```

3. **Clone or Download the Code**: Obtain the `main.py` file containing the `sum_to_n` function. You can clone the repository or download the file directly.

## How to Use

1. **Open a Python Environment**: You can use any Python environment such as IDLE, PyCharm, VSCode, or simply the command line.

2. **Import the Function**: If you have the `main.py` file in your working directory, you can import the function directly:
   ```python
   from main import sum_to_n
   ```

3. **Call the Function**: Use the function by passing an integer value to it:
   ```python
   result = sum_to_n(10)
   print(result)  # Output: 55
   ```

4. **Run Tests**: You can test the function with various inputs to ensure it works as expected.

## Conclusion

The `sum_to_n` function is a straightforward and efficient tool for calculating the sum of integers from 1 to `n`. With no external dependencies, it is easy to integrate into any Python project. Enjoy using the function, and feel free to modify it to suit your needs!