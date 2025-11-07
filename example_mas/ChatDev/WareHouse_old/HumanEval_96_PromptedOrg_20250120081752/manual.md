# Prime Number Finder

This software provides a simple utility to find all prime numbers less than a given non-negative integer `n`. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `count_up_to(n)`

- **Description**: This function takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.
- **Parameters**: 
  - `n` (int): A non-negative integer.
- **Returns**: 
  - A list of integers, which are the prime numbers less than `n`.

### `is_prime(num)`

- **Description**: This helper function checks if a given number is a prime number.
- **Parameters**: 
  - `num` (int): The number to check for primality.
- **Returns**: 
  - `True` if the number is prime, `False` otherwise.

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

3. **Run the script**: You can execute the script using a Python interpreter. Open a terminal or command prompt and navigate to the directory containing `main.py`. Run the following command:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the function**: If you want to use the `count_up_to` function in another script, you can import it:

   ```python
   from main import count_up_to
   ```

2. **Call the function**: Use the function by passing a non-negative integer as an argument:

   ```python
   primes = count_up_to(10)
   print(primes)  # Output: [2, 3, 5, 7]
   ```

3. **Modify and Extend**: Feel free to modify the code to suit your needs or extend its functionality.

## Example Usage

Here are some example usages of the `count_up_to` function:

```python
print(count_up_to(5))   # Output: [2, 3]
print(count_up_to(11))  # Output: [2, 3, 5, 7]
print(count_up_to(0))   # Output: []
print(count_up_to(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))   # Output: []
print(count_up_to(18))  # Output: [2, 3, 5, 7, 11, 13, 17]
```

## Documentation

For further details on the implementation and to understand the logic behind the prime number detection, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the flow and logic used to determine prime numbers.