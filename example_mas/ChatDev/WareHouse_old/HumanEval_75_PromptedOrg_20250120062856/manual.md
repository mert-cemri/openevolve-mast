# is_multiply_prime User Manual

This software provides a function to determine if a given number is the product of exactly three prime numbers. It is designed to work with numbers less than 100.

## Main Functionality

The main function provided by this software is `is_multiply_prime(a)`. This function checks if the input number `a` is the product of exactly three prime numbers. If it is, the function returns `True`; otherwise, it returns `False`.

### Example

```python
is_multiply_prime(30)  # Returns: True, because 30 = 2 * 3 * 5
is_multiply_prime(28)  # Returns: False, because 28 is not the product of three primes
```

## Installation

There are no external dependencies required for this software. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Start

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your directory to the cloned repository:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code:**

   You can run the code directly using Python. Open a terminal and execute:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   To use the `is_multiply_prime` function in your own scripts, first import it:

   ```python
   from main import is_multiply_prime
   ```

2. **Call the Function:**

   Pass the number you want to check as an argument to the function:

   ```python
   result = is_multiply_prime(30)
   print(result)  # Output: True
   ```

## Documentation

The function `is_multiply_prime(a)` works by first generating a list of prime numbers less than 100. It then checks all possible combinations of three primes to see if their product equals the input number `a`.

### Prime Checking

The helper function `is_prime(n)` is used to determine if a number `n` is prime. It checks divisibility from 2 up to the square root of `n`.

### Limitations

- The function is designed to work only with numbers less than 100.
- It assumes that the input is a positive integer.

For any further questions or support, please contact our development team.