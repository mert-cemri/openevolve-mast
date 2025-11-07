manual.md

```
# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `prime_fib(n: int) -> int`

- **Description**: This function returns the n-th Fibonacci number that is also a prime number.
- **Parameters**: 
  - `n` (int): The position of the prime Fibonacci number to be returned.
- **Returns**: 
  - An integer representing the n-th Fibonacci number that is also prime.
- **Example Usage**:
  ```python
  >>> prime_fib(1)
  2
  >>> prime_fib(2)
  3
  >>> prime_fib(3)
  5
  >>> prime_fib(4)
  13
  >>> prime_fib(5)
  89
  ```

## Installation

This software does not require any external libraries or dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is installed**:
   - You can download Python from [python.org](https://www.python.org/downloads/).

3. **Run the script**:
   - You can directly run the `main.py` file using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the function**:
   - If you are using this function in another script, import it as follows:
   ```python
   from main import prime_fib
   ```

2. **Call the function**:
   - Use the `prime_fib` function to find the desired prime Fibonacci number:
   ```python
   result = prime_fib(5)
   print(result)  # Output will be 89
   ```

## Documentation

For further details on the implementation and usage, refer to the code comments and docstrings within the `main.py` file. The code is designed to be self-explanatory and easy to understand.

```