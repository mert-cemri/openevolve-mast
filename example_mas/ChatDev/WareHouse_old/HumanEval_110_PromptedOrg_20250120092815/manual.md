# Exchange Function User Manual

Welcome to the user manual for the Exchange Function, a Python-based utility designed to determine if it's possible to exchange elements between two lists to make the first list consist entirely of even numbers.

## Overview

The Exchange Function is a simple yet powerful tool that evaluates two lists of numbers and checks if an exchange of elements between them can result in the first list containing only even numbers. This function is useful in scenarios where list manipulation and number properties are essential.

## Main Functionality

The core functionality of the Exchange Function is encapsulated in the `exchange` function. Here's a brief overview of its capabilities:

- **Input**: Two non-empty lists of integers, `lst1` and `lst2`.
- **Output**: A string, either "YES" or "NO".
  - "YES" indicates that it's possible to exchange elements between the lists to make `lst1` consist entirely of even numbers.
  - "NO" indicates that such an exchange is not possible.

### Example Usage

- `exchange([1, 2, 3, 4], [1, 2, 3, 4])` returns "YES".
- `exchange([1, 2, 3, 4], [1, 5, 3, 4])` returns "NO".

## Installation

To use the Exchange Function, you need to have Python installed on your system. The function itself does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the script**: Obtain the `main.py` file containing the `exchange` function.

3. **Run the script**: You can execute the script in any Python environment or integrate it into your existing Python projects.

## How to Use

1. **Open your Python environment**: This could be a terminal, command prompt, or an IDE like PyCharm or VSCode.

2. **Import the function**: If you're using the function in another script, ensure you import it correctly.
   ```python
   from main import exchange
   ```

3. **Call the function**: Pass two lists of integers as arguments to the `exchange` function.
   ```python
   result = exchange([1, 2, 3, 4], [1, 2, 3, 4])
   print(result)  # Output: "YES"
   ```

## Conclusion

The Exchange Function is a straightforward utility designed to solve a specific problem involving list manipulation and number properties. With no additional dependencies required, it is easy to integrate and use in various Python projects. Enjoy using the Exchange Function to simplify your list operations!