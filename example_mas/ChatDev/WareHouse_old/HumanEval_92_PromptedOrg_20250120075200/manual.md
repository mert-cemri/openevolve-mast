# Any_Int Function User Manual

Welcome to the user manual for the `any_int` function. This document will guide you through the main functionalities of the software, how to install the necessary environment dependencies, and how to use the function effectively.

## Introduction

The `any_int` function is a simple utility written in Python that checks if one of three given numbers is equal to the sum of the other two, provided all numbers are integers. This function is useful for quick mathematical checks and validations in various applications.

### Main Functionality

- **Function Name:** `any_int`
- **Purpose:** To determine if one of the three input numbers is equal to the sum of the other two, with the condition that all numbers must be integers.
- **Return Value:** The function returns `True` if the condition is met, otherwise it returns `False`.

### Examples

- `any_int(5, 2, 7)` ➞ `True` (because 5 + 2 = 7)
- `any_int(3, 2, 2)` ➞ `False` (no number is the sum of the other two)
- `any_int(3, -2, 1)` ➞ `True` (because 3 + (-2) = 1)
- `any_int(3.6, -2.2, 2)` ➞ `False` (because not all numbers are integers)

## Installation

### Prerequisites

To use the `any_int` function, you need to have Python installed on your machine. The function does not require any additional libraries or dependencies.

### Installing Python

1. **Windows:**
   - Download the latest version of Python from the [official website](https://www.python.org/downloads/).
   - Run the installer and follow the instructions. Make sure to check the option "Add Python to PATH" during installation.

2. **macOS:**
   - You can install Python using Homebrew. Open Terminal and run the following command:
     ```bash
     brew install python
     ```

3. **Linux:**
   - Python is usually pre-installed on most Linux distributions. You can check your installation by running:
     ```bash
     python3 --version
     ```
   - If Python is not installed, you can install it using your package manager. For example, on Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

## Usage

To use the `any_int` function, follow these steps:

1. **Open a Python Environment:**
   - You can use any Python environment such as IDLE, PyCharm, VSCode, or simply the command line.

2. **Define the Function:**
   - Copy the following code into your Python environment:
     ```python
     def any_int(x, y, z):
         # Check if all inputs are integers
         if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
             # Check if one of the numbers is equal to the sum of the other two
             if x == y + z or y == x + z or z == x + y:
                 return True
         return False
     ```

3. **Call the Function:**
   - You can now call the `any_int` function with three numbers as arguments. For example:
     ```python
     result = any_int(5, 2, 7)
     print(result)  # Output: True
     ```

## Conclusion

The `any_int` function is a straightforward utility for checking specific mathematical conditions among three integers. With no additional dependencies required, it is easy to integrate into any Python project. If you have any questions or need further assistance, please feel free to reach out to our support team.