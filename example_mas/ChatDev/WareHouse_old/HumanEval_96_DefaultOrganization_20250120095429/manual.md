manual.md

```
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
  - `True` if `num` is a prime number, `False` otherwise.

## Installation

This software does not require any external libraries or dependencies. It is implemented in pure Python. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Script**: You can run the script using Python. For example, to find all prime numbers less than 20, you can use the following command:

   ```bash
   python -c "from main import count_up_to; print(count_up_to(20))"
   ```

   This will output:

   ```
   [2, 3, 5, 7, 11, 13, 17, 19]
   ```

4. **Modify and Use**: You can modify the `n` value in the command to find prime numbers less than any other integer.

## Example Usage

Here are some example usages of the `count_up_to` function:

- `count_up_to(5)` returns `[2, 3]`
- `count_up_to(11)` returns `[2, 3, 5, 7]`
- `count_up_to(0)` returns `[]`
- `count_up_to(1)` returns `[]`
- `count_up_to(18)` returns `[2, 3, 5, 7, 11, 13, 17]`

## Documentation

For further details on the implementation, you can refer to the comments within the `main.py` file. The code is straightforward and well-commented to facilitate understanding and potential modifications.
```