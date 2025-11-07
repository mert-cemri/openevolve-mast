manual.md

```
# Sum to N Function

A simple Python function to calculate the sum of all integers from 1 to a given number `n`.

## Overview

The `sum_to_n` function is designed to efficiently compute the sum of all integers from 1 to `n` using a mathematical formula. This function is useful for quickly obtaining the sum without the need for iterative loops.

## Main Functionality

- **Function Name**: `sum_to_n`
- **Purpose**: Calculate the sum of all integers from 1 to `n`.
- **Input**: A single integer `n`.
- **Output**: The sum of integers from 1 to `n`.

### Example Usage

```python
# Example usage of sum_to_n function
result = sum_to_n(10)
print(result)  # Output: 55
```

## Installation

This project does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the files directly.

3. **Run the Code**: Navigate to the directory containing `main.py` and execute the script using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you are using this function in another script, import it as follows:

```python
from main import sum_to_n
```

2. **Call the Function**: Use the function by passing an integer value to it.

```python
result = sum_to_n(30)
print(result)  # Output: 465
```

## Documentation

The function uses a mathematical formula to compute the sum, which is both efficient and fast. The formula used is:

\[ \text{Sum} = \frac{n \times (n + 1)}{2} \]

This formula allows the function to compute the sum in constant time, O(1), making it highly efficient even for large values of `n`.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the code comments.

```