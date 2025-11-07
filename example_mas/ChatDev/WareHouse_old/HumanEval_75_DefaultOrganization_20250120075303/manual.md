# is_multiply_prime User Manual

This document serves as a user manual for the `is_multiply_prime` function, which is designed to determine if a given number is the product of exactly three prime numbers. This function is implemented in Python and is part of a simple application that does not require any external dependencies.

## Overview

The `is_multiply_prime` function checks whether a given integer, `a`, is the product of exactly three prime numbers. The function returns `True` if the condition is met and `False` otherwise. This functionality is particularly useful for mathematical computations and educational purposes.

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository:**
   - You can clone the repository containing the `main.py` file to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the directory containing the `main.py` file:
     ```bash
     cd <repository-directory>
     ```

2. **Set Up Environment:**
   - No external dependencies are required for this application, so you can directly run the Python script without additional setup.

## Usage

### Running the Function

To use the `is_multiply_prime` function, follow these steps:

1. **Open the `main.py` file** in a text editor or IDE of your choice.

2. **Call the Function:**
   - You can call the `is_multiply_prime` function by passing an integer value as an argument. For example:
     ```python
     print(is_multiply_prime(30))  # This should return True
     ```

3. **Execute the Script:**
   - Run the script using Python from your terminal or command prompt:
     ```bash
     python main.py
     ```

### Example

Here is an example of how to use the function:

```python
# Example usage
print(is_multiply_prime(30))  # Should return True
print(is_multiply_prime(31))  # Should return False
```

## Function Details

### `is_multiply_prime(a)`

- **Parameters:**
  - `a` (int): The number to be checked.

- **Returns:**
  - `bool`: `True` if `a` is the product of exactly three prime numbers, `False` otherwise.

- **Description:**
  - The function first generates a list of prime numbers less than 100.
  - It then checks all combinations of three primes to see if their product equals the given number `a`.

## Conclusion

The `is_multiply_prime` function is a simple yet effective tool for determining if a number is the product of three prime numbers. With no external dependencies, it is easy to set up and use in any Python environment. This manual provides all the necessary information to get started with the function and integrate it into your projects.