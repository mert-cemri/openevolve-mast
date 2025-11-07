manual.md

```
# Fruit Distribution Software

This software calculates the number of mangoes in a fruit basket given the number of apples and oranges described in a string and the total number of fruits.

## Main Functionality

The main function of this software is to determine the number of mangoes in a basket of fruits. The function `fruit_distribution` takes two inputs:
- A string that specifies the number of apples and oranges.
- An integer that represents the total number of fruits in the basket.

The function returns the number of mangoes by subtracting the number of apples and oranges from the total number of fruits.

## Installation

### Environment Setup

This project does not require any external dependencies, so setting up the environment is straightforward. Ensure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/).

### Quick Install

Since there are no external dependencies, you can directly use the Python script without any additional installations. Simply download or clone the repository containing the `main.py` file.

## How to Use

1. **Open the `main.py` file**: This file contains the function `fruit_distribution`.

2. **Function Usage**: 
   - Import the function into your Python script or interactive shell.
   - Call the function with the appropriate parameters.

### Example Usage

```python
from main import fruit_distribution

# Example 1
result1 = fruit_distribution("5 apples and 6 oranges", 19)
print(result1)  # Output: 8

# Example 2
result2 = fruit_distribution("0 apples and 1 oranges", 3)
print(result2)  # Output: 2

# Example 3
result3 = fruit_distribution("2 apples and 3 oranges", 100)
print(result3)  # Output: 95

# Example 4
result4 = fruit_distribution("100 apples and 1 oranges", 120)
print(result4)  # Output: 19
```

## Documentation

The function is well-documented within the code itself. You can refer to the docstring in the `fruit_distribution` function for a detailed explanation of the parameters and return value.

For any further questions or support, please contact our support team.

```