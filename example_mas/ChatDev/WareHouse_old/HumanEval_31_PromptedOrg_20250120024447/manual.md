# Prime Number Checker

This software provides a simple function to determine if a given number is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Main Function

The main function provided by this software is `is_prime(n)`. It takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise.

### Function Signature

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    """
```

### Example Usage

```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply copy the `main.py` file into your project and use the `is_prime` function as needed.

### Requirements

There are no external dependencies required for this software. The `requirements.txt` file is empty, indicating that no additional packages need to be installed.

## How to Use

1. **Copy the Code**: Copy the `main.py` file containing the `is_prime` function into your project directory.

2. **Import the Function**: If you are using this function in another Python file, you can import it using:

    ```python
    from main import is_prime
    ```

3. **Call the Function**: Use the `is_prime` function by passing an integer as an argument to check if it is a prime number.

    ```python
    result = is_prime(101)
    print(result)  # Output: True
    ```

## Documentation

The function is designed to be efficient and checks for primality by:

- Returning `False` for numbers less than or equal to 1.
- Returning `True` for the number 2, which is the only even prime number.
- Returning `False` for any other even number.
- Checking divisibility from 3 up to the square root of the number, skipping even numbers.

This approach ensures that the function runs efficiently even for larger numbers.