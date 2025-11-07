# Prime Fibonacci Finder

This software provides a function to find the n-th number that is both a Fibonacci number and a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `prime_fib(n: int) -> int`

- **Description**: This function returns the n-th number that is both a Fibonacci number and a prime number.
- **Parameters**: 
  - `n` (int): The position of the desired prime Fibonacci number in the sequence.
- **Returns**: 
  - An integer representing the n-th prime Fibonacci number.

### `is_prime(num: int) -> bool`

- **Description**: This helper function checks if a given number is prime.
- **Parameters**: 
  - `num` (int): The number to check for primality.
- **Returns**: 
  - A boolean value indicating whether the number is prime.

### `fibonacci_sequence()`

- **Description**: This is a generator function that yields Fibonacci numbers indefinitely.
- **Yields**: 
  - The next Fibonacci number in the sequence.

## Installation

This software does not require any external dependencies, so there is no need to install additional packages. It is implemented in pure Python.

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine to access the `main.py` file.

2. **Run the Code**: You can run the code using any Python environment. Ensure you have Python installed on your machine.

3. **Example Usage**:
   - Open a Python interpreter or create a Python script.
   - Import the `prime_fib` function from `main.py`.
   - Call the `prime_fib` function with the desired position of the prime Fibonacci number.

   ```python
   from main import prime_fib

   # Example: Find the 5th prime Fibonacci number
   result = prime_fib(5)
   print(result)  # Output: 89
   ```

4. **Testing**: You can test the function with different values of `n` to find various prime Fibonacci numbers.

## Additional Information

- **Documentation**: The code is documented with docstrings to provide insights into the functionality of each component.
- **No External Libraries**: The implementation relies solely on Python's standard library, ensuring ease of use and compatibility.

This manual provides all the necessary information to effectively use the Prime Fibonacci Finder software. If you have any questions or need further assistance, please contact our support team.