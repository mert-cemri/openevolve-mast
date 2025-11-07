# Prime Length Checker

This software provides a simple utility function to determine if the length of a given string is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

The software includes the following main function:

- `prime_length(string)`: This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.

### Supporting Function

- `is_prime(n)`: A helper function used by `prime_length` to check if a given number `n` is a prime number.

## Installation

Since this software does not require any external dependencies, you can use it directly without any additional installation steps. Simply ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## Usage

To use the `prime_length` function, follow these steps:

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Python Script**: You can test the function by running the script in a Python environment. For example:

    ```bash
    python main.py
    ```

4. **Example Usage**: You can use the `prime_length` function in your own scripts by importing it. Here is an example of how to use it:

    ```python
    from main import prime_length

    # Test the function with different strings
    print(prime_length('Hello'))    # Output: True
    print(prime_length('abcdcba'))  # Output: True
    print(prime_length('kittens'))  # Output: True
    print(prime_length('orange'))   # Output: False
    ```

## Documentation

The code is straightforward and documented with comments explaining each function. You can refer to the comments in the `main.py` file for more details on how the functions work.

## Support

For any issues or questions, please contact the development team at ChatDev. We are here to assist you with any inquiries related to the software.