manual.md

```
# Prime Multiplication Checker

This software provides a simple function to determine if a given number is the product of exactly three distinct prime numbers. It is designed to work with numbers less than 100.

## Main Functionality

The main function provided by this software is `is_multiply_prime(a)`. This function checks if the input number `a` is the product of three distinct prime numbers and returns `True` if it is, and `False` otherwise.

### Function Details

- **`is_multiply_prime(a)`**: 
  - **Input**: An integer `a` (where 0 < a < 100).
  - **Output**: Returns `True` if `a` is the product of exactly three distinct prime numbers, otherwise returns `False`.
  - **Example**: 
    - `is_multiply_prime(30)` returns `True` because 30 = 2 * 3 * 5.
    - `is_multiply_prime(60)` returns `False` because 60 = 2 * 2 * 3 * 5.

## Installation

This software is implemented in Python. To use it, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: 
   - Clone the repository to your local machine using `git clone <repository-url>`.

2. **Navigate to the Project Directory**:
   - Use the command line to navigate to the directory where the repository is cloned.

3. **Install Dependencies**:
   - This project does not have any external dependencies. Ensure Python is installed and you're ready to go.

## Usage

To use the `is_multiply_prime` function, follow these steps:

1. **Open a Python Environment**:
   - You can use any Python environment like IDLE, PyCharm, or VSCode.

2. **Import the Function**:
   - Navigate to the directory containing `main.py` and import the function:
     ```python
     from main import is_multiply_prime
     ```

3. **Call the Function**:
   - Use the function with any integer less than 100:
     ```python
     result = is_multiply_prime(30)
     print(result)  # Output: True
     ```

## Additional Information

- **Limitations**: The function is designed to work with numbers less than 100. It may not perform correctly for numbers equal to or greater than 100.
- **Support**: For any issues or questions, please contact the development team through the repository's issue tracker.

This manual provides all necessary information to set up and use the Prime Multiplication Checker software effectively. Enjoy using the software to explore prime number products!
```