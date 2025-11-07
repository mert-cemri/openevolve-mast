# Largest Prime Factor Finder

This software module provides a function to find the largest prime factor of a given number. It is designed to be simple and efficient, focusing solely on the task of identifying the largest prime factor of a number greater than 1, which is not a prime itself.

## Main Functionality

The main function provided by this module is:

- `largest_prime_factor(n: int) -> int`: This function takes an integer `n` as input and returns the largest prime factor of `n`. It assumes that `n` is greater than 1 and is not a prime number itself.

### Example Usage

```python
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
```

## Installation

This module does not have any external dependencies, so you can use it directly in your Python environment. However, if you are setting up a new environment, you might want to ensure you have Python installed.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the module**: Obtain the `main.py` file containing the `largest_prime_factor` function.

3. **Run the function**: You can execute the function directly in a Python script or an interactive Python session.

## How to Use

1. **Open a Python environment**: You can use an IDE like PyCharm, VSCode, or simply run Python in your terminal.

2. **Import the function**: If you have saved the `main.py` file in your project, you can import the function using:

   ```python
   from main import largest_prime_factor
   ```

3. **Call the function**: Pass an integer greater than 1 (which is not a prime) to the function to get its largest prime factor.

   ```python
   result = largest_prime_factor(13195)
   print(result)  # Output will be 29
   ```

## Documentation

For further information on how the function works internally, you can refer to the docstring provided within the `main.py` file. The function uses a straightforward algorithm to determine the largest prime factor by iteratively dividing the number by its smallest factors.

Feel free to modify or extend the functionality as needed for your specific use case. This module is designed to be a simple, standalone solution for finding the largest prime factor of a number.