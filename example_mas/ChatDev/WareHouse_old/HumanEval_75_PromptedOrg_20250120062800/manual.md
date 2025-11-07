# Prime Multiplication Checker

This software provides a function to determine if a given number is the product of exactly three prime numbers. It is designed to work with numbers less than 100.

## Main Functionality

The main function provided by this software is `is_multiply_prime(a)`. This function checks if the input number `a` is the product of exactly three prime numbers. If it is, the function returns `True`; otherwise, it returns `False`.

### Example

```python
is_multiply_prime(30)  # Returns: True, because 30 = 2 * 3 * 5
is_multiply_prime(28)  # Returns: False, because 28 is not the product of three prime numbers
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. Open the `main.py` file in your preferred Python IDE or text editor.

2. You can directly call the `is_multiply_prime(a)` function with the desired integer `a` to check if it is the product of three prime numbers.

3. Run the script to see the results.

### Example Usage

```python
# Import the function from the module
from main import is_multiply_prime

# Test the function with a number
result = is_multiply_prime(30)
print(result)  # Output: True

result = is_multiply_prime(28)
print(result)  # Output: False
```

## Documentation

The function `is_multiply_prime(a)` is designed to be straightforward and easy to use. It leverages a helper function `is_prime(n)` to determine if a number is prime and checks combinations of prime numbers to verify if the input number is a product of exactly three primes.

For any further questions or support, please contact our development team.