# Prime Number Finder

This software provides a simple utility to find all prime numbers less than a given non-negative integer. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `count_up_to(n)`

- **Description**: This function takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.
- **Parameters**: 
  - `n` (int): A non-negative integer.
- **Returns**: 
  - A list of integers representing the prime numbers less than `n`.

### `is_prime(num)`

- **Description**: This helper function checks if a given number is a prime number.
- **Parameters**: 
  - `num` (int): The number to check for primality.
- **Returns**: 
  - `True` if the number is prime, `False` otherwise.

## Quick Install

Since this software does not require any external dependencies, you can directly run the Python script without any additional installation steps.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: You can run the script using Python. For example, to find all prime numbers less than 20, you can execute the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Example Usage**: You can test the function by calling it with different values of `n`:

   ```python
   print(count_up_to(5))  # Output: [2, 3]
   print(count_up_to(11)) # Output: [2, 3, 5, 7]
   print(count_up_to(0))  # Output: []
   print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
   print(count_up_to(1))  # Output: []
   print(count_up_to(18)) # Output: [2, 3, 5, 7, 11, 13, 17]
   ```

## Documentation

This software is straightforward and does not require extensive documentation. The main functionality is encapsulated in the `count_up_to` function, which is designed to be intuitive and easy to use.

For any questions or further assistance, please refer to the comments within the code for additional context and examples.