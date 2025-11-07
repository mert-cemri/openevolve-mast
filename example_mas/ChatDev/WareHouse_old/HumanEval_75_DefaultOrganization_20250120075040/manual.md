manual.md

```
# Prime Multiplication Checker

This software provides a simple function to determine if a given number is the product of exactly three prime numbers. It is designed to work with numbers less than 100.

## Main Functionality

The main function provided by this software is `is_multiply_prime(a)`. This function checks whether the input number `a` can be expressed as the product of exactly three prime numbers.

### Function Definition

```python
def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers and False otherwise."""
```

### Example Usage

- `is_multiply_prime(30)` returns `True` because 30 can be expressed as 2 * 3 * 5, which are all prime numbers.
- `is_multiply_prime(60)` returns `False` because 60 cannot be expressed as the product of exactly three prime numbers.

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Requirements

- Python 3.x

### Setting Up the Environment

1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script using the command:

   ```bash
   python main.py
   ```

4. You can modify the script to test different numbers by changing the input to the `is_multiply_prime` function.

## Additional Information

- The function `is_prime(n)` is used internally to check if a number is prime.
- The software is designed to handle numbers less than 100 efficiently.

Feel free to modify and extend the code to suit your needs. If you encounter any issues or have questions, please reach out to our support team.
```