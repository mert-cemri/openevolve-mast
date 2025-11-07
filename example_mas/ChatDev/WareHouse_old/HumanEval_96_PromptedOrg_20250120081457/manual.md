# Prime Number Finder

This software module provides a function to find all prime numbers less than a given non-negative integer. It is designed to be simple and efficient, with no external dependencies required.

## Main Functions

### `count_up_to(n)`

- **Description**: This function takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.
- **Parameters**: 
  - `n` (int): A non-negative integer.
- **Returns**: 
  - A list of integers that are prime numbers less than `n`.

### `is_prime(num)`

- **Description**: This helper function determines if a given number is prime.
- **Parameters**: 
  - `num` (int): The integer to check for primality.
- **Returns**: 
  - `True` if `num` is a prime number, `False` otherwise.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: 
   - Download or clone the repository containing the `main.py` file to your local machine.

2. **Run the Code**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Run the Python script using the command:
     ```bash
     python main.py
     ```
   - You can also import the `count_up_to` function into your own Python scripts to use it directly.

3. **Example Usage**:
   - To find all prime numbers less than 10, you can use the function as follows:
     ```python
     from main import count_up_to
     
     primes = count_up_to(10)
     print(primes)  # Output: [2, 3, 5, 7]
     ```

## Notes

- The function `count_up_to` is designed to handle non-negative integers. Ensure that the input is a non-negative integer to avoid unexpected behavior.
- The algorithm used for checking primality is efficient for small to moderately large numbers. For very large numbers, consider using more advanced algorithms or libraries specialized in number theory.

This user manual provides all the necessary information to understand, install, and use the Prime Number Finder software effectively. Enjoy finding prime numbers with ease!