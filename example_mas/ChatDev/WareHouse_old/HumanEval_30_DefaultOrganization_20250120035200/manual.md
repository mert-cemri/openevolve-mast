# User Manual for Positive Number Filter

## Introduction

This software module is designed to filter and return only positive numbers from a given list. It is a simple utility function written in Python that can be used in various applications where filtering positive numbers is required.

## Main Function

The main function provided by this module is `get_positive`. This function takes a list of numbers as input and returns a new list containing only the positive numbers from the input list.

### Function Signature

```python
def get_positive(l: list) -> list:
```

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]

>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This module does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Download the Module:**
   - Download the `main.py` file containing the `get_positive` function.

3. **Run the Code:**
   - You can run the code directly using Python. Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the script using the command:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - To use the `get_positive` function in your own scripts, you need to import it from the `main.py` file.
   ```python
   from main import get_positive
   ```

2. **Call the Function:**
   - Pass a list of numbers to the `get_positive` function to get a list of positive numbers.
   ```python
   positive_numbers = get_positive([-1, 2, -4, 5, 6])
   print(positive_numbers)  # Output: [2, 5, 6]
   ```

## Conclusion

This module provides a simple yet effective way to filter positive numbers from a list. With no external dependencies, it is easy to integrate into any Python project. Whether you are working on data analysis, scientific computing, or any other domain where list filtering is needed, this function can be a valuable tool.