# Largest Prime Factor Finder

This software provides a function to determine the largest prime factor of a given integer. It is designed to handle integers greater than 1 that are not prime themselves.

## Main Functionality

The core functionality of this software is encapsulated in the `largest_prime_factor` function. This function takes an integer `n` as input and returns the largest prime factor of `n`.

### Function Definition

```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
```

### How It Works

1. **Initial Check for Factor of 2**: The function first checks how many times the number 2 divides `n` and updates the largest factor accordingly.
2. **Odd Factors Check**: It then iterates through odd numbers starting from 3 up to the square root of `n`. For each odd number, it checks if it divides `n` and updates the largest factor.
3. **Final Prime Check**: If after all iterations `n` is still greater than 2, then `n` itself is a prime number and is the largest prime factor.

## Installation

This software does not require any external dependencies. It is implemented using standard Python libraries.

### Quick Install

To use this software, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.
3. **Run Python Interpreter**: Open the Python interpreter by typing `python` in your terminal.
4. **Import the Function**: Import the function by typing `from main import largest_prime_factor`.
5. **Call the Function**: Use the function by passing an integer greater than 1 that is not a prime. For example:
   ```python
   >>> largest_prime_factor(13195)
   29
   >>> largest_prime_factor(2048)
   2
   ```

## Example Usage

```python
# Example usage of the largest_prime_factor function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This software is a simple yet effective tool for finding the largest prime factor of a given integer, leveraging efficient algorithms to ensure quick computation even for larger numbers.