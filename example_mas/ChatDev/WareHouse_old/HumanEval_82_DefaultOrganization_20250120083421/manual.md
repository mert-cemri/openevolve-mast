# Prime Length Checker

This software module provides a function to determine if the length of a given string is a prime number. It is a simple utility that can be used in various applications where such a check is necessary.

## Main Functions

The main function provided by this module is:

- `prime_length(string)`: This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.

### Example Usage

```python
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False
```

## Installation

This module does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file.

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the `main.py` file using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it directly.

   ```python
   from main import prime_length
   ```

2. **Call the Function**: Use the `prime_length` function with any string to check if its length is a prime number.

   ```python
   result = prime_length("example")
   print(result)  # Output will be either True or False
   ```

## Documentation

This module is designed to be simple and easy to use. The function `prime_length` leverages an internal helper function `is_prime` to determine the primality of the string length.

- **`is_prime(n)`**: This helper function checks if a given number `n` is a prime number. It is used internally by `prime_length`.

For further details on the implementation or to contribute, please refer to the source code in `main.py`.